from bank_account import bank_accounts
import time
#the next 2 line was for make the deposit is input by the clint but we will walk with course code to be the same 
# amount=input("enter you deposit:  ")
# amount=int(amount)
balance=500
tran=[]
user1= bank_accounts(balance)

# make deposit method on print statement and its work
# f in print statement look like that to be with method or function 
# print(f"this your current balance:   {user1.balance}")

print(f"this your current balance:   {user1.balance}")
print(f"this your balance after deposit {user1.deposit(0)}")
print(f"this your balance after mins amount: {user1.mins_deposit(5000)}") 
print(f"this the return of the balance :{user1.show_balance()}")

print(user1.transaction)