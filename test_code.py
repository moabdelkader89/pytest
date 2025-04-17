from bank_account import bank_accounts 
import pytest


def test_balance():
    balance=100
    account=bank_accounts(balance)
    assert account.balance==100
    
    
def test_deposit():
    balance=100
    account=bank_accounts(balance)
    account.deposit(50)
    assert account.balance==150
    
    
def test_mins():
    balance=100
    account=bank_accounts(balance)
    account.mins_deposit(100)
    assert account.balance==0   

def test_show_balance():
    balance=100
    account=bank_accounts(balance)
    result=account.show_balance()
    assert result==100    
    
    
def test_deposit_trans():
    balance=100
    account=bank_accounts(balance)
    account.transaction.append(account.deposit(100))
    assert [100,200] ==  account.transaction
    

    
def test_mins_deposit_trans():
    balance=100
    account=bank_accounts(balance)
    account.transaction.append(account.mins_deposit(100))
    assert [100,0] ==  account.transaction   
    
    
    
def test_invalid_deposit():
    balance=100
    account=bank_accounts(balance)
    account.deposit(-50)
    assert account.balance==100    
    

def test_invalid_mins_deposit():
    balance=100
    account=bank_accounts(balance)
    account.mins_deposit(500)
    assert account.balance==100        
    
    
    
def test_show_balance():
    balance=100
    account=bank_accounts(balance)
    assert account.show_balance()==100 
    account.deposit(200)
    assert account.show_balance()==300 
    account.mins_deposit(300) 
    assert account.show_balance()==0  
