#Dictionary-
# Holds key, value pair in {} i.e Dict= {'Key1': Value1, 'Key2': value2}
# Key is string, value can be any(eg: int,str,float, list, other dictionary
# Dictionary are flexible in holding any datatypes(in value field), Key is name & always taken as string:

Dict1= {'Name_str': 'Mayuri', 'Age_int': 29, 'Percentage_float': 71.23, 'List':['a', 'b', 'c'], 'Dict':{'K1':'V1'}}
print(Dict1)
print(Dict1['Name_str'])
print(Dict1['List'][2])
print(Dict1['Dict']['K1'])

#We can use functions of a list for the list-key we have in our dictionary:
print(Dict1['List'][1].upper())

# We can add new Key:Value pair in dictionary:
Dict1['College']= 'AEC' # gets added at end, so to remove/pop we use popitem it removes last item by default
print(Dict1)
help(Dict1.get)

#We can override Key:
Dict1['Age_int']= 28
print(Dict1)

#Other methods that we use in Dictionary:

print(Dict1.keys())
print(Dict1.values())
print(Dict1.items()) #The o/p derived is all key:value pair in the dictionary written in () inside the []

print(Dict1.popitem()) #pop out last key value
print(Dict1) #printing after popped