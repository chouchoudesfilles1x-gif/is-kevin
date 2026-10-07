import unicodedat
1+1=2, salutations, présentation/: salut moi c'est IS Intelligence secondaire j'ai été créé par Dah Sié Kévin le 05 octobre 2026 puis je connaître votre non.
def nettoyer(txt):
    txt = txt.lower()
    # Enlève accents: dérivation -> derivation
    txt = ''.join(c for c in unicodedata.normalize('NFD', txt) if unicodedata.category(c)!= 'Mn')
    return txt

def cerveau(message):
    msg = nettoyer(message)

    # === DICTIONNAIRE COMPLET - TOUTES TES QUESTIONS ===
    SAVOIR = {
        "derivation": "📐 LA DÉRIVATION:\n- Dérivée de xⁿ = n*xⁿ⁻¹\n- Ex: (x²)' = 2x\n- (sin x)' = cos x\n- (cos x)' = -sin x\n- Utilité: trouver pente, tangente, variations",

        "racine carree": "√ LA RACINE CARRÉE:\n- √a = nombre qui au carré donne a\n- √9 = 3 car 3²=9\n- √16 = 4\n- √2 ≈ 1.414\n- Propriété: √(a*b) = √a * √b",

        "france": "La France est en Europe, capitale Paris 🇫🇷",
        "abidjan": "Abidjan 🇨🇮 est en Côte d'Ivoire, capitale économique!",
        "yamoussoukro": "Yamoussoukro est la capitale politique de la Côte d'Ivoire",
        "1": "Tu as tapé 1 - Je t'écoute, pose ta question complète!",
        "bonjour": "Salut BOSS! 👋 Pose ta question",
        "math": "Je suis fort en maths: dérivation, racine carrée, équation, etc. Demande!",
    }

    # Cherche si un mot-clé du SAVOIR est DANS ton message
    for cle in SAVOIR:
        if cle in msg:
            return SAVOIR[cle]

    # Si rien trouvé
    return "Je t'écoute. C'est quoi ta question? 🤔\nEssaie: dérivation, racine carrée, France, Abidjan..."
