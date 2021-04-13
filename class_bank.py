#!/usr/bin/env python
# coding: utf-8

# In[14]:


#class Bank account
# Displays the balance after deposit and withdrawal. Raises error if there is not enough balance to withdraw or deposit invalid amount

class BankAccount:
    
    def __init__(self):
        self.balance = 0.0
   
    def deposit(self,amount):
        if amount > 0:
            self.balance= self.balance + amount
         
        else:
            raise ValueError("Enter Valid amount to deposit") 
            
    def widthdraw(self,amount):
        if amount < self.balance:
            self.balance = self.balance - amount
        else:
            raise ValueError("You don't have enought balance to withdraw") # if the value is more than the account balance

    def balance1(self):
        return self.balance   

def main():
    BA = BankAccount()
    BA.deposit(1000)
    print("DEPOSIT BALANCE: ")
    print("The deposit Balance is: £",BA.balance1())

    BA.widthdraw(100)
    print("WITHDRAWAL BALANCE: ")
    print("The Account Balance after withdrawal is: £",BA.balance1())

main()


# In[ ]:




