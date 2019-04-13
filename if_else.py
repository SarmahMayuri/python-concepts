#if,elif, else
#Eg:1
name= 'Mayuri'

if name == 'Mayuri':
    print('Hi Mayuri')
elif name== 'Sameer':
    print('Hi Sameer!')
elif name== 'Nayanita':
    print('Hi Nayanita')
else:
    print('Name not present!')

#Eg: 2
#hungry is set to a boolean value, and since if,else statement search for a T/F condition
#  we don't set hungry again in if statement:
Hungry = True

if Hungry:
    print('I am hungry!')
else:
    print('I am not hungry!')


#Eg: 3: To check num is even/odd:

num=9%2

if num==0:
    print('The number is Even')
else:
    print('The number is Odd!')

