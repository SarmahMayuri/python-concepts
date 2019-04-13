#Map: used for iterable objects
my_list= ['Mayuri', 'Maina', 'Sumpy']
def check(my_str):
    if len(my_str)%2==0:
        return (my_str)
    else:
        return my_str[0]
#Result output:
print(list(map(check,my_list)))
#OR
print(tuple(map(check,my_list)))
#OR
for items in map(check,my_list):
    print(items)

#Another eg:
def cube(nums):
    return nums**3

def is_even(num):
    if num%2==0:
        return num

my_num= [1,2,3,4,5,6]

print(list(map(cube,my_num)))
print(list(filter(is_even,my_num)))

#Lambda:
print(list(map(lambda n: n**2, my_num)))
print(list(filter(lambda n: n%2!=0, my_num)))
