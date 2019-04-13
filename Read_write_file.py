file_name = open('sample.txt', 'w') #sample.txt is file name in text extension, file_name is simply a file object
file_name.write('I am Mayuri Sarmah.\nI am working in IBM.\n')
file_name.write('I studied in Assam Engineering College')
file_name.close() #to save memory

#open means basically preparing a file

file_name = open('sample.txt', 'r')
any_variable = file_name.read()
print(any_variable)
file_name.close()

file_name = open('sample.txt', 'a') #'a' to append lines
file_name.write('\nI was in ETE dept')
file_name.close()


file_name = open('sample.txt', 'r')
any_variable = file_name.read() #used var to store in it the read file
file_name.readlines()
print(any_variable)
file_name.seek(0) #seek used to move the cursor to zero pos, you cant read a file twice at a time, so cursor is moved
print(file_name.readlines())
file_name.seek(0)
print(file_name.readline())
file_name.close()

file_name = open('sample.txt', 'r+')
file_name.write('\nETE means Electronics & Telecommunication Engg')
text= file_name.read()
print(text)
file_name.close()



#different modes: r, w, a, r+, w+

