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
phone = int(input())

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

#CreditScore =int(input('enter your credit_score'))

#for i in range(CreditScore):
CreditScore = 800
if CreditScore>=780 and CreditScore<= 850:
       downPayment = 0.0 * price
       credit_status=("Zero Down Payment")
       
elif CreditScore>=740 and CreditScore <=779:
       downPayment = 0.2 * price
       print("Very Good")
       
elif CreditScore>=720 and CreditScore <=739:
       downPayment = 0.3 * price
       print("Above Average")
       
elif CreditScore>=680 and CreditScore <=719:
       downPayment = 0.6 * price
       print("Average")
       
elif CreditScore>=620 and CreditScore <=679: 
       downPayment = 0.18 * price
       print("Below Average")
       
elif CreditScore>=580 and CreditScore <=619: 
       downPayment = 0.20 * price
       print('Not qualified for a new home')
       credit_Status=("Poor Credit Score")
       
else:
       downPayment = 0.25 * price
       print('Try next time')
       credit_status=("Poor Credit Score")




print('='*60)
print('Full names:', fullnames)
print("Email:",email,phone)
print('Physical Address:',mailing)
print("Mailing City:",city), print("Zipcode :", zipcode)
print("New House Price:",price)
print('Credit Score:', CreditScore)
print('Credit Status:',credit_status)
print('Down Payment:',downPayment)
print("Congratulations you now own your dream home: ",fullnames)
print('='*60)