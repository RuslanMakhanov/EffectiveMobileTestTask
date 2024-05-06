import data_manager
import csv

def read_transactions(file_path):
    transactions = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions

read_transactions('transactions.csv')