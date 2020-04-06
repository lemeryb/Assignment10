# Assignment10
# Benjamin Lemery
# This program checks if a string is a palindrome and removes any non-alphanumeric characters from the string.

def PalindromeCheck(user_string):

    if len(user_string) < 2:
        return ("The string you entered is a palindrome string.")
    if user_string[0] != user_string[-1]:
        return ("The string you entered is not a palindrome string.")
    else:
         return (PalindromeCheck(user_string[1: -1]))

def purify_string(user_string):
    permitted_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    user_string = "".join(letter for letter in user_string if letter in permitted_characters)
    print('\n' + PalindromeCheck(user_string))
    print("The alphanumeric string is: " + user_string)


while True:
    user_string = input('Enter a string. This program will check if the string is a palindrome.\nEnter a string: ')
    purify_string(user_string)