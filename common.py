""" Common module
implement commonly used functions here
"""

import random



def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''

    special_characters = '#&'
    letters_lower = 'abcdefghijklmnopqrstuvwxyz'
    letters_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'

    random_lower = [''.join(random.choice(letters_lower)) for x in range(1)]
    random_upper = [''.join(random.choice(letters_upper)) for x in range(1)]
    random_numbers = [''.join(random.choice(numbers)) for x in range(2)]
    generated = random_lower + random_upper + random_numbers + random_upper + random_lower
    generated = ''.join(generated) + special_characters

    return generated
