#!/usr/bin/env python
# coding: utf-8

# In[1]:


#  Money transfer between accounts using Class
class BankAccount:
    def __init__(self):
        self.balance = 0.0
        self.savings = self.balance
       
    def deposit(self,amount):    
        if amount > 0:
            self.balance = self.balance + amount
         
        else:
            raise ValueError("Enter Valid amount to deposit") 
    
    def widthdraw(self,amount):
        if amount < self.balance:
            self.balance = self.balance - amount
        else:
            raise ValueError("You don't have enought balance to withdraw") # if the value is more than the account balance

    def transfer(self,t_amount,savings):
        savings.balance = savings.balance + t_amount
        self.balance  = self.balance - savings.balance
                
    def Balance(self):
        return self.balance
    
def main(): 
    checking = BankAccount()

    savings = BankAccount()

    checking.deposit(500)

    checking.transfer(200, savings)

    print("The balance in main account after transfer : £",checking.Balance())  

    print("The balance in the new account after transfer : £",savings.Balance())  

main()


# In[ ]:




