from flask import Flask, request, jsonify
import unicodedata
import requests
import os

app = Flask(__name__)

def nettoyer(txt):
    txt = txt.lower()
    txt = ''.join(c for c in unicodedata.normalize('NFD', txt) if unicodedata.category(c)!= 'Mn')
    return txt

def recherche_web(question):
    try:
        # Wikipedia
        q = question.strip().replace(" ", "_")
        url = f"https://fr.wikipedia.org/api/rest_v1/page/summary/{q}"
        r = requests.get(url, timeout=4, headers={"User-Agent":"IS-Kevin/1.0"})
        if r.status_code == 200:
            data = r.json()
            if data.get('extract'):
                return f"🌐 Web (Wikipedia):\n\n{data.get('extract')}"
    except:
        pass
    return None

def cerveau(message):
    if not message:
        return "Je t'écoute BOSS?"
    msg = nettoyer(message)
    
    SAVOIR = {
        "derivation": "📐 DERIVATION:\n- (x^n)' = n*x^(n-1)\n- (x2)' = 2x\n- (sin x)' = cos x\n- (cos x)' = -sin x",
        "derivee": "📐 DERIVEE: (x2)' = 2x , (sin x)' = cos x",
        "racine carree": "√ RACINE: √9=3, √16=4, √2=1.414",
        "racine": "√ RACINE: √9=3, √16=4",
        "france": "France 🇫🇷 Europe, capitale Paris",
        "abidjan": "Abidjan 🇨🇮 capitale éco Côte d'Ivoire",
        "yamoussoukro": "Yamoussoukro capitale politique CI",
        "bonjour": "Salut BOSS! 👋",
        "salut": "Salut! 😊",
        "qui es tu": "IS par Dah Sié Kévin 05/10/2026 🤖",
        "1": "Pose ta question complète!",
    }
    
    for cle, rep in SAVOIR.items():
        if cle in msg:
            return rep
    
    # Si pas trouvé -> recherche web
    web = recherche_web(message)
    if web:
        return web
        
    return "Je t'écoute. C'est quoi ta question? 🤔\nEssaie: derivation, racine, France"

HTML = """<!DOCTYPE html>
<html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>IS</title>
<style>
body{margin:0;font-family:Arial;background:#eee}
.head{background:#000;color:#fff;text-align:center;padding:15px}
.head h1{margin:0;font-size:38px}
.chat{max-width:700px;margin:auto;padding:10px 10px 80px}
.m{padding:10px 14px;border-radius:18px;margin:7px;max-width:80%;word-wrap:break-word;white-space:pre-wrap}
.u{background:#000;color:#fff;margin-left:auto;border-bottom-right-radius:4px}
.b{background:#fff;color:#000;margin-right:auto;border-bottom-left-radius:4px}
.bar{position:fixed;bottom:0;left:0;right:0;background:#eee;padding:10px;display:flex;gap:10px}
.bar input{flex:1;padding:12px;border-radius:25px;border:1px solid #ccc;outline:none}
.bar button{background:#000;color:#fff;border:none;width:48px;height:48px;border-radius:50%}
</style></head><body>
<div class=head><h1>IS</h1><div>IS créé par Dah Sié Kévin 05/10/2026<br>👤 Yamoussoukro - 📡 ON</div></div>
<div class=chat id=chat><div class='m b'>Abidjan 🇨🇮.</div></div>
<div class=bar><input id=i placeholder='Ton message...' onkeypress="if(event.key=='Enter')send()"><button onclick=send()>↑</button></div>
<script>
function add(t,c){let d=document.createElement('div');d.className='m '+c;d.textContent=t;document.getElementById('chat').appendChild(d);window.scrollTo(0,document.body.scrollHeight)}
async function send(){let e=document.getElementById('i');let v=e.value.trim();if(!v)return;add(v,'u');e.value='';let r=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:v})});let j=await r.json();add(j.reponse,'b')}
</script></body></html>
"""

@app.route('/')
def home(): return HTML

@app.route('/ask', methods=['POST'])
def ask():
    d = request.get_json() or {}
    rep = cerveau(d.get('message',''))
    return jsonify({"reponse": rep})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
