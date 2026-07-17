class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ''):
        transaction = {
            'amount': amount,
            'description': description
        }
        self.ledger.append(transaction)
    
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            transaction = {
                'amount': -amount,
                'description': description
            }
            self.ledger.append(transaction)
            return True
        return False

    def get_balance(self):
        total = 0
        for i in self.ledger:
            total += i['amount']
        return total
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        total_to_print = ''

        total_char = 30 - len(self.name)
        left_char = total_char // 2
        for i in range(total_char):
            title_line = ('*' * left_char) + self.name + ('*' * left_char)
        total_to_print += title_line + '\n'

        total_transactions = ''
        parcial_transactions = ''
        for i in self.ledger:
            parcial_transactions = i['description'][:23].ljust(23)
            parcial_transactions += f"{i['amount']:.2f}".rjust(7) + '\n'
            total_transactions += parcial_transactions
        total_to_print += total_transactions

        total = 0
        for i in self.ledger:
            total += i['amount']
        total_to_print += f'Total: {total}' 

        return total_to_print


def create_spend_chart(categories):
    printable = 'Percentage spent by category\n'

    total_spent = []
    for cat in categories:
        spent = sum(t['amount'] for t in cat.ledger if t['amount'] < 0)
        total_spent.append(abs(spent))
    
    total_global = sum(total_spent)
    
    category_percentage = []
    for spent in total_spent:
        category_percentage.append((spent / total_global * 100) // 10 * 10)

    for i in range(100, -1, -10):
        printable += str(i).rjust(3) + '|'
        for cat in category_percentage:
            if cat >= i:
                printable += ' o '
            else:
                printable += '   '
        printable += ' \n'

    printable += '    '
    for i in categories:
        printable += '---'
    printable += '-\n'

    max_len = 0
    for cat in categories:
        max_len = len(cat.name) if len(cat.name) > max_len else max_len

    for i in range(0, max_len):
        printable += '    '
        for cat in categories:
            if len(cat.name) > i:
                printable += f' {cat.name[i]} '
            else:
                printable += '   '
        printable += ' \n'

    return printable.rstrip('\n')
    

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
#print(food)

categories = [clothing, food]

print(clothing.ledger)

print(create_spend_chart(categories))