""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


ID = 0
NAME = 1
BIRTH_YEAR = 2
title_list = ["Id", "Name", "Birth Year"]


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    file_name = "hr/persons.csv"
    table = data_manager.get_table_from_file(file_name)

    options = ["Display a table",
               "Add new record",
               "Remove record",
               "Update record",
               "Show the oldest person",
               "Show the closest to the average age"]

    while True:
        try:
            ui.print_menu("Human resources manager", options, "Back to main menu")
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                show_table(table)
                continue
            elif option == "2":
                add(table)
                data_manager.write_table_to_file(file_name, table)
                continue
            elif option == "3":
                remove(table, id_=ui.get_inputs(["Please enter: "], title_list[ID]))
                data_manager.write_table_to_file(file_name, table)
                continue
            elif option == "4":
                update(table, id_=ui.get_inputs(["Please enter: "], title_list[ID]))
                data_manager.write_table_to_file(file_name, table)
                continue
            elif option == "5":
                get_oldest_person(table)
                continue
            elif option == "6":
                get_persons_closest_to_average(table)
                continue
            elif option == "0":
                break
            else:
                raise KeyError("There is no such option.")
        except KeyError as err:
            ui.print_error_message(str(err))


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    global title_list
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    global title_list
    table = common.add_item(table, title_list)

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    table = common.remove_item(table, id_)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    global title_list
    table = common.update_item(table, title_list, id_)

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    # for line in table:
    #     max_index = line[BIRTH_YEAR]
    #     for year in line:
    #         if year > max_index:
    #             max_index = year
    birth_year_list = list()
    oldest_persons = list()
    for line in table:
        birth_year_list.append(line[BIRTH_YEAR])
    oldest_year = common.oldest_year(birth_year_list)
    for line in table:
        if oldest_year == line[BIRTH_YEAR]:
            oldest_persons.append(line[NAME])
    label = 'Oldest (person/persons) (is/are)'
    ui.print_result(oldest_persons, label)
    return oldest_persons


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    birth_year_list = list()
    sum_of_years = 0
    person_closest_to_avarage = list()
    for line in table:
        birth_year_list.append(line[BIRTH_YEAR])
    for year in birth_year_list:
        sum_of_years += int(year)
    average_birth_year = sum_of_years // len(birth_year_list)
    for line in table:
        if str(average_birth_year - 1) == line[BIRTH_YEAR] or str(average_birth_year + 1) == line[BIRTH_YEAR]:
            person_closest_to_avarage.append(line[NAME])
    label = '(Person/persons) closest to the average age (is/are)'
    ui.print_result(person_closest_to_avarage, label)
    return person_closest_to_avarage
