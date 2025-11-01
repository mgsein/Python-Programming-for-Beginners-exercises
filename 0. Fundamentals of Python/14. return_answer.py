def withdraw_money(current_balance, amount):
    if(current_balance >= amount):
        current_balance = current_balance - amount
    print("The balance is", current_balance)
    
    return current_balance

balance = withdraw_money(100, 80)

if(balance <= 50):
    print("Need deposit")
else:
    print("No need to deposit")
