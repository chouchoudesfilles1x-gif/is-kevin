     from flask import Flask, request, jsonify
app = Flask(__name__)
from flask import Flask, request, jsonify
from datetime import datetime
app = Flask(__name__)

# ===== CERVEAU GÉANT DE IS - By Dah Sié Kévin =====
CONNAISSANCE = {
    "cote d'ivoire": "La Côte d'Ivoire est située en Afrique de l'Ouest, au sud du Sahara, au bord du Golfe de Guinée, entre le Liberia à l'ouest et le Ghana à l'est. Capitale Yamoussoukro, capitale éco Abidjan. 🇨🇮",
    "ou est la cote d'ivoire": "La Côte d'Ivoire est située en Afrique de l'Ouest, au sud, au bord de l'océan Atlantique, entre Liberia et Ghana. 🇨🇮",
    "france": "La France est située en Europe de l'Ouest, capitale Paris, 68M habitants. 🇫🇷",
    "irobo": "Irobo est situé dans la sous-préfecture de Jacqueville, au sud de la Côte d'Ivoire, au bord de la lagune. C'est là que IS a été créé.",
    "abidjan": "Abidjan est située au sud de la Côte d'Ivoire, au bord de la lagune Ebrié.",
    "messi": "Messi est un footballeur argentin, GOAT, 8 Ballon d'Or.",
    "ronaldo": "Cristiano Ronaldo, portugais, 5 Ballon d'Or.",
    "python": "Python est un langage créé en 1991, c'est avec ça que IS est codé!",
    "ia": "IA = Intelligence Artificielle. IS est une IA créée par Dah Sié Kévin.",
    "amour": "L'amour est un sentiment fort d'affection. ❤️",
    "football": "Football: sport à 11 joueurs, le plus populaire au monde.",
}

INTRO = "Salut moi c'est IS j'ai été créé par Dah Sié Kévin le 05 octobre 2026"

def cerveau(m):
    l = m.lower().strip()

    # 1. PRESENTATION OBLIGATOIRE
    if l in ["salut","bonjour","cc","slt","hello","yo","salut is"]:
        return f"{INTRO}! Je suis là pour répondre à tes questions BOSS!"

    # 2. QUI ES TU / TON NOM
    if "ton nom" in l or "t'appelles" in l or "comment tu t'appelles" in l or "c'est quoi ton nom" in l:
        return "Moi c'est IS, Intelligent System. Je ne dis pas ton nom BOSS, je t'appelle BOSS par respect. Mon créateur c'est Dah Sié Kévin."

    # 3. TON CREATEUR
    if "ton createur" in l or "ton créateur" in l or "qui t'a créé" in l or "qui t'a cree" in l or "qui est ton createur" in l:
        return "Mon créateur c'est Dah Sié Kévin. C'est lui qui m'a créé le 05 octobre 2026 à Irobo."

    # 4. AGE DE CREATION - 14 ANS
    if "quel age" in l and ("cree" in l or "créé" in l) or "a quel age" in l or "âge" in l and "créé" in l or "14 ans" in l or "il avait quel age" in l:
        return "Dah Sié Kévin m'a créé à l'âge de 14 ans, le 05 octobre 2026 à Irobo. Un génie BOSS!"

    # 5. OU EST LA COTE D'IVOIRE
    if "ou est la cote" in l or "ou se situe la cote" in l or "cote d'ivoire est situe" in l or "ou se trouve la ci" in l:
        return "La Côte d'Ivoire est située en Afrique de l'Ouest, au sud, au bord du Golfe de Guinée, entre le Liberia et le Ghana. 🇨🇮"

    # 6. DATE / HEURE
    if "date" in l and "creation" in l or "quand t'a" in l:
        return "J'ai été créé le 05 octobre 2026 par Dah Sié Kévin à Irobo."
    if "heure" in l:
        return f"Il est {datetime.now().strftime('%H:%M')} BOSS. Moi j'ai été créé le 05 octobre 2026."

    # 7. CONNAISSANCE GENERALE
    for mot, defaut in sorted(CONNAISSANCE.items(), key=lambda x: -len(x[0])):
        if mot in l:
            return defaut

    # 8. FALLBACK
    return f"{INTRO}. Tu m'as dit: '{m}'. Je connais beaucoup de choses BOSS! Demande moi: c'est où la Côte d'Ivoire, c'est quoi ton nom, ton créateur a quel âge, etc."

HTML = f"""
<html><head><meta name='viewport' content='width=device-width'><title>IS - By Dah Sié Kévin</title>
<style>
body{{font-family:system-ui;text-align:center;padding:0;margin:0;background:#fff}}
.box{{background:#000;color:#fff;padding:20px;border-radius:0 0 25px 25px}}
#chat{{max-width:700px;margin:10px auto;background:#f5f5f5;padding:12px;border-radius:15px;height:62vh;overflow-y:auto;text-align:left}}
.u{{background:#000;color:#fff;padding:11px 14px;border-radius:18px 18px 0 18px;margin:8px 0 8px 15%;text-align:right}}
.i{{background:#fff;padding:11px 14px;border-radius:18px 18px 18px 0;margin:8px 15% 8px 0;box-shadow:0 1px 2px rgba(0,0,0,0.1)}}
.bar{{max-width:700px;margin:auto;display:flex;gap:8px;padding:10px;background:#fff;position:fixed;bottom:0;left:0;right:0;border-top:1px solid #eee}}
input{{flex:1;padding:13px 16px;border-radius:25px;border:1px solid #ddd;outline:none;font-size:16px}}
button{{background:#000;color:#fff;padding:13px 18px;border-radius:25px;border:none;font-weight:bold}}
small{{color:#888}}
</style></head><body>
<div class='box'><h1 style='margin:0'>IS</h1><small>Salut moi c'est IS j'ai été créé par Dah Sié Kévin le 05 octobre 2026 - 14 ans - Irobo</small></div>
<div id='chat'><div class='i'>{INTRO}! Pose moi une question BOSS: Où est la Côte d'Ivoire? C'est quoi ton nom? Ton créateur t'a créé à quel âge?</div></div>
<div style='height:70px'></div>
<div class='bar'><input id='m' placeholder='Ex: c est ou la Cote d Ivoire?'><button onclick='go()'>↑</button></div>
<script>
async function go(){{
let v=document.getElementById('m').value.trim();if(!v)return;
let c=document.getElementById('chat');
c.innerHTML+="<div class='u'>"+v+"</div>";document.getElementById('m').value='';
c.scrollTop=c.scrollHeight;
let r=await fetch('/chat?message='+encodeURIComponent(v));
let j=await r.json();
c.innerHTML+="<div class='i'>"+j.IS+"</div>";c.scrollTop=c.scrollHeight;
try{{let s=window.speechSynthesis; s.speak(new SpeechSynthesisUtterance(j.IS));}}catch(e){{}}
}}
document.getElementById('m').addEventListener('keypress',e=>{{if(e.key==='Enter')go()}});
</script></body></html>
"""

@app.route('/')
def home(): return HTML
@app.route('/chat')
def chat(): return jsonify({"IS": cerveau(request.args.get('message',''))})
if __name__=='__main__': app.run(host='0.0.0.0',port=10000)
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
