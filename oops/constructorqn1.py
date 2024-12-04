class Bank:
    acc_no:int
    balance:int
    ac_type=str
    customer_name=str

    def __init__(self,acc_no,balance,ac_type,customer_name):
        self.acc_no=acc_no
        self.balance=balance
        self.ac_type=ac_type
        self.customer_name=customer_name
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"your account {self.acc_no} has been credited with amount {amount} avl balance {self.balance}")

    def withdraw(self,amount):
        if self.balance<amount:
            print("insufficient bank balance")
        else:
            self.balance=self.balance-amount
            print(f" your account {self.acc_no} has been debited with amount {amount} avl balance {self.balance}")

    def get_balance(self):
        print("ur available balance",self.balance)
bank_instance1=Bank(123344455,3000,"savings","abhi")
bank_instance1.withdraw(5000)
bank_instance1.deposit(1000)
bank_instance1.get_balance()