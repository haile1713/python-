unit=input("what the temperature in celsius or fahrenheit (c/f)?")

temp=float(input("current temperature ="))

if unit =="c" :
    temp=(((9*temp)/5)+32)

    print(f"the temperature in fahrenheit is: {temp}")
elif unit =="f" :
    temp=(((9*temp)/5)+32)

    print(f"the temperature in celsius is: {temp}")

else :
    print("invalid temperature unit")