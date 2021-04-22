name = input('Enter first and last name: ')
student_ID = input('Enter your student ID: ')
Mailing_Address = input('Enter your mailing address: ')
City = input('Enter your City: ')
Country = input('Enter your Country: ')

Phone = input('Enter your phone number: ')
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check(email):
    if (re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")
if __name__ == '__main__':
    email = input('Enter your email address: ')
    check(email)

region = input('Enter your Region [A,0]?')
print()
print('Full name: ',name)
print("Student's ID is :", student_ID)
print("Student's mailing Address is: ", Mailing_Address )
print("Student's Email address is: ", email)
print("Student's city is: ", City)
print("Student's Country is: ", Country)
print("Student's Region is: ", region)
if region == 'A':
    print("Student " + name + "is Qualified for Scholarship")
else:
    print("Student " + name + "is NOT Qualified for Scholarship")

quiz = float(input('Enter your first quiz score: '))
quiz2 = float(input('Enter your second quiz score: '))
quiz3 = float(input('Enter your third quiz score: '))
test1 = float(input('Enter your first test score: '))
test2 = float(input('Enter your second test score: '))

regex = "^(10|[0-9]?)$"
def check(zoom_score):
    if (re.search(regex, zoom_score)):
        print("Valid number")
    else:
        print("Invalid number")
if __name__ == '__main__':
    zoom_score = input('Enter your Zoom call points: ')
    check(zoom_score)
assignment_score = input('Enter your programming assignment points:')
Totals = [quiz, quiz2, quiz3, test1, test2]
avg = sum(Totals)/len(Totals)

print(name + " Your scores are as follows: ")
print('First Quiz:', quiz)
print('Second Quiz:', quiz2)
print('Third Quiz:', quiz3)
print('First Test:', test1)
print('Second Test:', test2)
print('Third Quiz:', quiz3)
print(name + " Your points are as follows:")
print('Zoom:', zoom_score)
print('Assignments:', assignment_score)
print("The average score of " + name + " is ", round(avg,2))
