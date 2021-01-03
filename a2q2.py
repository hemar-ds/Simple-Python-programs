#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


# Monty-Hall simulation: Always SWITCHING the door - Top down design

import random
from random import randrange
def main():
    printIntro()
    win,doors,n_doors,n = getInputs()
    win = simulation(win,doors,n_doors,n)
    printReport(n,win)

def printIntro():
    print("This program simulates winning probability of Monty Hall problem with SWITCH ")

def getInputs():
    win = 0
    doors = [1,2,3]
    n_doors = len(doors)
    n = int(input("Enter number of simulations: "))
    return win,doors,n_doors,n

def simulation(win,doors,n_doors,n):
    switch = True # as the option is always switch
    def no_prize_door(prize_door,n_doors,contestant_choice): # choosing the "no prize door" as a host door
        i = 1
        while(i == prize_door or i == contestant_choice):
            i = i+1
        return i
    
    def door_switch(host_door, n_doors, contestant_choice):# choosing the door after switch
        i = 1
        while (i == host_door or i== contestant_choice ):
            i = (i+1)
        return i
    
    for i in range(n): # calculating winning percentage
        prize_door = random.choice(doors)
        contestant_choice = random.choice(doors)
        host_door = no_prize_door(prize_door,n_doors,contestant_choice)
        if switch == True:
            contestant_choice = door_switch(host_door,n_doors,contestant_choice)
        if contestant_choice == prize_door and switch == True:
            win = win + 1
    return win
                
def printReport(n,win):
    prob_win_percentage = win/n
    print("The probability of winning with switch : {:.2%}".format(prob_win_percentage))

if __name__== "__main__":
    main()


# In[ ]:




