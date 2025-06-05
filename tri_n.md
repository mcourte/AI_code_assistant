Pour trouver des éléments dans une liste qui commencent par une certaine lettre, comme 'n', tu peux utiliser une boucle `for` et une condition pour vérifier si chaque élément commence par cette lettre. Voici un exemple de code Python pour accomplir cela :

```python
def trouver_items_commençant_par_lettre(liste, lettre):
    resultats = []
    for item in liste:
        if isinstance(item, str) and item.startswith(lettre):
            resultats.append(item)
    return resultats

# Exemple d'utilisation
ma_liste = ["noix", "pomme", "nuage", "banane", "nuit"]
lettre_recherchée = "n"
items_trouvés = trouver_items_commençant_par_lettre(ma_liste, lettre_recherchée)
print(items_trouvés)
```

Dans cet exemple, la fonction `trouver_items_commençant_par_lettre` prend une liste et une lettre en entrée, et retourne une nouvelle liste contenant tous les éléments de la liste d'origine qui commencent par cette lettre. La fonction vérifie également que chaque élément est une chaîne de caractères (`str`) avant de vérifier s'il commence par la lettre spécifiée.

Si tu veux une solution plus concise, tu peux utiliser une compréhension de liste :

```python
def trouver_items_commençant_par_lettre(liste, lettre):
    return [item for item in liste if isinstance(item, str) and item.startswith(lettre)]

# Exemple d'utilisation
ma_liste = ["noix", "pomme", "nuage", "banane", "nuit"]
lettre_recherchée = "n"
items_trouvés = trouver_items_commençant_par_lettre(ma_liste, lettre_recherchée)
print(items_trouvés)
```

Cette version utilise une compréhension de liste pour générer la liste des éléments qui commencent par la lettre spécifiée.