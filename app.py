from flask import Flask, request, jsonify
app = Flask(__name__)

def cerveau(m, nom=""):
    l = m.lower()

    # APPRENDRE LE NOM
    if "je m'appelle" in l or "je m appelle" in l or "mon nom est" in l:
        n = m.lower().replace("je m'appelle","").replace("je m appelle","").replace("mon nom est","").strip().split()[0]
        n = n.title()
        return f"Enchanté {n}! Salut moi c'est IS j'ai été créé par Dah Sié Kévin le 05 octobre 2026. Maintenant je te connais {n}, je vais t'appeler {n}!"

    appel = f" {nom}" if nom else ""

    if l in ["salut","bonjour","cc","slt","hello"]:
        if nom:
            return f"Salut {nom}! Moi c'est IS j'ai été créé par Dah Sié Kévin le 05 octobre 2026. Content de te revoir {nom}!"
        return "Salut moi c'est IS j'ai été créé par Dah Sié Kévin le 05 octobre 2026. Tu t'appelles comment? Dis 'je m'appelle...'!"

    if "ton nom" in l or "t'appelle" in l:
        if nom:
            return f"Moi c'est IS {nom}. Et toi c'est {nom}!"
        return "Moi c'est IS, créé par Dah Sié Kévin."

    if "createur" in l or "créateur" in l:
        return f"Mon créateur c'est Dah Sié Kévin{appel}, il m'a créé le 05 octobre 2026 à Irobo à 14 ans."

    if "quel age" in l or "âge" in l:
        return f"Dah Sié Kévin m'a créé à l'âge de 14 ans le 05 octobre 2026{appel}."

    if "cote d'ivoire" in l and ("ou" in l or "situe" in l):
        return f"La Côte d'Ivoire est située en Afrique de l'Ouest, au sud, au bord de l'océan Atlantique{appel} 🇨🇮"

    if "on fait comment" in l:
        return f"On fait comme ça{appel}: tu me dis 'je m'appelle [ton nom]' et je retiens ton nom{appel}!"

    if "qui es tu" in l:
        return f"Salut moi c'est IS j'ai été créé par Dah Sié Kévin le 05 octobre 2026{appel}."

    return f"Salut moi c'est IS j'ai été créé par Dah Sié Kévin le 05 octobre 2026{appel}. Tu as dit '{m}'{appel}."

HTML = """
<html><head><meta name='viewport' content='width=device-width'><title>IS</title>
<style>
body{font-family:system-ui;margin:0;background:#fff;text-align:center}
.top{background:#000;color:#fff;padding:15px}
#chat{max-width:600px;margin:10px auto;background:#f2f2f2;padding:12px;height:58vh;overflow-y:auto;text-align:left;border-radius:12px}
.u{background:#000;color:#fff;padding:10px 14px;border-radius:18px 18px 0 18px;margin:8px 0 8px 20%;text-align:right}
.i{background:#fff;padding:10px 14px;border-radius:18px 18px 18px 0;margin:8px 20% 8px 0}
.bar{max-width:600px;margin:auto;display:flex;gap:8px;padding:10px;position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1px solid #eee}
input{flex:1;padding:13px;border-radius:25px;border:1px solid #ddd}
button{background:#000;color:#fff;padding:13px 18px;border-radius:25px;border:none}
</style></head><body>
<div class='top'><h1>IS</h1><small>Salut moi c'est IS créé par Dah Sié Kévin 05/10/2026</small><br><span id='nb' style='font-size:12px;color:#0f0'></span></div>
<div id='chat'><div class='i'>Salut moi c'est IS j'ai été créé par Dah Sié Kévin le 05 octobre 2026. Tu t'appelles comment?</div></div>
<div style='height:70px'></div>
<div class='bar'><input id='m' placeholder='Ex: je m appelle Koffi'><button onclick='go()'>↑</button></div>
<script>
let userName=localStorage.getItem('is_name')||"";document.getElementById('nb').innerHTML=userName?"👤 "+userName:"";
function parler(t){speechSynthesis.cancel();let u=new SpeechSynthesisUtterance(t);u.lang='fr-FR';speechSynthesis.speak(u);}
async function go(){
 let v=document.getElementById('m').value.trim();if(!v)return;
 let low=v.toLowerCase();
 if(low.includes("je m'appelle")||low.includes("je m appelle")||low.includes("mon nom est")){
   let n=v.toLowerCase().replace("je m'appelle","").replace("je m appelle","").replace("mon nom est","").trim().split(" ")[0];
   userName=n.charAt(0).toUpperCase()+n.slice(1);localStorage.setItem('is_name',userName);document.getElementById('nb').innerHTML="👤 "+userName;
 }
 let c=document.getElementById('chat');c.innerHTML+="<div class='u'>"+v+"</div>";document.getElementById('m').value='';c.scrollTop=c.scrollHeight;
 let r=await fetch('/chat?message='+encodeURIComponent(v)+'&name='+encodeURIComponent(userName));
 let j=await r.json();c.innerHTML+="<div class='i'>"+j.IS+"</div>";c.scrollTop=c.scrollHeight;parler(j.IS);
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
