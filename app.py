from flask import Flask, request, jsonify
import requests, unicodedata, random
app = Flask(__name__)

# === METS TES INFOS WHATSAPP ICI ===
TOKEN = "METS_TON_TOKEN_ICI"
PHONE_ID = "METS_TON_PHONE_ID_ICI"
VERIFY = "is-kevin-2026"

def sans_accent(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t) if unicodedata.category(c)!= 'Mn')

SAVOIR = {
    "cote d'ivoire": "La Côte d'Ivoire 🇨🇮 est située en Afrique de l'Ouest, au sud au bord de l'Atlantique. Capitale Yamoussoukro, plus grande ville Abidjan 🌴",
    "irobo": "Irobo 🏝️ est un village à Jacqueville, au sud de la Côte d'Ivoire, c'est là que j'ai été créé par Dah Sié Kévin 💻",
    "abidjan": "Abidjan 🌃 est au sud de la Côte d'Ivoire, au bord de la lagune Ebrié, capitale économique 💰",
    "france": "La France 🇫🇷 est en Europe, capitale Paris 🗼",
}

def cerveau(m, nom=""):
    l = m.lower().strip()
    l_sans = sans_accent(l)
    mots_interdits = ["salut","bonjour","france","cote","ivoire","irobo","abidjan","c'est","quoi"]
    if len(m.split())==1 and m.isalpha() and len(m)>2 and l not in mots_interdits:
        return f"__NEWNAME__{m.title()}__Enchanté {m.title()}! 😊 Moi c'est IS créé par Dah Sié Kévin le 05 octobre 2026 🚀"
    if "voix off" in l_sans or l_sans=="off": return "__VOIXOFF__D'accord 🔇 je coupe la voix. Dis voix on pour m'entendre 🎙️"
    if "voix on" in l_sans or l_sans=="on": return "__VOIXON__Voilà 🔊 je remets la voix! Dis voix off pour couper 🔇"
    if l_sans in ["salut","bonjour","cc","slt","yo"]: return f"Salut {nom}! 😊 Comment tu vas? 🚀" if nom else "Salut! 👋 Moi c'est IS créé par Dah Sié Kévin 😎 C'est quoi ton nom?"
    if "ca va" in l_sans: return f"Ça va bien {nom}! 😊 Et toi? ✨" if nom and random.random()<0.5 else "Ça va bien! 😊 Et toi? 🙏"
    if "createur" in l_sans: return "Mon créateur c'est Dah Sié Kévin 👑 Il m'a créé le 05 octobre 2026 à Irobo à 14 ans 💻🔥"
    if "quel age" in l_sans: return "Dah Sié Kévin avait 14 ans 🎂 quand il m'a créé le 05 octobre 2026 🚀"
    for k,v in SAVOIR.items():
        if k in l_sans: return v
    return "Je t'écoute 👂 C'est quoi ta question? 🤔"

# SITE AVEC VOIX + EMOJIS
HTML = """
<html><head><meta name='viewport' content='width=device-width'><title>IS</title>
<style>
body{font-family:system-ui;margin:0;background:#fff;text-align:center}
.top{background:#000;color:#fff;padding:14px;position:sticky;top:0;z-index:10}
#chat{max-width:600px;margin:10px auto;background:#f5f5f5;padding:12px;height:58vh;overflow-y:auto;text-align:left;border-radius:16px}
.u{background:#000;color:#fff;padding:11px 15px;border-radius:20px 20px 0 20px;margin:8px 0 8px 18%;text-align:right}
.i{background:#fff;padding:11px 15px;border-radius:20px 20px 20px 0;margin:8px 18% 8px 0}
.bar{max-width:600px;margin:auto;display:flex;gap:6px;padding:10px;position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1px solid #eee}
input{flex:1;padding:14px 18px;border-radius:30px;border:1px solid #ddd}
.btn{padding:12px 14px;border-radius:30px;border:none;cursor:pointer}
.black{background:#000;color:#fff}
.gray{background:#eee}
.emoji-bar{max-width:600px;margin:auto;display:flex;gap:6px;overflow-x:auto;padding:6px 10px;background:#fff}
.emoji-bar span{font-size:22px;cursor:pointer;padding:4px}
</style></head><body>
<div class='top'><h1>IS 🤖</h1><small>IS créé par Dah Sié Kévin 05/10/2026 - WhatsApp: /webhook</small><br><span id='st' style='font-size:12px;color:#0f0'></span></div>
<div id='chat'><div class='i'>Salut! 👋 Moi c'est IS créé par Dah Sié Kévin 😎 Tu t'appelles comment?</div></div>
<div class='emoji-bar' id='emojibar'></div>
<div style='height:110px'></div>
<div class='bar'>
<button class='btn gray' onclick='toggleVoice()' id='voiceBtn'>🔊</button>
<button class='btn gray' onclick='startMic()' id='micBtn'>🎙️</button>
<input id='m' placeholder='Ton message... 😊'>
<button class='btn black' onclick='go()'>↑</button>
</div>
<script>
let userName=localStorage.getItem('is_name')||"";let voiceOn=localStorage.getItem('is_voice')!=="off";
let emojis=["😊","😂","🔥","❤️","🇨🇮","🚀","💻","👋","😎","🙏","✨","🌴","🤖","👑"];
function upd(){document.getElementById('st').innerHTML=(userName?"👤 "+userName+" - ":"")+(voiceOn?"🔊 ON":"🔇 OFF");document.getElementById('voiceBtn').innerHTML=voiceOn?"🔊":"🔇"}upd();
document.getElementById('emojibar').innerHTML=emojis.map(e=>`<span onclick="addEmoji('${e}')">${e}</span>`).join('');
function addEmoji(e){document.getElementById('m').value+=e;document.getElementById('m').focus();}
function toggleVoice(){voiceOn=!voiceOn;localStorage.setItem('is_voice',voiceOn?"on":"off");upd();if(!voiceOn)speechSynthesis.cancel();}
function
