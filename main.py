from controller.investment_controller import InvestmentController

def main():
    controller = InvestmentController()

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Force Brute (uniquement data_test.csv)")
        print("2. Programmation Dynamique (plusieurs fichiers possibles)")
        print("3. Quitter")

        choice = input("Entrez votre choix (1, 2 ou 3) : ").strip()

        if choice == '1':
            print("\n=== MODE : FORCE BRUTE ===")
            controller.run_force_brute()
        elif choice == '2':
            print("\n=== MODE : PROGRAMMATION DYNAMIQUE ===")
            controller.run_dp()
        elif choice == '3':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Réessayez.")

if __name__ == "__main__":
    main()
