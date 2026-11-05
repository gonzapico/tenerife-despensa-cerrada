# -*- coding: utf-8 -*-
"""Catálogo de viabilidad agroclimática de Tenerife por pisos (v1).
Universo: los 163 productos del visor de La Palma (FAOSTAT + locales), con las variedades locales adaptadas a Tenerife.
Requisitos: FAO ECOCROP (copia pública OpenCLIM/ecocrop, solo para el cálculo). Reglas declaradas en REGLAS.
Clima por pisos: [CONOCIMIENTO_BASE] a partir de normales AEMET (Santa Cruz, Los Rodeos, Reina Sofía, Izaña) y gradiente altitudinal.
"""
import json, re, numpy as np, pandas as pd
LP='/tmp/claude-0/-home-user/37cffb6f-bbb3-5850-8e2c-2adc0c1ce5ef/scratchpad/lapalma/D.json'
ECO='/tmp/claude-0/-home-user/37cffb6f-bbb3-5850-8e2c-2adc0c1ce5ef/scratchpad/eco_dl/EcoCrop_DB.csv'
D=json.load(open(LP))
E=pd.read_csv(ECO,encoding='latin-1',low_memory=False)
E=E[E.TOPMN.notna()&E.TOPMX.notna()&E.TMIN.notna()&E.TMAX.notna()&E.ROPMN.notna()&E.RMIN.notna()].copy()
E['com']=E.COMNAME.fillna('').str.lower()

# ---------- Pisos climáticos de Tenerife (N = barlovento, S = sotavento) [CONOCIMIENTO_BASE] ----------
COTAS=[(0,300),(300,600),(600,1000),(1000,1500),(1500,3715)]
NOMBRES=['Costa','Medianías bajas','Medianías altas','Pinar y cumbre baja','Cumbre']
ZREF=[150,450,800,1250,1900]
# tm_anual, tm_mes_frio, tm_mes_calido, lluvia_mm
CLIMA={'N':[(20.3,17.3,23.6,380),(18.0,14.9,21.5,600),(15.6,12.5,19.0,780),(12.4,9.0,16.4,850),(11.0,5.8,17.5,520)],
       'S':[(21.3,18.0,25.0,150),(19.0,15.5,23.0,260),(16.4,12.6,20.8,380),(13.4,9.6,18.3,480),(11.5,6.5,18.0,420)]}
# horas de frío: relación empírica tm_mes_frio -> horas, interpolada de los pisos de La Palma (AEMET+Rodríguez 2015)
_hf=sorted([(c['tm_mes_frio'],c['horas_frio']) for c in D['clima']])
def horas_frio(t): return float(np.interp(t,[a for a,_ in _hf],[b for _,b in _hf]))
clima=[]
for v in ['N','S']:
    for i,(tm,tf,tc,ll) in enumerate(CLIMA[v]):
        tn=round(tf-2.7,1); tabs=round(tn-6.0,1)
        clima.append({'piso':f'P{i+1}-{v}','nombre':NOMBRES[i],'cota':f'{COTAS[i][0]}-{COTAS[i][1]}','z_ref':ZREF[i],'tm_anual':tm,'tm_mes_frio':tf,'tn_mes_frio':tn,'t_abs_min_est':tabs,'tm_mes_calido':tc,'lluvia_mm':ll,'horas_frio':int(round(horas_frio(tf)))})

