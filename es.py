# Es
# Program that reads text file and outputs number of e's it contains.
# Will also show how to deal with errors such as no argument, non existing files and opening files that are not txt files.
# Author: Faitima Oliveira

# A txt file needs to exist in order to Python read and count the number of e's of a file. 
# The following code will create a new txt file so we can run MAIN program.
FILENAME = "moby-dick.txt"
with open(FILENAME, "w") as f: # The "w" will create a new file with name "moby-dick.txt". 
    f.write("116960\n")
    f.close()
# https://www.w3schools.com/python/python_file_write.asp
    
def my_function(FILENAME):
    f = open(FILENAME, "rt")
    print(f.read())
my_function(FILENAME)
# This argument will print out the contents of the txt file.
# https://realpython.com/python-command-line-arguments/#file-handling
# https://www.w3schools.com/python/gloss_python_function_arguments.asp

# MAIN
def letterFrequency(FILENAME, letter):
    f = open(FILENAME, 'r')
    text = f.read() # store content of the file in a variable
    return text.count(letter)
print(letterFrequency(FILENAME, 'e')) # call the function and display the letter count

# https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# https://realpython.com/python-counter/#putting-counter-into-action

#-------------------------------------------------------------------------------------------------------------------------------------


    ## ERROR - NO ARGUMENT
FILENAME2 = "moby-dick2.txt" 

f = open(FILENAME2, "rt")
print(f.read())
f.close()
# There's no argument, nothing will be printed out because there's nothing written in text file.


    ## ERROR - FILENAME DOES NOT EXIST:
FILENAME3 = "moby-dick3.txt"
'''
f = open(FILENAME3, "rt")
print(f.read())
f.close()
# Will give error because moby-dick2.txt doesn't exist, so it can't read it.
# https://www.w3schools.com/python/python_file_handling.asp
'''


    ## ERROR - IS NOT A TXT FILE

FILENAME4 = "Python-logo.png" # Image taken from: https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/64px-Python-logo-notext.svg.png
'''
f = open(FILENAME4, "r")
print(f.read())
f.close()
# Will give error because file is a image, not a text file. To read image, need to write rb instead of only r.
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.tutorialsteacher.com/python/python-read-write-file
'''

# Python can show images through many ways and Pillow library is one of them.
# https://realpython.com/image-processing-with-the-python-pillow-library/
from PIL import Image
with Image.open(FILENAME4) as img:
    img.load()
    img.show() # This will open the image in a program that shows images like Photos app, depending on the computer.