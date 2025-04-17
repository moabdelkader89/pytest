

# we made the fixture for dont repeat the obj and the balance variable and that why we use the fixture 
#we put the fixture inside the parameters of the def to make obj from it 
#and the old code i hash it to can review it


# we have too many markers that can work with the function and every one has it job
#@pytest.mark.skip(reason="not useful") >to skip the test
#@pytest.mark.slow> to see the time of test and most take time.sleep(2) inside the function  
# @pytest.xfail(reason="more than the balance")>to say we expect the test will fail   
#


from bank_account import bank_accounts
import pytest
import time

@pytest.fixture()
def fix():
    balance=100
    account=bank_accounts(balance)
    return account
    
@pytest.mark.skip(reason="not useful")
def test_balance(fix):
    assert fix.balance==100
    
    
  
def test_de(fix):
    fix.deposit(50)
    assert fix.balance==150
    
    

def test_mins(fix):
    
    fix.mins_deposit(50)
    assert fix.balance==50
    
 # this test should fail as long as we mark it as xfail      
@pytest.mark.xfail(reason="more than the balance")     
def test_show_balance(fix):
    result=fix.show_balance()
    assert result==100
    
    
    
 #this for can pass param in function and see the outcome & run the same test with many value    
@pytest.mark.parametrize("num1,num2",[(10,5),(12,6),(20,10)])    
def test_equal(num1,num2):
    assert num1/num2==2
    
    
def test_deposit_trans(fix):
    
    fix.transaction.append(fix.deposit(100))
    assert [100,200] ==  fix.transaction    
    
def test_mins_deposit_trans(fix):
    fix.transaction.append(fix.mins_deposit(100))
    assert [100,0] ==  fix.transaction     
    
    
    
def test_invalid_deposit(fix):
    fix.deposit(-50)
    assert fix.balance==100         
    
    
    
def test_invalid_mins_deposit(fix):
    fix.mins_deposit(500)
    assert fix.balance==100     
    
    
# I called it test_show_balance2 cause there is another test above by the same name    
def test_show_balance2(fix):
    assert fix.show_balance()==100 
    fix.deposit(200)
    assert fix.show_balance()==300 
    fix.mins_deposit(300) 
    assert fix.show_balance()==0           