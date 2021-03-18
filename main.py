"""
This application converts alphanumerics to morse code.
"""

from morse_code import INTERNATIONAL_MORSE_CODE


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

    return converted_message


# Default displays
print('Inputs should only be alphanumeric (Alphabets and Numbers).')
print('The characters will be separated by a space and words will be separated by the hash symbol (#)\n')
user_input = input('Type your message: \n').upper()
print(convert(user_input))
