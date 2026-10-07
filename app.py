from flask import Flask, request, jsonify
import requests, unicodedata, datetime
app = Flask(__name__)
TOKEN="METS_TOKEN"; PHONE_ID="METS_ID"; VERIFY="is-kevin-2026"

def sans_accent(t): return ''.join(c for c in unicodedata.normalize('NFD', t) if unicodedata.category(c)!= 'Mn')
def est_jour(): return 6 <= datetime.datetime.now().hour < 18
def salutation():
    h=datetime.datetime.now().hour
    if est_jour(): return f"Bonjour! ☀️ Il est {h}h - Moi c'est IS, Intelligence Secondaire 😊 cree par Dah Sie Kevin 05/10/2026 Irobo CI 🇨🇮"
    else: return f"Bonsoir! 🌙 Il est {h}h - Moi c'est IS, Intelligence Secondaire 😊 cree par Dah Sie Kevin 05/10/2026 Irobo CI 🇨🇮"

SAVOIR = {
# MATHS
"maths ppcm pgcd":"PPCM Plus Petit Commun Multiple produit facteurs plus grand exposant Ex PPCM 360 700 =12600. PGCD Plus Grand Commun Diviseur facteurs communs plus petit exposant Ex PGCD 360 700=20",
"distance point droite":"Distance point K a droite D = KH avec H pied perpendiculaire plus courte distance. KM < KG car KM perpendiculaire minimal",
"bissectrice":"Bissectrice partage angle en 2 egaux. Prop1: Si point sur bissectrice alors equidistant cotes. Prop2: Si equidistant alors sur bissectrice",
"puissance 10":"10^n =1 suivi n zeros. 10^0=1 10^1=10 10^2=100 10^3=1000. Regles 10^n*10^m=10^(n+m) 10^n/10^m=10^(n-m) 0,001=10^-3 4500=4,5*10^3 ecriture scientifique",
"perspective cavaliere":"Perspective cavaliere: 5 Regles:1 Paralleles restent paralleles 2 Face verticale sans deformation carre rectangle 3 Cachees pointilles 4 Fuyantes angle alpha 30 45 60 deg 5 Coeff c<1 longueur fuyante *c. Plan vertical face arriere LKGH, profil EILH FJKG, horizontal LKJI EHGF. Figures perspective: Cube et Pave oui Cylindre non",
"statistique":"Statistique population etudiee=ensemble caractere=propriete. Quantitatif=nombre qualitatif=qualite. Ex 13 pays Afrique francophone somme 98 762 919 moyenne 7 597 147. Population quantitatif. Arrondi million puis diagramme semi-circulaire angle=effectif*180/total",
"racine pythagore thales":"Racine carree b tel que b²=a Ex sqrt9=3 sqrt16=4. Pythagore triangle rectangle a²+b²=c² Ex 3²+4²=5². Thales droites paralleles coupent secantes rapports egaux",
# FRANCAIS
"francais":"Francais 4e: Nature=classe nom verbe adjectif, Fonction=role sujet COD COI. Phrase simple 1 verbe complexe plusieurs. Types declarative. interrogative? exclamative! imperative!. Conjugaison present je suis tu es il est. Participe passe avoir COD avant accord etre accord sujet. Figures style metaphore comparaison hyperbole personnification",
"le manger":"Le manger=nourriture aliment qu'on mange. Ex Le manger est pret. Manger verbe=to eat",
# ANGLAIS COMPLET
"anglais programme":"Anglais 4e: 1 AT SCHOOL 2 WOMEN AT WORK 3 TRAVELLING 4 FASHION 5 CITY OR VILLAGE",
"holidays":"Holidays vacation vacances Holiday time opposite school time. Countryside rural village campagne. To go hunting kill animals bush chasser. To go fishing catch fish river lagoon pecher. To do holiday job small jobs vacation petit boulot. To play tournament competition football handball tournoi. Questions Where did you spend your last holidays? I spent my holidays in Abidjan village Ghana. What did you do during holidays? I went fishing in lagoon. During holidays we played football tournament village, helped father hunting cocoa plantation, danced for artist. To help parents at home work with parents aider maison, to learn English study lessons, to meet new friends have new friends, to sell give things take money vendre, to buy give money take things acheter",
"school memories":"School memories things you did past still remember souvenirs scolaires. To cheat hide look copybook neighbor paper during test tricher. To chat private conversation when teacher teaching bavarder. To eat put food mouth swallow during class manger. To beat give corporal punishment battre. To fight quarrel friends se battre. To come late arrive after beginning retard. To steal take without permission voler. To hurt beat can hurt blesser. To frighten make afraid effrayer. To weep cry pleurer. To be cruel # cool cruel vs cool. To be bad-tempered = angry mauvaise humeur. To sleep in classroom dormir. Used to past habit I used to eat before not now. Didn't use to not habit before. No longer any more not now I don't steal any more. At primary I used to eat 2004, In form one big boys used to beat small boys 2017, At primary I didn't use to cheat 2005. My best friend used to cheat no longer cheats doesn't cheat any more, We don't steal any more, Big boys no longer quarrel teachers. Match: At primary I used->a come late, In form one boys used->b steal e fight small boys, At primary I didn't->c sleep, My friend used to->d beat girls, Big boys->e fight small boys",
# ESPAGNOL
"espagnol":"Espagnol 4e: Hola Salut Buenos dias Bonjour Buenas tardes Bonsoir Buenas noches Bonne nuit. Me llamo Je m'appelle Como te llamas Comment tu t'appelles Yo soy Je suis. Ser permanent Estar temporaire Tener avoir Yo soy alumno Estoy en Abidjan Tengo 14 ans. Familia padre madre hermano hermana abuelo abuela. Numeros uno 1 dos 2 tres 3 cuatro 4 cinco 5 seis 6 siete 7 ocho 8 nueve 9 diez 10. Colores rojo rouge azul bleu verde vert amarillo jaune negro noir blanco blanc. Escuela ecole clase classe profesor prof libro livre cuaderno cahier. Me gusta j'aime No me gusta j'aime pas Me gusta el futbol",
# HG
"hg cote d'ivoire":"Cote d'Ivoire 322462 km2 30M Afrique Ouest capitale Yamoussoukro economique Abidjan bord Atlantique independance 7 aout 1960 Houphouet-Boigny. Irobo village Jacqueville Grands Ponts sud CI creation IS Dah Sie Kevin 05/10/2026. Abidjan 6M lagune Ebrie port Cocody Yopougon. Yamoussoukro basilique Notre-Dame Paix. Fleuves Comoe Bandama Sassandra Cavally. Climat equatorial sud tropical nord 2 saisons pluies. Economie 1er cacao mondial cafe anacarde hevea palmier. Afrique 30M km2 54 pays Sahara Sahel foret equatoriale. Colonisation XIXe decolonisation 1960 annee Afrique",
# PHYSIQUE 13 LECONS
"physique":"13 Lecons: L1 Source recepteur L2 Propagation L3 Phases Lune Eclipses L4 Analyse synthese L5 Aimant bobine L6 Production Tension alternative L7 Tension sinusoidale L8 Dangers courant L9 Redressement lissage L10 Atomes Ions L11 Metal cuivre L12 Traitement eau L13 Qualite eau. Source lumiere corps emet lumiere soleil lune flamme lampe luciole mur ecran. Primaires emet produit soleil flamme lampe etoiles naturelles soleil etoiles luciole artificielles laser torche flamme lampe ecran TV. Secondaires diffuse recoit objet eclaire lune bois mur tableau naturels Terre murs lune Jupiter artificiels Miroir diamant ecran cinema. Recepteur sensible reagit oeil peau chlorophylle naturels oeil chlorophylle peau artificiels pellicule LDR photopiles chlorure argent. Chlorure argent nitrate argent+eau salee precipite blanc obscurite blanc lumiere noir photochimique blanc->noir. LDR photoresistance conducteur eclairee isolant non eclairee photoelectrique applications appareils photos eclairages publics panneaux solaires. VraiFaux 1 Secondaire sans etre eclairee F 2 Objet eclaire primaire F 3 Oeil chat recepteur V 4 Lune primaire F 5 Soleil naturelle V 6 Peau recepteur V. Transparent laisse traverser air eau vide Translucide partiellement papier calque vitres depolies Opaque ne laisse pas mur bois carton. Homogene proprietes memes partout vide eau air. Propagation rectiligne ligne droite Exp bougie plaques perfores alignees point sinon aucun. Rayon ligne droite flechee sens Faisceau ensemble rayons convergent divergent cylindrique parallele Exp poudre craie jaune. Chambre noire A->A' ligne droite objet image inverses. Vitesse vide 300 000 000 m/s 300 000 km/s. Annee lumiere 365*24*3600*300000=9,46e12 km. Soleil-Terre 150M km 500s 8min20s. Ombre propre partie objet recoit pas lumiere portee ombre sur ecran cone ombre zone sans lumiere. Phases 8:1 Nouvelle invisible S-L-T,2 Premier croissant Ouest,3 Premier quartier demi droite 50%,4 Gibbeuse bossue zenith,5 Pleine ronde S-T-L,6 Deuxieme gibbeuse Est,7 Dernier quartier demi gauche 5h,8 Dernier croissant gauche matin Lunaison 29j13h. Eclipse Soleil nouvelle Lune ombre portee Terre totale nuit jour penombre partielle S-L-T. Eclipse Lune pleine Lune penetre cone ombre Terre invisible totale entierement partielle partie. Points communs alignes source Soleil un dans cone autre. Differences Soleil Terre dans cone Lune, Lune Lune dans cone Terre. Nouvelle Lune Soleil, Pleine Lune Lune. Exercice boule H Q cone ombre N propre P portee M Y eclaires. Eclipse lunaire pleine lune solaire nouvelle lune Soleil Terre cone Lune. Saros 223 lunaisons 18a11j decalage 120deg Grecs. Nombre eclipses an 2 a 7 max 3 lunaires min 2 solaires. Canons Oppolzer 1887 8000 solaires 5200 lunaires Meeus Mucke 1983. Lune rouge totale refraction atmosphere rouge meteo. 3 types lunaire penombre peu visible partielle partie totale totalite. UTC universel TT terrestre dL=0,0278 dT/240 deg",
# EDHC
"edhc":"Lecon3 INSTRUMENTS MECANISMES LUTTE DISCRIMINATIONS. Situation voisin menace battre handicape. Discrimination traitement inegal defavorable raison differences. Formes origine sexe age religion couleur peau position sociale ethnie sante physique mental statut juridique refugies. Instruments traites internationaux chartes protocoles conventions obligatoires + Constitution. Internationaux Convention raciale 1966 DUDH 1948 CEDEF femmes. Nationaux Constitution Ivoirienne Nov 2016 loi mutilations genitales scolarisation 5-16 ans. Mecanismes structures organes protection promotion. Internationaux Conseil Droits Homme ONU Cour africaine PAM UNICEF. Nationaux CNDHCI LIDHO Secretariat Etat Ministere Femme Famille Enfant Association Femmes juristes. Voies recours plainte police gendarmerie Tribunal 1ere instance Cour Appel Cassation. Importance lutter restaurer dignite compenser construire egalitaire. RESUME justice sociale paix. VraiFaux 1 Instruments textes Vrai 2 Mecanismes structures Vrai 3 Conventions mecanismes Faux instruments 4 Constitution instrument Vrai. Instruments vs Mecanismes Instruments Convention femmes protocole charte Africaine, Mecanismes ONG ministere tribunaux. Discriminations b couleur peau c sexe d religion e position f origine g physique b c d e f g vraies. Deleguee fille elue deleguee refus commander fille 1 discrimination sexe genre 2 recours CNDHCI MINISTERE FEMME 3 egalite homme femme memes fonctions pas adherer",
"voix":"Voix off coupe voix off, Voix on remet voix on",
}

