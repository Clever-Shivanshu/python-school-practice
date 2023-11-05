#Greeting him/her
print("Welcome to Mayur Transport Company!! We transport parcel for you. This program is made to calculate the charge for a parcel")
#Taking the weight of parcel from the user
weight=int(input("Enter the weight of your parcel in kg--> "))

#if the weight is equal or lower than 10, cost sets to 15, weight/2*cost
if weight<10 or weight==10:
    cost=15
    print("₹", weight/2*cost)
#if the weight is equal or lower than 30,cost sets to 25 ,weight/2*cost
elif weight<30 or weight==30:
    cost=25
    print("₹", weight/2*cost)
#if the weight is greater than 30,cost sets to 35 ,weight/2*cost

elif weight>30:
    cost=35
    print("₹", weight/2*cost)
# © Copyright 2022 Shivanshu Bhashkar. All right Reserved 
