# Es
# Program that reads text file and outputs number of e's it contains.
# I will also show how to deal with errors such as no argument, non existing files and opening files that are not txt files.
# Author: Faitima Oliveira

# I will donwload the Moby Dick book as TXT file from the followig URL: https://www.gutenberg.org/files/2701/old/moby10b.txt
# https://realpython.com/python-download-file-from-url/#using-urllib-from-the-standard-library

from urllib.request import urlretrieve
url = (
    "https://www.gutenberg.org/files/2701/old/moby10b.txt"
)
FILENAME = "moby-dick.txt"
urlretrieve(url, FILENAME)

# MAIN
def letterFrequency(FILENAME, letter):
    f = open(FILENAME, 'r')
    text = f.read() # store content of the file in a variable
    return text.count(letter)
print(letterFrequency(FILENAME, 'e')) # call the function and display the letter count
# https://realpython.com/python-command-line-arguments/#file-handling
# https://www.w3schools.com/python/gloss_python_function_arguments.asp
# https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# https://realpython.com/python-counter/#putting-counter-into-action

#-------------------------------------------------------------------------------------------------------------------------------------


    ## ERROR - NO ARGUMENT

# I'll create a blank txt file and then use reading function.
# https://www.geeksforgeeks.org/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function/
'''
FILENAME2 = "moby-dick2.txt" 
with open(FILENAME2, "w+") as f: # The "w+" will create a new file with name "moby-dick2.txt" and then read it. 
    f.write("")
    print(f.read())
    f.close()
'''
# There's no argument, nothing will be printed out because there's nothing written in text file.

    ## ERROR - FILENAME DOES NOT EXIST:

'''
FILENAME3 = "moby-dick3.txt"
f = open(FILENAME3, "rt")
print(f.read())
f.close()
'''
# Will give error because moby-dick3.txt doesn't exist, so it can't read it.
# https://www.w3schools.com/python/python_file_handling.asp

    ## ERROR - IS NOT A TXT FILE

# I will download a file from following URL, that's not a txt file, it's an image.
'''
url2 = (
    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/64px-Python-logo-notext.svg.png"
)
FILENAME4 = "Python-logo.png"
urlretrieve(url2, FILENAME4)
'''
# Now let's use the read function for the image downloaded.
'''
f = open(FILENAME4, "r")
print(f.read())
f.close()
'''
# It will give error because file is an image, not a text file. To read image, I need to write rb instead of only r.
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.tutorialsteacher.com/python/python-read-write-file

# We can show images through Python command. There's many ways to do it, and Pillow library is one of them.
# https://realpython.com/image-processing-with-the-python-pillow-library/
'''
from PIL import Image
with Image.open(FILENAME4) as img:
    img.show() 
'''
# This will open the image in a program that shows images like Photos app, depending on the computer.