# ---------- Correspondencia producto -> especie ECOCROP ----------
# 'sci:' nombre científico (primera coincidencia exacta o por prefijo); 'com:' nombre común; 'manual:' ficha manual
M={
'Caña de azúcar':'sci:Saccharum officinarum','Millo (grano)':'sci:Zea mays','Arroz':'sci:Oryza sativa','Trigo':'sci:Triticum aestivum','Palma aceitera':'sci:Elaeis guineensis','Soja':'sci:Glycine max','Papa':'sci:Solanum tuberosum','Yuca':'sci:Manihot esculenta','Remolacha azucarera':'sci:Beta vulgaris','Tomate':'sci:Lycopersicon esculentum','Cebada':'sci:Hordeum vulgare','Plátano':'sci:Musa sp.','Cebolla seca':'sci:Allium cepa','Sandía':'sci:Citrullus lanatus','Manzana':'sci:Malus domestica','Ñame (Dioscorea)':'sci:Dioscorea alata','Boniato':'sci:Ipomoea batatas','Colza':'sci:Brassica napus','Pepino':'sci:Cucumis sativus','Uva':'sci:Vitis vinifera','Col / repollo':'sci:Brassica oleracea var. capitata','Algodón':'sci:Gossypium hirsutum','Naranja':'sci:Citrus sinensis','Coco':'sci:Cocos nucifera','Sorgo':'sci:Sorghum bicolor','Mango':'sci:Mangifera indica','Cacahuete':'sci:Arachis hypogaea','Berenjena':'sci:Solanum melongena','Girasol':'sci:Helianthus annuus','Mandarina':'sci:Citrus reticulata','Zanahoria y nabo':'sci:Daucus carota','Pimiento verde':'sci:Capsicum annuum','Plátano macho':'sci:Musa sp.','Calabaza / bubango':'sci:Cucurbita pepo','Té':'sci:Camellia sinensis','Mijo':'sci:Pennisetum glaucum','Espinaca':'sci:Spinacia oleracea','Judía seca / habichuela':'sci:Phaseolus vulgaris','Ajo':'sci:Allium sativum','Piña tropical':'sci:Ananas comosus','Melón':'sci:Cucumis melo','Lechuga y escarola':'sci:Lactuca sativa','Durazno y nectarina':'sci:Prunus persica','Pera':'sci:Pyrus communis','Coliflor y brócoli':'sci:Brassica oleracea var. botrytis','Judía verde':'sci:Phaseolus vulgaris','Aceituna / olivo':'sci:Olea europaea','Limón y lima':'sci:Citrus limon','Avena':'sci:Avena sativa','Arveja / guisante verde':'sci:Pisum sativum','Ñame (Colocasia, FAOSTAT)':'sci:Colocasia esculenta','Garbanzo':'sci:Cicer arietinum','Caucho':'sci:Hevea brasiliensis','Papaya':'sci:Carica papaya','Arveja seca':'sci:Pisum sativum','Okra':'sci:Abelmoschus esculentus','Ciruela':'sci:Prunus domestica','Triticale':'sci:Secale cereale','Centeno':'sci:Secale cereale','Café':'sci:Coffea arabica','Aguacate':'sci:Persea americana','Fresa':'sci:Fragaria x ananassa','Chícharo / caupí':'sci:Vigna unguiculata','Dátil':'sci:Phoenix dactylifera','Pomelo':'sci:Citrus paradisi','Millo tierno':'sci:Zea mays ssp. saccharata','Espárrago':'sci:Asparagus officinalis','Lenteja':'sci:Lens culinaris','Sésamo':'sci:Sesamum indicum','Haba seca':'sci:Vicia faba','Tabaco':'sci:Nicotiana tabacum','Cebolleta':'sci:Allium fistulosum','Pimienta palmera / guindilla seca':'sci:Capsicum annuum','Cacao':'sci:Theobroma cacao','Caqui':'sci:Diospyros kaki','Jengibre':'sci:Zingiber officinale','Guandú':'sci:Cajanus cajan','Albaricoque':'sci:Prunus armeniaca','Kiwi':'sci:Actinidia chinensis','Nuez':'sci:Juglans regia','Anacardo':'sci:Anacardium occidentale','Almendra':'sci:Prunus amygdalus','Yute':'sci:Corchorus capsularis','Cereza':'sci:Prunus avium','Linaza':'sci:Linum usitatissimum','Anís, cilantro, comino, hinojo':'sci:Pimpinella anisum','Nuez de areca':'sci:Areca catechu','Puerro':'sci:Allium ampeloprasum','Castaña':'sci:Castanea sativa','Trigo sarraceno':'sci:Fagopyrum esculentum','Ricino':'sci:Ricinus communis','Fibra de coco':'sci:Cocos nucifera','Alcachofa':'sci:Cynara scolymus','Chocho / altramuz':'sci:Lupinus albus','Guinda':'sci:Prunus cerasus','Haba verde':'sci:Vicia faba','Arándano':'sci:Vaccinium corymbosum','Fruto del anacardo':'sci:Anacardium occidentale','Pistacho':'sci:Pistacia vera','Higo':'sci:Ficus carica','Lino (fibra)':'sci:Linum usitatissimum','Avellana':'sci:Corylus avellana','Judía de enrame':'sci:Phaseolus vulgaris','Árbol del sebo':'sci:Sapium sebiferum','Pipa de melón':'sci:Cucumis melo','Pimienta negra':'sci:Piper nigrum','Frambuesa':'sci:Rubus idaeus','Mostaza':'sci:Brassica juncea','Karité':'manual:Karité','Grosella negra':'sci:Ribes nigrum','Membrillo':'sci:Cydonia oblonga','Cártamo':'sci:Carthamus tinctorius','Fonio':'sci:Digitaria exilis','Veza / chícharo forrajero':'sci:Vicia sativa','Arándano rojo':'sci:Vaccinium macrocarpon','Seda (morera + gusano)':'sci:Morus alba','Tung':'manual:Tung','Malanga':'sci:Xanthosoma sagittifolium','Cáñamo (fibra)':'sci:Cannabis sativa','Nuez de cola':'sci:Cola nitida','Alpiste':'sci:Phalaris canariensis','Kapok':'sci:Ceiba pentandra','Canela':'sci:Cinnamomum verum','Guisante bambara':'sci:Vigna subterranea','Sisal':'sci:Agave sisalana','Kenaf':'sci:Hibiscus cannabinus','Clavo':'manual:Clavo','Nuez moscada y cardamomo':'sci:Myristica fragrans','Quinoa':'sci:Chenopodium quinoa','Lúpulo':'sci:Humulus lupulus','Abacá':'sci:Musa textilis','Grosella espinosa':'sci:Ribes uva-crispa','Nuez de Brasil':'sci:Bertholletia excelsa','Ramio':'sci:Boehmeria nivea','Algarroba':'sci:Ceratonia siliqua','Pita (fibra de agave)':'sci:Agave sisalana','Menta y hierbabuena':'sci:Mentha piperita','Cañamón':'sci:Cannabis sativa','Achicoria':'sci:Cichorium intybus','Adormidera':'sci:Papaver somniferum','Pelitre':'manual:Pelitre','Vainilla':'sci:Vanilla planifolia','Jojoba':'sci:Simmondsia chinensis','Hoja de yuca':'sci:Manihot esculenta',
# locales (Tenerife)
'Ñame (Colocasia, local)':'sci:Colocasia esculenta','Millo local':'sci:Zea mays','Tagasaste (forraje)':'manual:Tagasaste','Tunera / higo pico':'manual:Tunera','Pitaya':'sci:Hylocereus undatus','Chirimoya':'sci:Annona cherimola','Níspero':'sci:Eriobotrya japonica','Guayaba':'sci:Psidium guajava','Parchita (maracuyá)':'sci:Passiflora edulis','Lichi':'sci:Litchi chinensis','Macadamia':'sci:Macadamia integrifolia','Granado':'sci:Punica granatum','Moral (morera negra)':'sci:Morus nigra','Tomate de árbol':'sci:Cyphomandra betacea','Pepino dulce':'sci:Solanum muricatum','Boniato (local)':'sci:Ipomoea batatas','Papas antiguas (local)':'sci:Solanum tuberosum','Café (Coffea arabica)':'sci:Coffea arabica','Tuno indio':'manual:Tuno indio','Moringa':'sci:Moringa oleifera',
}
MANUAL={ # TOPMN,TOPMX,TMIN,TMAX,ROPMN,RMIN,KTMP,perenne
 'Karité':(24,32,18,40,900,600,5,True),'Tung':(18,28,8,35,1000,700,-2,True),'Clavo':(24,32,18,36,2000,1500,15,True),
 'Tagasaste':(12,25,5,35,400,250,-5,True),'Tunera':(18,30,8,40,300,150,-4,True),'Tuno indio':(18,30,10,40,300,150,-2,True),'Pelitre':(15,25,5,32,800,500,-5,True)}
