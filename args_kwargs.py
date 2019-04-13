#UDEMY: *args & **kwargs
# (*args) means arguments, u can take any number of argument, 'args' can be named anything, important is *
#(**kwargs) means keyword arguments,** defines kwargs, but kwarg can be renamed any
# *args return in form of TUPLE & **kwargs return in the form of DICTIONARY

def my_func1(*args):
    print(args)
my_func1(1,2,3,4,5)

def my_func2(**kwargs):
    print(kwargs)
my_func2(name= 'Sameer', midname='Paran', surname='Sarmah')

def my_func3(*args):
    for items in args:
        print(items)
my_func3('Mayuri', 'Sumpy', 'Maina')


# we can combine args, kwargs:
def my_func4(*args, **kwargs):

        print(args[0])
        name = kwargs.get('name') # get func gives the value of the key
        qualification = kwargs.get('qualification')
        College = kwargs.get('College')
        print(f"name is {name},qualification is {qualification},College is {College}")

my_func4(28,29,20, name='Mayuri', qualification= 'B.E', College= 'AEC')

#OR:

def my_func4(*args, **kwargs):
    print(f"I am {args[1]} and my name is {kwargs['name']}")
my_func4(28,29,20, name='Mayuri', qualification= 'B.E', College= 'AEC')




def func5(**kwargs):
    print(f"I m {kwargs['name']}, and I work in {kwargs['Org']}")
func5(name= 'Mayuri', Org= 'IBM')
