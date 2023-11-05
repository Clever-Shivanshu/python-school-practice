def calculate_operations(x, y):
    product = x * y
    sum_result = x + y
    difference = x - y
    quotient = x / y

    print("Product:", product)
    print("Sum:", sum_result)
    print("Difference:", difference)
    print("Quotient:", quotient)


# Get user input for X and Y
x = float(input("Enter the first number : "))
y = float(input("Enter the second number : "))

# Calculate and display the operations
calculate_operations(x, y)

