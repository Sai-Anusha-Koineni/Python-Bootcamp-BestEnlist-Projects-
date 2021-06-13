#program to print Hello,World!
print("Hello,World!")

#Arithmetic operators 

a=20
b=20
print(a+b)
print(a*b)
print(a-b)
print(a%b)
print(a/b)

#program to find odd and even number

a=int(input("Enter the number:"))
if(a%2==0):
    print(a, "even number")
else:
    print(a,"odd number")

#program to fint maximun of given number

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
maximum=max(a,b)
print(maximum)

#program to swap the two numbers
a=5
b=6
temp=a
a=b
b=temp
print("After swapping",a,b)

#program to find given number is postive or negative

a=int(input("Enter the number:"))
if(a>0):
    print(a,"is postive")
else:
    print(a,"is negative")

#program to find given year is leap year or not

a=int(input("Enter the year:"))
if(a%4==0):
    print(a,"is leap year")
else:
    print(a,"is not leap year")

#print lists

l=[1,2,3,4,5]
l[2]=5
del l[3]
l.append(6)
l.insert(2,5)
l.sort()
l.reverse()    
print(l)


