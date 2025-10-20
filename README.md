#  Projet d'Analyse Décisionnelle
### *Module : Programmation Python*
**Étudiant : Kunimboa David**

---

##  1. Contexte du projet

L’objectif de ce projet est de concevoir un programme permettant de **sélectionner les meilleurs investissements** à partir d’un fichier CSV contenant des actions financières.  
Chaque action est définie par :
- un **nom** (`name`),  
- un **prix** (`price`),  
- et un **taux de profit** (`profit_pct`).  

Le programme doit proposer deux solutions :
1. Une **solution de force brute**, explorant toutes les combinaisons possibles.  
2. Une **solution optimisée**, basée sur la **programmation dynamique (problème du sac à dos 0/1)**.  

L’objectif final est de **maximiser le profit total** tout en respectant une **contrainte de budget maximum (500 000 F CFA)**.

---

##  2. Structure du projet (MVC)

Le projet suit le **modèle MVC (Model–View–Controller)** :

```
Analyse_Décisionnelle/
│
├── controller/
│   └── investment_controller.py
│
├── model/
│   └── investment_model.py
│
├── view/
│   └── investment_view.py
│
├── main.py
|
└── data_test.csv
└── dataset1_Python+P3.csv
└── dataset2_Python+P3.csv
```

- **Model** : Contient la logique métier (calculs, algorithmes, lecture du CSV).  
- **View** : Gère l’affichage des résultats à l’écran.  
- **Controller** : Fait le lien entre la vue et le modèle.

---

##  3. Données d’entrée (CSV)

exemple:

Le fichier `dataset1_Python+P3.csv` contient les colonnes suivantes :

| name       | price  | profit_pct |
|-------------|--------|------------|
| Share-ABCD  | 10000  | 0.12       |
| Share-EFGH  | 25000  | 0.05       |
| ...         | ...    | ...        |

Ces données sont lues et converties en une liste d’actions, chaque action étant représentée par un dictionnaire Python :  
```python
{
  'id': 'Share-ABCD',
  'cost': 10000.0,
  'profit': 1200.0
}
```

---

##  4. Algorithmes implémentés

### 🔹 4.1 Solution par Force Brute

**Principe :**
Explorer **toutes les combinaisons possibles d’actions** et choisir celle dont le profit est maximal sans dépasser le budget.

**Pseudocode :**
```
meilleur_profit ← 0
meilleure_combinaison ← []

pour i de 1 à n:
    pour chaque combinaison de i actions:
        coût_total ← somme des coûts
        profit_total ← somme des profits
        si coût_total ≤ budget et profit_total > meilleur_profit:
            mettre à jour meilleure_combinaison et meilleur_profit
```

**Complexité :**  
→ **O(2ⁿ)** (exponentielle)  
→ Très lente quand le nombre d’actions augmente.

---

### 🔹 4.2 Solution par Programmation Dynamique

**Principe :**
C’est une approche **optimisée du problème du sac à dos 0/1**.  
On remplit une matrice `dp[i][w]` représentant le **profit maximal** possible avec :
- les `i` premières actions,
- pour un budget `w`.

**Pseudocode :**
```
initialiser dp[n+1][budget+1] à 0

pour i de 1 à n:
    coût = actions[i].cost
    profit = actions[i].profit
    pour w de 0 à budget:
        si coût ≤ w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-coût] + profit)
        sinon:
            dp[i][w] = dp[i-1][w]
```

**Complexité :**  
→ **O(n × budget)**  
→ Beaucoup plus rapide que la force brute.

---

##  5. Résultats obtenus

###  Solution par Force Brute
```
Coût total : 500000 F CFA
Profit total : 90400 F CFA
```

###  Solution par Programmation Dynamique
```
Coût total : 265 780 F CFA
Profit total : 5 850 504 F CFA
```

###  Interprétation :
Les deux méthodes trouvent **exactement différentes combinaison d’actions optimales**, ce qui prouve la **correctitude** de la solution optimisée.

---

##  6. Comparaison des performances

| Méthode | Complexité | Avantage principal | Temps d’exécution (approx.) |
|----------|-------------|--------------------|-----------------------------|
| Force Brute | O(2ⁿ) | Exacte, simple à comprendre | Long pour n>20 |
| Prog. Dynamique | O(n × budget) | Très rapide, scalable | Court (quelques secondes) |

---

##  7. Analyse et discussion

- La **force brute** garantit le résultat optimal, mais devient inutilisable dès que le nombre d’actions augmente fortement.  
- La **programmation dynamique** permet de résoudre le même problème en un **temps polynomial**, grâce à une **approche tabulaire**.  
- Les deux approches respectent les contraintes du problème du **sac à dos 0/1**.  
- Le **budget maximal (500 000 F CFA)** est bien respecté dans les deux cas.

---

##  8. Conclusion

Ce projet démontre la différence entre une **approche exhaustive** et une **approche optimisée** pour un même problème décisionnel.

- La **force brute** est utile pour les petits ensembles de données (validation).  
- La **programmation dynamique** est indispensable pour les grands volumes.  

Les résultats obtenus (mêmes profits et coûts totaux) confirment la **validité et l’efficacité** de la solution optimisée.

---

##  Exécution du programme

###  Étapes :
1. Ouvre un terminal dans le dossier `investment_selection/`
2. Lance le programme avec :
   python main.py
