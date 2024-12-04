#account_number=9876776544
account_number=int(input("Enter the account number:"))
#bank_name="Federal Bank"
bank_name=input("Enter the bank name:")
total_balance=int(input("Enter the total balance:"))
amount=int(input("Enter the amount to be credited:"))
#amount=5000
balance=total_balance+amount
print(f"hi user your {bank_name} bank account {account_number}A/C has been credited with {amount} your available balance is {balance}")