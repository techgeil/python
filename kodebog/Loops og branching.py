

message = str("Hello, World!")

for i in range(0, 10, 1):
    print(message + " " + str(i))
    
# Branching if statement
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    