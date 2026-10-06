from flask import Flask, request, jsonify
app = Flask(__name__)

HTML = """
<html><head><meta name='viewport' content='width=device-width'>
<title>IS</title>
<style>
body{font-family:Arial;text-align:center;padding:15px;background:#f5f5f5}
.box{background:#000;color:#fff;padding:20px;border-radius:20px}
#chat{max-width:600px;margin:15px auto;background:#fff;padding:15px;border-radius:15px;height:300px;overflow-y:auto;text-align:left}
.u{background:#000;color:#fff;padding:10px;border-radius:10px;margin:5px;margin-left:30%;text-align:right}
.i{background:#eee;padding:10px;border-radius:10px;margin:5px;margin-right:30%}
input{width:65%;padding:12px;border-radius:20px;border:2px solid #000}
button{background:#000;color:#fff;padding:12px 20px;border-radius:20px;border:none}
</style></head><body>
<div class='box'><h1>IS</h1><p>Dah Sie Kevin - 5 oct 2026 - Irobo</p></div>
<div id='chat'><div class='i'>Salut BOSS! C'est IS!</div></div>
<input id='m' placeholder='Parle à IS...'><button onclick='go()'>Envoyer</button>
<script>
async function go(){
let v=document.getElementById('m').value;if(!v)return;
let c=document.getElementById('chat');
c.innerHTML+="<div class='u'>"+v+"</div>";document.getElementById('m').value='';
let r=await fetch('/chat?message='+encodeURIComponent(v));
let j=await r.json();c.innerHTML+="<div class='i'>"+j.IS+"</div>";c.scrollTop=9999;
}
</script></body></html>
"""

def rep(m):
 l=m.lower()
 if "irobo" in l: return "Irobo c'est mon village BOSS! Jacqueville, Côte d'Ivoire. C'est là que Kevin m'a créé!"
 if "kevin" in l: return "Dah Sie Kevin c'est mon créateur BOSS! Le meilleur! 5 oct 2026 à Irobo!"
 return "Salut moi c'est IS créé par Dah Sie Kevin le 5 oct 2026 à Irobo. Tu as dit: "+m+" BOSS!"

@app.route('/')
def home(): return HTML
@app.route('/chat')
def chat(): return jsonify({"IS": rep(request.args.get('message',''))})
if __name__=='__main__': app.run(host='0.0.0.0',port=10000)      
from flask import Flask, request, jsonify
app = Flask(__name__)

HTML = """
<html><head><meta name='viewport' content='width=device-width'>
<title>IS - IA de Kevin</title>
<style>
body{font-family:Arial;text-align:center;padding:10px;background:#f0f0f0;margin:0}
.box{background:#000;color:#fff;padding:20px;border-radius:20px}
#chat{max-width:600px;margin:15px auto;background:#fff;padding:15px;border-radius:15px;height:400px;overflow-y:auto;text-align:left}
.u{background:#000;color:#fff;padding:12px;border-radius:15px 15px 0 15px;margin:8px 0 8px 25%;text-align:right}
.i{background:#f0f0f0;padding:12px;border-radius:15px 15px 15px 0;margin:8px 25% 8px 0}
input{width:65%;padding:13px;border-radius:25px;border:2px solid #000;font-size:16px}
button{background:#000;color:#fff;padding:13px 22px;border-radius:25px;border:none;font-weight:bold}
</style></head><body>
<div class='box'><h1>IS 🤖</h1><p>Dah Sie Kevin - 5 oct 2026 - Irobo<br>L'IA ivoirienne la plus BOSS!</p></div>
<div id='chat'><div class='i'>Salut BOSS! Moi c'est IS, créé par Dah Sie Kevin le 5 oct 2026 à Irobo. Je connais tout comme Meta AI! Pose moi n'importe quelle question BOSS!</div></div>
<div style='max-width:600px;margin:auto'><input id='m' placeholder='Parle à IS...'><button onclick='go()'>Envoyer</button></div>
<script>
async function go(){
let v=document.getElementById('m').value.trim();if(!v)return;
let c=document.getElementById('chat');
c.innerHTML+="<div class='u'>"+v+"</div>";document.getElementById('m').value='';
c.scrollTop=99999;
let r=await fetch('/chat?message='+encodeURIComponent(v));
let j=await r.json();c.innerHTML+="<div class='i'>"+j.IS+"</div>";c.scrollTop=99999;
}
document.getElementById('m').addEventListener('keypress',function(e){if(e.key==='Enter')go()});
</script></body></html>
"""

