#for in string, list, tuple, dict, even_odd, sum of num in list:

my_name= 'Mayuri'
for _ in my_name:
    print(_)

my_list= [1,2,3,4,5,6,7,8,9,10]
for x in my_list:
    if x%2==0:
        print(f'{x} is an even number')
    else:
        print(f'{x} is an odd number')

list2=[10,20,30,40,50]
for sum in list2:
    x=0
    sum= sum+x
print(sum) #notice the identation; prints only the last result of the iteration


list2=[10,20,30,40,50]
for sum in list2:
    x=0
    sum= sum+x
    print(sum) #notice the identation

list2=[10,20,30,40,50]
sum = 0
for x in list2:
    sum= sum+x
    print(sum) #notice the identation

ist2=[10,20,30,40,50]
sum = 0
for x in list2:
    sum= sum+x
print(sum) #notice the identation; prints only the last result of the iteration

#tuple unpacking using For loop:

tup= [(1,2),(3,4),(5,6),(7,8)]
for x in tup:
    print(x)
for (a,b) in tup:
    print(a)
    print(b)


dict= {'k1':'v1', 'k2':'v2', 'k3': 'v3'}
for y in dict:
    print(y) # prints only keys

dict= {'k1':'v1', 'k2':'v2', 'k3': 'v3'}
for y in dict.items():
    print(y) # prints keys & values on using .items

dict= {'k1':'v1', 'k2':'v2', 'k3': 'v3'}
for y,z in dict.items():
    print(y)
    print(z)

dict= {'k1':'v1', 'k2':'v2', 'k3': 'v3'}
for y in dict.keys(): #prints only keys
    print(y)

dict= {'k1':'v1', 'k2':'v2', 'k3': 'v3'}
for y in dict.values(): #prints only values
    print(y)




