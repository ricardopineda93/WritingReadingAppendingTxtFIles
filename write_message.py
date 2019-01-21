filename = 'text_files/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write(str(input('What is your name?: ') + '\n'))
    file_object.write('This is your file.\n')


with open(filename) as file_object:
    contents = file_object.read()
    print(contents)


with open(filename, 'w') as file_object: #if I call to open and write again as the same file,
    #it deletes the original contents and overwrites.
    file_object.write('Sorry, this is not your file any more. I used the write method over it so now this is what it is.\n')


with open(filename) as file_object: #just reading the current contents of the file.
    contents = file_object.read()
    print(contents)



with open(filename, 'a') as file_object: #we want to use the 'a' append functionality to add new lines to the bottom of our existing file.
    file_object.write('Actually, it turns out we can share.\n')
    file_object.write('We can opt to append to text files rather than overwrite.\n')
    file_object.write('This is now OUR file! ')


with open(filename) as file_object:
    contents = file_object.read()
    print(contents)