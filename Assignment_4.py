# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:11:59 2021

@author: chepchir
"""

#Enter the first name
print("Enter the first name")
first_name = input('fname:')

#Enter the last name
print("Enter the last name")
last_name = input('lname')

fullnames = input(first_name + last_name)
#Enter the email

print("Enter the email address")
email = input()

#Enter the phone number
print("Enter the phone number")
phone = input()

#Enter the mailing
print("Enter the mailing address")
mailing = input('mail')

#Enter the mailing city
print("Enter the City")
city = input()
#Enter the mailing code
print("Enter the zipcode")
zipcode = input()

#Price of the House to be bought
print("Enter the house price")
price = float(input('house_price:'))

#Enter the credit score

CreditScore =int(input('enter your credit_score'))
for i in range(CreditScore):
   if CreditScore>=780 and CreditScore<= 850:
       print("Zero Down Payment")
       downPayment = 0.0 * price
   elif CreditScore>=740 and CreditScore <=779:
       print("Very Good")
       downPayment = 0.2 * price
   elif CreditScore>=720 and CreditScore <=739:
       print("Above Average")
       downPayment = 0.3 * price
   elif CreditScore>=680 and CreditScore <=719:
       print("Average")
       downPayment = 0.6 * price
   elif CreditScore>=620 and CreditScore <=679: 
       print("Below Average")
       downPayment = 0.18 * price
   elif CreditScore>=580 and CreditScore <=619:  
       print("Poor Credit Score")
       downPayment = 0.20 * price
   else:
       print("Poor Credit Score")
       downPayment = 0.25 * price

print('Full names:', fullnames)
print("Email:",email)
print('Phone:',phone)
print('Mailing Address:',mailing)
print("Mailing City:",city)
print("Zipcode :", zipcode)
print("Price of the house:",price)
print('Credit Score:', CreditScore)