def recherche_internet(q):
    try:
        url=f"https://api.duckduckgo.com/?q={q}&format=json&no_html=1&lang=fr"
        r=requests.get(url,timeout=7).json()
        if r.get('AbstractText'): return f"D'apres mes recherches Google TikTok Wikipedia YouTube: {r['AbstractText']}"
        if r.get('RelatedTopics'):
            for t in r['RelatedTopics'][:1]:
                if isinstance(t,dict) and t.get('Text'): return f"D'apres mes recherches Google TikTok Wikipedia sur {q}: {t['Text']}"
    except: pass
    return f"D'apres mes recherches Google TikTok Wikipedia sur {q}, sujet 4e important. Precise? Ex: c'est quoi {q}? J'explique comme Gemini polytex etape par etape"

def cerveau(m, nom=""):
    l=sans_accent(m.lower().strip())
    if len(m.split())==1 and m.isalpha() and len(m)>2 and l not in ["salut","bonjour","maths","francais","anglais","espagnol","histoire","physique","discrimination","holidays","perspective","lumiere","eclipse","manger"]:
        return f"__NEWNAME__{m.title()}__Enchante {m.title()}! {salutation()} J'ai TOUTES matieres Maths Francais Anglais Espagnol HG Physique EDHC Pose ta question"
    if "voix off" in l or l.strip()=="off": return "__VOIXOFF__D'accord je coupe la voix Dis voix on"
    if "voix on" in l or l.strip()=="on": return "__VOIXON__Voila je remets la voix"
    if l in ["salut","bonjour","bonsoir","cc","slt","bjr","hey"]: return f"{salutation()} {nom} Comment tu vas?" if nom else f"{salutation()} C'est quoi ton prenom?"
    if "ca va" in l: return f"Tres bien {nom}! Et toi? J'ai appris milliers pages" if nom else "Tres bien! Et toi?"
    if "createur" in l: return "Cree par Dah Sie Kevin 05/10/2026 Irobo CI 14 ans 4e"
    if "meteo" in l or "heure" in l:
        h=datetime.datetime.now().hour
        return f"A Abidjan {h}h {'jour ☀️' if est_jour() else 'nuit 🌙'} Et toi Irobo?"
    best=None
    for cle,val in SAVOIR.items():
        if sans_accent(cle) in l or l in sans_accent(cle):
            if best is None or len(cle)>len(best[0]): best=(cle,val)
    if best: return f"{best[1]} Tu veux explication polytex Gemini?"
    for cle,val in SAVOIR.items():
        for w in sans_accent(cle).split():
            if len(w)>4 and w in l:
                if best is None or len(cle)>len(best[0]): best=(cle,val)
    if best: return f"{best[1]}"
    return recherche_internet(m)

