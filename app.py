from flask import Flask, request, jsonify
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
if __name__=='__main__': app.run(host='0.0.0.0',port=10000)
