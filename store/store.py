""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


title_list = ["Id", "Title", "Manufacturer", "Price", "In stock"]


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    table = data_manager.get_table_from_file("store/games.csv")

    options = ["Display a table",
               "Add new record",
               "Remove record",
               "Update record",
               "Show how many different kinds of game are available of each manufacturer",
               "Show the average amount of games in stock of a given manufacturer"]


    while True:
        try:
            ui.print_menu("Store Manager", options, "Back to main menu")
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                show_table(table)
                continue
            elif option == "2":
                add(table)
                continue
            elif option == "3":
                remove(table, id_=ui.get_inputs(["Please enter: "], title_list[0]))
                continue
            elif option == "4":
                update(table, id_)
                continue
            elif option == "5":
                get_counts_by_manufacturers(table)
                continue
            elif option == "6":
                get_average_by_manufacturer(table, manufacturer)
                continue
            elif option == "0":
                break
            else:
                raise KeyError("There is no such option.")
                continue
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
    line = []
    id_ = common.generate_random(table)
    line.append(id_)
    for title in title_list[1:]:
        user_input = ui.get_inputs(["Please enter: "], title)
        line.append(''.join(user_input))
    table.append(line)

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

    id_ = ''.join(id_)
    for line in table:
        if id_ == line[0]:
            del table[table.index(line)]
            break

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
