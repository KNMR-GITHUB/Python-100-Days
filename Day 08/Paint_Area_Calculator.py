import math

def paintAreaCalculator(height,width,cover):
    print(f"You need {math.ceil((height*width)/cover)} cans of paint.")

paintAreaCalculator(3,8,5)