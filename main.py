from utils import *
valor= input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):").lower()
while True:
    if valor == "add":
        val1= int(input("Enter the first number:"))
        val2= int(input("Enter the second number:"))
        result= add(val1,val2)
        print(f"The result is: {result}")
    elif valor == "subtract":
        val1= float((input("Enter the first number:")))
        val2= float((input("Enter the second number:")))
        result= sub(val1,val2)
        print(f"The result is: {result}")
    elif valor == "multiply":
        val1= int(input("Enter the first number:"))
        val2= int(input("Enter the second number:"))
        result= multiply(val1,val2)
        print(f"The result is: {result}")
    elif valor == "divide":
        val1= int(input("Enter the first number:"))
        val2= int(input("Enter the second number:"))
        result= divide(val1,val2)
        print(f"The result is: {result}")
    elif valor == "exponent":
        val1= int(input("Enter the first number:"))
        val2= int(input("Enter the second number:"))
        result= exponent(val1,val2)
        print(f"The result is: {result}")
    elif valor == "modulo":
        val1= int(input("Enter the first number:"))
        val2= int(input("Enter the second number:"))
        result= modulo(val1,val2)
        print(f"The result is: {result}")
    elif valor == "floor_divide":
        val1= int(input("Enter the first number:"))
        val2= int(input("Enter the second number:"))
        result= floor_divide(val1,val2)
        print(f"The result is: {result}")
    elif valor == "absolute":
        val1= int(input("Enter the number:"))
        result= abs(val1)
        print(f"The result is: {result}")
    elif valor == "exit":
        break
    else: 
        print("Invalid option!")
    valor= input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):").lower()