from controller.investment_controller import InvestmentController

def main():
    # Demande à l'utilisateur plusieurs fichiers séparés par des espaces
    file_input = input(
        "Entrez les fichiers CSV à traiter (ex: dataset1_Python+P3.csv dataset2_Python+P3.csv data_test.csv) : "
    )
    file_paths = file_input.split()  # transforme la saisie en liste
    controller = InvestmentController(file_paths)
    controller.run()

if __name__ == "__main__":
    main()
