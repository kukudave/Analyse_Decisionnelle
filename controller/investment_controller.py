import os
import time
from model.brute_force_model import BruteForceModel
from model.dp_model import DPModel
from view.investment_view import InvestmentView

class InvestmentController:
    def __init__(self):
        self.view = InvestmentView()

    def run_force_brute(self):
        """Exécuter la force brute uniquement sur data_test.csv"""
        file_path = input("Entrez le chemin du fichier CSV (ex: data_test.csv) : ").strip()

        if not os.path.isfile(file_path):
            self.view.display_message(f"❌ Erreur : le fichier '{file_path}' est introuvable.")
            return

        self.view.display_message(f"\n=== TRAITEMENT DU FICHIER {file_path} (Force Brute) ===")
        model = BruteForceModel()
        model.load_actions_from_csv(file_path)

        start_time = time.time()
        actions, total_cost, total_profit = model.brute_force_selection()
        end_time = time.time()

        self.view.display_message("===== SOLUTION PAR FORCE BRUTE =====")
        self.view.display_results(actions, total_cost, total_profit)
        self.view.display_message(f"\n⏱ Temps d'exécution (Force Brute) : {end_time - start_time:.4f} secondes\n")

    def run_dp(self):
        """Exécuter la programmation dynamique sur plusieurs fichiers"""
        file_input = input(
            "Entrez les fichiers CSV à traiter (ex: data_test.csv dataset1_Python+P3.csv dataset2_Python+P3.csv) : "
        ).strip()
        file_paths = file_input.split()

        for file_path in file_paths:
            if not os.path.isfile(file_path):
                self.view.display_message(f"❌ Erreur : le fichier '{file_path}' est introuvable.")
                continue

            self.view.display_message(f"\n=== TRAITEMENT DU FICHIER {file_path} (Programmation Dynamique) ===")
            model = DPModel()
            model.load_actions_from_csv(file_path)

            start_time = time.time()
            actions, total_cost, total_profit = model.dynamic_programming_selection()
            end_time = time.time()

            self.view.display_message("===== SOLUTION PAR PROGRAMMATION DYNAMIQUE =====")
            self.view.display_results(actions, total_cost, total_profit)
            self.view.display_message(f"\n⏱ Temps d'exécution (DP) : {end_time - start_time:.4f} secondes\n")
