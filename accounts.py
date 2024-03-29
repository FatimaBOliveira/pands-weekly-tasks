# Accounts
# Program that shows only the last 4 digits of the bank account number
# Author: Fatima Oliveira

accountnumber = "1234567890" # We need to treat the numbers as strings so we can use the replace() function.
print ((f"Please enter an 10 digit account number: ") + str(accountnumber))
print (accountnumber.replace("123456", "XXXXXX")) # https://www.w3schools.com/python/ref_string_replace.asp


## EXTRA: Modify the program to deal with account numbers of any length

# To use present any bank number with only the last 4 digits showing, I will request the client to write the first numbers and the last 4 numbers apart, so I can use the "replace" function for the final presentation of the number.
accountnumberA = str(int(input("Please enter the first numbers of your account: ")))
a = (accountnumberA.replace(accountnumberA, "XXXXXX"))
accountnumberB = int(input("Please enter the last 4 numbers of your account: "))

print (f"{a}{accountnumberB}")