"""
This application converts alphanumeric message to morse code.
"""
import re
from morse_code import INTERNATIONAL_MORSE_CODE


def check_message(message):
    """This function checks the validity of the users input."""
    feedback = []
    for char in message:
        if re.match(r'[A-Za-z0-9 ]', char):
            feedback.append(True)
        else:
            feedback.append(False)

    if feedback_check(feedback):
        convert(message)


def feedback_check(feedback_list):
    """This function provides the feedback"""
    if False in feedback_list:
        print('Invalid input included in the message, only alphabets and numbers are allowed.')
        return False
    else:
        return True


def convert(message):
    """This function converts the message."""
    converted_message = ''
    for char in message:
        # Not touching the space between the message
        if char != ' ':
            # adding space to the character
            converted_message += INTERNATIONAL_MORSE_CODE[char] + ' '
        else:
            # Add the hash symbol to replace the space between the words
            converted_message += '# '

    print(converted_message)


# Default displays
print('Inputs should only be alphanumeric (Alphabets and Numbers).')
print('The characters will be separated by a space and words will be separated by the hash symbol (#)\n')
user_input = input('Type your message: \n').upper()
check_message(user_input)
