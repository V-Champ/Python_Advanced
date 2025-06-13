# to check ID in the python
#Every object in Python is assigned a unique identity
#(ID) which remains the same for the lifetime of that object.
#This ID is akin to the memory address of the object. The
#function id() returns the identity of an object.

A=10
B=20
print(A)
print("id of A is \n",id(A))
print("id of B is",id(B))
print("\n value is=",id(B)-id(A))
s="vineetha"
print(s)
print("\n type of s =",type(s))
#######LIST###########
list =[1,2,3,4,5]
print(list)
list.append(22)
print(list)
print(list[0])
print(list[1:])
list.pop(1)
print(list)
print(list.pop())
print(list)
#in place sorting,reverse 
my_numlist = [1,8,9,8,2,7,3,0,2]

print(my_numlist.sort())# returns None as sort function in place or the same list
print(my_numlist)
my_numlist.reverse()
print(my_numlist)
###########DICT##############
my_dict ={'CCZM': 0, 'DDZM': 1, 'IPZM': 2, 'PDZM': 3, 'RZM': 4, 'FZM': 5}
print(my_dict)
fname = input("enter your name")
age=int(input("enter your age"))
print("\n Name and age is =",fname,age)#print(value [, ..., sep = ' ', end = '\n'])
print(fname [, ..., sep = ' ', end = '\n'])