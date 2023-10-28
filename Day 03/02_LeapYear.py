year = int(input("Enter the year.\n"))

if year%4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print("Leap Year")
    elif year % 100 == 0 and year % 400 != 0:
        print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")
