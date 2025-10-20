class InvestmentView:
    def display_message(self, message):
        print(message)

    def display_results(self, actions, total_cost, total_profit):
        print("\nActions sélectionnées :")
        for action in actions:
            print(f" - {action['id']} | Coût : {round(action['cost'], 2)} | Profit : {round(action['profit'], 2)}")
        print(f"\nCoût total : {round(total_cost, 2)} F CFA")
        print(f"Profit total : {round(total_profit, 2)} F CFA")
