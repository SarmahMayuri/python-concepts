#Assessment on try,except,else & finally:
#Prob1: handle exception thrown by type error

try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print('Input given is not integer to get a result')

finally:
    print('Try again!')

#Prob2: Print finally 'All done' after handling exception:

try:
    x= 5
    y= 'May'
    z= x/y


except ZeroDivisionError:
    print('Denominator cannot be a zero')

except:
    print('Check the numbers given are correct!')

else:
    print(f'The division result is {z}')

finally:
    print('All done')


#Prob3: Define a function. asks an integer print square of it, use while loop with try,except,else

def find_sqr():

    while True:
        try:
            num=int(input('Give a number to find its square: '))
        except:
            print('Check the number given is correct')
            continue
        else:
            print(f'The square of {num} is {num**2}')
            break

find_sqr()