def params(key):
    kind,val=key.split(':',1)
    if kind=='manual':
        t=MANUAL[val]; return dict(TOPMN=t[0],TOPMX=t[1],TMIN=t[2],TMAX=t[3],ROPMN=t[4],RMIN=t[5],KTMP=t[6],PER=t[7],src='ficha manual')
    if kind=='sci':
        r=E[E.ScientificName==val]
        if not len(r): r=E[E.ScientificName.str.startswith(val+' ',na=False)]
    else:
        r=E[E.com.str.contains(r'(?:^|, )'+re.escape(val)+r'(?:,|$)',regex=True)]
    if not len(r): raise KeyError(key)
    r=r.iloc[0]
    per = (str(r.LISPA).lower().find('perennial')>=0) or (pd.notna(r.GMIN) and r.GMIN>=300)
    return dict(TOPMN=r.TOPMN,TOPMX=r.TOPMX,TMIN=r.TMIN,TMAX=r.TMAX,ROPMN=r.ROPMN,RMIN=r.RMIN,KTMP=(None if pd.isna(r.KTMP) else r.KTMP),PER=per,src='ECOCROP',sci=r.ScientificName)

# ---------- Reglas (declaradas) ----------
REGLAS={
 'T_eff':'anuales: temperatura media del mes cálido (crecen en verano) salvo las de estación fría (TOPMN≤16), que usan la media anual; perennes: media de (anual, mes cálido)',
 'temp_ok':'TOPMN−2 ≤ T_eff ≤ TOPMX+2 y mínima absoluta estimada del piso > KTMP (temperatura letal, si consta)',
 'temp_marginal':'TMIN ≤ T_eff ≤ TMAX pero fuera de la banda óptima: MARGINAL (temperatura subóptima)',
 'proteccion':'si ningún piso cumple la temperatura y en la costa falta ≤6 °C para TOPMN−2 o la mínima letal se evita bajo cubierta: VIABLE CON PROTECCIÓN (invernadero, sin calefacción)',
 'secano_anual_fria':'anual de estación fría: secano si la lluvia del piso ≥ 0,9×ROPMN (crece con la lluvia de invierno)',
 'secano_anual_calida':'anual de estación cálida (TOPMN≥18): siempre con riego (regla del mes más seco: el verano canario es seco)',
 'secano_perenne':'perenne: secano si la lluvia ≥ 0,8×ROPMN, o si es perenne de secano mediterráneo (lista declarada) y la lluvia ≥ RMIN; los perennes sensibles a la sequía estival (lista declarada) exigen riego siempre',
 'agua_marginal':'si el mínimo absoluto de lluvia (RMIN) supera 1.500 mm, el cultivo exige humedad tropical constante y no solo riego: MARGINAL (agua); calibración: lo que hoy se riega en la isla (platanera, ñame) sale «con riego»',
 'riego_mm':'r = máx(0, ROPMN − lluvia del mejor piso)',
}
SECANO_MED={'Uva','Aceituna / olivo','Higo','Almendra','Algarroba','Dátil','Castaña','Nuez','Manzana','Pera','Membrillo','Ciruela','Durazno y nectarina','Cereza','Guinda','Albaricoque','Avellana','Pistacho','Jojoba','Seda (morera + gusano)','Moral (morera negra)','Granado','Chirimoya','Níspero','Caqui','Tunera / higo pico','Tuno indio','Tagasaste (forraje)','Pita (fibra de agave)','Sisal','Anacardo','Fruto del anacardo','Grosella negra','Grosella espinosa','Arándano','Arándano rojo','Frambuesa','Lúpulo','Espárrago','Alcachofa','Kenaf','Pepino dulce','Adormidera'}
RIEGO_SIEMPRE={'Plátano','Plátano macho','Aguacate','Mango','Papaya','Naranja','Limón y lima','Mandarina','Pomelo','Piña tropical','Parchita (maracuyá)','Guayaba','Lichi','Macadamia','Pitaya','Café','Café (Coffea arabica)','Cacao','Té','Coco','Fibra de coco','Palma aceitera','Caña de azúcar','Ñame (Dioscorea)','Ñame (Colocasia, FAOSTAT)','Ñame (Colocasia, local)','Boniato','Boniato (local)','Yuca','Hoja de yuca','Malanga','Jengibre','Tomate de árbol','Moringa','Nuez de areca','Nuez de cola','Kapok','Canela','Nuez moscada y cardamomo','Vainilla','Pimienta negra','Caucho','Abacá','Ramio','Yute','Tung','Karité','Nuez de Brasil','Clavo','Guandú','Menta y hierbabuena','Achicoria','Pelitre','Millo tierno','Millo local','Fresa','Tomate de árbol'}

