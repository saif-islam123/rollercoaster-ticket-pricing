print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
adult = 18
child = 5
youth = 7
bill =0
p_charges = 3
if height >= 120:
    print("You can ride ")
    age = int(input("Enter the age. "))
    if age > 45 and age < 55:
        print("Thier ticket is free ")
    else:
        if age >= 18:
            bill = adult
            print(f"Your ticket price is {adult}$")
        elif age < 12:
            bill = child
            print(f"Your ticket price is {child}$")
        else:
            bill = youth
            print(f"Your ticket price is {youth}$")

        want_photo = input("Do you want photo? (yes, no): ")
        if want_photo == "yes":
            bill += p_charges
            print(f"The total bill is {bill}$")
        else:
            print(f"The total bill is {bill}$")
else:
    print("You can't ride")