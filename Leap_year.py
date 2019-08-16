print('Program to check wheather the year is Leap year')
a=int(input("Enter a year:"))
if((a%4==0 and a%100!=0) or (a%400==0)):
    print('Entered year is a leap year.')
else:
    print('Entered year is NOT a leap year.')
