# -*- coding: utf-8 -*-
"""C1-C2 (tierra y agua que libera la platanera) y balance de suficiencia C3-C5 de Tenerife (v1).
Programación lineal (scipy/HiGHS) con la misma estructura que el visor de La Palma: tres bolsas de tierra
(A: costa regada ex platanera; Bs: medianías secano; Br: medianías regadío), forraje, ganado, abono y pesca.
"""
import json, numpy as np, pandas as pd
from scipy.optimize import linprog
LP=json.load(open('/tmp/claude-0/-home-user/37cffb6f-bbb3-5850-8e2c-2adc0c1ce5ef/scratchpad/lapalma/D.json'))
par=pd.read_parquet('tf_parcelas_v2.parquet',columns=['crop','ha'])
ha=par.groupby('crop').ha.sum()

# ---------- C1-C2 ----------
POB=961745            # ISTAC, cifras oficiales de población a 1-1-2025 (E30245A_000002, publicado 15/12/2025) [VERIFICADO]
PLAT=float(ha['Platanera'])   # Mapa de Cultivos de Tenerife 2020-21 [VERIFICADO]
KG_HAB=15; REND=44    # consumo [REQUIERE_FUENTE]; rendimiento t/ha [APROXIMADO] (mismos supuestos que La Palma)
ret=POB*KG_HAB/1000/REND
lib=PLAT-ret
DEM_AGR=84.23         # hm³/año, consumo hídrico en regadío agrícola 2016 (BHITF), memoria del PHT 3.er ciclo, apdo. 3.1.2.4.2.1 [VERIFICADO]
SUP_REG=12304         # ha regadas en 2021 según la memoria del PHT (apdo. 3.1.1.1.3.1); el Mapa de Cultivos da 13.507 ha con REGADIO=Sí [VERIFICADO]
dot_A=round(DEM_AGR*1e6/SUP_REG,0)   # m³/ha·año, media del regadío de la isla
dot_B=[8760.0,11680.0]               # 15-20 L/planta·día × 1.600 plantas/ha (mismo método B que La Palma) [APROXIMADO]
SANU=float(ha['Superficie agrícola no utilizada'])
agua_A=lib*dot_A
c1={'poblacion':POB,'poblacion_fuente':'ISTAC, cifras oficiales a 1-1-2025','platanera_invernadero_ha':1447.6,'regado_mapa_ha':13506.8,'censo_2025':{'caprino':28452,'bovino':5137,'ovino':6797,'porcino':20400,'gallinas':1812705},'platanera_ha':round(PLAT,2),'c1_liberada_ha':round(lib,2),'dot_A':dot_A,'dot_B':dot_B,'demanda_agraria_hm3':DEM_AGR,'sanu_ha':round(SANU,2),'sup_regada_ha':SUP_REG,'barbecho_ha':round(float(ha['Barbecho']),1)}
print('C1',c1,'agua liberada hm3',round(agua_A/1e6,1),'-',round(lib*dot_B[1]/1e6,1))

# ---------- Parámetros del balance (misma estructura que La Palma; coeficientes [APROXIMADO]/[CONOCIMIENTO_BASE]) ----------
P=json.loads(json.dumps(LP['param']))
P['POB']=POB; P['SUP_A']=round(lib,1); P['AGUA']=float(round(agua_A,-3)); P['SANU']=round(SANU,1)
P['MONTE_CAP']=13000.0  # t MS/año del monte y el matorral para el caprino [APROXIMADO]: con 0,35 t/cabra·año equivale a 37.000 cabras, el máximo del censo ISTAC 2014-2025 (37.253 en 2014; 28.452 en 2025)
P['PESCA_T']=4278.7   # t, primera venta 2021 en puertos de Tenerife (registro de primera venta, Gobierno de Canarias, CC BY 4.0) [VERIFICADO]
P['GAN']['Cabra tinerfeña']=P['GAN'].pop('Cabra palmera'); P['LECHE']['Cabra tinerfeña']=P['LECHE'].pop('Cabra palmera')
CULT=LP['cult']   # rendimientos FAOSTAT España/mundo y composición (mismos que La Palma)
F={'autarquia':None,'insular':P['F_CON'],'espana':1.0}

