import csv
import datetime
import sys


# Добавление записи
def write_transaction(file_path):
    """Добавляет новую транзакцию в файл CSV.
    
    Args:
        file_path (str): Путь к файлу транзакций.
    """
    
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
    """Поиск транзакций по заданным параметрам.
    Args:
        file_path (str): Путь к файлу транзакций.
    
    Returns:
        List[Dict[str, Any]]: Список найденных транзакций.
    """

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
    print(f"\nОбщий Баланс: {balance:.2f} руб.")
    print(f"Всего доходов: {total_income:.2f} руб.")
    print(f"Всего расходов: {total_expense:.2f} руб.")
    return balance # Возвращаем баоанс

# Редактировать запись
def edit_transaction(file_path):
    """Редактирует существующую транзакцию в файле CSV.
    
    Args:
        file_path (str): Путь к файлу транзакций.
        transaction_id (int): ID транзакции для редактирования.
    """

    # Чтение всех транзакций
    try:
        transactions = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            transactions = list(reader)
    except FileNotFoundError:
        print("Файл данных не найден. Пожалуйста, убедиитесь, что транзакции были записаны.")
        return
    
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
    """Возвращает выбор Категории "Доход" или "Расход"
    
   
    """

    while True:
        category_input = input("Введите 'Д' для дохода или 'Р' для расхода: ").strip().upper()
        if category_input in ['Д', 'Р']:
            return 'Доход' if category_input == 'Д' else 'Расход'
        print("Неверный ввод. Пожалуйста, введите 'Д' или 'Р'.")


def search_transactions(file_path):
    """Поиск транзакций по заданным параметрам.
    
    Args:
        file_path (str): Путь к файлу транзакций.
        search_params (Dict[str, Any]): Параметры для поиска транзакций.
    
    Returns:
        List[Dict[str, Any]]: Список найденных транзакций.
    """

    # Чтение всех транзакций
    transactions = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            transactions = list(reader)
    except FileNotFoundError:
        print("Файл данных не найден. Пожалуйста, убедиитесь, что транзакции были записаны.")
        return
    # Вывод доступных полей для поиска
    print("Доступные поля для поиска: I - ID, Д - Дата, К - Категория, С - Сумма")
    
    # Получение поля для поиска от пользователя
    field_input = input("Введите букву поля для поиска: ").strip().lower()
    field_map = {'i': 'ID', 'д': 'Дата', 'к': 'Категория', 'с': 'Сумма', 'о': 'Описание'}
    
    if field_input not in field_map:
        print("Неверный ввод. Пожалуйста, используйте одну из предложенных букв.")
        return
    
    # Присваиваем правильное имя поля
    field = field_map[field_input]

    #Проверка если юзер выбрал поиск по категории
    if field_input == "к":
        search_value = get_category_choice()
    elif field_input=="д":
        search_value = input("Для поиска по дате используйте формат yyyy-mm-dd)\n")
    else:
        # Ввод значения для поиска
        search_value = input("Введите значение для поиска: \n (Для поиска по дате используйте формат yyyy-mm-dd)\n")

    # Поиск и вывод результатов
    found_transactions = [transaction for transaction in transactions if transaction[field].lower().startswith(search_value.lower())]
    if found_transactions:
        print("Найденные транзакции:")
        for transaction in found_transactions:
            print(transaction)
    else:
        print("Транзакции не найдены.")

# Пример вызова функции
#search_transactions('transactions.csv')
# edit_transaction("transactions.csv")
# write_transaction('transactions.csv')
# calculate_balance('transactions.csv')
