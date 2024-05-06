import data_manager

def main_menu():
    while True:
        print("\n<------Личный Финансовый Кошелек------>\n")
        print("1. Добавить новую транзакцию")
        print("2. Редактировать транзакцию")
        print("3. Поиск транзакций")
        print("4. Вывести баланс")
        print("5. Выход\n")

        choice = input("Выберите действие: ")

        if choice == '1':
            data_manager.write_transaction('transactions.csv')
        elif choice == '2':
            data_manager.edit_transaction('transactions.csv')
        elif choice == '3':
            data_manager.search_transactions('transactions.csv')
        elif choice == '4':
            data_manager.calculate_balance('transactions.csv')
        elif choice == '5':
            print("\nСпасибо за использование приложения!")
            break
        else:
            print("Неверный ввод, попробуйте еще раз.")

if __name__ == '__main__':
    main_menu()