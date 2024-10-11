#Functions to generate reports for admin
# utils/reporting.py
import json

def generate_transaction_report():
    with open('data/transactions.json', 'r') as f:
        transactions = f.readlines()

    report = {}
    for transaction in transactions:
        data = json.loads(transaction)
        if data['movie'] not in report:
            report[data['movie']] = {'rent': 0, 'purchase': 0}
        report[data['movie']][data['transaction_type']] += 1
    
    return report
