print("Calculator")
a = int(input("Enter a digit"))
b = input("Choose one of this +,-,*,**,/,//,%")
c = int(input("Enter another digit"))

if (b == "+") :
    outcome = a + c
elif (b == "-") :
    outcome = a - c
elif (b == "*") :
    outcome = a * c
elif (b == "/") :
    outcome = a / c
elif (b == "//") :
    outcome = a // c
elif (b == "%") :
    outcome = a % c
elif (b == "**"):
    outcome = a ** c
else :
    print("Invalid number")
print(outcome)
