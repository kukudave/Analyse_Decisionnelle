import csv
import itertools

class BruteForceModel:
    def __init__(self, budget_max=500000):
        self.budget_max = budget_max
        self.actions = []

    def load_actions_from_csv(self, file_path):
      """Charge les actions depuis un fichier CSV, quel que soit le format de colonnes."""
      self.actions = []
      with open(file_path, newline='', encoding='cp1252') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        # Détection automatique des colonnes
        fieldnames = [f.strip().lower() for f in reader.fieldnames]

        for i, row in enumerate(reader):
            if i >= 15:  # limite à 15 actions pour les tests
                break

            if 'name' in fieldnames and 'price' in fieldnames and 'profit_pct' in fieldnames:
                name = row['name']
                cost = float(row['price'])
                profit_pct = float(row['profit_pct'])
            
            elif 'actions' in fieldnames and 'cout par action (en euros)' in fieldnames and 'bénéfice après 2 ans' in fieldnames:
                name = row['Actions']
                cost = float(row[' Cout par action (en euros)'])
                profit_pct = float(row[' Bénéfice après 2 ans'].replace('%', '')) / 100
            
            else:
                raise ValueError(f"Format de colonnes non reconnu dans {file_path}: {reader.fieldnames}")

            profit = cost * profit_pct
            self.actions.append({
                'id': name,
                'cost': cost,
                'profit': profit
            })

    def brute_force_selection(self):
        """Solution de force brute : explore toutes les combinaisons"""
        best_profit = 0
        best_combination = []
        n = len(self.actions)

        for i in range(1, n + 1):
            for combo in itertools.combinations(self.actions, i):
                total_cost = sum(a['cost'] for a in combo)
                total_profit = sum(a['profit'] for a in combo)
                if total_cost <= self.budget_max and total_profit > best_profit:
                    best_profit = total_profit
                    best_combination = combo

        total_cost = sum(a['cost'] for a in best_combination)
        return best_combination, total_cost, best_profit

    def dynamic_programming_selection(self, budget=500000):
      """Algorithme optimisé (programmation dynamique) — version corrigée et stable."""
      if not self.actions:
        print("Aucune action chargée.")
        return [], 0, 0

      # Nettoyer les données
      actions = [
        (a['id'], int(a['cost']), float(a['profit']))
        for a in self.actions
        if a['cost'] > 0 and a['profit'] > 0
      ]

      # Filtrer les actions trop coûteuses
      max_cost = max(cost for _, cost, _ in actions)
      if max_cost > budget:
        print(f" Certaines actions dépassent le budget ({max_cost} > {budget}), elles seront ignorées.")
        actions = [a for a in actions if a[1] <= budget]

      n = len(actions)
      dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

      # Remplissage du tableau DP
      for i in range(1, n + 1):
        name, cost, profit = actions[i - 1]
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + profit)
            else:
                dp[i][w] = dp[i - 1][w]

      # Reconstruction du meilleur ensemble d'actions
      selected_actions = []
      w = budget
      for i in range(n, 0, -1):
        name, cost, profit = actions[i - 1]
        if cost <= w and dp[i][w] == dp[i - 1][w - cost] + profit:
            selected_actions.append((name, cost, profit))
            w -= cost

      # Transformer les tuples en dictionnaires pour la vue
      selected_actions_dicts = [
        {'id': name, 'cost': cost, 'profit': profit}
        for name, cost, profit in selected_actions[::-1]
      ]

      total_cost = sum(a['cost'] for a in selected_actions_dicts)
      total_profit = sum(a['profit'] for a in selected_actions_dicts)

      return selected_actions_dicts, total_cost, total_profit
