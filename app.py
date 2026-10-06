from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

produits = []
credits = []

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>IS KÉVIN</title>
<style>
body{font-family:Arial;background:#f5f5f5;padding:15px}
h1{background:#111;color:#fff;padding:15px;text-align:center;border-radius:10px}
.card{background:#fff;padding:15px;border-radius:10px;margin:10px 0;box-shadow:0 2px 5px #ccc}
input,button{width:100%;padding:12px;margin:5px 0;border-radius:8px;border:1px solid #ccc}
button{background:#111;color:#fff;font-weight:bold}
.badge{background:#25D366;color:#fff;padding:3px 8px;border-radius:10px;font-size:12px}
</style>
</head>
<body>
<h1>IS KÉVIN 👕👗</h1>
<div class="card">
<h3>➕ Ajouter Produit</h3>
<form method="post" action="/add">
<input name="nom" placeholder="Nom du vêtement ex: Robe" required>
<input name="prix" type="number" placeholder="Prix" required>
<input name="stock" type="number" placeholder="Stock" required>
<button>Ajouter</button>
</form>
</div>
<div class="card">
<h3>📦 Stock ({{ produits|length }})</h3>
{% for p in produits %}
<p><b>{{ p.nom }}</b> - {{ p.prix }} FCFA - Stock: {{ p.stock }}</p>
{% else %}
<p>Aucun produit</p>
{% endfor %}
</div>
<div class="card">
<h3>💳 Crédit Client</h3>
<form method="post" action="/credit">
<input name="client" placeholder="Nom client" required>
<input name="montant" type="number" placeholder="Montant" required>
<button>Ajouter Crédit</button>
</form>
{% for c in credits %}
<p>{{ c.client }} doit {{ c.montant }} FCFA</p>
{% endfor %}
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, produits=produits, credits=credits)

@app.route("/add", methods=["POST"])
def add():
    produits.append({"nom":request.form["nom"],"prix":request.form["prix"],"stock":request.form["stock"]})
    return redirect("/")

@app.route("/credit", methods=["POST"])
def credit():
    credits.append({"client":request.form["client"],"montant":request.form["montant"]})
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