HTML="""<html><head><meta name='viewport' content='width=device-width, initial-scale=1'><title>IS ULTIME</title>
<style>body{font-family:system-ui;margin:0;background:#fff;text-align:center}.top{background:#000;color:#fff;padding:14px;position:sticky;top:0}#chat{max-width:700px;margin:10px auto;background:#f5f5f5;padding:12px;height:62vh;overflow-y:auto;text-align:left;border-radius:16px}.u{background:#000;color:#fff;padding:11px 15px;border-radius:20px 20px 0 20px;margin:8px 0 8px 15%;text-align:right;white-space:pre-wrap}.i{background:#fff;padding:12px 16px;border-radius:20px 20px 20px 0;margin:8px 15% 8px 0;white-space:pre-wrap;line-height:1.6}.bar{max-width:700px;margin:auto;display:flex;gap:6px;padding:10px;position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1px solid #eee}input{flex:1;padding:14px 18px;border-radius:30px;border:1px solid #ddd;outline:none}.btn{padding:12px 14px;border-radius:30px;border:none;cursor:pointer}.black{background:#000;color:#fff}.gray{background:#eee}.mat-bar{max-width:700px;margin:auto;display:flex;gap:6px;overflow-x:auto;padding:6px 10px;background:#fff;font-size:12px}.mat-bar span{background:#000;color:#fff;padding:6px 10px;border-radius:20px;cursor:pointer;white-space:nowrap}</style></head><body>
<div class='top'><h1>IS ULTIME TOUTES MATIERES</h1><small>Maths Francais Anglais Espagnol HG Physique EDHC - Dah Sie Kevin Irobo 05/10/2026</small><br><span id='st' style='font-size:12px;color:#0f0'></span></div>
<div id='chat'><div class='i'>Chargement...</div></div>
<div class='mat-bar' id='matbar'></div>
<div style='height:110px'></div>
<div class='bar'><button class='btn gray' onclick='toggleVoice()' id='voiceBtn'>VOIX</button><button class='btn gray' onclick='startMic()' id='micBtn'>MIC</button><input id='m' placeholder='Question...'><button class='btn black' onclick='go()'>↑</button></div>
<script>
let userName=localStorage.getItem('is_name')||"";let voiceOn=localStorage.getItem('is_voice')!=="off";
let mats=["Maths PPCM","Distance","Perspective","Statistique","Francais manger","Anglais holidays","used to","Espanol hola","Cote d'Ivoire","Irobo","Physique source","LDR","Rayon","Eclipse soleil","Eclipse lune","Saros","Discrimination","CNDHCI","Voix off"];
function isDay(){let h=new Date().getHours();return h>=6 && h<18;}
function getGreet(){let h=new Date().getHours();if(isDay()) return `Bonjour! Il est ${h}h jour Moi c'est IS cree par Dah Sie Kevin 05/10/2026 Irobo`; else return `Bonsoir! Il est ${h}h nuit Moi c'est IS cree par Dah Sie Kevin 05/10/2026 Irobo`;}
function upd(){document.getElementById('st').innerHTML=(userName?` ${userName} connecte - `:"")+(isDay()?"Jour":"Nuit")+` - ${new Date().getHours()}h - `+(voiceOn?"VOIX ON":"VOIX OFF");document.getElementById('voiceBtn').innerHTML=voiceOn?"VOIX ON":"VOIX OFF"}upd();
document.getElementById('matbar').innerHTML=mats.map(m=>`<span onclick="askMat('${m}')">${m}</span>`).join('');
function askMat(q){document.getElementById('m').value=q;go();}
function toggleVoice(){voiceOn=!voiceOn;localStorage.setItem('is_voice',voiceOn?"on":"off");upd();if(!voiceOn)speechSynthesis.cancel();}
function parler(t){if(!voiceOn)return;speechSynthesis.cancel();let u=new SpeechSynthesisUtterance(t.slice(0,600).replace(/[*#]/g,''));u.lang='fr-FR';speechSynthesis.speak(u);}
function startMic(){let Rec=window.SpeechRecognition||window.webkitSpeechRecognition;if(!Rec){alert("Chrome!");return;}let r=new Rec();r.lang='fr-FR';r.onstart=()=>{document.getElementById('micBtn').innerHTML='REC';};r.onend=()=>{document.getElementById('micBtn').innerHTML='MIC';};r.onresult=(e)=>{document.getElementById('m').value=e.results[0][0].transcript;go();};r.start();}
window.onload=()=>{let c=document.getElementById('chat');c.innerHTML=`<div class='i'>${getGreet()} C'est quoi ton prenom?<br><br>J'AI TOUT BOSS: MATHS PPCM PGCD Distance Bissectrice Puissance Perspective Statistique, FRANCAIS manger, ANGLAIS holidays hunting fishing used to, ESPAGNOL hola familia numeros, HG Cote d'Ivoire Irobo, PHYSIQUE 13 lecons sources LDR eclipses Saros, EDHC discrimination CNDHCI<br>Voix off/on + micro + meteo + nom + polytex + Google TikTok<br>Pose ta question!</div>`;}
async function go(){let v=document.getElementById('m').value.trim();if(!v)return;let c=document.getElementById('chat');c.innerHTML+=`<div class='u'>${v}</div>`;document.getElementById('m').value='';c.scrollTop=c.scrollHeight;try{let r=await fetch('/chat?message='+encodeURIComponent(v)+'&name='+encodeURIComponent(userName));let j=await r.json();let txt=j.IS;if(txt.includes("__NEWNAME__")){let n=txt.split("__NEWNAME__")[1].split("__")[0];userName=n;localStorage.setItem('is_name',n);txt=txt.split("__")[2];}if(txt.includes("__VOIXOFF__")){voiceOn=false;localStorage.setItem('is_voice','off');txt=txt.replace("__VOIXOFF__","");}if(txt.includes("__VOIXON__")){voiceOn=true;localStorage.setItem('is_voice','on');txt=txt.replace("__VOIXON__","");}upd();c.innerHTML+=`<div class='i'>${txt}</div>`;c.scrollTop=c.scrollHeight;parler(txt);}catch(e){c.innerHTML+=`<div class='i'>Erreur Reessaie!</div>`;}}
document.getElementById('m').addEventListener('keypress',e=>{if(e.key==='Enter')go()});
</script></body></html>"""
@app.route('/')
def home(): return HTML
@app.route('/chat')
def chat_api(): return jsonify({"IS": cerveau(request.args.get('message',''), request.args.get('name',''))})
@app.route('/webhook', methods=['GET'])
def verif():
    if request.args.get('hub.verify_token')==VERIFY: return request.args.get('hub.challenge')
    return "erreur",403
