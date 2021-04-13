#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Monty-Hall simulation with NO Switch - Top down design

import random
from random import randrange
def main():
    printIntro()
    win,doors,n = getInputs()
    win = simulation(win,doors,n)
    printReport(n,win)

def printIntro():
    print("Winning probability of Monty Hall game - NO SWITCH ")

def getInputs():
    win = 0
    doors = [1,2,3]
    n = int(input("Enter number of simulations: "))
    return win,doors,n

def simulation(win,doors,n):
    for i in range(n): 
        prize_door = random.choice(doors)
        contestant_choice = random.choice(doors)
        if contestant_choice == prize_door:
            win = win + 1
    return win
                
def printReport(n,win):
    prob_win_percentage = win/n
    print("The probability of winning (NO SWITCH) : {:.2%}".format(prob_win_percentage))

if __name__== "__main__":
    main()


# In[ ]:




