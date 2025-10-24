import csv

class DPModel:
    def __init__(self, budget_max=500000):
        self.budget_max = budget_max
        self.actions = []

    def load_actions_from_csv(self, file_path):
        """Charge les actions depuis un CSV, compatible colonnes anglaises ou françaises."""
        self.actions = []
        with open(file_path, newline='', encoding='cp1252') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            fieldnames = [f.strip().lower() for f in reader.fieldnames]

            for row in reader:
                # Colonnes anglaises
                if 'name' in fieldnames and 'price' in fieldnames and 'profit_pct' in fieldnames:
                    name = row['name']
                    cost = float(row['price'])
                    profit_pct = float(row['profit_pct'])
                # Colonnes françaises
                elif 'actions' in fieldnames and 'cout par action (en euros)' in fieldnames and 'bénéfice après 2 ans' in fieldnames:
                    name = row['Actions']
                    cost = float(row[' Cout par action (en euros)'])
                    profit_pct = float(row[' Bénéfice après 2 ans'].replace('%', '')) / 100
                else:
                    raise ValueError(f"Format de colonnes non reconnu : {reader.fieldnames}")

                profit = cost * (profit_pct / 100)
                self.actions.append({'id': name, 'cost': cost, 'profit': profit})

    def dynamic_programming_selection(self):
        """Algorithme optimisé (programmation dynamique)"""
        if not self.actions:
            return [], 0, 0

        # Nettoyer les données
        actions = [
          (a['id'], int(a['cost']), float(a['profit']))
          for a in self.actions
          if a['cost'] > 0 and a['profit'] > 0
        ]

        budget = self.budget_max
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

        # Reconstruction de la solution
        selected = []
        w = budget
        for i in range(n, 0, -1):
            name, cost, profit = actions[i - 1]
            if cost <= w and dp[i][w] == dp[i - 1][w - cost] + profit:
                selected.append((name, cost, profit))
                w -= cost

        # Transformer les tuples en dictionnaires pour la vue
        selected_dicts = [{'id': n, 'cost': c, 'profit': p} for n, c, p in selected[::-1]]
        total_cost = sum(a['cost'] for a in selected_dicts)
        total_profit = sum(a['profit'] for a in selected_dicts)

        return selected_dicts, total_cost, total_profit
