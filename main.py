courses = ["1" == "Engineering","2" == "Accounting","3" == "Education","4" == "Nursing"]
while True:
    print("Courses offered")
    print("1.Engineering")
    print("2.Accounting")
    print("3.Education")
    print("4. Nursing")
    print("5. quit")


    choice = input("Enter a number to choose your choice of preference: ")
    if choice == "1":
        print(f"Your preference course is {"engineering"}")
    elif choice == "2":
        print(f"your choice of preference is {"Accounting"}")
    elif choice == "3":
        print(f"Your course of preference is {"education"}")
    elif choice == "4":
        print(f"Your course of preference is {"Nursing"}")
    elif choice == "5":
        print("quit")
    else:
        print("The course you are searching for is not offered")
