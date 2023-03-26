#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Guess the number

import random
print ("Welcome to Guess the number game!!!")

SysNumber = random.randint(1,20)
InpNumber = int(input("Guess the number between 1 to 20!!You have 5 chances! All the best:- "))
game = "START"

while (game == "START"):
    if ( InpNumber > 0 and InpNumber < 21):
        for i in range (0,4):
            if (InpNumber > SysNumber):
                print ("Oops! Number you enetered is above the Lucky draw number. Pls try again")
                InpNumber = int(input("Enter the number again between 1 to 20:- "))
            elif (SysNumber > InpNumber):
                print ("You just missed it! Number you entered is less than Lucky draw number. Pls try again")
                InpNumber = int(input("Enter the number again between 1 to 20:- "))
            else:
                print ("\n")
                print ("Woooh!!! You won it.. That's the right number:::::"+str(SysNumber))
                print ("Your Score!:"+ str(10*(5-i)))
                game = "STOP"
                break
        if game == "START":
            print ("\n")
            print ("You lost it :( Correct number is:"+str(SysNumber))
            game = "STOP"
    else:
        print ("Entered number is not between 0 and 20. Please enter the number again to begin the Game!")
        InpNumber = int(input("Enter the number again between 1 to 20:- "))

