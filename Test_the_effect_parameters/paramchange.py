from xml.dom.minidom import parse
import numpy as np
#1.参数字典
alphaCO2 = {'name':'alphaCO2','formname':'effect_of_atmospheric_CO2_concentration','formorder':1,'orderinform':0,'type':'real','min':1,'max':2}
tdmin = {'name':'tdmin','formname':'phasic_development','formorder':2,'orderinform':0,'type':'real','min':-10,'max':15}
tdmax = {'name':'tdmax','formname':'phasic_development','formorder':2,'orderinform':1,'type':'real','min':15,'max':40}
coeflevamf = {'name':'coeflevamf','formname':'phasic_development','formorder':2,'orderinform':2,'type':'real','min':1,'max':2}
coefamflax = {'name':'coefamflax','formname':'phasic_development','formorder':2,'orderinform':3,'type':'real','min':1,'max':2}
coeflaxsen = {'name':'coeflaxsen','formname':'phasic_development','formorder':2,'orderinform':4,'type':'real','min':1,'max':2}
coefsenlan = {'name':'coefsenlan','formname':'phasic_development','formorder':2,'orderinform':5,'type':'real','min':1,'max':2}
coeflevdrp = {'name':'coeflevdrp','formname':'phasic_development','formorder':2,'orderinform':6,'type':'real','min':1,'max':2}
coefdrpmat = {'name':'coefdrpmat','formname':'phasic_development','formorder':2,'orderinform':7,'type':'real','min':1,'max':2}
coefflodrp = {'name':'coefflodrp','formname':'phasic_development','formorder':2,'orderinform':8,'type':'real','min':1,'max':2}
phobase = {'name':'phobase','formname':'phasic_development','formorder':2,'orderinform':9,'type':'real','min':0,'max':24}
phosat = {'name':'phosat','formname':'phasic_development','formorder':2,'orderinform':10,'type':'real','min':0,'max':24}
stressdev = {'name':'stressdev','formname':'phasic_development','formorder':2,'orderinform':11,'type':'real','min':0.1,'max':0.9}
jvcmini = {'name':'jvcmini','formname':'phasic_development','formorder':2,'orderinform':12,'type':'int','min':0,'max':7}
julvernal = {'name':'julvernal','formname':'phasic_development','formorder':2,'orderinform':13,'type':'int','min':1,'max':731}
tfroid = {'name':'tfroid','formname':'phasic_development','formorder':2,'orderinform':14,'type':'real','min':-5,'max':10}
ampfroid = {'name':'ampfroid','formname':'phasic_development','formorder':2,'orderinform':15,'type':'real','min':1,'max':30}
stdordebour = {'name':'stdordebour','formname':'phasic_development','formorder':2,'orderinform':16,'type':'real','min':0,'max':20000}
tdmindeb = {'name':'tdmindeb','formname':'phasic_development','formorder':2,'orderinform':17,'type':'real','min':0,'max':40}
tdmaxdeb = {'name':'tdmaxdeb','formname':'phasic_development','formorder':2,'orderinform':18,'type':'real','min':0,'max':40}
ifindorm = {'name':'ifindorm','formname':'phasic_development','formorder':2,'orderinform':19,'type':'int','min':1,'max':731}
q10 = {'name':'q10','formname':'phasic_development','formorder':2,'orderinform':20,'type':'real','min':1.5,'max':3.5}
idebdorm = {'name':'idebdorm','formname':'phasic_development','formorder':2,'orderinform':21,'type':'int','min':1,'max':731}
tgmin = {'name':'tgmin','formname':'emergence_and_starting','formorder':3,'orderinform':0,'type':'real','min':-10,'max':15}
nbfeuilplant = {'name':'nbfeuilplant','formname':'emergence_and_starting','formorder':3,'orderinform':1,'type':'int','min':0,'max':10}
stpltger = {'name':'stpltger','formname':'emergence_and_starting','formorder':3,'orderinform':2,'type':'real','min':0,'max':100}
potgermi = {'name':'potgermi','formname':'emergence_and_starting','formorder':3,'orderinform':3,'type':'real','min':0.0001,'max':1}
nbjgerlim = {'name':'nbjgerlim','formname':'emergence_and_starting','formorder':3,'orderinform':4,'type':'int','min':1,'max':50}
propjgermin = {'name':'propjgermin','formname':'emergence_and_starting','formorder':3,'orderinform':5,'type':'real','min':0,'max':100}
belong = {'name':'belong','formname':'emergence_and_starting','formorder':3,'orderinform':6,'type':'real','min':0.005,'max':0.04}
celong = {'name':'celong','formname':'emergence_and_starting','formorder':3,'orderinform':7,'type':'real','min':1,'max':10}
elmax = {'name':'elmax','formname':'emergence_and_starting','formorder':3,'orderinform':8,'type':'real','min':2,'max':40}
nlevlim1 = {'name':'nlevlim1','formname':'emergence_and_starting','formorder':3,'orderinform':9,'type':'int','min':1,'max':100}
nlevlim2 = {'name':'nlevlim2','formname':'emergence_and_starting','formorder':3,'orderinform':10,'type':'int','min':1,'max':100}
vigueurbat = {'name':'vigueurbat','formname':'emergence_and_starting','formorder':3,'orderinform':11,'type':'real','min':0.0001,'max':1}
laiplantule = {'name':'laiplantule','formname':'emergence_and_starting','formorder':3,'orderinform':12,'type':'real','min':0,'max':8}
masecplantule = {'name':'masecplantule','formname':'emergence_and_starting','formorder':3,'orderinform':13,'type':'real','min':0.002,'max':4}
zracplantule = {'name':'zracplantule','formname':'emergence_and_starting','formorder':3,'orderinform':14,'type':'real','min':0,'max':200}
phyllotherme = {'name':'phyllotherme','formname':'leaves','formorder':4,'orderinform':0,'type':'real','min':10,'max':150}
bdens = {'name':'bdens','formname':'leaves','formorder':4,'orderinform':1,'type':'real','min':1,'max':200}
laicomp = {'name':'laicomp','formname':'leaves','formorder':4,'orderinform':2,'type':'real','min':0,'max':1}
hautbase = {'name':'hautbase','formname':'leaves','formorder':4,'orderinform':3,'type':'real','min':0.1,'max':2}
hautmax = {'name':'hautmax','formname':'leaves','formorder':4,'orderinform':4,'type':'real','min':0.1,'max':5}
tcmin = {'name':'tcmin','formname':'leaves','formorder':4,'orderinform':5,'type':'real','min':-10,'max':15}
tcmax = {'name':'tcmax','formname':'leaves','formorder':4,'orderinform':6,'type':'real','min':10,'max':50}
tcxstop = {'name':'tcxstop','formname':'leaves','formorder':4,'orderinform':7,'type':'real','min':0,'max':100}
vlaimax = {'name':'vlaimax','formname':'leaves','formorder':4,'orderinform':8,'type':'real','min':1.5,'max':2.5}
pentlaimax = {'name':'pentlaimax','formname':'leaves','formorder':4,'orderinform':9,'type':'real','min':0,'max':10}
udlaimax = {'name':'udlaimax','formname':'leaves','formorder':4,'orderinform':10,'type':'real','min':1,'max':3}
ratiodurvieI = {'name':'ratiodurvieI','formname':'leaves','formorder':4,'orderinform':11,'type':'real','min':0,'max':1}
ratiosen = {'name':'ratiosen','formname':'leaves','formorder':4,'orderinform':12,'type':'real','min':0,'max':1}
abscission = {'name':'abscission','formname':'leaves','formorder':4,'orderinform':13,'type':'real','min':0,'max':100}
parazofmorte = {'name':'parazofmorte','formname':'leaves','formorder':4,'orderinform':14,'type':'real','min':10,'max':20}
innturgmin = {'name':'innturgmin','formname':'leaves','formorder':4,'orderinform':15,'type':'real','min':-2,'max':1}
dlaimin = {'name':'dlaimin','formname':'leaves','formorder':4,'orderinform':16,'type':'real','min':0.01,'max':1}
dlaimax = {'name':'dlaimax','formname':'leaves','formorder':4,'orderinform':17,'type':'real','min':0.000005,'max':0.5}
tustressmin = {'name':'tustressmin','formname':'leaves','formorder':4,'orderinform':18,'type':'real','min':0.3,'max':1}
dlaimaxbrut = {'name':'dlaimaxbrut','formname':'leaves','formorder':4,'orderinform':19,'type':'real','min':0.000005,'max':0.5}
durviesupmax = {'name':'durviesupmax','formname':'leaves','formorder':4,'orderinform':20,'type':'real','min':0,'max':1}
innsen = {'name':'innsen','formname':'leaves','formorder':4,'orderinform':21,'type':'real','min':-2,'max':1}
rapsenturg = {'name':'rapsenturg','formname':'leaves','formorder':4,'orderinform':22,'type':'real','min':0.5,'max':1.5}
phobasesen = {'name':'phobasesen','formname':'leaves','formorder':4,'orderinform':23,'type':'real','min':1,'max':12}
dltamsmaxsen = {'name':'dltamsmaxsen','formname':'leaves','formorder':4,'orderinform':24,'type':'real','min':0.01,'max':0.1}
dltamsminsen = {'name':'dltamsminsen','formname':'leaves','formorder':4,'orderinform':25,'type':'real','min':0.01,'max':0.1}
alphaphot = {'name':'alphaphot','formname':'leaves','formorder':4,'orderinform':26,'type':'real','min':0,'max':1000}
tauxrecouvmax = {'name':'tauxrecouvmax','formname':'leaves','formorder':4,'orderinform':27,'type':'real','min':0.5,'max':1}
tauxrecouvkmax = {'name':'tauxrecouvkmax','formname':'leaves','formorder':4,'orderinform':28,'type':'real','min':0.5,'max':1}
pentrecouv = {'name':'pentrecouv','formname':'leaves','formorder':4,'orderinform':29,'type':'real','min':0,'max':10}
infrecouv = {'name':'infrecouv','formname':'leaves','formorder':4,'orderinform':30,'type':'real','min':0,'max':3}
extin = {'name':'extin','formname':'radiation_interception','formorder':5,'orderinform':0,'type':'real','min':0.1,'max':1.5}
ktrou = {'name':'ktrou','formname':'radiation_interception','formorder':5,'orderinform':1,'type':'real','min':0.1,'max':2}
forme = {'name':'forme','formname':'radiation_interception','formorder':5,'orderinform':2,'type':'int','min':1,'max':3}
rapforme = {'name':'rapforme','formname':'radiation_interception','formorder':5,'orderinform':3,'type':'real','min':-5,'max':5}
adfol = {'name':'adfol','formname':'radiation_interception','formorder':5,'orderinform':4,'type':'real','min':-10,'max':10}
dfolbas = {'name':'dfolbas','formname':'radiation_interception','formorder':5,'orderinform':5,'type':'real','min':1,'max':10}
dfolhaut = {'name':'dfolhaut','formname':'radiation_interception','formorder':5,'orderinform':6,'type':'real','min':1,'max':10}
temin = {'name':'temin','formname':'shoot_biomass_growth','formorder':6,'orderinform':0,'type':'real','min':-10,'max':15}
temax = {'name':'temax','formname':'shoot_biomass_growth','formorder':6,'orderinform':1,'type':'real','min':15,'max':40}
teopt = {'name':'teopt','formname':'shoot_biomass_growth','formorder':6,'orderinform':2,'type':'real','min':10,'max':30}
teoptbis = {'name':'teoptbis','formname':'shoot_biomass_growth','formorder':6,'orderinform':3,'type':'real','min':10,'max':30}
efcroijuv = {'name':'efcroijuv','formname':'shoot_biomass_growth','formorder':6,'orderinform':4,'type':'real','min':1,'max':7}
efcroiveg = {'name':'efcroiveg','formname':'shoot_biomass_growth','formorder':6,'orderinform':5,'type':'real','min':1,'max':10}
efcroirepro = {'name':'efcroirepro','formname':'shoot_biomass_growth','formorder':6,'orderinform':6,'type':'real','min':1,'max':10}
remobres = {'name':'remobres','formname':'shoot_biomass_growth','formorder':6,'orderinform':7,'type':'real','min':0,'max':0.5}
coefmshaut = {'name':'coefmshaut','formname':'shoot_biomass_growth','formorder':6,'orderinform':8,'type':'real','min':2,'max':50}
slamax = {'name':'slamax','formname':'partitioning_of_biomass_in_organs','formorder':7,'orderinform':0,'type':'real','min':50,'max':500}
slamin = {'name':'slamin','formname':'partitioning_of_biomass_in_organs','formorder':7,'orderinform':1,'type':'real','min':50,'max':500}
tigefeuil = {'name':'tigefeuil','formname':'partitioning_of_biomass_in_organs','formorder':7,'orderinform':2,'type':'real','min':0,'max':3}
envfruit = {'name':'envfruit','formname':'partitioning_of_biomass_in_organs','formorder':7,'orderinform':3,'type':'real','min':0,'max':0.5}
sea = {'name':'sea','formname':'partitioning_of_biomass_in_organs','formorder':7,'orderinform':4,'type':'real','min':0,'max':300}
nbjgrain = {'name':'nbjgrain','formname':'yield_information','formorder':8,'orderinform':0,'type':'int','min':5,'max':40}
cgrain = {'name':'cgrain','formname':'yield_information','formorder':8,'orderinform':1,'type':'real','min':0.01,'max':1}
cgrainv0 = {'name':'cgrainv0','formname':'yield_information','formorder':8,'orderinform':2,'type':'real','min':0,'max':15000}
nbgrmin = {'name':'nbgrmin','formname':'yield_information','formorder':8,'orderinform':3,'type':'real','min':0,'max':10000}
nboite = {'name':'nboite','formname':'yield_information','formorder':8,'orderinform':4,'type':'real','min':1,'max':20}
allocfrmax = {'name':'allocfrmax','formname':'yield_information','formorder':8,'orderinform':5,'type':'real','min':0.05,'max':1}
afpf = {'name':'afpf','formname':'yield_information','formorder':8,'orderinform':6,'type':'real','min':0.01,'max':1}
bfpf = {'name':'bfpf','formname':'yield_information','formorder':8,'orderinform':7,'type':'real','min':0,'max':30}
cfpf = {'name':'cfpf','formname':'yield_information','formorder':8,'orderinform':8,'type':'real','min':0.1,'max':100}
dfpf = {'name':'dfpf','formname':'yield_information','formorder':8,'orderinform':9,'type':'real','min':0.01,'max':5}
stdrpnou = {'name':'stdrpnou','formname':'yield_information','formorder':8,'orderinform':10,'type':'real','min':0,'max':6000}
spfrmin = {'name':'spfrmin','formname':'yield_information','formorder':8,'orderinform':11,'type':'real','min':0,'max':1}
spfrmax = {'name':'spfrmax','formname':'yield_information','formorder':8,'orderinform':12,'type':'real','min':0.7,'max':2}
splaimin = {'name':'splaimin','formname':'yield_information','formorder':8,'orderinform':13,'type':'real','min':0.01,'max':1}
splaimax = {'name':'splaimax','formname':'yield_information','formorder':8,'orderinform':14,'type':'real','min':0.7,'max':2}
nbinflo = {'name':'nbinflo','formname':'yield_information','formorder':8,'orderinform':15,'type':'real','min':1,'max':1000}
inflomax = {'name':'inflomax','formname':'yield_information','formorder':8,'orderinform':16,'type':'real','min':0,'max':100}
pentinflores = {'name':'pentinflores','formname':'yield_information','formorder':8,'orderinform':17,'type':'real','min':0,'max':10}
tminremp = {'name':'tminremp','formname':'yield_information','formorder':8,'orderinform':18,'type':'real','min':0,'max':20}
tmaxremp = {'name':'tmaxremp','formname':'yield_information','formorder':8,'orderinform':19,'type':'real','min':10,'max':40}
vitpropsucre = {'name':'vitpropsucre','formname':'yield_information','formorder':8,'orderinform':20,'type':'real','min':0.001,'max':0.01}
vitprophuile = {'name':'vitprophuile','formname':'yield_information','formorder':8,'orderinform':21,'type':'real','min':0.001,'max':0.01}
vitirazo = {'name':'vitirazo','formname':'yield_information','formorder':8,'orderinform':22,'type':'real','min':0.001,'max':0.04}
vitircarb = {'name':'vitircarb','formname':'yield_information','formorder':8,'orderinform':23,'type':'real','min':0.001,'max':0.02}
irmax = {'name':'irmax','formname':'yield_information','formorder':8,'orderinform':24,'type':'real','min':0.2,'max':1}
sensanox = {'name':'sensanox','formname':'root','formorder':9,'orderinform':0,'type':'real','min':0,'max':1}
stoprac = {'name':'stoprac','formname':'root','formorder':9,'orderinform':1,'type':'cha','min':0,'max':100}
sensrsec = {'name':'sensrsec','formname':'root','formorder':9,'orderinform':2,'type':'real','min':0,'max':1}
contrdamax = {'name':'contrdamax','formname':'root','formorder':9,'orderinform':3,'type':'real','min':0,'max':1}
zlabour = {'name':'zlabour','formname':'root','formorder':9,'orderinform':4,'type':'real','min':0,'max':100}
zpente = {'name':'zpente','formname':'root','formorder':9,'orderinform':5,'type':'real','min':10,'max':200}
zprlim = {'name':'zprlim','formname':'root','formorder':9,'orderinform':6,'type':'real','min':10,'max':200}
draclong = {'name':'draclong','formname':'root','formorder':9,'orderinform':7,'type':'real','min':1,'max':1000}
debsenrac = {'name':'debsenrac','formname':'root','formorder':9,'orderinform':8,'type':'real','min':0,'max':2000}
lvfront = {'name':'lvfront','formname':'root','formorder':9,'orderinform':9,'type':'real','min':0.02,'max':1}
longsperac = {'name':'longsperac','formname':'root','formorder':9,'orderinform':10,'type':'real','min':250,'max':25000}
minefnra = {'name':'minefnra','formname':'root','formorder':9,'orderinform':11,'type':'real','min':0,'max':1}
minazorac = {'name':'minazorac','formname':'root','formorder':9,'orderinform':12,'type':'real','min':0,'max':5}
maxazorac = {'name':'maxazorac','formname':'root','formorder':9,'orderinform':13,'type':'real','min':0.1,'max':5}
repracpermax = {'name':'repracpermax','formname':'root','formorder':9,'orderinform':14,'type':'real','min':0.1,'max':0.9}
repracpermin = {'name':'repracpermin','formname':'root','formorder':9,'orderinform':15,'type':'real','min':0.1,'max':0.9}
krepracperm = {'name':'krepracperm','formname':'root','formorder':9,'orderinform':16,'type':'real','min':0.0001,'max':1}
repracseumax = {'name':'repracseumax','formname':'root','formorder':9,'orderinform':17,'type':'real','min':0.1,'max':0.9}
repracseumin = {'name':'repracseumin','formname':'root','formorder':9,'orderinform':18,'type':'real','min':0.1,'max':0.9}
krepracseu = {'name':'krepracseu','formname':'root','formorder':9,'orderinform':19,'type':'real','min':0.0001,'max':1}
tletale = {'name':'tletale','formname':'frost','formorder':10,'orderinform':0,'type':'real','min':-30,'max':-1}
tdebgel = {'name':'tdebgel','formname':'frost','formorder':10,'orderinform':1,'type':'real','min':-5,'max':5}
nbfgellev = {'name':'nbfgellev','formname':'frost','formorder':10,'orderinform':2,'type':'int','min':1,'max':5}
tgellev10 = {'name':'tgellev10','formname':'frost','formorder':10,'orderinform':3,'type':'real','min':-25,'max':0}
tgellev90 = {'name':'tgellev90','formname':'frost','formorder':10,'orderinform':4,'type':'real','min':-25,'max':0}
tgeljuv10 = {'name':'tgeljuv10','formname':'frost','formorder':10,'orderinform':5,'type':'real','min':-25,'max':0}
tgeljuv90 = {'name':'tgeljuv90','formname':'frost','formorder':10,'orderinform':6,'type':'real','min':-25,'max':0}
tgelveg10 = {'name':'tgelveg10','formname':'frost','formorder':10,'orderinform':7,'type':'real','min':-25,'max':0}
tgelveg90 = {'name':'tgelveg90','formname':'frost','formorder':10,'orderinform':8,'type':'real','min':-25,'max':0}
tgelflo10 = {'name':'tgelflo10','formname':'frost','formorder':10,'orderinform':9,'type':'real','min':-25,'max':0}
tgelflo90 = {'name':'tgelflo90','formname':'frost','formorder':10,'orderinform':10,'type':'real','min':-25,'max':0}
psisto = {'name':'psisto','formname':'water','formorder':11,'orderinform':0,'type':'real','min':1,'max':25}
psiturg = {'name':'psiturg','formname':'water','formorder':11,'orderinform':1,'type':'real','min':1,'max':15}
h2ofeuilverte = {'name':'h2ofeuilverte','formname':'water','formorder':11,'orderinform':2,'type':'real','min':0.5,'max':1}
h2ofeuiljaune = {'name':'h2ofeuiljaune','formname':'water','formorder':11,'orderinform':3,'type':'real','min':0.05,'max':1}
h2otigestruc = {'name':'h2otigestruc','formname':'water','formorder':11,'orderinform':4,'type':'real','min':0.5,'max':1}
h2oreserve = {'name':'h2oreserve','formname':'water','formorder':11,'orderinform':5,'type':'real','min':0.5,'max':1}
h2ofrvert = {'name':'h2ofrvert','formname':'water','formorder':11,'orderinform':6,'type':'real','min':0.1,'max':1}
deshydbase = {'name':'deshydbase','formname':'water','formorder':11,'orderinform':7,'type':'real','min':-0.02,'max':0.02}
tempdeshyd = {'name':'tempdeshyd','formname':'water','formorder':11,'orderinform':8,'type':'real','min':0.0004,'max':0.05}
kmax = {'name':'kmax','formname':'water','formorder':11,'orderinform':9,'type':'real','min':0.5,'max':4}
rsmin = {'name':'rsmin','formname':'water','formorder':11,'orderinform':10,'type':'real','min':20,'max':500}
mouillabil = {'name':'mouillabil','formname':'water','formorder':11,'orderinform':11,'type':'real','min':0.05,'max':3}
stemflowmax = {'name':'stemflowmax','formname':'water','formorder':11,'orderinform':12,'type':'real','min':0,'max':1}
kstemflow = {'name':'kstemflow','formname':'water','formorder':11,'orderinform':13,'type':'real','min':0.1,'max':2}
Vmax1 = {'name':'Vmax1','formname':'nitrogen','formorder':12,'orderinform':0,'type':'real','min':0.0002,'max':0.01}
Kmabs1 = {'name':'Kmabs1','formname':'nitrogen','formorder':12,'orderinform':1,'type':'real','min':20,'max':200}
Vmax2 = {'name':'Vmax2','formname':'nitrogen','formorder':12,'orderinform':2,'type':'real','min':0.002,'max':0.1}
Kmabs2 = {'name':'Kmabs2','formname':'nitrogen','formorder':12,'orderinform':3,'type':'real','min':4000,'max':40000}
adil = {'name':'adil','formname':'nitrogen','formorder':12,'orderinform':4,'type':'real','min':1,'max':7}
bdil = {'name':'bdil','formname':'nitrogen','formorder':12,'orderinform':5,'type':'real','min':0.01,'max':0.8}
masecNmax = {'name':'masecNmax','formname':'nitrogen','formorder':12,'orderinform':6,'type':'real','min':0.05,'max':5}
INNmin = {'name':'INNmin','formname':'nitrogen','formorder':12,'orderinform':7,'type':'real','min':0,'max':1}
INNimin = {'name':'INNimin','formname':'nitrogen','formorder':12,'orderinform':8,'type':'real','min':0,'max':1}
inngrain1 = {'name':'inngrain1','formname':'nitrogen','formorder':12,'orderinform':9,'type':'real','min':0.3,'max':2}
inngrain2 = {'name':'inngrain2','formname':'nitrogen','formorder':12,'orderinform':10,'type':'real','min':0.3,'max':2}
bdilmax = {'name':'bdilmax','formname':'nitrogen','formorder':12,'orderinform':11,'type':'real','min':0.01,'max':0.8}
adilmax = {'name':'adilmax','formname':'nitrogen','formorder':12,'orderinform':12,'type':'real','min':3,'max':10}
Nmeta = {'name':'Nmeta','formname':'nitrogen','formorder':12,'orderinform':13,'type':'real','min':0,'max':100}
masecmeta = {'name':'masecmeta','formname':'nitrogen','formorder':12,'orderinform':14,'type':'real','min':0.1,'max':1}
Nreserve = {'name':'Nreserve','formname':'nitrogen','formorder':12,'orderinform':15,'type':'real','min':0,'max':100}
stlevdno = {'name':'stlevdno','formname':'nitrogen','formorder':12,'orderinform':16,'type':'real','min':0,'max':500}
stdnofno = {'name':'stdnofno','formname':'nitrogen','formorder':12,'orderinform':17,'type':'real','min':0,'max':500}
stfnofvino = {'name':'stfnofvino','formname':'nitrogen','formorder':12,'orderinform':18,'type':'real','min':0,'max':500}
vitno = {'name':'vitno','formname':'nitrogen','formorder':12,'orderinform':19,'type':'real','min':0.001,'max':0.01}
profnod = {'name':'profnod','formname':'nitrogen','formorder':12,'orderinform':20,'type':'real','min':10,'max':50}
concNnodseuil = {'name':'concNnodseuil','formname':'nitrogen','formorder':12,'orderinform':21,'type':'real','min':0,'max':10}
concNrac0 = {'name':'concNrac0','formname':'nitrogen','formorder':12,'orderinform':22,'type':'real','min':0,'max':10}
concNrac100 = {'name':'concNrac100','formname':'nitrogen','formorder':12,'orderinform':23,'type':'real','min':0,'max':2}
tempnod1 = {'name':'tempnod1','formname':'nitrogen','formorder':12,'orderinform':24,'type':'real','min':-10,'max':40}
tempnod2 = {'name':'tempnod2','formname':'nitrogen','formorder':12,'orderinform':25,'type':'real','min':-10,'max':40}
tempnod3 = {'name':'tempnod3','formname':'nitrogen','formorder':12,'orderinform':26,'type':'real','min':-10,'max':40}
tempnod4 = {'name':'tempnod4','formname':'nitrogen','formorder':12,'orderinform':27,'type':'real','min':-10,'max':40}
fixmax = {'name':'fixmax','formname':'nitrogen','formorder':12,'orderinform':28,'type':'real','min':2,'max':12}
fixmaxveg = {'name':'fixmaxveg','formname':'nitrogen','formorder':12,'orderinform':29,'type':'real','min':0,'max':50}
fixmaxgr = {'name':'fixmaxgr','formname':'nitrogen','formorder':12,'orderinform':30,'type':'real','min':0,'max':50}
stlevamf = {'name':'stlevamf','formname':'cultivar_parameters','formorder':14,'orderinform':0,'type':'real','min':0,'max':6000}
stamflax = {'name':'stamflax','formname':'cultivar_parameters','formorder':14,'orderinform':1,'type':'real','min':0,'max':6000}
stlevdrp = {'name':'stlevdrp','formname':'cultivar_parameters','formorder':14,'orderinform':2,'type':'real','min':0,'max':6000}
stflodrp = {'name':'stflodrp','formname':'cultivar_parameters','formorder':14,'orderinform':3,'type':'real','min':0,'max':500}
stdrpdes = {'name':'stdrpdes','formname':'cultivar_parameters','formorder':14,'orderinform':4,'type':'real','min':0,'max':900}
pgrainmaxi = {'name':'pgrainmaxi','formname':'cultivar_parameters','formorder':14,'orderinform':5,'type':'real','min':0,'max':5}
adens = {'name':'adens','formname':'cultivar_parameters','formorder':14,'orderinform':6,'type':'real','min':-2,'max':0}
croirac = {'name':'croirac','formname':'cultivar_parameters','formorder':14,'orderinform':7,'type':'real','min':0,'max':0.5}
durvieF = {'name':'durvieF','formname':'cultivar_parameters','formorder':14,'orderinform':8,'type':'real','min':10,'max':500}
jvc = {'name':'jvc','formname':'cultivar_parameters','formorder':14,'orderinform':9,'type':'int','min':0,'max':70}
sensiphot = {'name':'sensiphot','formname':'cultivar_parameters','formorder':14,'orderinform':10,'type':'real','min':0,'max':1}
stlaxsen = {'name':'stlaxsen','formname':'cultivar_parameters','formorder':14,'orderinform':11,'type':'real','min':0,'max':6000}
stsenlan = {'name':'stsenlan','formname':'cultivar_parameters','formorder':14,'orderinform':12,'type':'real','min':0,'max':6000}
nbgrmax = {'name':'nbgrmax','formname':'cultivar_parameters','formorder':14,'orderinform':13,'type':'real','min':0,'max':1000000}
stdrpmat = {'name':'stdrpmat','formname':'cultivar_parameters','formorder':14,'orderinform':14,'type':'real','min':0,'max':2000}
afruitpot = {'name':'afruitpot','formname':'cultivar_parameters','formorder':14,'orderinform':15,'type':'real','min':0.5,'max':20}
dureefruit = {'name':'dureefruit','formname':'cultivar_parameters','formorder':14,'orderinform':16,'type':'real','min':10,'max':2000}

