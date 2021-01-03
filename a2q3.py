#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Implementing a class to represent a till
class Till:
    
    def __init__(self):
        self.amount = 0
        
    def startTransaction(self):
        self.current_Transaction = 0.00
        
    def Till_amount(self):
        self.amount = float(input("Enter the bill amount: "))
    
    def addItem(self,amount):
        T1.Till_amount()
        self.current_Transaction += self.amount
        
    def total(self):
        return self.current_Transaction
    
           
T1 = Till() 

T1.startTransaction()

T1.addItem(0)
print("The total is: ", T1.total())

T1.addItem(0)
print("The total is: ", T1.total())


T1.addItem(0)
print("The total is: ", T1.total())


# In[ ]:





# # 

# In[ ]:




