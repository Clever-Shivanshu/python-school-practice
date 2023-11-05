a=int(input("Enter your 1st no. "))
b=int(input("Enter your 2nd no. "))
c=input("Choice a operator,+-*/ ")
if c=='+':
    print("The sum is ",a+b)
elif c=='-':
    print("The difference is ",a-b)
elif c=='*':
    print("The product is ",a*b)
elif c=='/':
    print("The quotient is ",a/b)
else:
    print("Something went Wrong!!")
