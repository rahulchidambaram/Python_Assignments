def  atm_withdrawal(withdrawal_amount):
    current_balance = 5000
    if withdrawal_amount <= 0:
        print("Error: Withdrawal amount must be greater than 0")
        return False
    elif withdrawal_amount >= current_balance:
        print(f"Error: Insufficient balance. Available: {current_balance}")
        return False
    elif withdrawal_amount % 500 != 0:
        print("Error: Withdrawal amount must be multiple of 500")
        return False
    else:
        rem_balance = current_balance - withdrawal_amount
        print(f"""Withdrawal successful. Amount: {withdrawal_amount} /-
 Remaining Balance: {rem_balance} /-""")
        return True


withdraw = int(input("Please enter an amount to withdraw:  "))
result = atm_withdrawal(withdraw) 
print(f"Return: {result}")