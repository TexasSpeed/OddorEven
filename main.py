number = input("Enter a number: ")
number = int(number)

if number % 4 == 0:
    print("Number is multiple of 4")
elif number % 2 == 0:
    print("Even")
else:
    print("Odd")

print("Now choose two numbers")

num = input("Choose first number: ")
num = int(num)
check = input("Choose second number: ")
check = int(check)

if num % check == 0:
    print("These two numbers divide evenly into each other.")
else:
    print("These two numbers do not divide evenly into each other.")

squared = input("Choose a number to square")
result = int(squared) * int(squared)
print(result)
