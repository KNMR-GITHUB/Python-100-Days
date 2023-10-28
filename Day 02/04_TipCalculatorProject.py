print("Welcome to Tip Calculator.\n")
bill = float(input("What is the total bill ?\n"))
tip = int(input("What is tip percentage ?\n"))
no_of_people = int(input("How many people are splitting the bill ?\n"))

pay = (bill + (bill*tip)/100)/no_of_people

print("Amount each one pays: ", pay)