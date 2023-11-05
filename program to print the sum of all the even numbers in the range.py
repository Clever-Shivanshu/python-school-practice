#Taking the max no. from the user
maxno = int(input(" Please Enter the Maximum Value : "))
even = 0
odd = 0
for number in range(1, maxno + 1):
 if(number % 2 == 0):
  even = even + number
 else:
  odd = odd + number
#The format() method formats the specified value(s) and insert them inside the string's placeholder.
print("The Sum of Even Numbers from 1 to {0} = {1}".format(number, even))
print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, odd))
# © Copyright 2022 Shivanshu Bhashkar. All right Reserved 
