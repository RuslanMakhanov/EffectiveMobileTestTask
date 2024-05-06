import csv
import datetime
import sys

def read_transactions(file_path):
    transactions = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions

# Добавление записи
def write_transaction(file_path):
    # Получение текущей даты
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')  # Форматирование даты в строку

   # Использование функции get_category_choice для запроса категории транзакции
    category = get_category_choice()

    # Запрос суммы транзакции
    while True:
        try:
            amount = float(input("Введите сумму транзакции: "))
            break
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число.")

    # Запрос описания транзакции
    description = input("Введите описание транзакции: ")

    # Определение следующего ID
    next_id = 1
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next_id = sum(1 for row in reader)  # Считаем количество строк для определения следующего ID
    except FileNotFoundError:
        print("Файл не найден, будет создан новый файл.")

    # Составление словаря для записи
    transaction = {
        'ID': next_id,
        'Дата': date_str,
        'Категория': category,
        'Сумма': amount,
        'Описание': description
    }

    # Запись данных в файл
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['ID', 'Дата', 'Категория', 'Сумма', 'Описание'])
        if file.tell() == 0:  # Проверяем, пустой ли файл, если да, то пишем заголовки
            writer.writeheader()
        writer.writerow(transaction)


    print("Транзакция успешно сохранена.")

# Вывод Баланса
def calculate_balance(file_path):
    total_income = 0.0
    total_expense = 0.0

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for transaction in reader:
                if transaction['Категория'] == 'Доход':
                    total_income+=float(transaction['Сумма'])
                elif transaction['Категория'] == 'Расход':
                    total_expense += float(transaction['Сумма'])
    except FileNotFoundError:
        print("Файл данных не найден. Пожалуйста, убедиитесь, что транзакции были записаны.")
        return
    
    # Вычисление итогового баланса
    balance = total_income - total_expense

    #Вывод баланса и детализации по доходам и расходам
    print(f"Общий Баланс: {balance:.2f} руб.")
    print(f"Всего доходов: {total_income:.2f} руб.")
    print(f"Всего расходов: {total_expense:.2f} руб.")
    return balance # Возвращаем баоанс

# Редактировать запись
def edit_transaction(file_path):
    # Чтение всех транзакций
    transactions = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        transactions = list(reader)
    
    # Вывод всех транзакций с их ID
    for transaction in transactions:
        print(f"ID: {transaction['ID']}, Дата: {transaction['Дата']}, Категория: {transaction['Категория']}, Сумма: {transaction['Сумма']}, Описание: {transaction['Описание']}")

    # Выбор транзакции для редактирования
    edit_id = input("Введите ID транзакции, которую хотите отредактировать: ")
    transaction_to_edit = next((t for t in transactions if t['ID'] == edit_id), None)

    if not transaction_to_edit:
        print("Транзакция с таким ID не найдена.")
        return

    # Ввод новых значений
    
    transaction_to_edit['Категория'] = get_category_choice()
    transaction_to_edit['Сумма'] = input(f"Введите новую сумму (текущая: {transaction_to_edit['Сумма']}): ") or transaction_to_edit['Сумма']
    transaction_to_edit['Описание'] = input(f"Введите новое описание (текущее: {transaction_to_edit['Описание']}): ") or transaction_to_edit['Описание']

    # Запись обратно в файл
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['ID', 'Дата', 'Категория', 'Сумма', 'Описание'])
        writer.writeheader()
        writer.writerows(transactions)

    print("Транзакция успешно обновлена.")

def get_category_choice():
    while True:
        category_input = input("Введите 'Д' для дохода или 'Р' для расхода: ").strip().upper()
        if category_input in ['Д', 'Р']:
            return 'Доход' if category_input == 'Д' else 'Расход'
        print("Неверный ввод. Пожалуйста, введите 'Д' или 'Р'.")

edit_transaction("transactions.csv")
write_transaction('transactions.csv')
calculate_balance('transactions.csv')