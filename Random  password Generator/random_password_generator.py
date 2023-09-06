'''Create a Python script that generates
strong and random passwords for various applications, such as online accounts,
security keys, or user authentication. The script should allow users to customize the password criteria.
The password should be stored in a text file for now'''
import os.path

'''Future Notes:
The password file should be encrypted
The file should be updated in git automatically'''


import random
import string
import datetime

def random_password_generator(length = 8 , uppercase=True, lowercase = 'True', special_char = 'True', number_digits = 'True', purpose =''):
    characters = ''
    print("upeecase" + str(uppercase))
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if special_char:
        characters += string.punctuation
    if number_digits:
        characters += string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    dictionary[purpose] = password

    if(os.path.isfile("purpose_pwd.txt")):
        file = open("purpose_pwd.txt", "a")
        file.write("\n")
        file.write(purpose + "password:  " + password + "  " + str(datetime.date.today()))
        file.close()
        print(dictionary)
    else:
        file = open("purpose_pwd.txt","w")
        file.write(purpose + "password:  " + password + "  " + str(datetime.date.today()))
        file.close()
        print(dictionary)




if __name__ == '__main__':

    purpose = input("Enter the password generated for which purpose").strip()
    if len(purpose) == 0:
        print("Purpose is mandatory")

    dictionary = dict()

    print("Password choosen is for" + purpose)

    print("Choose the customisations required for the password")
    uppercase = (input("Choose uppercase is needed yes/no").strip()).lower() == "yes"
    lowercase = (input("Choose uppercase is needed yes/no").strip()).lower() == "yes"
    special_char = (input("Choose uppercase is needed yes/no").strip()).lower() == "yes"
    number_digits = (input("Choose uppercase is needed yes/no").strip()).lower() == "yes"
    length = int(input("enter the length needed for the password"))
    random_password_generator(length,uppercase,lowercase,special_char,number_digits,purpose)









