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
