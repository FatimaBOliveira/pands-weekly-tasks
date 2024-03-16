# Es
# Program that reads text file and outputs number of e's it contains.
# I will also show how to deal with errors such as no argument, non existing files and opening files that are not txt files.
# Author: Faitima Oliveira


from urllib.request import urlretrieve
url = (
    "https://www.gutenberg.org/files/2701/old/moby10b.txt"
)
FILENAME = "moby-dick.txt"
urlretrieve(url, FILENAME)
# It will donwload the Moby Dick book as txt file from the URL mentioned above.
# https://realpython.com/python-download-file-from-url/#using-urllib-from-the-standard-library

def letterFrequency(FILENAME, letter):
    f = open(FILENAME, 'r')
    text = f.read()
    return text.count(letter)
print(letterFrequency(FILENAME, 'e')) 
# It will read the txt file and display the count of the letter "e".
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
# It will give an error because moby-dick3.txt doesn't exist, so it can't read it. If the file doesn't exist and I want to create one, I can use "w", "a" or "x".
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

# There's better ways to show images through Python command. We can do it in many ways, and Pillow library is one of them.
# https://realpython.com/image-processing-with-the-python-pillow-library/
'''
from PIL import Image
with Image.open(FILENAME4) as img:
    img.show() 
'''
# This will open the image in a program that shows images like Photos app, depending on the apps that are installed in the computer.