#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 21:41:26 2019

@author: apple
"""

import re #Importing regex

#class declaration
class PasswordAuthentication:
    
    #defining the init function
    def __init__(self, Password):
        self._Password = Password
    
    #Defining the business logic
    def Authentication(self, Password = ''):
        Password = self._Password
        UserPassword = re.split(r',', Password) #converting string into list when comma(,) is discvered
    
        try:
            Bool1 = False #Verification Boolian 1
            Bool2 = False #Verification Boolian 2
            Bool3 = False #Verification Boolian 3
            Bool4 = False #Verification Boolian 4
            Bool5 = False #Verification Boolian 5
            Bool6 = False #Verification Boolian 6
            Bool7 = False #Verification Boolian 7
            Bool8 = False #Verification Boolian 8
            
            for i in range(len(UserPassword)): #For loop will run for the length of list
                
                print('')
    
                Boolaz = re.search("[a-z]", UserPassword[i]) #Checking for alphabets from [a-z]
                if Boolaz:
                    Boolaz = True
        
                BoolAZ = re.search("[A-Z]", UserPassword[i]) #Checking for alphabets from [A-S]
                if BoolAZ:
                    BoolAZ = True
        
                Bool09 = re.search("[0-9]", UserPassword[i]) #Checking for numbers from [0-9]
                if Bool09:
                    Bool09 = True
        
                Boolsym = re.search("[*$_#=@]", UserPassword[i]) #Checking for characters
                if Boolsym:
                    Boolsym = True
        
                Boolexp = re.search("[%!)(]", UserPassword[i]) #Checking for alphabets expressions
                if Boolexp:
                    Boolexp = True

                if len(UserPassword[i]) < 6: #Checking the length if less than 6
                    print(UserPassword[i], ' Failure Password must be at least 6 characters long.')
                    Bool1 = True
            
                elif len(UserPassword[i]) > 12: #Checking the length if greater than 12
                    print(UserPassword[i], " Failure Password must be smaller than 12 characters long.")
                    Bool2 = True
             
                elif Boolaz != True: #using if - elif - else so as to throw print only once per string in list
                    print(UserPassword[i], " Failure Password must contain at least one letter from a-z.")
                    Bool3 = True
        
                elif Bool09 != True:
                    print(UserPassword[i], " Failure Password must contain at least one number from 0-9.")
                    Bool4 = True
        
                elif BoolAZ != True:
                    print(UserPassword[i], " Failure Password must contain at least one letter from A-Z.")
                    Bool5 = True
        
                elif Boolsym != True:
                    print(UserPassword[i], " Failure Password must contain at least one letter from *$_#=@.")
                    Bool6 = True
        
                elif Boolexp == True:
                    print(UserPassword[i], " Failure Password cannot contain %!)(.")
                    Bool7 = True
        
                else:
                    print(UserPassword[i], " Success")
                    Bool8 = False
                
        except:
            print("Exception Occured")
        
        
        finally:
            #if error occured even once show hits
                if (Bool2 == True or Bool3 == True or Bool4 == True or Bool5 == True or Bool6 == True or Bool7 == True or Bool1 == True) or Bool8 == True:
                    print('''
-------------------------------------------------------------------------------------                 
|            Hint: Error messages for each check:                                    |
|                                                                                    |
|            1. Password must be at least 6 characters long.                         |
|            2. Password must be at max 12 characters long.                          |
|            3. Password must contain at least one letter from <set_that_failed>.    |
|            4. Password cannot contain %!)(.)                                       |
-------------------------------------------------------------------------------------''')


#these will be called when the python script runs
Password = input("Entre User Password: ")
Output = PasswordAuthentication(Password)
Output.Authentication()