# ---------- Producción actual sin plátano (bases) ----------
# constantes por cultivo derivadas de las bases de La Palma (kcal/prot/grasa por t producida y kg comestibles por t), rendimiento FAOSTAT × factor
def derive(name):
    r=[b for b in LP['bases']['insular'] if b['cultivo']==name][0]
    t=r['t']; return dict(rend=r['t']/r['ha']/0.7, kf=r['kcal']/(t*1e4), pf=r['prot']/(t*1e4), gf=r['grasa']/(t*1e4), fyh=r['fyh']/t)
def from_cult(name,fyh=None):
    c=CULT[name]; return dict(rend=c['rend'], kf=c['kcal']*c['frac'], pf=c['prot']*c['frac'], gf=c['grasa']*c['frac'], fyh=(1000*c['frac'] if (c['fyh'] if fyh is None else fyh) else 0))
K={'Aguacate':derive('Aguacate'),'Viña (uva)':derive('Viña (uva)'),'Cítricos':derive('Cítricos'),'Papa':derive('Papa'),'Almendro':derive('Almendro'),'Mango':derive('Mango'),
   'Hortalizas':derive('Hortalizas'),'Olivo (aceite)':derive('Olivo (aceite)'),'Higuera':derive('Higuera'),'Boniato':derive('Boniato'),'Ñame':derive('Ñame'),'Millo':derive('Millo'),'Plátano retenido':derive('Plátano retenido'),
   'Cereal (trigo y cebada, gofio)':from_cult('Trigo (gofio)'),'Papaya':from_cult('Papaya'),'Leguminosa seca':from_cult('Judía seca'),
   'Frutales templados':dict(rend=15000,kf=52*0.9,pf=0.3*0.9,gf=0.2*0.9,fyh=900),      # manzana/pera/hueso [APROXIMADO]
   'Subtropicales (guayaba, chirimoya…)':dict(rend=8000,kf=70*0.7,pf=1.2*0.7,gf=0.5*0.7,fyh=700),  # [APROXIMADO]
   'Tunera':dict(rend=8000,kf=41*0.6,pf=0.7*0.6,gf=0.5*0.6,fyh=600)}   # [APROXIMADO]
HA_BASE={'Viña (uva)':ha['Viña']+ha['Asociación Viña-Barbecho']+ha['Asociación Viña-Huerta Limpia']+ha['Asociación Viña-Papa']+ha['Asociación Viña-Templados']+ha['Asociación Viña-Hortaliza']+ha['Asociación Viña-Cítricos']+ha['Asociación Viña-Tunera'],
 'Hortalizas':ha['Huerta Limpia']+ha['Hortaliza Otras Mezclas']+ha['Huerto Familiar']+ha['Tomate']+ha['Cebolla']+ha['Melón-Sandía']+ha['Pepino']+ha['Fresas']+ha['Asociación Cítricos-Hortaliza'],
 'Papa':ha['Papa']+ha['Asociación Templados-Papa']+ha['Asociación Cítricos-Papa'],'Aguacate':ha['Aguacate'],'Cereal (trigo y cebada, gofio)':ha['Cereal Otros'],
 'Frutales templados':ha['Templado Otras Mezclas']+ha['Templado Pepita']+ha['Templado Hueso'],'Subtropicales (guayaba, chirimoya…)':ha['Subtropicales Otras Mezclas']+ha['Piña']+ha['Parchita']+ha['Pitaya']+ha['Granado'],
 'Cítricos':ha['Cítricos'],'Millo':ha['Millo']+ha['Asociación Templados-Millo'],'Papaya':ha['Papaya'],'Olivo (aceite)':ha['Olivo'],'Mango':ha['Mango'],'Leguminosa seca':ha['Leguminosa'],
 'Higuera':ha['Higuera'],'Tunera':ha['Tunera'],'Boniato':ha['Batata'],'Almendro':ha['Almendro'],'Ñame':ha['Ñame'],'Plátano retenido':ret}
bases={}
for esc in ['autarquia','insular','espana']:
    f={'autarquia':0.5,'insular':0.7,'espana':1.0}[esc]
    rows=[]
    for n,h in HA_BASE.items():
        k=K[n]; t=h*k['rend']*f/1000
        rows.append({'cultivo':n,'ha':round(float(h),1),'t':int(round(t)),'kcal':t*1e4*k['kf'],'prot':t*1e4*k['pf'],'grasa':t*1e4*k['gf'],'fyh':t*k['fyh']})
    bases[esc]=rows
MANTIENE_HA=sum(float(v) for n,v in HA_BASE.items() if n!='Plátano retenido')

