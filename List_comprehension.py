#UDEMY: list comprehension
#eg1:
my_str= 'Mayuri'
my_list= []
for x in my_str:
    my_list.append(x)
print(my_list)

#OR:
my_list2= [x for x in 'Sameer']
print(my_list2)

#Eg2:
my_list2= [x for x in range(0,101) if x%2==0]
print(my_list2)

#eg3:
my_list3= [(x**2) for x in range (0,11)]
print(my_list3)

#eg4: #if else the format is different
my_list4= [x if x%2==0 else 'ODD number it is!' for x in range(0,11)]
print(my_list4)

#eg5: #nested
my_list5= []
for x in [1,2,3]:
    for y in[1,10,100]:
        my_list5.append(x*y)
print(my_list5)

#or,

my_list6= [(x*y) for x in [1,2,3] for y in [1,10,100]]
print(my_list6)
