def checkPrime(no):
    for i in range(2,no):
        if no%i == 0:
            print("Not a prime no.")
            return 0
    print("It's a Prime !")

val = int(input("Enter no. you want to check: \n"))
checkPrime(val)