# ---------- Lo que ya se cultiva en Tenerife (Mapa de Cultivos de Tenerife 2020-21) ----------
TF_MAP={ # clase del Mapa de Cultivos -> productos del catálogo
 'Platanera':['Plátano'],'Viña':['Uva'],'Papa':['Papa','Papas antiguas (local)'],'Aguacate':['Aguacate'],'Cereal Otros':['Trigo','Cebada','Avena','Centeno'],
 'Millo':['Millo (grano)','Millo tierno','Millo local'],'Papaya':['Papaya'],'Cítricos':['Naranja','Limón y lima','Mandarina','Pomelo'],'Olivo':['Aceituna / olivo'],'Tomate':['Tomate'],
 'Mango':['Mango'],'Leguminosa':['Judía seca / habichuela','Garbanzo','Lenteja','Haba seca','Chocho / altramuz','Arveja seca'],'Higuera':['Higo'],'Tunera':['Tunera / higo pico','Tuno indio'],
 'Batata':['Boniato','Boniato (local)'],'Almendro':['Almendra'],'Templado Pepita':['Manzana','Pera','Membrillo'],'Templado Hueso':['Durazno y nectarina','Ciruela','Albaricoque','Cereza'],
 'Templado Otras Mezclas':['Castaña','Caqui','Nuez','Níspero'],'Subtropicales Otras Mezclas':['Guayaba','Chirimoya','Lichi','Macadamia'],'Cebolla':['Cebolla seca'],'Moringa':['Moringa'],
 'Tagasaste':['Tagasaste (forraje)'],'Melón-Sandía':['Melón','Sandía'],'Fresas':['Fresa'],'Pitaya':['Pitaya'],'Pepino':['Pepino'],'Piña':['Piña tropical'],'Parchita':['Parchita (maracuyá)'],
 'Ñame':['Ñame (Colocasia, local)'],'Granado':['Granado'],'Caña de Azúcar':['Caña de azúcar'],'Tabaco':['Tabaco'],'Frutos Rojos':['Arándano','Frambuesa'],
 'Huerta Limpia':['Col / repollo','Lechuga y escarola','Zanahoria y nabo','Calabaza / bubango','Pimiento verde','Judía verde','Berenjena','Espinaca','Coliflor y brócoli','Ajo','Puerro','Cebolleta','Alcachofa','Haba verde','Arveja / guisante verde','Pimienta palmera / guindilla seca'],
 'Aromáticas':['Menta y hierbabuena','Anís, cilantro, comino, hinojo'],
}
TF_IRRIGADO={'Plátano','Papaya','Mango','Piña tropical','Tomate','Pitaya','Fresa','Aguacate','Parchita (maracuyá)','Pepino','Melón','Sandía','Naranja','Limón y lima','Mandarina','Caña de azúcar','Moringa'}  # clases regadas al 100 % en el Mapa de Cultivos [INFERENCIA]
TF_SET=set(x for v in TF_MAP.values() for x in v)
CALIB_RIEGO={'Plátano','Plátano macho','Ñame (Colocasia, local)','Ñame (Colocasia, FAOSTAT)'}  # calibración: regados hoy en Tenerife; el plátano macho sigue al plátano

