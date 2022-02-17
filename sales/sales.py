""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


ID = 0
TITLE = 1
PRICE = 2
MONTH = 3
DAY = 4
YEAR = 5
title_list = ["Id", "Title", "Price", "Month", "Day", "Year"]


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    file_name = "sales/sales.csv"
    table = data_manager.get_table_from_file(file_name)
    options = ["Display a table",
               "Add new record",
               "Remove record",
               "Update record",
               "Show the id of the item that was sold for the lowest price",
               "Show the items that are sold between two given dates"]
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
                get_lowest_price_item_id(table)
                continue
            elif option == "6":
                get_items_sold_between(
                    table,
                    month_from=int(ui.get_inputs(["Please enter: "], title_list[MONTH])[0]),
                    day_from=int(ui.get_inputs(["Please enter: "], title_list[DAY])[0]),
                    year_from=int(ui.get_inputs(["Please enter: "], title_list[YEAR])[0]),
                    month_to=int(ui.get_inputs(["Please enter: "], title_list[MONTH])[0]),
                    day_to=int(ui.get_inputs(["Please enter: "], title_list[DAY])[0]),
                    year_to=int(ui.get_inputs(["Please enter: "], title_list[YEAR])[0])
                )
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

    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

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

    table = common.update_item(table, title_list, id_)

    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    prices_list = list()
    for line in table:
        prices_list.append(line[PRICE])
    lowest_price = common.min(prices_list)
    for line in table:
        if lowest_price == line[PRICE]:
            id_ = line[ID]
            break
    label = 'ID of the item that was sold for the lowest price'
    ui.print_result(id_, label)
    return id_


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    filtered_list = list()
    timestamp_from = (month_from * 2629743) + (day_from * 86400) + (year_from * 31556926)
    timestamp_to = (month_to * 2629743) + (day_to * 86400) + (year_to * 31556926)
    for line in table:
        table_timestamp = (int(line[MONTH]) * 2629743) + (int(line[DAY]) * 86400) + (int(line[YEAR]) * 31556926)
        if timestamp_from < table_timestamp < timestamp_to:
            filtered_list.append(line)
    for value in filtered_list:
        value[PRICE] = int(value[PRICE])
        value[MONTH] = int(value[MONTH])
        value[DAY] = int(value[DAY])
        value[YEAR] = int(value[YEAR])
    label = 'Items sold between two given dates'
    ui.print_result(filtered_list, label)
    return filtered_list
