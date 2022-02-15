""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


ID = 0
MONTH = 1
DAY = 2
YEAR = 3
TYPE = 4
AMOUNT = 5
title_list = ["Id", "Month", "Day", "Year", "Type", "Amount"]


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    file_name = "accounting/items.csv"
    table = data_manager.get_table_from_file(file_name)

    options = ["Display a table",
               "Add new record",
               "Remove record",
               "Update record",
               "Show the year with the highest profit",
               "Show the the average (per item) profit in a given year"]

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
                which_year_max(table)
                continue
            elif option == "6":
                avg_amount(table, year=ui.get_inputs(["Please enter: "], title_list[YEAR]))
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

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    years_list = list()
    years = set()
    years_profit = dict()
    for line in table:
        years_list.append(line[YEAR])
        years.add(line[YEAR])
    for year in years:
        profit_in = list()
        profit_out = list()
        for line in table:
            if year == line[YEAR]:
                if "in" == line[TYPE]:
                    profit_in.append(line[AMOUNT])
                else:
                    profit_out.append(line[AMOUNT])
        sum_of_profit_in = 0
        sum_of_profit_out = 0
        for amount in profit_in:
            sum_of_profit_in += int(amount)
        for amount in profit_out:
            sum_of_profit_out += int(amount)
        profit = sum_of_profit_in - sum_of_profit_out
        years_profit[year] = profit
    profit_years = list()
    profit_amount = list()
    for year in years_profit:
        profit_years.append(year)
        profit_amount.append(years_profit[year])
    max_profit = common.max(profit_amount)
    index = 0
    for i in range(len(profit_amount)):
        if max_profit == profit_amount[i]:
            index = i

    label = 'Year of the highest profit'
    ui.print_result(profit_years[index], label)
    year_max = profit_years[index]
    return int(year_max)


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # year = year[0]
    profit_in = list()
    profit_out = list()
    for line in table:
        if str(year) == line[YEAR]:
            if "in" == line[TYPE]:
                profit_in.append(line[AMOUNT])
            else:
                profit_out.append(line[AMOUNT])
    sum_of_profit_in = 0
    sum_of_profit_out = 0
    for amount in profit_in:
        sum_of_profit_in += int(amount)
    for amount in profit_out:
        sum_of_profit_out += int(amount)
    profit = sum_of_profit_in - sum_of_profit_out
    avg_profit = profit / (len(profit_in) + len(profit_out))

    label = f'Average (per item) profit in a {year}'
    ui.print_result(avg_profit, label)
    return avg_profit
