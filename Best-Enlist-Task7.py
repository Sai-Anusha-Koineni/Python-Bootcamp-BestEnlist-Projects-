#program1

n1=int(input("Enter the first value:"))
n2=int(input("Enter the second value:"))
signs=input("Enter '+' for addition,'-'for subtraction,'*'for multiplication,'/' for division")

def math_function(num1,num2,sign):
    if sign=='+':
        print("Addition of num1 and num2 is",str(num1+num2))
    elif sign=='-':
        print("Subtaction of num1 and num2 is",str(num1-num2))
    elif sign=='*':
        print("Multiplication of num1 and num2 is",str(num1*num))
    elif sign=='/':
        print("Division of num1 and num2 is",str(num1/num2))
math_function(num1,num2,signs)



#program2


def covid(name,temp):
    print("Enter name",name)
    if temp=='':
        print("Temp is:98")
    else:
        print("Temp is:",temp)

name=input("Enter the name ")
temp=input("Enter temp")
covid(name,temp)
