# -*- coding: utf-8 -*-
"""Nevera, despensa, semana y botiquín tinerfeños. Criterio de entrada: probado en Tenerife (Mapa de Cultivos 2020-21) o con antecedentes.
Temporadas y platos [CONOCIMIENTO_BASE]; pescado: registro de primera venta 2021, puertos de Tenerife (Gobierno de Canarias, CC BY 4.0): las 14 especies con más peso y los meses con al menos el 3 % de su venta anual [VERIFICADO]."""
import json
A=list(range(12))
PV=json.load(open('pesca_tf_2021.json'))
NOMBRE={'Tuna':('Tuna (patudo)','fish','#33506e'),'Barrilote':('Barrilote (atún blanco)','fish','#4f6f8f'),'Caballa del Atlántico':('Caballa','fish','#567b9c'),'Atún rojo o de aleta azul':('Atún rojo','fish','#2f4a66'),
 'Bonito o Bonito listado':('Bonito listado','fish','#4f6f8f'),'Pez espada o Aguja paladar':('Pez espada','fish','#8fa7b5'),'Chicharro':('Chicharro','fish','#567b9c'),'Rabil':('Rabil','fish','#567b9c'),
 'Sardina arencada':('Alacha (sardina)','fish','#b9c3c9'),'Vieja':('Vieja','fish','#d0533d'),'Camarón narval':('Camarón','shrimp','#e8826a'),'Pargo macho':('Sama de pluma','fish','#a35a3a'),'Bocinegro':('Bocinegro','fish','#a35a3a'),
 'Fula colorada':('Alfonsiño (fula colorada)','fish','#e04a3a'),'Sierra o Corriguelo':('Sierra','fish','#3f6a86'),'Seifía o Seifío':('Seifía','fish','#7d6c55'),'Chopa o Negrón':('Chopa','fish','#6f7570'),'Pulpo':('Pulpo','octo','#b0607a'),'Morena':('Morena','fish','#6b5a3a')}
PESCADO=[]
for k,t in list(PV['especies_t'].items())[:14]:
    n,i,c=NOMBRE.get(k,(k,'fish','#567b9c')); m=PV['meses'].get(k,A)
    PESCADO.append({'n':n,'o':f"{t:,.0f} t en 2021".replace(',','.'),'m':m,'i':i,'c':c})
def it(n,o,m,i,c=''): return {'n':n,'o':o,'m':m,'i':i,'c':c}
nevera=[
 {'t':'Puerta · lácteos y huevos','x':[
   it('Queso de cabra tinerfeño','fresco, tierno y ahumado · queserías de medianías',A,'cheese','#f2d27a'),
   it('Leche de cabra','cabra tinerfeña · medianías y cumbre',[0,1,2,3,4,5,9,10,11],'bottle','#f7f4ea'),
   it('Leche de vaca','vacas con forraje de la isla',A,'carton','#4a8fc0'),
   it('Yogur','leche de vaca o cabra',A,'cup','#e07a8a'),
   it('Queso de flor y curado de oveja','pequeñas queserías · antecedente',A,'cheese','#e9c66a'),
   it('Mantequilla y requesón','nata y suero',A,'jar','#f3dc84'),
   it('Huevos','gallinas, escala doméstica',A,'egg','')]},
 {'t':'Balda alta · carne','x':[
   it('Cabrito y baifo','cabra tinerfeña',[0,1,2,3,11],'meat','#b5473b'),
   it('Ternera y vaca','terneros y desvieje',A,'meat','#a83a32'),
   it('Cochino negro canario','subproductos de huerta y gofio',[0,1,10,11],'meat','#d98c86'),
   it('Carne fiesta y chicharrones','matanza y fiestas',[0,1,11],'sausage','#5a1f1f'),
   it('Conejo','forraje y huerta',A,'meat','#cf8b7a'),
   it('Pollo','escala doméstica',A,'meat','#e8b98c')]},
 {'t':'Bandeja · pescado del día','x':PESCADO},
 {'t':'Balda media · fruta','x':[
   it('Plátano','P1 · costa, regadío',A,'banana','#f2d33a'),
   it('Aguacate','P1-P3 · 802 ha hoy',[0,1,2,3,9,10,11],'round','#4f6b2a'),
   it('Mango','P1 · costa sur y oeste',[6,7,8,9],'round','#f0a12a'),
   it('Papaya','P1 · costa · 149 ha',A,'round','#f08a3a'),
   it('Naranja y limón','P1-P3 · regadío',[0,1,2,3,4,10,11],'round','#f39a1f'),
   it('Fresa','medianías del norte · Valle Guerra',[1,2,3,4,5],'round','#d7363a'),
   it('Higo','P1-P3 · secano',[6,7,8],'round','#6d3b5c'),
   it('Tuno (higo pico)','P1-P3 · secano',[6,7,8,9],'round','#d9506a'),
   it('Durazno y ciruela','P3 · medianías altas',[5,6,7],'round','#f2a36a'),
   it('Manzana y pera','P3-P4 · El Sauzal, La Esperanza',[7,8,9],'round','#c7383a'),
   it('Uva de mesa','viña · 2.836 ha',[7,8,9],'round','#5b3a6e'),
   it('Pitaya','P1-P2 · costa',[7,8,9,10],'round','#d63a8a'),
   it('Chirimoya y guayaba','medianías del norte',[8,9,10,11,0],'round','#c8d36a'),
   it('Castañas','Acentejo y La Orotava · otoño',[9,10,11],'round','#7a4a2a')]},
 {'t':'Cajón · hortalizas','x':[
   it('Papas','P1-P3 · varias siembras · 1.745 ha',A,'tuber','#c79a62'),
   it('Papas antiguas (bonitas, negras)','medianías altas · siembra de invierno',[4,5,6,7,8],'tuber','#8a5a3a'),
   it('Batata','P1-P2',[7,8,9,10,11,0],'tuber','#b5534f'),
   it('Ñame','barrancos húmedos del norte',[0,1,2,10,11],'tuber','#8a6a5a'),
   it('Millo tierno (piña de millo)','P1-P3',[6,7,8,9],'cob','#f2c230'),
   it('Tomate','P1 · costa sur',A,'round','#e0352b'),
   it('Col, coliflor y bubango','P2-P4',[0,1,2,3,10,11],'leafy','#7fb069'),
   it('Cebolla','P1-P3 · Guía de Isora',[3,4,5,6,7],'round','#c9a0c8'),
   it('Zanahoria','P1-P3',A,'root','#f08a24'),
   it('Calabaza','P1-P2',[4,5,6,7,8,9],'pumpkin','#e8922a'),
   it('Lechuga','P1-P4',A,'leafy','#9ad15a'),
   it('Pimiento y pimienta picona','P1-P2',[6,7,8,9,10],'pepper','#d1302a'),
   it('Judía verde','P1-P3',[3,4,5,6,7,8,9],'pod','#6aa84f'),
   it('Arveja y haba verde','P2-P4',[0,1,2,3,4],'pod','#86c06a'),
   it('Berros','nacientes y barrancos del norte',[0,1,2,3,11],'leafy','#3e8e4a')]}]