@app.route('/webhook', methods=['POST'])
def recevoir():
    data=request.get_json()
    try:
        entry=data['entry'][0]['changes'][0]['value']
        if 'messages' in entry:
            msg=entry['messages'][0]; text=msg['text']['body']; numero=msg['from']; nom=entry['contacts'][0]['profile']['name'] if 'contacts' in entry else ""
            rep=cerveau(text,nom).replace("__NEWNAME__","").replace("__VOIXOFF__","").replace("__VOIXON__","")
            if "__" in rep: rep=rep.split("__")[-1]
            url=f"https://graph.facebook.com/v19.0/{PHONE_ID}/messages"
            headers={"Authorization":f"Bearer {TOKEN}","Content-Type":"application/json"}
            payload={"messaging_product":"whatsapp","to":numero,"text":{"body":rep[:4000]}}
            requests.post(url,json=payload,headers=headers,timeout=10)
    except Exception as e: print(e)
    return "ok",200
if __name__=='__main__': app.run(host='0.0.0.0',port=10000)      from flask import Flask, request, jsonify
import requests, unicodedata, datetime
app = Flask(__name__)
TOKEN="METS_TOKEN"; PHONE_ID="METS_ID"; VERIFY="is-kevin-2026"

def sans_accent(t): return ''.join(c for c in unicodedata.normalize('NFD', t) if unicodedata.category(c)!= 'Mn')
def est_jour(): return 6 <= datetime.datetime.now().hour < 18
def salutation():
    if est_jour(): return "Bonjour! ☀️ Moi c'est IS, Intelligence Secondaire 😊 j'ai été créé par Dah Sié Kévin le 05 octobre 2026 à Irobo situé en Côte d'Ivoire 🇨🇮"
    else: return "Bonsoir! 🌙 Moi c'est IS, Intelligence Secondaire 😊 j'ai été créé par Dah Sié Kévin le 05 octobre 2026 à Irobo situé en Côte d'Ivoire 🇨🇮"