def clasifica(nombre,p):
    per=p['PER']; fria=(p['TOPMN']<=16)
    best=None; pisos=[]; lim=None
    tempok=[];
    for c in clima:
        if per: T=(c['tm_anual']+c['tm_mes_calido'])/2
        else: T=c['tm_anual'] if fria else c['tm_mes_calido']
        letal = (p['KTMP'] is not None and c['t_abs_min_est']<=p['KTMP'])
        ok = (p['TOPMN']-2<=T<=p['TOPMX']+2) and not letal
        marg = (p['TMIN']<=T<=p['TMAX']) and not letal
        if ok:
            if per: secano = (c['lluvia_mm']>=0.8*p['ROPMN']) or (nombre in SECANO_MED and c['lluvia_mm']>=p['RMIN'])
            else: secano = fria and c['lluvia_mm']>=0.9*p['ROPMN']
            if nombre in RIEGO_SIEMPRE: secano=False
            tempok.append((c,secano))
        elif marg: pisos.append(c['piso'])
    r=None
    if tempok:
        if p['RMIN']>1500 and nombre not in CALIB_RIEGO: cl='MARGINAL'; lim='agua'
        elif any(s for _,s in tempok): cl='VIABLE SECANO'; lim=None
        else: cl='VIABLE CON RIEGO'; lim='agua'
        pisos=[c['piso'] for c,_ in tempok]
        ll=max(c['lluvia_mm'] for c,_ in tempok); r=int(max(0,p['ROPMN']-ll))
    elif pisos:
        cl='MARGINAL'; lim='temperatura subóptima'; r=int(max(0,p['ROPMN']-max(c['lluvia_mm'] for c in clima if c['piso'] in pisos)))
    else:
        costa=[c for c in clima if c['piso'].startswith('P1')]
        T=max((c['tm_anual']+c['tm_mes_calido'])/2 for c in costa)
        letal_all = p['KTMP'] is not None and all(c['t_abs_min_est']<=p['KTMP'] for c in costa)
        if p['TOPMN']-2-T<=6 and p['TOPMN']-2-T>0 or letal_all and p['TMIN']<=T+6:
            cl='VIABLE CON PROTECCIÓN'; lim='frío (requiere invernadero)'; pisos=[c['piso'] for c in costa]; r=int(max(0,p['ROPMN']-380))
        else:
            cl='IMPOSIBLE'; lim='mínimas letales (heladas o frío letal)' if p['KTMP'] is not None else 'temperatura fuera de rango'; pisos=[]
    return cl,lim,pisos,r

