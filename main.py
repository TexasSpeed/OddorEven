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
    print("The numbers divide evenly into each other.")
else:
    print("The numbers don't divide evenly into each other.")