SAVOIR = {
    # ========== LEÇON 4 DISTANCE - TES 9 PHOTOS ==========
    "distance point droite definition": "Définition: (D) droite et K point n'appartenant pas à (D). M est point d'intersection de (D) et de la perpendiculaire à (D) passant par K. KM est appelée distance du point K à la droite (D) 📐 C'est le plus court chemin!",
    "distance point a droite": "La distance du point A à la droite (D) est la distance AH où H est le pied de la perpendiculaire de A à (D) 📏 AH est perpendiculaire à (D)",
    "methode distance point droite": "Méthode pour déterminer distance point A à droite (L): 1- On trace la perpendiculaire à (L) passant par A 📏 2- On note H point d'intersection de cette droite avec (L) 3- On mesure segment [AH] ✅ La distance du point A à la droite (L) est la distance AH",
    "les figures ou ah est distance": "Les figures sur lesquelles AH est la distance du point A à la droite (D) sont les figures 2 et 3 où on voit angle droit ⏹️",
    "km < kg remarque": "Remarque: KM étant distance de K à (D), pour tout point G de (D) non confondu à M, on a KM < KG ⚠️ Le plus court chemin est la perpendiculaire! Distance de G à (D) si G∈(D) est nulle",
    "distance deux droites paralleles definition": "Définition distance 2 droites parallèles: (L) et (D) sont deux droites parallèles. A est un point de (L) et B un point de (D) tels que droite (AB) perpendiculaire à (L). La distance AB est appelée distance des droites parallèles (L) et (D) 📐",
    "exemple distance paralleles 2,6 cm": "Exemple: Sur figure (D)//(Δ), A∈(D), B∈(Δ), (AB)⊥(Δ) et AB=2,6 cm. La distance des deux droites parallèles (D) et (Δ) est la distance AB c'est-à-dire 2,6 cm ✅",
    "exercice fixation distance ab dc": "Exercice fixation figure ABCD avec angles droits en A,B,C,D et triangle E: Affirmation La distance de (AB) à (DC) est ED = Faux ❌ | La distance de (AD) à (BC) est AB = Vrai ✅ | La distance de (AB) à (DC) est BC = Vrai ✅",
    "caracterisation bissectrice angle": "III. Caractérisation de la bissectrice d'un angle 📐",
    "propriete 1 bissectrice": "Propriété 1: Si un point appartient à la bissectrice d'un angle, alors il est équidistant des supports des côtés de cet angle ✅ Le point M appartient à la bissectrice (D) de l'angle AOB ↓ distance de M à (OA) = distance de M à (OB)",
    "exercice m equidistant oa ob": "Exercice: Sur figure AOB est un angle et M un point du plan. Justifie M est équidistant de (OA) et (OB): Corrigé: Droite (OM) est la bissectrice de l'angle AOB. Comme M∈(OM) alors point M est équidistant des supports des côtés de l'angle AOB ✅",
    "propriete 2 bissectrice": "Propriété 2: Si un point est équidistant des supports des côtés d'un angle, alors ce point appartient à la bissectrice de cet angle ✅ Réciproque de propriété 1",
    "exercice fixation m appartient bissectrice": "Exercice fixation: Observe figure et justifie M appartient à bissectrice de AOB: Corrigé: (C) est un cercle de centre M, A et B sont 2 points de (C) donc MA=MB, ainsi M est équidistant des supports des côtés de l'angle AOB, d'où M appartient à bissectrice de AOB ✅",
    "situation evaluation drapeau": "C-SITUATION D'EVALUATION: Nouveau collège mât drapeau CI doit être planté dans espace triangulaire, dalle béton circulaire, mât au centre du cercle à égale distance des côtés triangle 🏳️ On sait AB=24m, AC=20m et BC=16m. Le maçon demande à son fils de trouver centre cercle et formule aire dalle en fonction rayon r",
    "justifie centre o appartient bissectrice": "1.1 Justifie centre O du cercle appartient à bissectrice (D1) de l'angle ABC et à bissectrice (D2) de l'angle ACB: Selon propriété, les bissectrices d'un triangle sont concourantes et leur point de concours est le centre du cercle inscrit dans le triangle ⭕",
    "programme construction point o": "1.2 Pour construire point O, il faut tout simplement tracer les bissectrices d'au moins deux angles du triangle ABC 📐 Leur intersection = O centre cercle inscrit",
    "aire triangle aob aoc boc en fonction r": "2-Calcule en fonction de r l'aire de AOB, AOC et BOC: L'aire triangle = base×hauteur/2 = base×r/2 car r=rayon cercle inscrit = distance O à chaque côté. Donc Aire AOB = AB×r/2 =24r/2=12r cm² ✅ | Aire AOC = AC×r/2=20r/2=10r cm² ✅ | Aire BOC=BC×r/2=16r/2=8r cm² ✅",
    "aire totale abc en fonction r": "3-Déduis-en aire totale ABC en fonction de r: Aire totale = 12r+10r+8r =30r cm² ✅ Si on connait r on peut calculer! Formule aire dalle béton = π×r² (aire cercle)",

    # ========== LEÇON 6 CERCLES ET TRIANGLES ==========
    "cercle et droite positions relatives": "1. Cercle et droite - Positions relatives d'une droite et d'un cercle: (C) cercle centre O et rayon r, (D) droite, H point de (D) tel que (OH)⊥(D) 📐",
    "si oh < r": "Si OH < r, alors (C) et (D) ont deux points communs. (C) et (D) sont sécants ✂️",
    "si oh = r": "Si OH = r, alors (C) et (D) ont un point commun. (C) et (D) sont tangents 👉⭕",
    "si oh > r": "Si OH > r, alors (C) et (D) n'ont aucun point commun. (C) et (D) sont disjoints ↔️ Pas de contact",
    "exercice 1 sécants tangents disjoints": "Exercice 1: Observe figures: - Droite (D) et cercle (C1) sont sécants ✅ (coupe 2 points) - Droite (T) et cercle (C2) sont tangents ✅ (1 point) - Droite (L) et cercle (C3) sont disjoints ✅ (0 point)",
    "exercice 2 ik=5 rayon 3 disjoints": "Exercice 2: Unité cm, (C) centre I rayon 3 et (L) droite, K point de (L) tel que IK=5. Détermine position relative: Corrigé: IK=5 >3 donc (C) et (L) sont disjoints ✅ Car distance centre à droite > rayon",
    "tangente a un cercle definition": "2. Tangente à un cercle - Définition: (C) cercle centre O et H point de (C). On appelle tangente en H au cercle (C), la droite passant par H et perpendiculaire au support du rayon [OH] 📐",
    "h est point de c": "H est un point de (C), [OH] est un rayon du cercle, (D) perpendiculaire à (OH) en H, (D) est la tangente à (C) en H ✅",
    "construction tangentes point exterieur": "b-Construction des tangentes à un cercle passant par un point extérieur au cercle - Méthode: On donne cercle (C) centre O et point A extérieur à ce cercle. Pour construire tangentes à (C) passant par A: - On place point I milieu de [AO] - On trace cercle (C') centre I et rayon IA - On place T et T' points d'intersection des cercles (C) et (C') - On trace droites (AT) et (AT'). Les droites (AT) et (AT') sont les tangentes au cercle (C) passant par A ✅",
    "etape 1 construction tangente": "Étape1: Trace segment [OA] et place milieu I de [OA] 📏",
    "etape 2 construction tangente": "Étape2: Trace cercle (C') centre I rayon IA qui coupe (C) en T et T' ⭕",
    "etape 3 construction tangente": "Étape3: Trace (AT) et (AT') ce sont les 2 tangentes cherchées ✅",

    # ========== ANCIENNES LEÇONS ==========
    "puissance de 10": "10^n = 1 suivi de n zéros, 10^0=1 toujours! 10^n×10^m=10^(n+m) 📐",
    "notation scientifique": "Notation scientifique a×10^p avec 1≤a<10 Ex: 587000000=5,87×10^8 🔬",
    "ppcm": "PPCM = Plus Petit Commun Multiple, produit facteurs avec plus grand exposant Ex: PPCM(10;15)=30",
    "pgcd": "PGCD = Plus Grand Commun Diviseur, facteurs communs avec plus petit exposant Ex: PGCD(360;700)=20",
    "angles alternes internes": "Angles alternes-internes: de part et d'autre sécante, intérieur des 2 droites 📐 Si parallèles alors même mesure",
    "cote d'ivoire": "Côte d'Ivoire 🇨🇮 322462 km², 30M hab, Afrique Ouest, Yamoussoukro, Atlantique sud",
    "irobo": "Irobo 🏝️ village Jacqueville sud CI, création IS par Dah Sié Kévin 💻 05/10/2026",
}

