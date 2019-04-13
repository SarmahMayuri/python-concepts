#While loop; break, continue & pass keywords
#we can use a else statement with a while loop

x=0
while x<=5:
     print(x)
     x+=1
else:
    print('The number exceeds 5')

#break, continue & pass keywords:
#continue:
list1= [1,2,3,4,5,6,7,8,9]
for x in list1:
    if x%2==1:
        continue
    else:
        print(x)


#break:
list1= [1,2,3,4,5,6,7,8,9]
for x in list1:
    if x==6:
        break
    print(x)

x=0
while x<=5:
     if x==3:
         break
     print(x)
     x+=1

#pass:
list2=[1,2,3,4,5]
for a in list2:
    pass
print('Nothing to print!')


