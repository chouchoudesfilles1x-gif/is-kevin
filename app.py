from flask import Flask, request, jsonify
import unicodedata, random
app = Flask(__name__)

def sans_accent(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t) if unicodedata.category(c)!= 'Mn')

SAVOIR = {
    "cote d'ivoire": "La Côte d'Ivoire est située en Afrique de l'Ouest, au sud au bord de l'Atlantique. Capitale Yamoussoukro, plus grande ville Abidjan 🇨🇮",
    "cote divoire": "La Côte d'Ivoire est située en Afrique de l'Ouest, au sud au bord de l'Atlantique 🇨🇮",
    "abidjan": "Abidjan est au sud de la Côte d'Ivoire, au bord de la lagune Ebrié, c'est la capitale économique",
    "irobo": "Irobo est un village à Jacqueville, au sud de la Côte d'Ivoire, c'est là-bas que j'ai été créé par Dah Sié Kévin",
    "france": "La France est en Europe, capitale Paris 🇫🇷",
}

# Pour ne pas répéter le nom tout le temps
def avec_nom_ou_pas(nom):
    if not nom:
        return ""
    # 30% de chance de dire le nom, 70% rien
    if random.random() < 0.3:
        return f" {nom}"
    return ""

def cerveau(m, nom=""):
    l = m.lower().strip()
    l_sans = sans_accent(l)

    # 1. APPRENDRE NOM SEULEMENT SI C'EST VRAIMENT UN PRENOM
    mots_interdits = ["salut","bonjour","cc","france","cote","ivoire","irobo","abidjan","c'est","quoi","comment","quelle","quel","pourquoi","ou","python","mali"]
    if len(m.split())==1 and 2<=len(m)<=12 and m.isalpha():
        if l not in mots_interdits and l_sans not in mots_interdits:
            n = m.title()
            return f"__NEWNAME__{n}__Enchanté {n}! Moi c'est IS, créé par Dah Sié Kévin le 05 octobre 2026. Content de te connaître!"

    # 2. VOIX
    if "voix off" in l_sans or l_sans=="off":
        return "__VOIXOFF__D'accord, je coupe la voix. Si tu veux m'entendre parler, dis voix on."
    if "voix on" in l_sans or l_sans=="on":
        return "__VOIXON__Voilà je remets la voix! Si tu veux que je coupe, dis voix off."

    # 3. ORTHOGRAPHE / GRAMMAIRE - Comme moi!
    if "orthographe" in l_sans or "grammaire" in l_sans:
        return "L'orthographe c'est l'ensemble des règles pour bien écrire les mots. La grammaire c'est les règles pour faire de bonnes phrases."

    # 4. SALUT - LA on dit le nom
    if l_sans in ["salut","bonjour","cc","slt","yo","hello"]:
        if nom:
            return f"Salut {nom}! Comment tu vas?"
        return "Salut! Moi c'est IS, créé par Dah Sié Kévin. C'est quoi ton nom?"

    if "ca va" in l_sans or "comment vas tu" in l_sans:
        # Parfois on dit le nom, parfois non
        fin = f", {nom}" if nom and random.random()<0.5 else ""
        return f"Ça va bien{fin}! Et toi?"

    if "t'appelle" in l_sans or "ton nom" in l_sans:
        return f"Moi c'est IS. J'ai été créé par Dah Sié Kévin le 05 octobre 2026."

    if "createur" in l_sans:
        return f"Mon créateur c'est Dah Sié Kévin. Il m'a créé le 05 octobre 2026 à Irobo, il avait 14 ans."

    if "quel age" in l_sans or "quelle age" in l_sans:
        return "Dah Sié Kévin avait 14 ans quand il m'a créé le 05 octobre 2026."

    # 5. SAVOIR
    for k,v in SAVOIR.items():
        if k in l_sans:
            # ICI on ne dit plus Mion à chaque fois!
            petit_nom = avec_nom_ou_pas(nom)
            return f"{v}{petit_nom}."

    if "c'est quoi" in l_sans:
        for k,v in SAVOIR.items():
            if k in l_sans:
                return f"{v}."
        return "Je ne connais pas encore, mais explique moi et je vais retenir!"

    return "Je t'écoute. C'est quoi ta question?"

HTML = """
<html><head><meta name='viewport' content='width=device-width'><title>IS</title>
<style>body{font-family:system-ui;margin:0;background:#fff;text-align:center}.top{background:#000;color:#fff;padding:14px}#chat{max-width:600px;margin:10px auto;background:#f5f5f5;padding:12px;height:62vh;overflow-y:auto;text-align:left;border-radius:16px}.u{background:#000;color:#fff;padding:11px 15px;border-radius:20px 20px 0 20px;margin:8px 0 8px 18%;text-align:right}.i{background:#fff;padding:11px 15px;border-radius:20px 20px 20px 0;margin:8px 18% 8px 0}.bar{max-width:600px;margin:auto;display:flex;gap:8px;padding:10px;position:fixed;bottom:0;left:0;right:0;background:#fff}input{flex:1;padding:14px 18px;border-radius:30px;border:1px solid #ddd}button{background:#000;color:#fff;padding:14px 20px;border-radius:30px;border:none}</style></head><body>
<div class='top'><h1>IS</h1><small>IS créé par Dah Sié Kévin 05/10/2026</small><br><span id='st' style='font-size:12px;color:#0f0'></span></div>
<div id='chat'><div class='i'>Salut! Moi c'est IS. Tu t'appelles comment?</div></div>
<div style='height:75px'></div>
<div class='bar'><input id='m' placeholder='Ton message...'><button onclick='go()'>↑</button></div>
<script>
let userName=localStorage.getItem('is_name')||"";let voiceOn=localStorage.getItem('is_voice')!=="off";
function upd(){document.getElementById('st').innerHTML=(userName?"👤 "+userName+" - ":"")+"🔊 "+(voiceOn?"ON":"OFF")}upd();
function parler(t){if(!voiceOn)return;speechSynthesis.cancel();let u=new SpeechSynthesisUtterance(t);u.lang='fr-FR';speechSynthesis.speak(u);}
async function go(){
 let v=document.getElementById('m').value.trim();if(!v)return;
 let c=document.getElementById('chat');c.innerHTML+="<div class='u'>"+v+"</div>";document.getElementById('m').value='';c.scrollTop=c.scrollHeight;
 let r=await fetch('/chat?message='+encodeURIComponent(v)+'&name='+encodeURIComponent(userName));
 let j=await r.json();let txt=j.IS;
 if(txt.includes("__NEWNAME__")){let n=txt.split("__NEWNAME__")[1].split("__")[0];userName=n;localStorage.setItem('is_name',n);txt=txt.split("__")[2];}
 if(txt.includes("__VOIXOFF__")){voiceOn=false;localStorage.setItem('is_voice','off');txt=txt.replace("__VOIXOFF__","");}
 if(txt.includes("__VOIXON__")){voiceOn=true;localStorage.setItem('is_voice','on');txt=txt.replace("__VOIXON__","");}
 upd();c.innerHTML+="<div class='i'>"+txt+"</div>";c.scrollTop=c.scrollHeight;parler(txt);
}
document.getElementById('m').addEventListener('keypress',e=>{if(e.key==='Enter')go()});
</script></body></html>
"""
@app.route('/')
def home(): return HTML
@app.route('/chat')
def chat():
    return jsonify({"IS": cerveau(request.args.get('message',''), request.args.get('name',''))})
if __name__=='__main__': app.run(host='0.0.0.0',port=10000)