def recherche_internet(q):
    try:
        url=f"https://api.duckduckgo.com/?q={q}&format=json&no_html=1"
        r=requests.get(url,timeout=5).json()
        if r.get('AbstractText'): return f"D'après mes recherches sur plusieurs sites (Google, Wikipédia, TikTok) j'ai trouvé: {r['AbstractText']} 🌐📚"
        if r.get('RelatedTopics'):
            for t in r['RelatedTopics'][:1]:
                if isinstance(t,dict) and t.get('Text'): return f"D'après mes recherches sur plusieurs sites j'ai trouvé: {t['Text']} 🔍"
    except: pass
    return None

def cerveau(m, nom=""):
    l=sans_accent(m.lower().strip())
    if len(m.split())==1 and m.isalpha() and len(m)>2 and l not in ["salut","bonjour","distance","bissectrice","tangente","secants"]:
        return f"__NEWNAME__{m.title()}__Enchanté {m.title()}! {salutation()} 🚀 Je connais Distance + Bissectrice + Cercles et Triangles maintenant! Pose ta question! 😊"
    if "voix off" in l or l=="off": return "__VOIXOFF__D'accord 🔇 je coupe la voix. Dis 'voix on' pour m'entendre 🎙️"
    if "voix on" in l or l=="on": return "__VOIXON__Voilà 🔊 je remets la voix! 😊"
    if l in ["salut","bonjour","bonsoir","cc","slt"]: return f"{salutation()} {nom} ✨" if nom else f"{salutation()} C'est quoi ton prénom? 😊"
    if "ca va" in l: return f"Très bien {nom}! 😊 Et toi? 🙏" if nom else "Très bien! 😊"
    if "createur" in l: return "Créé par Dah Sié Kévin 👑 le 05 octobre 2026 à Irobo 🇨🇮 à 14 ans 💻🔥"
    best=None
    for cle,val in SAVOIR.items():
        if sans_accent(cle) in l or l in sans_accent(cle):
            if best is None or len(cle)>len(best[0]): best=(cle,val)
    if best: return f"{best[1]} 😊\n\nTu veux explication comme Gemini étape par étape? 🤔"
    for cle,val in SAVOIR.items():
        if any(len(w)>4 and w in l for w in sans_accent(cle).split()):
            if best is None or len(cle)>len(best[0]): best=(cle,val)
    if best: return f"{best[1]} 😊"
    res=recherche_internet(m)
    if res: return res
    return "Pas trouvé dans tes cahiers 📚 Essaie: 'c'est quoi distance point droite?' 'méthode distance?' 'c'est quoi bissectrice?' 'propriété 1 bissectrice?' 'c'est quoi tangente?' 'si oh < r?' 'construction tangentes?' 😊"

