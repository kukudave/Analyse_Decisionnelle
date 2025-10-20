import os
from model.investment_model import InvestmentModel
from view.investment_view import InvestmentView

class InvestmentController:
    def __init__(self, file_paths):
        """
        file_paths : liste des fichiers CSV à traiter
        """
        self.file_paths = file_paths
        self.model = InvestmentModel()
        self.view = InvestmentView()

    def run(self):
        for file_path in self.file_paths:
            # Vérification que le fichier existe
            if not os.path.isfile(file_path):
                self.view.display_message(f"Erreur : le fichier '{file_path}' est introuvable.")
                continue

            self.view.display_message(f"\n=== Traitement du fichier {file_path} ===")
            self.model.load_actions_from_csv(file_path)

            # Algorithme Force Brute uniquement pour data_test.csv
            if 'data_test.csv' in file_path:
                brute_actions, brute_cost, brute_profit = self.model.brute_force_selection()
                self.view.display_message("===== SOLUTION PAR FORCE BRUTE =====")
                self.view.display_results(brute_actions, brute_cost, brute_profit)

            # Algorithme Programmation Dynamique pour tous les fichiers
            dp_actions, dp_cost, dp_profit = self.model.dynamic_programming_selection()
            self.view.display_message("===== SOLUTION PAR PROGRAMMATION DYNAMIQUE =====")
            self.view.display_results(dp_actions, dp_cost, dp_profit)
