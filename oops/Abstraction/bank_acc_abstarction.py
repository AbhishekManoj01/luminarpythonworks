class Bankaccount:
    def __init__(self,cusomer_name,mpin,acc_type,balance):
        self.customer_name=cusomer_name
        self.mpin=mpin
        self.acc_type=acc_type
        self.__balance=balance

    def __str__(self):
        return self.customer_name
    def get_balance(self):
        print(self.__balance)

bank_accontinstance=Bankaccount("hari",2543,"saving",45000)
print(bank_accontinstance)
print(bank_accontinstance.mpin)
bank_accontinstance.get_balance()