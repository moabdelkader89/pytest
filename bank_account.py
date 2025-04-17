class bank_accounts:
    def  __init__(self,balance):
        self.balance=balance
        self.transaction=[]
        
               # بتجمع الرصيد الموجود من السحب

    def deposit(self,amount):
        if amount > 0:
            self.balance=self.balance + amount
            self.transaction.append(amount)
            print(f"this is your last deposit:  {amount}")
            return self.balance
            
        else:
           print(f"no balance added, this is your exist balance:  {self.balance}")
           return self.balance
        
     # بتطرح الرصيد الموجود من السحب
     
    def mins_deposit(self,amount):
        if 0<= amount<=self.balance:
            self.balance=self.balance - amount
            self.transaction.append(amount)
            print(f"this is your last mins_deposit: {amount}")            
            return self.balance
        else:
            print(f"no enough amount in your account, this your exist balance: {self.balance}")
            return self.balance   
    
    
        
    def show_balance(self):
        account=bank_accounts(self.balance)
        return account.balance  
    
    
        
        