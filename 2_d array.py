#in python list is array: where we can have all types of data types unlike in Java, C++
#1-D array
list= [1,2.5,'Mayuri']

#2-D array
list1= [[1,2,3], [4,5,6], [0,9,8]]

for row in list1:
    for column in row:
        print(column, end=' ')
    print()

print('\n')

for row in list1:
    for column in row:
        pass
    print(row)