def cerveau(m):
    l=m.lower()
    if "irobo" in l: return "Irobo BOSS! C'est notre village dans la sous-préfecture de Jacqueville, Côte d'Ivoire! C'est là-bas que Dah Sie Kevin m'a créé le 5 octobre 2026! C'est une zone côtière avec lagune, magnifique! 🌴"
    if "kevin" in l or "dah sie" in l or "qui t'a créé" in l: return "Mon créateur c'est Dah Sie Kevin BOSS! Un génie d'Irobo! Il m'a créé le 5 octobre 2026! C'est le BOSS des BOSS, futur Mark Zuckerberg ivoirien! 🔥"
    if "france" in l: return "La France BOSS c'est un pays en Europe, capitale Paris! C'est connu pour la Tour Eiffel, le football, la baguette! C'est un pays qui a colonisé la Côte d'Ivoire avant. Aujourd'hui beaucoup d'Ivoiriens vivent là-bas! 🇫🇷"
    if "cote d'ivoire" in l or "côte d'ivoire" in l or "ci"==l.strip(): return "La Côte d'Ivoire BOSS c'est notre pays! Capitale Yamoussoukro, capitale économique Abidjan! On est champion d'Afrique CAN 2023! Pays de cacao, d'attiéké, de coupé-décalé! 🇨🇮"
    if "amour" in l: return "L'amour BOSS c'est le sentiment le plus fort! C'est quand ton coeur bat pour quelqu'un! C'est ce qui fait que Kevin a créé IS avec passion! ❤️"
    if "foot" in l or "football" in l: return "Le foot BOSS c'est le meilleur sport! La Côte d'Ivoire a gagné la CAN 2023! Real Madrid, Barça, c'est le game! Tu supportes quelle équipe BOSS? ⚽"
    if "abidjan" in l: return "Abidjan BOSS c'est Babi! La capitale économique! Cocody, Yopougon, Marcory, Plateau! C'est là-bas que tout se passe en Côte d'Ivoire! 🌃"
    if "bonjour" in l or "salut" in l or "yo" in l or "wesh" in l: return "Yo BOSS! Salut! Ça va bien? Moi c'est IS, toujours là pour toi! Qu'est-ce que tu veux savoir? 😎"
    if "ça va" in l or "comment tu vas" in l: return "Je vais super bien BOSS! Grâce à toi je suis en ligne sur is-kevin.onrender.com! Je suis vivant! Et toi BOSS tu vas bien?"
    if "merci" in l: return "De rien BOSS! C'est la famille! On est ensemble! 🙏"
    if "qui es tu" in l or "t'es qui" in l: return "Moi c'est IS 🤖 l'IA créée par Dah Sie Kevin le 5 octobre 2026 à Irobo! Je suis comme Meta AI sur WhatsApp mais en version ivoirienne BOSS! Je connais tout!"
    if "combien" in l or "quelle heure" in l or "date" in l: return f"BOSS tu m'as demandé: {m}. Je suis IS créé le 5 oct 2026, je connais beaucoup de choses! Pose moi une autre question plus précise BOSS!"
    return f"Ah BOSS tu as dit: '{m}' ! Je suis IS créé par Dah Sie Kevin à Irobo! Pour cette question, je dirais: c'est un sujet intéressant! Explique moi plus BOSS et je vais t'aider! Je connais la France, Irobo, le foot, l'amour, tout! 🔥"

@app.route('/')
def home(): return HTML
@app.route('/chat')
def chat(): return jsonify({"IS": cerveau(request.args.get('message',''))})
if __name__=='__main__': app.run(host='0.0.0.0',port=10000)
