# 🚀 AI Code Assistant

Un outil basé sur l’IA pour générer du code automatiquement en fonction de vos besoins !

🔑 Obtenir une clé API gratuite
Vous pouvez obtenir une clé API gratuite sur https://openrouter.ai.
Entrez votre clé API lors du lancement du script.


## 📦 Installation

1️⃣ Clonez le repo :

```
git clone https://github.com/mcourte/AI_Code_Assistant.git
cd AI_Code_Assistant
```

2️⃣ Installez les dépendances (OpenAI SDK) :

```
pip install -r requirements.txt
```

3️⃣ Lancer le script

```
python ai_code_generator.py
```

Amusez-vous bien ! 


## 🔑 Clé API OpenAI
Avant d'utiliser le script, vous devez obtenir une clé API OpenAI :  

Allez sur https://platform.openai.com/account/api-keys  

Connectez-vous ou créez un compte  

Générez une nouvelle clé API  

Copiez-la et collez-la dans le terminal quand demandé par le script  

## 💡 Utilisation
Au démarrage, le script vous demandera votre clé API OpenRouter.  
Ensuite, décrivez ce que vous voulez générer comme code en langage naturel.  
Le code généré s’affichera dans le terminal.  

Vous aurez la possibilité d’enregistrer ce code dans un fichier .md.  

## ℹ️ Modèle utilisé  
Ce script utilise le modèle mistralai/devstral-small:free via l’API OpenRouter.  

## ⚠️ Notes importantes
Assurez-vous que votre clé API est valide et a suffisamment de quota.  

En cas d’erreur liée au modèle, vérifiez que le nom du modèle est correct sur https://openrouter.ai/models.  
 
Le script utilise l’interface OpenAI Python SDK compatible avec OpenRouter.  


### 💡 Exemples
Vous trouverez deux exemples dans ce repository : sorted_n & tri_n