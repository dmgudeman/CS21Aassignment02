# -----------------------------------------------------------------------------
# Name:        translate
# Purpose:     assignment # 2
#
# Author:
# Date:
# -----------------------------------------------------------------------------
"""
Enter your docstring with a one-line overview here

and a more detailed description here.
"""


def starts_with_vowel(word):
    """
    return True if the word starts with a vowel and False otherwise
    """
    first = word[:1]
    if first in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


def encode(word):
    """
    # translate a single word to the secret language
    # call starts with vowel to decide which pattern to follow
    """
    if starts_with_vowel(word):
        word = word + 'way'
        return word
    else:
        word = word[1:] + word[:1] + 'ar'
        return word

def translate(message) -> object:
    """
    # translate the whole text to the secret language
    # call encode to translate individual words in text
    :rtype : object
    """
    encoded_string = ''
    messagesplit = message.split()
    for word in messagesplit:
        encoded_word = encode(word)
        encoded_string = encoded_string + ' ' + encoded_word
    print('The secret message is:' + encoded_string)

def get_input():
    """
    Obtain the input from the user

    :rtype : object
    """
    # prompt the user for input until they enter a non-empty string
    # return the string entered by the user
    #

    message = str(input('Please enter your message:'))
    while message == "":
        message = str(input('Please enter your message:'))

    return message
def main():
    """
    # get input and save it in a variable
    # translate the saved input by calling translate - save result
    # print the result
    """
    words = get_input()
    translate(words)


if __name__ == '__main__':
    main()
