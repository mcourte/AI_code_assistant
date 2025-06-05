import requests


def generate_code_openrouter(prompt, api_key):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    json_data = {
        "model": "mistralai/devstral-small:free",
        "messages": [
            {"role": "system", "content": "Tu es un assistant expert en génération de code Python."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 512
    }
    response = requests.post(url, headers=headers, json=json_data)
    if response.status_code == 200:
        data = response.json()
        # On récupère le texte dans choices
        return data["choices"][0]["message"]["content"].strip()
    else:
        return f"❌ Erreur API {response.status_code}: {response.text}"


if __name__ == "__main__":
    print("ℹ️ Vous pouvez obtenir une clé API gratuite sur https://openrouter.ai")
    api_key = input("🔑 Entrez votre clé API OpenRouter : ").strip()

    print("\n💡 Bienvenue dans AI Code Assistant (OpenRouter - mistralai/devstral-small:free) !")
    prompt = input("\n✏️ Décris le code que tu veux générer : ")

    code = generate_code_openrouter(prompt, api_key)
    print("\n📝 Code généré :\n")
    print(code)

    save = input("\n💾 Voulez-vous enregistrer ce code ? (y/n) : ")
    if save.lower() == "y":
        file_name = input("\n📂 Nom du fichier (sans extension) : ").strip() + ".md"
        with open(file_name, "w") as f:
            f.write(code)
        print(f"✅ Code enregistré dans '{file_name}' !")
