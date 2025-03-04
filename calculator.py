from functions import *

while True:
    print("what would you want to do?")
    print("1 addition")
    print("2 subtraction")
    print("3 multiplication")
    print("4 division")


    choice = input("enter your choice: ")
    if choice == 'q' or 'Q':
        break

    num1 = int(input("enter num1 :"))
    num2 = int(input("enter num2 :"))


    if choice == '1':
      addition(num1,num2)

    elif choice == '2':
        subtraction(num1,num2)

    elif choice == '3':
        multiplication(num1,num2)

    elif choice == '4':
       division(num1,num2)

    else:
        print("there is no such choice")
print(" ")