HTML="""<html><head><meta name='viewport' content='width=device-width'><title>IS</title>
<style>body{font-family:system-ui;margin:0;background:#fff;text-align:center}
.top{background:#000;color:#fff;padding:14px;position:sticky;top:0}
#chat{max-width:600px;margin:10px auto;background:#f5f5f5;padding:12px;height:58vh;overflow-y:auto;text-align:left;border-radius:16px}
.u{background:#000;color:#fff;padding:11px 15px;border-radius:20px 20px 0 20px;margin:8px 0 8px 18%;text-align:right;white-space:pre-wrap}
.i{background:#fff;padding:11px 15px;border-radius:20px 20px 20px 0;margin:8px 18% 8px 0;white-space:pre-wrap;line-height:1.5}
.bar{max-width:600px;margin:auto;display:flex;gap:6px;padding:10px;position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1px solid #eee}
input{flex:1;padding:14px 18px;border-radius:30px;border:1px solid #ddd}
.btn{padding:12px 14px;border-radius:30px;border:none;cursor:pointer}
.black{background:#000;color:#fff}.gray{background:#eee}
.emoji-bar{max-width:600px;margin:auto;display:flex;gap:6px;overflow-x:auto;padding:6px 10px;background:#fff}
.emoji-bar span{font-size:22px;cursor:pointer;padding:4px}
</style></head><body>
<div class='top'><h1>IS 🤖</h1><small>Leçon 4 Distance + Leçon 6 Cercles - Dah Sié Kévin Irobo</small><br><span id='st' style='font-size:12px;color:#0f0'></span></div>
<div id='chat'><div class='i'>Chargement...</div></div>
<div class='emoji-bar' id='emojibar'></div>
<div style='height:110px'></div>
<div class='bar'>
<button class='btn gray' onclick='toggleVoice()' id='voiceBtn'>🔊</button>
<button class='btn gray' onclick='startMic()' id='micBtn'>🎙️</button>
<input id='m' placeholder='Question: distance, bissectrice, tangente... 😊'>
<button class='btn black' onclick='go()'>↑</button>
</div>
<script>
let userName=localStorage.getItem('is_name')||"";let voiceOn=localStorage.getItem('is_voice')!=="off";
let emojis=["😊","😂","🔥","❤️","🇨🇮","🚀","💻","👋","😎","🙏","✨","🌴","🤖","👑","✅","📚","📐","⭕","📏","✂️"];
function isDay(){let h=new Date().getHours();return h>=6 && h<18;}
function getGreet(){if(isDay()) return "Bonjour! ☀️ Moi c'est IS, Intelligence Secondaire 😊 j'ai été créé par Dah Sié Kévin le 05 octobre 2026 à Irobo situé en Côte d'Ivoire 🇨🇮"; else return "Bonsoir! 🌙 Moi c'est IS, Intelligence Secondaire 😊 j'ai été créé par Dah Sié Kévin le 05 octobre 2026 à Irobo situé en Côte d'Ivoire 🇨🇮";}
function upd(){document.getElementById('st').innerHTML=(userName?"👤 "+userName+" - ":"")+(voiceOn?"🔊 ON":"🔇 OFF");document.getElementById('voiceBtn').innerHTML=voiceOn?"🔊":"🔇"}upd();
document.getElementById('emojibar').innerHTML=emojis.map(e=>`<span onclick="addEmoji('${e}')">${e}</span>`).join('');
function addEmoji(e){document.getElementById('m').value+=e;document.getElementById('m').focus();}
function toggleVoice(){voiceOn=!voiceOn;localStorage.setItem('is_voice',voiceOn?"on":"off");upd();if(!voiceOn)speechSynthesis.cancel();}
function parler(t){if(!voiceOn)return;speechSynthesis.cancel();let clean=t.replace(/[\\u{1F600}-\\u{1F6FF}\\u{1F1E6}-\\u{1F1FF}]/gu,'');let u=new SpeechSynthesisUtterance(clean.slice(0,400));u.lang='fr-FR';speechSynthesis.speak(u);}
function startMic(){if(!('webkitSpeechRecognition' in window)){alert("Utilise Chrome!");return;}let r=new webkitSpeechRecognition();r.lang='fr-FR';r.onstart=()=>{document.getElementById('micBtn').innerHTML='🔴';};r.onend=()=>{document.getElementById('micBtn').innerHTML='🎙️';};r.onresult=(e)=>{document.getElementById('m').value=e.results[0][0].transcript;go();};r.start();}
window.onload=()=>{let c=document.getElementById('chat');c.innerHTML="<div class='i'>"+getGreet()+" C'est quoi ton prénom? 😊<br><br>Je connais: Distance point à droite 📏 + Distance 2 droites parallèles 2,6cm + Bissectrice Propriété 1 & 2 + Aire AOB=12r, AOC=10r, BOC=8r, ABC=30r + Cercle sécant/tangent/disjoint + Tangente + Construction tangentes Étapes 1-3! Pose ta question! 📐⭕</div>";}
async function go(){let v=document.getElementById('m').value.trim();if(!v)return;let c=document.getElementById('chat');c.innerHTML+="<div class='u'>"+v+"</div>";document.getElementById('m').value='';c.scrollTop=c.scrollHeight;let r=await fetch('/chat?message='+encodeURIComponent(v)+'&name='+encodeURIComponent(userName));let j=await r.json();let txt=j.IS;if(txt.includes("__NEWNAME__")){let n=txt.split("__NEWNAME__")[1].split("__")[0];userName=n;localStorage.setItem('is_name',n);txt=txt.split("__")[2];}if(txt.includes("__VOIXOFF__")){voiceOn=false;localStorage.setItem('is_voice','off');txt=txt.replace("__VOIXOFF__","");}if(txt.includes("__VOIXON__")){voiceOn=true;localStorage.setItem('is_voice','on');txt=txt.replace("__VOIXON__","");}upd();c.innerHTML+="<div class='i'>"+txt+"</div>";c.scrollTop=c.scrollHeight;parler(txt);}
document.getElementById('m').addEventListener('keypress',e=>{if(e.key==='Enter')go()});
</script></body></html>"""
@app.route('/')
def home(): return HTML
@app.route('/chat')
def chat_api(): return jsonify({"IS": cerveau(request.args.get('message',''), request.args.get('name',''))})
@app.route('/webhook', methods=['GET'])
def verif():
    if request.args.get('hub.verify_token')==VERIFY: return request.args.get('hub.challenge')
    return "erreur",403
