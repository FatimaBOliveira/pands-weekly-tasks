# Accounts
# Program that shows only the last 4 digits of the bank account number
# Author: Fatima

accountnumber = "1234567890"

print ((f"Please enter an 10 digit account number: ") + str(accountnumber))

#https://www.w3schools.com/python/python_strings_modify.asp

print (accountnumber.replace("123456", "XXXXXX"))


#Extra:Modify the program to deal with account numbers of any length
#   To use present any bank number with only the last 4 digits showing, I will request the client to write the first numbers and the last 4 numbers apart, so I can use the "replace" funcion for the final presentation of the number.

accountnumberA = str(int(input("Please enter the first numbers of your account: ")))
a = (accountnumberA.replace(accountnumberA, "XXXXXX"))
accountnumberB = int(input("Please enter the last 4 numbers of your account: "))

print (f"{a}{accountnumberB}")