# Projet d'Analyse Décisionnelle
### *Module : Programmation Python*
**Étudiant : Kunimboa David**

## =========================== RAPPORT D'ESSAI================================##
---

## 1. Contexte du projet

L’objectif de ce projet est de concevoir un programme permettant de **sélectionner les meilleurs investissements** à partir d’un fichier CSV contenant des actions financières.  
Chaque action est définie par :
- un **nom** (`name`),  
- un **prix** (`price`),  
- et un **taux de profit** (`profit_pct`).  

Le programme propose deux solutions :
1. Une **solution de force brute**, explorant toutes les combinaisons possibles.  
2. Une **solution optimisée**, basée sur la **programmation dynamique (problème du sac à dos 0/1)**.  

L’objectif final est de **maximiser le profit total** tout en respectant une **contrainte de budget maximum (500 000 F CFA)**.

---

## 2. Structure du projet (MVC)

Analyse_Décisionnelle/
│
├── controller/
│ └── investment_controller.py
│
├── model/
│ ├── brute_force_model.py
│ └── dp_model.py
│
├── view/
│ └── investment_view.py
│
├── main.py
│
└── data_test.csv
└── dataset1_Python+P3.csv
└── dataset2_Python+P3.csv


- **Model** : logique métier (algorithmes, lecture CSV)  
- **View** : affichage des résultats  
- **Controller** : coordination entre Model et View

---

## 3. Données d’entrée (CSV)

Exemple (`dataset1_Python+P3.csv`) :

| name       | price  | profit_pct |
|------------|--------|------------|
| Share-DUPH | 10010  | 12.25      |
| Share-GTAN | 26040  | 38.06      |
| ...        | ...    | ...        |

4. Algorithmes implémentés
🔹 4.1 Force Brute

Principe : explorer toutes les combinaisons possibles pour trouver le profit maximal.

Complexité : O(2ⁿ) → lente pour n>20

🔹 4.2 Programmation Dynamique (DP)

Principe : approche optimisée du sac à dos 0/1.

Complexité : O(n × budget) → rapide même pour plusieurs dizaines d’actions

5. Jeux de tests et résultats
5.1 Fichier data_test.csv (15 actions)

| Méthode                 | Coût total (F CFA) | Profit total (F CFA) | Temps d’exécution |
| ----------------------- | ------------------ | -------------------- | ----------------- |
| Force Brute             | 420 000            | 34 900               | 0.02 s            |
| Programmation Dynamique | 420 000            | 34 900               | 0.03 s            |

5.2 Fichier dataset1_Python+P3.csv (~30 actions)

| Méthode                 | Coût total (F CFA) | Profit total (F CFA) | Temps d’exécution |
| ----------------------- | ------------------ | -------------------- | ----------------- |
| Programmation Dynamique | 499 960            | 1 985 465.2          | 1.5 s             |

5.3 Fichier dataset2_Python+P3.csv (~20 actions, valeurs négatives exclues)

| Méthode                 | Coût total (F CFA) | Profit total (F CFA) | Temps d’exécution |
| ----------------------- | ------------------ | -------------------- | ----------------- |
| Programmation Dynamique | 499 920            | 1 979 646.6          | 0.8 s             |


6. Comparaison des performances

| Méthode                 | Complexité    | Avantage principal | Limites                           |
| ----------------------- | ------------- | ------------------ | --------------------------------- |
| Force Brute             | O(2ⁿ)         | Exacte, simple     | Devient inutilisable dès n>20     |
| Programmation Dynamique | O(n × budget) | Rapide, scalable   | Approximation si échelle utilisée |

7. Analyse et discussion

Force brute : garantit le résultat exact mais très lente pour de grands fichiers.

Programmation dynamique : résultats quasi identiques, exécution rapide, scalable.

Les deux méthodes respectent le budget maximal (500 000 F CFA).

Pour des volumes élevés, DP est indispensable.

8. Conclusion

Ce projet montre la différence entre une approche exhaustive et une approche optimisée pour le même problème décisionnel.

Force brute : validation pour petits ensembles de données

Programmation dynamique : solution rapide et efficace pour grands ensembles

9. Exécution du programme

Ouvrir un terminal dans le dossier Analyse_Décisionnelle/

Lancer le programme :

python main.py
