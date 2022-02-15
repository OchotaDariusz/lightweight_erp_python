""" Common module
implement commonly used functions here
"""

import random
import ui


ID = 0


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

    for line in table:
        if generated == line[ID]:
            generated = generate_random(table)
            continue

    return generated


def add_item(table, title_list):
    new_line = []
    id_ = generate_random(table)
    for line in table:
        if id_ == line[ID]:
            id_ = generate_random(table)
            continue
    new_line.append(id_)
    for title in title_list[1:]:
        user_input = ui.get_inputs(["Please enter: "], title)
        new_line.append(''.join(user_input))
    table.append(new_line)

    return table


def remove_item(table, id_):
    id_ = ''.join(id_)
    line_counter = 0
    for line in table:
        if id_ == line[ID]:
            del table[line_counter]
            break
        line_counter += 1

    return table


def update_item(table, title_list, id_):
    new_line = []
    id_ = ''.join(id_)
    new_line.append(id_)
    line_counter = 0
    for line in table:
        if id_ == line[ID]:
            index_to_update = line_counter
            del table[index_to_update]
            for title in title_list[1:]:
                user_input = ui.get_inputs(["Please enter: "], title)
                new_line.append(''.join(user_input))
            if index_to_update <= len(table):
                table.append(new_line)
            else:
                table[index_to_update] = new_line
            break
        line_counter += 1

    return table


def oldest_year(values_list):
    max_index = values_list[0]
    for item in values_list:
        if item < max_index:
            max_index = item
    return max_index
