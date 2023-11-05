#Taking the value from the user
num=int(input("Enter your number--> "))
#Asking the user that what to do?
wtd=int(input("Type 1 for area of square or Type 2 for area of rectangle "))
#If the user type 1 the function multiplys by itself
if wtd==1 :
    print("The Area of square is ",num*num)
#If the user type 2 the function ask the second number & multiplys by it    
elif wtd==2 :
    sec=int(input("Enter your second number--> "))
    print("The Area of rectangle is ",num*sec)
#If the user type any invalid charater the function says sOmEtHiNg WeNt WrOnG!!
else:
    print("sOmEtHiNg WeNt WrOnG!!")

#© Copyright 2022 Shivanshu Bhashkar. All right Reserved     
