num1= float(input("input ur first number :"))
num2= float(input("input ur second number :"))
operator = input("Specify the math operation here (+, -, *, /): ")

if operator == "+":
    print (num1+num2)
elif operator == "-":
    print (num1-num2)
elif operator == "*":
    print (num1*num2)
elif operator == "/":
    print (num1/num2)
else :
    print ("f { operator }not a valid operator")