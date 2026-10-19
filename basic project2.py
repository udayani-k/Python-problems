#Calculator
def Addition(a,b):
    return a+b
def Subtraction(a,b):
    return a-b
def Multiplication(a,b):
    return a*b
def Division(a,b):
    if b==0:
        return "cannot divide with zero"
    return a/b
print("Welcome to the pyton")
print("1.Addittion")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("enter your choice:"))
a=float(input("enter a first number:"))
b=float(input("enter a second number:"))
if choice==1:
    print("Addition",Addition(a,b))
elif choice==2:
    print("Subtraction",Subtraction(a,b))
elif choice==3:
    print("Multiplication",Multiplication(a,b))
elif choice==4:
    print("Division",Division(a,b))
else:
    print("invalid choice selection")
