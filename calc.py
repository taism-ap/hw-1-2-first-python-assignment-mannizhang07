print("This is a simple calculator that only takes two values and can preform 4 functions")
num1= input("Please enter your first number: ")

op= input("Please select the appropriate symbols for the operation you would like perfromed, - is subtract, + is add, * is mutiply, and / is divide")

num2= input("Please enter your second number: ")


if op == "-":
          print(float(num1)-float(num2))
if op == "+":
          print(float(num1)+float(num2))
if op == "*":
          print(float(num1)*float(num2))
if op == "/":
          print(float(num1)/float(num2))


