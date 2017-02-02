# 10-6
print("Give me two numbers, and I'll plus them.")
print("Enter 'q' to quit")

while True:
    number1 = raw_input("The first number: ")
    if number1 == 'q':
        break
    try:
        num1 = int(number1)
    except ValueError:
        print("The number1 input must be integer. Please enter the integer.")
        break

    number2 = raw_input("The second number: ")
    if number2 == 'q':
        break
    try:
        num2 = int(number2)
    except ValueError:
        print("The input must be integer. Please enter the integer.")
        break
        
    sum = num1 + num2
    print("The sum is : " + str(sum))