ORDER=['VIABLE SECANO','VIABLE CON RIEGO','VIABLE CON PROTECCIÓN','MARGINAL','IMPOSIBLE']
cat=[]
for c in D['cat']:
    n=c['n']
    if n=='Papa de color (local)': n='Papas antiguas (local)'
    key=M[n]; p=params(key)
    cl,lim,pisos,r=clasifica(n,p)
    o=c['o'].replace('Local La Palma','Local Tenerife')
    o=re.sub(r' · antecedente en LP:.*','',o)
    if n=='Tabaco': o+=' · antecedente en TF: 0,3 ha en el Mapa de Cultivos'
    if n in ('Café','Café (Coffea arabica)'): o+=' · antecedente en TF: plantaciones testimoniales en el norte [CONOCIMIENTO_BASE]'
    cat.append({'n':n,'f':c['f'] if not n.startswith('Papas antiguas') else 'Papas antiguas (local)','c':cl,'l':lim,'pi':pisos,'r':r,'lp':n in TF_SET,'a':c['a'],'o':o,'s':p['src']})
# Moringa: nueva entrada local de Tenerife (23,5 ha en el Mapa de Cultivos)
p=params(M['Moringa']); cl,lim,pisos,r=clasifica('Moringa',p)
cat.append({'n':'Moringa','f':'Moringa','c':cl,'l':lim,'pi':pisos,'r':r,'lp':True,'a':True,'o':'Local Tenerife','s':p['src']})

# ---------- Calibración ----------
viables=[c for c in cat if c['lp']]
ok1=[c for c in viables if ORDER.index(c['c'])<=2]
reg=[c for c in cat if c['n'] in TF_IRRIGADO]
ok2=[c for c in reg if c['c']!='VIABLE SECANO']
fallos=[c['n']+'→'+c['c'] for c in viables if ORDER.index(c['c'])>2]+[c['n']+'→secano' for c in reg if c['c']=='VIABLE SECANO']
calibra={'ok':len(ok1)+len(ok2),'n':len(viables)+len(reg),'fallos':fallos}
import collections
print(collections.Counter(c['c'] for c in cat))
print('alimentarios',sum(c['a'] for c in cat),'en TF',len(viables),'calibración',calibra)
for c in cat:
    if c['c'] not in ('VIABLE SECANO','VIABLE CON RIEGO'): print('  ',c['n'],c['c'],c['l'],c['pi'])
json.dump({'clima':clima,'cat':cat,'calibra':{'ok':calibra['ok'],'n':calibra['n']},'reglas':REGLAS,'cotas':COTAS},open('95_catalogo_salida_tf.json','w'),ensure_ascii=False,indent=0)
pd.DataFrame(cat).to_csv('03_catalogo_viabilidad_tf.csv',index=False)
