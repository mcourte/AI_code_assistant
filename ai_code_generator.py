import google.generativeai as genai

# Clé API par défaut (remplace par la tienne)
DEFAULT_API_KEY = "AIzaSyBzmGVWz4zoLmDIGzSId0-gdEiz7dD2TvQ"

# Demande à l'utilisateur d'entrer sa clé API (optionnel)
user_api_key = input("🔑 Entrez votre API Key Google (ou appuyez sur Entrée pour utiliser la clé par défaut) : ").strip()

# Utilisation de la clé API fournie ou de la clé par défaut
API_KEY = user_api_key if user_api_key else DEFAULT_API_KEY
genai.configure(api_key=API_KEY)


def generate_code(prompt):
    """Génère du code avec Google Gemini"""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Utilise un modèle valide
        response = model.generate_content(prompt)
        return response.text if response else "Erreur : réponse vide."
    except Exception as e:
        return f"❌ Erreur lors de la génération : {e}"


if __name__ == "__main__":
    print("\n💡 Bienvenue dans AI Code Assistant (Gemini) !")

    prompt = input("\n✏️ Décris le code que tu veux générer : ")
    code = generate_code(prompt)

    print("\n📝 Code généré :\n")
    print(code)

    save = input("\n💾 Voulez-vous enregistrer ce code ? (y/n) : ")
    if save.lower() == "y":
        file_name = input("\n📂 Nom du fichier (sans extension) : ").strip() + ".md"
        with open(file_name, "w") as f:
            f.write(code)
        print(f"✅ Code enregistré dans '{file_name}' !")
