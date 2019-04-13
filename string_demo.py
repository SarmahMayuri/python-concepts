var1 = "Tutorial!"
var2 = "Software Testing"
# slicing variable from a string
print (var1[0]+ ' Mayuri') # adding a string
print (var2[1:5])

# replace a string
oldstring= 'I am sleeping'
oldstring= oldstring.replace('am', 'was')
print(oldstring)

#join a string
x= 'Python'
print(':'.join(x))

# upper & lower case
x= 'mayuri'
print(x.upper())
print(x.capitalize())
y= 'MAYURI'
print(y.lower())

#reverse string
z= 'ABCDEF'
print(''.join(reversed(z)))

#split
word= 'Mayuri Sarmah Mayuri'
print(word.split()) # string to List
print(word.split('r')) # split when letter r appears in the string

#String Properties: UDEMY
a= 'Mayuri Sarmah'
# Indexing
print(a[-1])
#Slicing
print(a[4:9])
print(a.upper())
print(a.capitalize())

#Spliting a string: Turns a string to LIST
print(a.split())
#->only split() is spacing split, so in every space of a string it splits
print(a.split('r'))
#->split(r) will split at letter r, so in every space of a string it splits

# a is a string object, so when u put a then give 'a dot(.)' next to 'a', we can see all methods applicable to string

#FORMATTING STRING & FLOATS:
#1st .format()...older version
#2nd  f-strings method- newer version, used in other language
#% placeholder technique

b= 0.123456
#float formatting: (value:width.'precision'f)
# .format is not supported
'''
print("The number is {b:2.3f}".format(b))
'''
# f- strings supported
print(f"The number is {b:2.3f}")

#second example:
'''
print('{0} is {1} years old'.format('Mayuri', '29'))
'''
# curly position gives index position, & if u dont give index position it takes 0 index in 1st position & 1 index in 2nd

age= 29
name= 'Mayuri'
print(f'{name} is {age} years old')

x,y= 'Sona', 6
print(f'{y} is age of {x}')

#3rd eg:

print('Hi, my name is %s,age is %d & my graduation percentage is %5.2f' %('Mayuri',29,71.45678))

a= 'Sumpy Sarmah'
print(a.endswith('mah'))