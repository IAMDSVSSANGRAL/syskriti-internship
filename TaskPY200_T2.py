# Take input from user
num = float(input("Enter a number: "))

# Check condition
if num > 0:
    print(f"Your entered number {num} was positive.")
elif num < 0:
    print(f"Your entered number {num} was negative, however positive value of your number is {abs(num)}.")
else:
    print(f"Your entered number {num} was zero.")