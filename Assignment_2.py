# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:58:28 2021

@author: chepchir
"""

#Enter Full Names
print("Enter First and Last Name:")
fname = input('fname:') #First Name
lname = input('lname:') #last Name
fullnames = fname + " " + lname

#Enter phone, email

print("Enter Customers Phone Number: ")
phone = input('phone')

print('Enter Customers email aaddress: ')
email = input('email')

#price of a used car
price = 10000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
   
else:
    down_payment = 0.2 * price
    
print('Fullnames:',fullnames)
print('phone:',phone)
print('Email:',email)
print("down payment:", down_payment)

