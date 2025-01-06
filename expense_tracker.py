import csv
from datetime import datetime

def log_expense(amount, category, description):
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), amount, category, description])

def generate_report():
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        total = 0
        print("Date & Time, Amount, Category, Description")
        for row in reader:
            print(", ".join(row))  # Display each row
            try:
                total += float(row[1])
            except ValueError:
                continue  # Skip rows with invalid amount values
        print(f'\nTotal Expenses: ${total:.2f}')

# Example usage
log_expense(50, 'Groceries', 'Bought fruits and vegetables')
log_expense(20, 'Transport', 'Bus fare')
generate_report()