despensa=[
 {'t':'Gofio y grano','x':[it('Gofio de millo','millo de regadío · molinos de la isla',A,'sack','#d9c08a'),it('Gofio de trigo y cebada','P2-P4 · secano',A,'sack','#d9c08a'),it('Pan de trigo y centeno','horno de leña',A,'loaf','#c9914a')]},
 {'t':'Legumbres','x':[it('Judías (habichuelas)','regadío',A,'sack','#b98a6a'),it('Garbanzos y lentejas','P2-P3 · secano',A,'sack','#e0c890'),it('Chochos','P2-P3 · secano',A,'sack','#eadb8a'),it('Habas y arvejas secas','P3-P4 · secano',A,'sack','#a9b46a')]},
 {'t':'Aceite y grasa','x':[it('Aceite de oliva','olivo · 112 ha hoy · almazaras del sur',A,'bottle','#8a9a2a'),it('Aceite de girasol','girasol · medianías',A,'bottle','#f2c22a'),it('Manteca de cochino','matanza',A,'jar','#f4efe2')]},
 {'t':'Conservas y salazones','x':[it('Pescado salado (jareas)','secado al sol',A,'fish','#c9b48a'),it('Atún y bonito en aceite','conserva casera',A,'jar','#c99a5a'),it('Tomate y pimienta en conserva','excedente de verano',A,'jar','#d24a2a'),it('Higos y uvas pasas','secado al sol',A,'sack','#7a4a5a'),it('Mojo (pimienta, ajo, cilantro)','huerta',A,'jar','#b8322a')]},
 {'t':'Dulce','x':[it('Miel de Tenerife','DOP · abeja negra canaria',A,'jar','#e8a21a'),it('Miel de caña','caña de azúcar · 1,2 ha hoy · antecedente',A,'jar','#6a3a1a'),it('Mermeladas','guayaba, higo, durazno, naranja',A,'jar','#c2304a'),it('Rosquetes y almendrados','almendra, miel, huevo',A,'jar','#e6c27a'),it('Frangollo y rapadura','millo, miel, almendra',A,'sweet','#b07a3a'),it('Truchas de batata','batata, almendra, masa de trigo',[10,11,0],'sweet','#d9a35a'),it('Quesadillas y huevos moles','queso, huevo, trigo, miel',A,'sweet','#e8c27a')]},
 {'t':'Bebidas','x':[it('Vino','DO Tacoronte-Acentejo, Valle de La Orotava, Ycoden-Daute-Isora, Abona y Güímar',A,'bottle','#6e1f2e'),it('Café','arábica · plantaciones testimoniales',A,'bag','#5a3a22'),it('Aguardiente y licores','orujo, miel, frutas',A,'bottle','#cfd8dc'),it('Infusiones','hierbaluisa, poleo, menta, tomillo',A,'jar','#9ab86a')]},
 {'t':'No alimentario','x':[it('Tabaco','0,3 ha en el Mapa de Cultivos · antecedente',A,'box','#8a5a32'),it('Sal','salinas de la costa · antecedente histórico',A,'jar','#f2f2f2'),it('Aloe vera','14,7 ha hoy · cosmética y botiquín',A,'jar','#9ad0a0')]}]
