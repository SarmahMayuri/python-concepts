while True:
    try:
        number = int(input('Give one number:'))
        print(18/number)
        break
# if we not use break, we can input more numbers to use the try clause
    except ValueError:
        print('Only number accepted')
# valueerror is one type of exception
    except:
        break
#if other kind of exception occurs, the loop will be ended
    finally:
        print('we are done!')
# finally clause is optional, to mean ended, it is executed no matter what
## for handlind execption we use try, except & finally(optional)

#############################################################################################

def reading_file():
    try:
        file = open("testfile.txt", "r")
        content = file.read()
        print(content)
        file.close()

    except FileNotFoundError:
        raise Exception('No file!')

    except:
        raise Exception('Other errors')

    finally:
        print('I am done!')
try:
    reading_file()
except Exception as error:
    print(error)


#or you can do as below:


def reading_file():
    try:
        file = open("testfile.txt", "r")
        content = file.read()
        print(content)
        file.close()

    except FileNotFoundError:
        print('No file!')

    except:
        print('Other errors')

    finally:
        print('I am done!')

reading_file()




