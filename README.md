# EffectiveMobileTestTask
# Личный Финансовый Кошелек

## Описание
Личный Финансовый Кошелек - это консольное приложение для управления личными финансами. Приложение позволяет пользователям управлять доходами и расходами, а также отслеживать общий баланс.

## Функционал
- **Добавление транзакций**: Пользователи могут добавлять информацию о доходах и расходах.
- **Редактирование транзакций**: Позволяет изменять существующие записи.
- **Поиск транзакций**: Поиск транзакций по различным критериям, таким как дата, категория и сумма.
- **Вывод баланса**: Отображение текущего финансового баланса пользователя.

## Технологии
- Python 3.8
- CSV файлы для хранения данных

## Установка и настройка
```bash
git clone https://yourrepository.git
cd your_project_folder

## Для пользователей Windows
python -m venv venv
venv\Scripts\activate

## Для пользователей macOS и Linux
python3 -m venv venv
source venv/bin/activate

## Запуск Приложения
cd src
python main.py
```
## Примеры использования
Выберите действие: 1
Введите 'Д' для дохода или 'Р' для расхода: Д
Введите сумму транзакции: 5000
Введите описание транзакции: Зарплата