huecos=[{'n':'Arroz','o':'marginal: falta calor'},{'n':'Té y cacao','o':'posibles, sin experiencia en la isla'},{'n':'Pimienta negra, canela, clavo, vainilla','o':'marginales o imposibles'},{'n':'Azúcar blanco a escala','o':'caña viable, sin refinería'},{'n':'Pasta y harina refinada en volumen','o':'trigo de secano limitado'},{'n':'Calorías para 962.000 personas','o':'la tierra cubre una quinta parte: el hueco mayor'}]
menu=[{'d':'Lunes','de':'Café con leche y gofio escaldado','al':'Potaje de berros con papas, millo y costilla','ce':'Papas arrugadas con mojo y queso de cabra'},
 {'d':'Martes','de':'Yogur con miel de Tenerife y plátano','al':'Vieja sancochada con papas y mojo verde','ce':'Ensalada de tomate, cebolla y aguacate'},
 {'d':'Miércoles','de':'Pan de millo con mantequilla y mermelada de guayaba','al':'Puchero canario (col, calabaza, bubango, garbanzos)','ce':'Queso asado con mojo y batata'},
 {'d':'Jueves','de':'Gofio amasado con miel de caña','al':'Conejo en salmorejo con papas','ce':'Tortilla de papas y queso tierno de vaca'},
 {'d':'Viernes','de':'Leche de cabra y fruta del tiempo','al':'Chicharros fritos con papas bonitas y mojo','ce':'Escaldón de gofio con caldo de pescado'},
 {'d':'Sábado','de':'Frangollo (millo, leche, almendra)','al':'Cabrito en adobo con papas y ñame','ce':'Rancho canario (fideos de trigo, garbanzos, papas)'},
 {'d':'Domingo','de':'Café, quesadilla y huevos moles','al':'Carne fiesta de cochino negro con papas y mojo','ce':'Castañas asadas, higos pasados y vino de Tacoronte'}]
botiquin={'grupos':[
 {'t':'Plantas medicinales de la huerta y el monte','e':'posible','x':['Aloe vera (ya en el Mapa de Cultivos: 14,7 ha)','Manzanilla, hierbaluisa, poleo, menta y hierbabuena','Tomillo, romero, salvia y llantén','Eucalipto (hojas para vahos)','Sauce canario: su corteza contiene salicina, el antecedente natural de la aspirina','Uso tradicional; eficacia variable y sin dosis controlada']},
 {'t':'Lo que se elabora con la despensa','e':'posible','x':['Alcohol de alta graduación destilado de caña o uva, para desinfectar superficies e instrumental','Jabón de aceite de oliva y potasa de ceniza','Miel (uso tradicional en curas)','Sal y vinagre','Suero oral casero con agua, sal y azúcar (receta de la OMS)','Alimentación suficiente: la primera medicina preventiva']},
 {'t':'Lo que ya hay en la isla y aguanta un tiempo','e':'limite','x':['Hospital Universitario de Canarias, Hospital Universitario Nuestra Señora de Candelaria, hospitales del norte y del sur, centros de salud y su personal','Cirugía, partos, urgencias, UCI y fisioterapia','Esterilización en autoclave y oxígeno de concentradores, con electricidad de la isla','Todo depende del material fungible y de los repuestos almacenados: con 962.000 habitantes las existencias duran menos']},
 {'t':'Adormidera','e':'limite','x':['Viable en el clima (secano de medianías)','De ella salen los analgésicos opiáceos','Su cultivo y transformación para uso farmacéutico están sujetos a control estatal de estupefacientes y requieren industria']},
 {'t':'Lo que siempre vendría de fuera','e':'imposible','x':['Antibióticos, vacunas e insulina','Anestésicos, anticoagulantes, quimioterapia, antirretrovirales y hormonas','Reactivos de laboratorio, contraste y radiofármacos','Jeringas, guantes, sondas, suturas y material estéril de un solo uso','Lentes, audífonos, prótesis y repuestos de equipos médicos']}],
 'conclusion':'<strong>Tenerife no podría cerrar la despensa, y mucho menos el botiquín.</strong> Con plantas, alcohol, jabón, miel y buena alimentación se cubre la higiene y parte del alivio de síntomas. La medicina moderna (antibióticos, vacunas, insulina, anestesia, material estéril) depende de una industria química y farmacéutica que no cabe en una isla. En un mundo cerrado, los hospitales funcionarían mientras duraran sus existencias; la medicina es la dependencia exterior más dura, y la comida, con casi un millón de habitantes, la segunda. [INFERENCIA]'}
json.dump({'nevera':{'nevera':nevera,'despensa':despensa,'huecos':huecos},'menu':menu,'botiquin':botiquin},open('04b_cocina_tf.json','w'),ensure_ascii=False)
print('ok',sum(len(b['x']) for b in nevera),'nevera',sum(len(b['x']) for b in despensa),'despensa')
