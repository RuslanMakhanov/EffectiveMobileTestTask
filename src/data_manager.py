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

def write_transaction(file_path):
    # Получение текущей даты
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')  # Форматирование даты в строку

    # Запрос типа транзакции
    while True:
        transaction_type = input("Введите 'Д' для дохода или 'Р' для расхода: ").strip().upper()
        if transaction_type in ['Д', 'Р']:
            break
        print("Неверный ввод. Пожалуйста, введите 'Д' или 'Р'.")

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
        'Категория': 'Доход' if transaction_type == 'Д' else 'Расход',
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


calculate_balance("transactions.csv")
write_transaction("transactions.csv")
calculate_balance("transactions.csv")