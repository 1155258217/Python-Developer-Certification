import math

class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name
    
    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else: 
            return False

    def get_balance(self):
        return sum(self.ledger[i]['amount'] for i in range(len(self.ledger)))

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        
        items = ""
        for item in self.ledger:
            desc = item['description'][0:23]

            desc = desc.ljust(23)
            

            amount = "{:.2f}".format(item['amount'])

            amount = amount.rjust(7)
            
            items += desc + amount + "\n"
        
        total = "Total: {:.2f}".format(self.get_balance())
        
        return title + items + total

def create_spend_chart(categories):
    result = "Percentage spent by category\n"

    category_spending = {}
    total_spending = 0
    for cat in categories:
        name = cat.name
        spending = sum(-cat.ledger[i]['amount'] for i in range (len(cat.ledger)) if cat.ledger[i]['amount'] < 0)
        
        total_spending += spending

        category_spending[name] = spending

    for cat in categories:
        if total_spending > 0:
            percentage = category_spending[cat.name] / total_spending * 100
            percentage = int(percentage // 10 * 10)
            category_spending[cat.name] = percentage
        else:
            category_spending[cat.name] = 0

    for percent in range(100,-1,-10):
        result += str(percent).rjust(3) + "| "
        for cat in categories:
            if category_spending[cat.name] >= percent:
                result += 'o  '
            else:
                result += '   '
        result += '\n'
    
    result += "    "+"-"*(len(categories)*3+1) + "\n"

    
    length = max(len(cat.name) for cat in categories)
    counter = 0
    result += '     '
    for i in range(length):
        for cat in categories:
            if len(cat.name) > counter:
                result += cat.name[counter] + '  '
            else:
                result += '   '

        if i != length -1:
            result += '\n     '

        counter += 1

    return result
