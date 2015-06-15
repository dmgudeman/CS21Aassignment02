# -----------------------------------------------------------------------------
# Name:         translate
# Purpose:      CS21A assignment 2
#
# Author:       David Gudeman
# Date:         June 15, 2015
# -----------------------------------------------------------------------------
"""
translate a string into a coded string

Takes a string from the user and determines if it starts with a consonant
or a vowel. If it is a vowel it returns the word modified by adding "way"
on the end. If it is a consonant it cuts the first letter off and adds it to
the end and then adds "ar" at the end.  It prints out the modified string.
"""

def starts_with_vowel(word):
    """
    # boolean function to determine if word starts with a vowel
    # parameter: a word
    # returns: True if word starts with a vowel, False otherwise
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
    # if a vowel add "way"
    # if a consenant cut character one, add it to the end then add "ar"
    """
    if starts_with_vowel(word):
        word =+ 'way'
        return word
    else:
        word = word[1:] + word[:1] + 'ar'
        return word

def translate(message):
    """
    # translate the whole text to the secret language
    # call encode to translate individual words in text
    # parameter: message from user input, get_input()
    # returns: displays a translated string
    """
    encoded_string = ''             # declare a variable by assignation
    messagesplit = message.split()  # parse the user input into words
    for word in messagesplit:       # iterate through the list of words
        encoded_word = encode(word) # encode each word
        encoded_string = encoded_string + ' ' + encoded_word # back to a string
    print('The secret message is:' + encoded_string) # provide to user

def get_input():
    """
    # Obtain the input from the user
    # prompt the user for input until they enter a non-empty string
    # return the string entered by the user
    #
    """
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
