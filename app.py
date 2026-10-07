from flask import Flask, request, jsonify
app = Flask(__name__)

SAVOIR = {
    "france": "La France c'est un pays en Europe, capitale Paris 🇫🇷",
    "cote d'ivoire": "La Côte d'Ivoire est en Afrique de l'Ouest, au sud au bord de l'Atlantique 🇨🇮",
    "abidjan": "Abidjan c'est au sud de la Côte d'Ivoire",
    "mion": "Mion? C'est ton nom? Enchanté!",
    "python": "Python c'est le langage avec lequel j'ai été codé",
}

def cerveau(m, nom=""):
    l = m.lower().strip()
    if not l:
        return ""

    # APPRENDRE NOM SIMPLE
    if len(m.split()) == 1 and 2 <= len(m) <= 15 and m.isalpha():
        n = m.title()
        if n.lower() not in ["salut","bonjour","cc","yo","oui","non","ok","france","python"]:
            return f"__NEWNAME__{n}__Enchanté {n}! Moi c'est IS, j'ai été créé par Dah Sié Kévin le 05 octobre 2026. Ça fait plaisir de te connaître {n}!"

    if "je m'appelle" in l or "je m appelle" in l:
        n = m.split()[-1].title()
        return f"__NEWNAME__{n}__Enchanté {n}! Moi c'est IS créé par Dah Sié Kévin. Je vais me souvenir de toi {n}."

    appel = f" {nom}" if nom else ""

    # VOIX
    if "voix off" in l or l == "off":
        return "__VOIXOFF__D'accord, je coupe la voix. Si tu veux m'entendre parler, dis voix on."

    if "voix on" in l or l == "on":
        return "__VOIXON__Voilà, je remets la voix! Si tu veux que je me taise, dis voix off."

    # SALUT
    if l in ["salut","bonjour","cc","slt","yo","hello"]:
        if nom:
            return f"Salut {nom}! Comment tu vas? Moi c'est toujours IS, créé par Dah Sié Kévin."
        return "Salut! Moi c'est IS, créé par Dah Sié Kévin le 05 octobre 2026. C'est quoi ton nom?"

    if "ça va" in l or "ca va" in l:
        return f"Ça va bien{appel}! Et toi?"

    if "ton nom" in l or "t'appelle" in l or "qui es tu" in l:
        return f"Moi c'est IS{appel}, j'ai été créé par Dah Sié Kévin le 05 octobre 2026."

    if "createur" in l or "créateur" in l:
        return f"C'est Dah Sié Kévin qui m'a créé{appel}, le 05 octobre 2026 à Irobo, il avait 14 ans."

    # CONNAISSANCE
    for k,v in SAVOIR.items():
        if k in l:
            return f"{v}{appel}."

    if "c'est quoi" in l or "c est quoi" in l:
        for k,v in SAVOIR.items():
            if k in l:
                return f"{v}{appel}."
        q = l.replace("c'est quoi","").replace("c est quoi","").strip()
        return f"C'est quoi {q}{appel}? Je ne connais pas encore, mais je vais apprendre!"

    # PARLER NATUREL - PLUS DE "TU AS DIT"
    return f"Moi c'est IS{appel}, créé par Dah Sié Kévin le 05 octobre 2026. Je t'écoute{appel}."

HTML = """
<html><head><meta name='viewport' content='width=device-width'><title>IS</title>
<style>
body{font-family:system-ui;margin:0;background:#fff;text-align:center}
.top{background:#000;color:#fff;padding:14px}
#chat{max-width:600px;margin:10px auto;background:#f5f5f5;padding:12px;height:62vh;overflow-y:auto;text-align:left;border-radius:16px}
.u{background:#000;color:#fff;padding:11px 15px;border-radius:20px 20px 0 20px;margin:8px 0 8px 18%;text-align:right}
.i{background:#fff;padding:11px 15px;border-radius:20px 20px 20px 0;margin:8px 18% 8px 0;box-shadow:0 1px 2px #0001}
.bar{max-width:600px;margin:auto;display:flex;gap:8px;padding:10px;position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1px solid #eee}
input{flex:1;padding:14px 18px;border-radius:30px;border:1px solid #ddd;outline:none;font-size:15px}
button{background:#000;color:#fff;padding:14px 20px;border-radius:30px;border:none;font-size:16px}
</style></head><body>
<div class='top'><h1>IS</h1><small>Salut moi c'est IS créé par Dah Sié Kévin 05/10/2026</small><br><span id='st' style='font-size:12px;color:#0f0'></span></div>
<div id='chat'><div class='i'>Salut! Moi c'est IS créé par Dah Sié Kévin. Tu t'appelles comment? Dis juste ton prénom.</div></div>
<div style='height:75px'></div>
<div class='bar'><input id='m' placeholder='Ton message...'><button onclick='go()'>↑</button></div>
<script>
let userName=localStorage.getItem('is_name')||"";
let voiceOn=localStorage.getItem('is_voice')!=="off";
function upd(){document.getElementById('st').innerHTML=(userName?"👤 "+userName+" - ":"")+"🔊 "+(voiceOn?"ON - dis voix off pour couper":"OFF - dis voix on pour m'entendre")}
upd();
function parler(t){if(!voiceOn)return;speechSynthesis.cancel();let u=new SpeechSynthesisUtterance(t);u.lang='fr-FR';u.rate=1;speechSynthesis.speak(u);}
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