#字典列表
pardictionary = [alphaCO2,tdmin,tdmax,coeflevamf,coefamflax,coeflaxsen,coefsenlan,coeflevdrp,coefdrpmat,coefflodrp,phobase,phosat,stressdev,jvcmini,julvernal,tfroid,ampfroid,stdordebour,tdmindeb,tdmaxdeb,ifindorm,q10,idebdorm,tgmin,nbfeuilplant,stpltger,potgermi,nbjgerlim,propjgermin,belong,celong,elmax,nlevlim1,nlevlim2,vigueurbat,laiplantule,masecplantule,zracplantule,phyllotherme,bdens,laicomp,hautbase,hautmax,tcmin,tcmax,tcxstop,vlaimax,pentlaimax,udlaimax,ratiodurvieI,ratiosen,abscission,parazofmorte,innturgmin,dlaimin,dlaimax,tustressmin,dlaimaxbrut,durviesupmax,innsen,rapsenturg,phobasesen,dltamsmaxsen,dltamsminsen,alphaphot,tauxrecouvmax,tauxrecouvkmax,pentrecouv,infrecouv,extin,ktrou,forme,rapforme,adfol,dfolbas,dfolhaut,temin,temax,teopt,teoptbis,efcroijuv,efcroiveg,efcroirepro,remobres,coefmshaut,slamax,slamin,tigefeuil,envfruit,sea,nbjgrain,cgrain,cgrainv0,nbgrmin,nboite,allocfrmax,afpf,bfpf,cfpf,dfpf,stdrpnou,spfrmin,spfrmax,splaimin,splaimax,nbinflo,inflomax,pentinflores,tminremp,tmaxremp,vitpropsucre,vitprophuile,vitirazo,vitircarb,irmax,sensanox,stoprac,sensrsec,contrdamax,zlabour,zpente,zprlim,draclong,debsenrac,lvfront,longsperac,minefnra,minazorac,maxazorac,repracpermax,repracpermin,krepracperm,repracseumax,repracseumin,krepracseu,tletale,tdebgel,nbfgellev,tgellev10,tgellev90,tgeljuv10,tgeljuv90,tgelveg10,tgelveg90,tgelflo10,tgelflo90,psisto,psiturg,h2ofeuilverte,h2ofeuiljaune,h2otigestruc,h2oreserve,h2ofrvert,deshydbase,tempdeshyd,kmax,rsmin,mouillabil,stemflowmax,kstemflow,Vmax1,Kmabs1,Vmax2,Kmabs2,adil,bdil,masecNmax,INNmin,INNimin,inngrain1,inngrain2,bdilmax,adilmax,Nmeta,masecmeta,Nreserve,stlevdno,stdnofno,stfnofvino,vitno,profnod,concNnodseuil,concNrac0,concNrac100,tempnod1,tempnod2,tempnod3,tempnod4,fixmax,fixmaxveg,fixmaxgr,stlevamf,stamflax,stlevdrp,stflodrp,stdrpdes,pgrainmaxi,adens,croirac,durvieF,jvc,sensiphot,stlaxsen,stsenlan,nbgrmax,stdrpmat,afruitpot,dureefruit]
pardictionaryname = ['alphaCO2','tdmin','tdmax','coeflevamf','coefamflax','coeflaxsen','coefsenlan','coeflevdrp','coefdrpmat','coefflodrp','phobase','phosat','stressdev','jvcmini','julvernal','tfroid','ampfroid','stdordebour','tdmindeb','tdmaxdeb','ifindorm','q10','idebdorm','tgmin','nbfeuilplant','stpltger','potgermi','nbjgerlim','propjgermin','belong','celong','elmax','nlevlim1','nlevlim2','vigueurbat','laiplantule','masecplantule','zracplantule','phyllotherme','bdens','laicomp','hautbase','hautmax','tcmin','tcmax','tcxstop','vlaimax','pentlaimax','udlaimax','ratiodurvieI','ratiosen','abscission','parazofmorte','innturgmin','dlaimin','dlaimax','tustressmin','dlaimaxbrut','durviesupmax','innsen','rapsenturg','phobasesen','dltamsmaxsen','dltamsminsen','alphaphot','tauxrecouvmax','tauxrecouvkmax','pentrecouv','infrecouv','extin','ktrou','forme','rapforme','adfol','dfolbas','dfolhaut','temin','temax','teopt','teoptbis','efcroijuv','efcroiveg','efcroirepro','remobres','coefmshaut','slamax','slamin','tigefeuil','envfruit','sea','nbjgrain','cgrain','cgrainv0','nbgrmin','nboite','allocfrmax','afpf','bfpf','cfpf','dfpf','stdrpnou','spfrmin','spfrmax','splaimin','splaimax','nbinflo','inflomax','pentinflores','tminremp','tmaxremp','vitpropsucre','vitprophuile','vitirazo','vitircarb','irmax','sensanox','stoprac','sensrsec','contrdamax','zlabour','zpente','zprlim','draclong','debsenrac','lvfront','longsperac','minefnra','minazorac','maxazorac','repracpermax','repracpermin','krepracperm','repracseumax','repracseumin','krepracseu','tletale','tdebgel','nbfgellev','tgellev10','tgellev90','tgeljuv10','tgeljuv90','tgelveg10','tgelveg90','tgelflo10','tgelflo90','psisto','psiturg','h2ofeuilverte','h2ofeuiljaune','h2otigestruc','h2oreserve','h2ofrvert','deshydbase','tempdeshyd','kmax','rsmin','mouillabil','stemflowmax','kstemflow','Vmax1','Kmabs1','Vmax2','Kmabs2','adil','bdil','masecNmax','INNmin','INNimin','inngrain1','inngrain2','bdilmax','adilmax','Nmeta','masecmeta','Nreserve','stlevdno','stdnofno','stfnofvino','vitno','profnod','concNnodseuil','concNrac0','concNrac100','tempnod1','tempnod2','tempnod3','tempnod4','fixmax','fixmaxveg','fixmaxgr','stlevamf','stamflax','stlevdrp','stflodrp','stdrpdes','pgrainmaxi','adens','croirac','durvieF','jvc','sensiphot','stlaxsen','stsenlan','nbgrmax','stdrpmat','afruitpot','dureefruit']
#函数：替换参数
def parset(parnamestr,parvalue,model_dir):
    if parnamestr in pardictionaryname:
        problem = 0
        parname = eval(parnamestr)
        if parname['type'] == 'cha':
            if type(parvalue) != str:
                print('The type of parmeter('+parnamestr+')is chr'+'\n')
                problem = 1
        elif parname['type'] == 'int':
            if type(parvalue) != int:
                print('The type of parmeter('+parnamestr+')is int'+'\n')
                problem = 1
            else:
                if parvalue > parname['max'] or parvalue < parname['min']:
                    print('Value out of range! range:['+str(parname['min'])+','+str(parname['max'])+']'+'\n')
                    problem = 1
        elif parname['type'] == 'real':
            if isinstance(parvalue,(np.int32, int, float, np.int8, np.int64, np.float64, np.float32)) == False:
                print('The type of parmeter('+parnamestr+')is real')
                problem = 1
            else:
                if parvalue > parname['max'] or parvalue < parname['min']:
                    print('Value out of range! range:['+str(parname['min'])+','+str(parname['max'])+']'+'\n')
                    problem = 1
        
        if problem == 0:
            if parname['formorder'] != 14:
                DOMTree = parse(model_dir) #读取文件为树
                fich_list = DOMTree.documentElement #list第一父节点元素
                formalisme = fich_list.getElementsByTagName('formalisme')[parname['formorder']]
                formalisme.getElementsByTagName('param')[parname['orderinform']].childNodes[0].data = parvalue
                with open(model_dir, 'w') as f:
                    fich_list.writexml(f)
            else:
                DOMTree = parse(model_dir) #读取文件为树
                fich_list = DOMTree.documentElement #list第一父节点元素
                formalisme = fich_list.getElementsByTagName('formalisme')[parname['formorder']]
                tv = formalisme.getElementsByTagName('tv')[0]
                variete =tv.getElementsByTagName('variete')[0]
                variete.getElementsByTagName('param')[parname['orderinform']].childNodes[0].data = parvalue
                with open(model_dir, 'w') as f:
                    fich_list.writexml(f)
    else:
        print('Parmeter('+parnamestr+')is not in plant file')
        
        
        



































