# Taking a number from user
num=int(input("Enter your number--> "))
# Function to check whether the number is divisible by 7
def isDivisibleBy7(num) :
	
	if num < 0 :
	    return isDivisibleBy7( -num )

	if( num == 0 or num == 7 ) :
	    return True
	
	if( num < 10 ) :
	    return False
		
	return isDivisibleBy7( num // 10 - 2 * ( num - num // 10 * 10 ) )	
# Driver program
if(isDivisibleBy7(num)) :
    print ("The number can Divisible with 7")
else :
    print ("The number cannot Divisible with 7")
# Function to check whether the number ends with 7
if(num%10==7) :
    print ("The Number ends with 7")
else :
    print ("The Number does not ends with 7")
# Function to check whether the number is buzz or not
if(isDivisibleBy7(num)) or (num%10==7) :
    print (num, "is a buzz number.")
else:
    print (num, "is not a buzz number.")
#© Copyright 2022 Shivanshu Bhashkar. All right Reserved 
