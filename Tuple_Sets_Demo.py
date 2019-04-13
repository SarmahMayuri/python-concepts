#Tuples, Sets, Booleans

#Tuple: can have any datattypes like list, str, float, int, list
T= (10,20.3,'Mayuri', [1,2,3])
print(T[0])
print(T[-1])

#Tuple is not mutable; can't change like LISt:

List1= ['Mayuri', 'Sameer', 29, 10.9]
Tuple1= ('Sarmah', 'Bangalore', 10, 9.8)
print(List1)
print(Tuple1)

List1[1]= 'Sameer Paran'
print(List1) #mutable
'''
Tuple1[1]= 'Kolkata'
print(Tuple1) # immutable
'''

#methods in tuple: 1. index 2. count
t= ('a', 'b', 'a', 1,1,2)
print(t.index('a')) # takes index position 1st one though appears in index 0 & 2
print(t.count(1)) # 1 appears in 't' twice

#SETS:
set1= {1,2,3,4,5,6}
print(set1)
a= set()
a.add(1)
a.add(2)
a.add(3)
a.add(1)
print(a) # though 1 is entered twice set o/p gives only once

llist=['Mayuri', 'Sarmah', 'Sameer', 'Sarmah',1,2,]
print(llist)
print(set(llist))
print(set('Mayuri'))

A= set('Sarmah')
print(A)
print(A.pop()) #this prints any one element from set
A.pop()
print(A) #this print the set after removing anyone element from set
A.discard('S') # this removes the element u want to remove from the set
print(A)


#Booleans operators: True/False: True is correct & taken as boolean operator but 'true' is taken as variable

print(1>2)
print(5<10)
print(type(True))
#print(Type(false)) # taken false as var, shows error on running

# Packing of Tuple:
Tuple1= ('Mayu', 'Nabi', 'Naba')
Tuple2= (1,2,3,4,5)
Tuple3= (1,3,5,7)
print(Tuple1)
print(Tuple2[1:3]) #Slicing of Tuple
# Comparing Tuples: each element is compared st to 1st if its equal, goes to next 2nd to 2nd element comparison
if Tuple2>Tuple3:
    print(Tuple2)
else:
    print(Tuple3) #here1=1, 3>2 so prints tuple3

#unpacking tuple
x=('Mayuri', 'Sarmah', 'Sumpy')
print(*x)
