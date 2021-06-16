#program1
list=[50,68,75,1,4,10]
list.append(8)
print(list)

del list[1]
print(list)

list.sort()
print("Largest number is",max(list))
print("Smallest number is",min(list))


#program2
def reverse(Tuple):
    new_tuple=Tuple[::-1]
    return(new_tuple)

Tuple=('a','n','u','s','h','a')
print(reverse(Tuple))


#program3
aTuple = (123, 'xyz', 'zara', 'abc');
aList = list(aTuple)
print("List elements : ", aList)




