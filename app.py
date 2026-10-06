from flask import Flask, request, jsonify

app = Flask(__name__)

HTML = """
<html><head><meta name="viewport" content="width=device-width">
<title>IS</title>
<style>
body{font-family:Arial;text-align:center;padding:20px}
.box{background:#111;color:#fff;padding:30px;border-radius:15px}
input{width:80%;padding:15px;margin:10px}
button{background:#111;color:#fff;padding:15px 30px;border-radius:10px}
</style></head>
<body>
<div class="box">
<h1>Salut moi c'est IS 🤖</h1>
<p>J'ai été créé par Dah Sie Kevin le 5 octobre 2026 à Irobo</p>
</div>
<input id="msg" placeholder="Parle avec IS...">
<br><button onclick="parler()">Envoyer</button>
<p id="rep"></p>
<script>
async function parler(){
 let m=document.getElementById('msg').value;
 let r=await fetch('/chat?message='+m);
 let d=await r.json();
 document.getElementById('rep').innerText=d.IS;
}
</script>
</body></html>
"""

@app.route('/')
def home():
    return HTML

@app.route('/chat')
def chat():
    message = request.args.get('message','')
    reponse = "Salut moi c'est IS j'ai été créé par Dah Sie Kevin le 5 octobre 2026 à Irobo"
    if message:
        reponse += f". Tu m'as dit: {message} BOSS!"
    return jsonify({"IS": reponse})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
