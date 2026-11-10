# -*- coding: utf-8 -*-
"""Nevera, despensa, semana y botiquín de la isla (pipeline multi-isla). Base canaria común + particularidades de cada isla (cocina_islas.json)
[CONOCIMIENTO_BASE]; pescado del registro de primera venta 2021 de la isla [VERIFICADO]."""
import os, sys, json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import isla, out, fmt_es
C=isla(); A=list(range(12))
K=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cocina_islas.json'),encoding='utf-8')); B=K['_base']; I=K.get(C['slug'],{})
MAPA=json.load(open(out(C,'mapa_oficial_resumen.json'))); IS=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'islas_istac_pesca.json')))[C['nombre']]
def it(x): return {'n':x[0],'o':x[1],'i':x[2],'c':x[3],'m':(x[4] if len(x)>4 else A)}
def lista(grupo):
    base=[it(x) for x in B[grupo]]
    if grupo in I: base=[it(x) for x in I[grupo]]
    extra=[it(x) for x in I.get(grupo+'_extra',[])]
    # quitar de la base lo que la isla redefine por nombre
    nombres={e['n'] for e in extra}; base=[b for b in base if b['n'] not in nombres]
    return extra+base
NOMBRE_PEZ={'Tuna':('Tuna (patudo)','fish','#33506e'),'Barrilote':('Barrilote (atún blanco)','fish','#4f6f8f'),'Caballa del Atlántico':('Caballa','fish','#567b9c'),'Atún rojo o de aleta azul':('Atún rojo','fish','#2f4a66'),'Bonito o Bonito listado':('Bonito listado','fish','#4f6f8f'),'Pez espada o Aguja paladar':('Pez espada','fish','#8fa7b5'),'Chicharro':('Chicharro','fish','#567b9c'),'Rabil':('Rabil','fish','#567b9c'),'Sardina arencada':('Alacha (sardina)','fish','#b9c3c9'),'Vieja':('Vieja','fish','#d0533d'),'Camarón narval':('Camarón','shrimp','#e8826a'),'Pargo macho':('Sama de pluma','fish','#a35a3a'),'Bocinegro':('Bocinegro','fish','#a35a3a'),'Fula colorada':('Alfonsiño (fula colorada)','fish','#e04a3a'),'Sierra o Corriguelo':('Sierra','fish','#3f6a86'),'Seifía o Seifío':('Seifía','fish','#7d6c55'),'Chopa o Negrón':('Chopa','fish','#6f7570'),'Pulpo':('Pulpo','octo','#b0607a'),'Morena':('Morena','fish','#6b5a3a'),'Cherne':('Cherne','fish','#6f7570'),'Sardina':('Sardina','fish','#b9c3c9'),'Lapa':('Lapas','octo','#7d6c55'),'Mero':('Mero','fish','#6f7570')}
pes=[]
for k,t in list(IS['pesca']['especies_t'].items())[:14]:
    n,i,c=NOMBRE_PEZ.get(k,(k,'fish','#567b9c')); pes.append({'n':n,'o':f"{fmt_es(t)} t en 2021",'m':IS['pesca']['meses'].get(k,A),'i':i,'c':c})
nevera=[{'t':'Puerta · lácteos y huevos','x':lista('lacteos')},{'t':'Balda alta · carne','x':lista('carne')},{'t':'Bandeja · pescado del día','x':pes},{'t':'Balda media · fruta','x':lista('fruta')},{'t':'Cajón · hortalizas','x':lista('hortalizas')}]
desp=[]
for t,xs in B['despensa']:
    items=[it(x) for x in xs]; ex=[it(x) for x in I.get('despensa_extra',{}).get(t,[])]; nombres={e['n'] for e in ex}
    desp.append({'t':t,'x':ex+[b for b in items if b['n'] not in nombres]})
huecos=[{'n':h[0],'o':h[1]} for h in B['huecos']+I.get('huecos_extra',[])]
menu=[{'d':d,'de':de,'al':al,'ce':ce} for d,de,al,ce in I['menu']] if 'menu' in I else json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','v4','04b_cocina_tf.json'),encoding='utf-8'))['menu']
pob=IS['poblacion']['2025']; aloe=MAPA['cultivo_ha'].get('Aloe',0)
botiquin={'grupos':[
 {'t':'Plantas medicinales de la huerta y el monte','e':'posible','x':[f"Aloe vera ({'ya en el Mapa de Cultivos: '+fmt_es(aloe,1)+' ha' if aloe>=0.5 else 'cultivo posible en toda la costa'})",'Manzanilla, hierbaluisa, poleo, menta y hierbabuena','Tomillo, romero, salvia y llantén','Eucalipto (hojas para vahos)','Sauce canario: su corteza contiene salicina, el antecedente natural de la aspirina','Uso tradicional; eficacia variable y sin dosis controlada']},
 {'t':'Lo que se elabora con la despensa','e':'posible','x':['Alcohol de alta graduación destilado de caña o uva, para desinfectar superficies e instrumental','Jabón de aceite de oliva y potasa de ceniza','Miel (uso tradicional en curas)','Sal y vinagre','Suero oral casero con agua, sal y azúcar (receta de la OMS)','Alimentación suficiente: la primera medicina preventiva']},
 {'t':'Lo que ya hay en la isla y aguanta un tiempo','e':'limite','x':[C['hospitales'],'Cirugía, partos, urgencias y fisioterapia','Esterilización en autoclave y oxígeno de concentradores, con electricidad de la isla',f"Todo depende del material fungible y de los repuestos almacenados; con {fmt_es(pob)} habitantes las existencias duran lo que duran"]},
 {'t':'Adormidera','e':'limite','x':['Viable en el clima (secano de medianías)','De ella salen los analgésicos opiáceos','Su cultivo y transformación para uso farmacéutico están sujetos a control estatal de estupefacientes y requieren industria']},
 {'t':'Lo que siempre vendría de fuera','e':'imposible','x':['Antibióticos, vacunas e insulina','Anestésicos, anticoagulantes, quimioterapia, antirretrovirales y hormonas','Reactivos de laboratorio, contraste y radiofármacos','Jeringas, guantes, sondas, suturas y material estéril de un solo uso','Lentes, audífonos, prótesis y repuestos de equipos médicos']}],
 'conclusion':f"<strong>{C['nombre']} {'podría acercarse a cerrar la despensa, pero no el botiquín' if pob<50000 else 'no podría cerrar la despensa, y mucho menos el botiquín'}.</strong> Con plantas, alcohol, jabón, miel y buena alimentación se cubre la higiene y parte del alivio de síntomas. La medicina moderna (antibióticos, vacunas, insulina, anestesia, material estéril) depende de una industria química y farmacéutica que no cabe en una isla. En un mundo cerrado, el hospital funcionaría mientras duraran sus existencias; la medicina es la dependencia exterior más dura. [INFERENCIA]"}
json.dump({'nevera':{'nevera':nevera,'despensa':desp,'huecos':huecos},'menu':menu,'botiquin':botiquin},open(out(C,'04b_cocina.json'),'w'),ensure_ascii=False)
print(C['nombre'],'nevera',sum(len(b['x']) for b in nevera),'despensa',sum(len(b['x']) for b in desp),'pescados',len(pes))
