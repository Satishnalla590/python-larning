#finding given number is positive or negative
#1 st method brute method
num = int(input())
if num > 0:
    print('The Number Is Positive')
elif num < 0:
    print('number is negative')
else :
    print('zero')



#2nd method
#nested if - else statement

num = int(input("enter a number"))
if num >= 0 :
    if num == 0:
        print('Zero')
    else:
        print('positive Number')
else :
    print('negative number')

#3rd method
# ternary operator
num = int(input("enter a number"))
print('positive' if num >= 0 else "negative")

# finding a given number is even or od
#1st method
# brute method
num = int(input('enter a number'))
if num%2 == 0:
    print('positive')
else:
    print('odd number')


#2nd method ternary method

num = int(input('enter a number'))
print('even' if num%2 == 0 else 'odd')
