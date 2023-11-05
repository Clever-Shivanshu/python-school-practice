a = str(input("What is your Name? "))
f = str(input("Do you study? "))

if f=='yes'or'Yes':
    s = str(input("In which School you study? "))
    y = str(input("In which Class you study? "))
    b = str(input("Where you live? "))
    c = str(input("What do you love to do? "))
    d = str(input("What do you love to eat? "))
    e = str(input("What is your favourite sport? "))
    print("Hi",a,"Who studies in ",s+y,"who lives in",b,"who loves❤ to", c, ", eat", d, "& play", e)
elif f=='no'or'No':
    b = str(input("Where you live? "))
    c = str(input("What do you love to do? "))
    d = str(input("What do you love to eat? "))
    e = str(input("What is your favourite sport? "))
    print("Hi",a,"who lives in",b,"who loves❤ to", c, ", eat", d, "& play", e)
else:
    print("something went wrong!!")

