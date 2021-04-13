# Please complete the functions that are associated with the given question in Assignment 1.
# Parameters and return values have been predefined. Don't change these but use these when developing your solution.

#1. Complete the function that takes in the x and y values, and returns the result of calling math.pow(x,y)

import math
def questionOne(x, y):
    result = math.pow(x,y)
    return result

questionOne(2,3)  # calling the function 

#2.Complete the function that takes a string of characters as input and returns the checksum. 

def questionTwo(word):
    total = 0
    for i in range(len(word)):
        string_new = ord(word[i])
        total = string_new + total
        checksum = total % 10
    return checksum
    
questionTwo("cat")
    

#3.Complete the function that takes in a number from 0 to 99 (representing the amount of change that’s due) as a parameter and #then returns, in the following order as individual variables, the number of one penny, two pence, 5 pence, 10 pence, 20 pence, #and 50 pence pieces that should be dispensed.  Your function should be as efficient as possible and dispense the fewest coins #possible

def questionThree(change):
    if change >= 0 and change <= 99:
        fiftyPence = int(change / 50) # calculates fifty pence
        balance = round(change -(fiftyPence *50),2)

        twentyPence = int(balance / 20)# calculates twnety pence            
        twenty_pence_balance = round(balance - (twentyPence * 20),2)

        tenPence = int(twenty_pence_balance / 10)# calculates ten pence
        ten_pence_balance = round(twenty_pence_balance - ((tenPence * 10)),2)

        fivePence = int(ten_pence_balance / 5)# calculates five pence
        five_pence_balance = round(ten_pence_balance - (fivePence * 5),2)

        twopennies = int(five_pence_balance / 2)# calculates two pence
        two_pence_balance = round(five_pence_balance - (twopennies * 2),2)

        penny = int(two_pence_balance / 1)# calculates one penny
        one_pence_balance = round(two_pence_balance - (penny * 1),2)
        
        return penny, twopennies, fivePence, tenPence, twentyPence, fiftyPence
    
    else:
        print("Please enter the value between 0 and 99") # Executes when we enter out of range values

questionThree(98)



#4.Complete the function that takes a filename and a word as the parameters and consequently will determine the number of times that the particular word appears in the file

def questionFour(filename, word):
      
    word = word.lower() # converts the string into lower case if we give the input in uppercase
    
    f = open(filename) # opening file
    
    f_content = f.read() # reading the content of the file
    
    f_case = f_content.lower() # changing the contents to lower case
    
    wordCount = f_case.count(word) # finding the count of the word

    return wordCount

questionFour(r'C:\Users\urshe\OneDrive - University of Birmingham\Programming for DS\test.txt',"data")



#5.Complete the function that allows the user to evaluate the score of any word. your function must use a sentinel 
#loop to allow the user to evaluate as many words as they would like until they enter the word “quit

def questionFive():
    char_sum = 0
    word = input("Enter the words on the board: << quit to exit >> : ")
    word = word.lower()
    while word != "quit":
        for i in range(len(word)):  # calculating the value of each character and iterating until the "while" condition is true
            word = word.lower()
            letter_ord_count = ord(word[i])- 97  
            char_sum = char_sum + letter_ord_count
        print("Word score : ",char_sum) 
        char_sum = 0
        word = input("\nEnter the words on the board: << quit to exit >>")
        word = word.lower()
        
        while word == "":
            print("\nYou have not entered any value\n ")
            word = input("\nEnter the words on the board: << quit to exit >>")
            word = word.lower()
        
        while word.isalpha() != True:
            print("\nThe word is not valid\n")
            word = input("\nEnter the words on the board: << quit to exit >>")
            word = word.lower()
      
    print("Good Bye!")
        
questionFive()