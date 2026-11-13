import os

BASE = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE, "data", "spending.csv")


# Read file data
def load_spending(): 
    spending = {}
    with open(path) as f:
        f.readline()
        for line in f:
            date, category, amount = line.strip().split(",") #Note that the amount section must be written as ".".
            if category not in spending: #If it does not exist, create the table first.
                spending[category] = []
            spending[category].append((date, float(amount)))
    return spending

#Calculate the amount for each month
def category_total(spending, category, month):
    return sum(amount for date, amount in spending[category] if date.startswith(month))

#Find the category with the highest spending each month.
def top_category(spending, month):
    totals = {}
    for category in spending: #Fill in the table
        totals[category] = month
    return max(totals, key = totals.get) #The key with the largest value

#Total amount spent in a month
def month_total(spending, month):
    totals = {}
    for category in spending:
        totals[category] = category_total(spending, category, month)
    return sum(totals.values())

