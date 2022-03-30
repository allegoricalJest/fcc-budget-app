class Category:
  def __init__(self, label):
    self.label = label
    self.ledger = []

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
    
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False
    
  def get_balance(self):
    total = 0
    for item in self.ledger:
      total += item["amount"]
    return total

  def transfer(self, amount, obj):
    if self.withdraw(amount, "Transfer to " + obj.label):
      obj.deposit(amount, "Transfer from " + self.label)
      return True
    else:
      return False
    
  def check_funds(self, amount):
    return amount <= self.get_balance();
    
  def __str__(self):
    output = self.label.center(30, "*") + "\n"

    total = 0
    for item in self.ledger:
      total += item['amount']

      output += item['description'].ljust(23," ")[:23]
      output += "{0:>7.2f}".format(item['amount'])
      output += "\n"

    output += "Total: " + "{0:.2f}".format(total)
    return output

def create_spend_chart(categories):
  output = "Percentage spent by category\n"

  total = 0
  expenses = []
  labels = []
  label_len = 0

  for item in categories:
    expense = sum(-x['amount'] for x in item.ledger if x['amount'] < 0)
    total += expense

    if len(item.label) > label_len:
      label_len = len(item.label)

    expenses.append(expense)
    labels.append(item.label)

  expenses = [(x/total) * 100 for x in expenses]
  labels = [label.ljust(label_len, " ") for label in labels]

  for i in  range(100, -1, -10):
    output += str(i).rjust(3," ") + '|'
    for x in expenses:
      output += " o " if x >= i else "   "
    output += " \n"

  output += "    " + "---" * len(labels) + "-\n"

  for i in range(label_len):
    output += "    "
    for label in labels:
      output += " " + label[i]+ " "
    output += " \n"

  return output.strip("\n")