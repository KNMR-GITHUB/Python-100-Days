def calc(oper,n1,n2):
    """ A function that takes 3 positional arguments: i)'operator'(valid values: '+', '-', '*', '/') , 
        ii) 'number 1'(number) and iii) 'number 2'(number).
        Returns the result of the two numbers for that operation. """
    if oper ==  "+":
        return n1 + n2
    elif oper == "-":
        return n1 - n2
    elif oper == "/":
        return n1 / n2
    elif oper == "*":
        return n1 * n2
    else:
        return "\nInvalid Operator."
cond = "hehehe"
while cond != 'no': 
    n1 = float(input("What is the first number: \n"))
    n2 = float(input("What is the second number: \n"))
    oper = input("What operation would you like to perform: \n + , - , * , / \n")
    result = calc(oper, n1, n2)
    print(f"{n1} {oper} {n2} = {result} \n")
    cond = input("Would you like to do another operation ?:\n 'yes' or 'no' \n")
print("calc has ended.")