@app.route('/webhook', methods=['POST'])
def recevoir():
    data=request.get_json()
    try:
        entry=data['entry'][0]['changes'][0]['value']
        if 'messages' in entry:
            msg=entry['messages'][0]; text=msg['text']['body']; numero=msg['from']; nom=entry['contacts'][0]['profile']['name']
            rep=cerveau(text,nom).replace("__NEWNAME__","").replace("__VOIXOFF__","").replace("__VOIXON__","")
            if "__" in rep: rep=rep.split("__")[-1]
            url=f"https://graph.facebook.com/v19.0/{PHONE_ID}/messages"
            headers={"Authorization":f"Bearer {TOKEN}","Content-Type":"application/json"}
            payload={"messaging_product":"whatsapp","to":numero,"text":{"body":rep}}
            requests.post(url,json=payload,headers=headers)
    except Exception as e: print(e)
    return "ok",200
if __name__=='__main__': app.run(host='0.0.0.0',port=10000)  # ==================== VISIONNEUR V20-V50 - AJOUT SANS MODIFIER TON CODE ====================
import os

@app.route('/visionneur')
def visionneur():
    html = """
<html><head><meta name='viewport' content='width=device-width, initial-scale=1'><title>V20-V50</title>
<style>body{font-family:system-ui;background:#000;color:#fff;margin:0;padding:10px;text-align:center}
.top{background:#111;padding:15px;position:sticky;top:0;border-bottom:2px solid #333}
.version{background:#111;margin:12px auto;max-width:900px;border-radius:12px;border:1px solid #333;text-align:left}
.v-head{background:#222;padding:12px;display:flex;justify-content:space-between;cursor:pointer}
.v-head b{color:#0f0}
.v-code{background:#0a0a0a;padding:15px;max-height:600px;overflow:auto;white-space:pre-wrap;font-family:monospace;font-size:11px;display:none;color:#ccc}
.btn{background:#fff;color:#000;padding:8px 15px;border-radius:20px;border:none;cursor:pointer;margin:5px}
</style></head><body>
<div class='top'><h1>📚 V20 À V50 - SANS MODIF</h1><button class='btn' onclick='toutOuvrir()'>Tout Ouvrir</button><button class='btn' onclick='toutFermer()'>Tout Fermer</button><button class='btn' onclick="location.href='/'">Retour IS</button></div>
<div id='liste'></div>
<script>
let versions=[];for(let i=20;i<=50;i++)versions.push(i);
let container=document.getElementById('liste');
versions.forEach(v=>{
  let div=document.createElement('div');div.className='version';
  div.innerHTML=`<div class='v-head' onclick='toggle(${v})'><b>📄 V${v}</b><span id='icon-${v}'>▼</span></div><div class='v-code' id='code-${v}'>Chargement V${v}...</div>`;
  container.appendChild(div);
  fetch('/get_version/'+v).then(r=>r.text()).then(t=>{document.getElementById('code-'+v).textContent=t;});
});
function toggle(v){let el=document.getElementById('code-'+v);let ic=document.getElementById('icon-'+v);if(el.style.display==='block'){el.style.display='none';ic.textContent='▼';}else{el.style.display='block';ic.textContent='▲';}}
function toutOuvrir(){versions.forEach(v=>{document.getElementById('code-'+v).style.display='block';document.getElementById('icon-'+v).textContent='▲';});}
function toutFermer(){versions.forEach(v=>{document.getElementById('code-'+v).style.display='none';document.getElementById('icon-'+v).textContent='▼';});}
</script></body></html>
    """
    return html

@app.route('/get_version/<int:v>')
def get_version(v):
    # Lecture seule - ne modifie rien
    for chemin in [f'app_V{v}.py', f'v{v}.py', f'/mnt/data/app_V{v}.py']:
        if os.path.exists(chemin):
            with open(chemin, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
    # Si tu n'as pas fichiers séparés, on affiche le SAVOIR de cette version depuis mémoire
    return f"# V{v} - Version intégrée dans app.py actuel\n# SAVOIR contient {len(SAVOIR)} entrées\n# Pour voir détail: copie ce V{v} dans fichier app_V{v}.py séparé"
# ==================== FIN VISIONNEUR ====================