# ---------- Modelo LP ----------
need=[POB*P['NEC']['kcal']*365, POB*P['NEC']['prot']*365, POB*P['NEC']['grasa']*365]
need_fyh=POB*P['FYH_DIA']/1000*365   # kg comestibles
cults=list(CULT.keys()); forr=list(P['FORRAJE'].keys()); gans=list(P['GAN'].keys())
def aporte_cult(c,f): # por ha: kcal, prot, grasa, fyh(kg), agua
    k=CULT[c]; g=k['rend']*f*k['frac']*1000
    return np.array([g*k['kcal']/100, g*k['prot']/100, g*k['grasa']/100]), (k['rend']*f*k['frac'] if k['fyh'] else 0.0), k['agua']
def aporte_gan(g):
    ms,leche,carne,n=P['GAN'][g]; a=np.zeros(3)
    if leche: l=P['LECHE'][g]; a+=np.array([leche*10*l[0],leche*10*l[1],leche*10*l[2]])
    a+=np.array([carne*10*P['CARNE'][0],carne*10*P['CARNE'][1],carne*10*P['CARNE'][2]]); return a
def resolver(esc,frac,pm,gan):
    supB=P['SANU']*frac; capA=P['SUP_A']
    pesca_t=P['PESCA_T']*pm; kgP=pesca_t*1000*P['PESCA'][0]
    pes=np.array([kgP*10*P['PESCA'][1],kgP*10*P['PESCA'][2],kgP*10*P['PESCA'][3]])
    base=np.array([sum(b[k] for b in bases[esc]) for k in ['kcal','prot','grasa']]); base_fyh=sum(b['fyh'] for b in bases[esc])
    # variables: cultivos (sin/con abono en autarquía), forrajes, ganado, z
    var=[]  # (tipo,nombre,f,abonado)
    for c in cults:
        if esc=='autarquia':
            if CULT[c]['leg']: var.append(('cultivo',c,P['F_CON'],False))
            else: var.append(('cultivo',c,P['F_SIN'],False)); var.append(('cultivo',c,P['F_CON'],True))
        else: var.append(('cultivo',c,F[esc],False))
    for fo in forr: var.append(('forraje',fo,None,False))
    for g in gans: var.append(('ganado',g,None,False))
    nv=len(var)+1; iz=nv-1
    A_ub=[]; b_ub=[]
    def row(): return np.zeros(nv)
    # tierra A y B
    rA=row(); rB=row(); rW=row(); rF=row(); rN=row(); rFyh=row(); rM=row()
    nut=[row(),row(),row()]
    for i,(t,n,f,ab) in enumerate(var):
        if t=='cultivo':
            b=CULT[n]['bolsa']; (rA if b=='A' else rB)[i]=1
            a,fyh,agua=aporte_cult(n,f); rW[i]=agua; rFyh[i]=-fyh
            for k in range(3): nut[k][i]=-a[k]
            if ab: rN[i]=P['N_REQ']
        elif t=='forraje':
            b,tms,agua=P['FORRAJE'][n]; (rA if b=='A' else rB)[i]=1; rW[i]=agua; rF[i]=-tms
        else:
            ms,leche,carne,nn=P['GAN'][n]; rF[i]=ms*(1-P['MONTE_MS']) if 'Cabra' in n else ms; rM[i]=ms*P['MONTE_MS'] if 'Cabra' in n else 0; rN[i]=-nn*P['N_DISP']
            a=aporte_gan(n)
            for k in range(3): nut[k][i]=-a[k]
    A_ub+= [rA,rB,rW]; b_ub+=[capA,supB,P['AGUA']]
    if gan: A_ub.append(rF); b_ub.append(0); A_ub.append(rM); b_ub.append(P['MONTE_CAP'])
    if esc=='autarquia': A_ub.append(rN); b_ub.append(0)
    for k in range(3):
        r=nut[k]/need[k]; r[iz]=1.0; A_ub.append(r); b_ub.append((base[k]+pes[k])/need[k])
    # cuota por cultivo (suma de sus variables) ≤ CUOTA × bolsa
    for c in cults:
        r=row()
        for i,(t,n,f,ab) in enumerate(var):
            if t=='cultivo' and n==c: r[i]=1
        A_ub.append(r); b_ub.append(P['CUOTA']*(capA if CULT[c]['bolsa']=='A' else supB))
    bounds=[(0,None)]*nv
    if not gan:
        for i,(t,n,f,ab) in enumerate(var):
            if t!='cultivo': bounds[i]=(0,0)
    cobj=np.zeros(nv); cobj[iz]=-1
    # frutas y hortalizas: cuarta cobertura dentro de z (misma proporción que energía, proteína y grasa) [DECISIÓN v1]
    rF2=rFyh/need_fyh; rF2[iz]=1.0
    res=linprog(cobj,A_ub=np.array(A_ub+[rF2]),b_ub=np.array(b_ub+[base_fyh/need_fyh]),bounds=bounds,method='highs')
    if res.status!=0:
        print('LP no factible',esc,frac,pm,gan,res.message)
        res=linprog(cobj,A_ub=np.array(A_ub),b_ub=np.array(b_ub),bounds=bounds,method='highs')
    x=res.x; z=x[iz]
    tot=base+pes; fyh=base_fyh; agua=0.0; filas=[]; tA=0; tB=0
    for i,(t,n,f,ab) in enumerate(var):
        v=x[i]
        if v<0.5: continue
        if t=='cultivo':
            a,fy,ag=aporte_cult(n,f); tot+=v*a; fyh+=v*fy; agua+=v*ag
            if CULT[n]['bolsa']=='A': tA+=v
            else: tB+=v
            filas.append({'tipo':'cultivo','nombre':n,'valor':round(v,1),'bolsa':CULT[n]['bolsa'],'t':int(round(v*CULT[n]['rend']*f/1000)),'agua':int(round(v*ag)),'abonado':ab,'f':f,'kcal':round(v*a[0],1),'prot':round(v*a[1],2),'grasa':round(v*a[2],2)})
        elif t=='forraje':
            b,tms,ag=P['FORRAJE'][n]; agua+=v*ag; (tA if False else None)
            if b=='A': tA+=v
            else: tB+=v
            filas.append({'tipo':'forraje','nombre':n,'valor':round(v,1),'bolsa':b,'t_ms':int(round(v*tms)),'agua':int(round(v*ag)),'kcal':0.0,'prot':0.0,'grasa':0.0})
        else:
            ms,leche,carne,nn=P['GAN'][n]; a=aporte_gan(n); tot+=v*a
            filas.append({'tipo':'ganado','nombre':n,'valor':round(v,1),'leche_t':int(round(v*leche/1000)),'carne_t':int(round(v*carne/1000)),'n_t':round(v*nn*P['N_DISP']/1000,1),'kcal':round(v*a[0],1),'prot':round(v*a[1],2),'grasa':round(v*a[2],2)})
    cob={k:round(tot[i]/need[i],4) for i,k in enumerate(['kcal','prot','grasa'])}
    return {'ok':res.status==0,'z':round(z,4),'cob':cob,'cob_fyh':round(fyh/need_fyh,4),'cob_base':{k:round(base[i]/need[i],4) for i,k in enumerate(['kcal','prot','grasa'])},
            'cob_pesca':{k:round(pes[i]/need[i],4) for i,k in enumerate(['kcal','prot','grasa'])},'agua_usada':round(agua,1),'filas':filas,'pesca_t':pesca_t,'tierraA':round(tA,1),'tierraB':round(tB,2),'supB':round(supB,2)}
rej={}
for esc in ['autarquia','insular','espana']:
    for fs in range(11):
        for pm in (1,3):
            for gan in (0,1):
                rej[f'{esc}|{fs/10:.1f}|{pm}|{gan}']=resolver(esc,fs/10,pm,gan)
k='insular|0.3|1|1'; r=rej[k]
print(k,'z',r['z'],r['cob'],'fyh',r['cob_fyh'],'base',r['cob_base'],'pesca',r['cob_pesca'],'agua',r['agua_usada']/1e6)
for f in r['filas']: print('   ',f['tipo'],f['nombre'],f['valor'],f.get('bolsa',''),f.get('t',f.get('t_ms',f.get('leche_t'))))
for kk in ['autarquia|0.0|1|0','autarquia|0.3|1|1','autarquia|1.0|1|1','insular|1.0|3|1','espana|1.0|3|1','insular|0.0|1|0']:
    print(kk, rej[kk]['z'], rej[kk]['cob'], 'fyh',rej[kk]['cob_fyh'])
json.dump({'c1':c1,'param':P,'cult':CULT,'bases':bases,'rejilla':rej,'mantiene_ha':round(MANTIENE_HA,1)},open('97_balance_salida_tf.json','w'),ensure_ascii=False)
