def main_marks():
    while True:
        try:
            subjects=int(input("Enter your subjects: "))
            total=int(input("Enter your total marks:"))
            if(subjects<0 or total<0 or subjects>total):
                print(f"Invalid input! MArks should be between 0 and {total}")
                continue
        except ValueError:
            print("Invalid input! please enter a number")
            continue
        else:
            percentage=(total/subjects)
            print(f"Your percentage of your marks is: {percentage}")
            if(percentage>=90):
                print("Your Grade:A+")
                break
            elif(percentage>=80 and percentage<=89):
                print("Your Grade:A")
                break
            elif(percentage>=70 and percentage<=79):
                print("Your Grade:B")
                break
            elif(percentage>=60 and percentage<=69):
                print("Your Grade:C")
                break
            elif(percentage>=50 and percentage<=59):
                print("Your Grade:D")
                break
            else:
                print("You failed!")
                break
main_marks()


