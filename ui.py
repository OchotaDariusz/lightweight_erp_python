""" User Interface (UI) module """




def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print("\n")
    if len(title_list) == 3:
        print("{:<10} {:<30} {:<8}".format(*title_list))
        for line in table:
            print("{:<10} {:<30} {:<8}".format(*line))
    # title_list wrzuć w table[0] - dodaj do tabeli poprzez insert()
    # znajdz max(len()) z wartosci tabeli i to jako szerokość

    if len(title_list) == 4:
        print("{:<10} {:<30} {:<35} {:<10}".format(*title_list))
        for line in table:
            print("{:<10} {:<30} {:35} {:<10}".format(*line))

    if len(title_list) == 5:
        print("{:<10} {:<40} {:<40} {:<15} {:<15}".format(*title_list))
        for line in table:
            print("{:<10} {:<40} {:40} {:<15} {:<15}".format(*line))

    if len(title_list) == 6:
        print("{:<10} {:<40} {:<10} {:<10} {:<10} {:<15}".format(*title_list))
        for line in table:
            print("{:<10} {:<40} {:<10} {:<10} {:<10} {:<15}".format(*line))


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print("\n")
    print(label)
    if isinstance(result, dict):
        for key, value in result.items():
            print(str(key) + ': ' + str(value))
    if isinstance(result, list):
        for item in result:
            print(str(item))
    if isinstance(result, set):
        for item in result:
            print(str(item))
    if isinstance(result, tuple):
        for item in result:
            print(str(item))
    if isinstance(result, str):
        print(result)
    if isinstance(result, int):
        print(result)
    if isinstance(result, float):
        print(result)


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print("\n" + title)
    counter = 0
    for option in list_options:
        counter += 1
        print(f"({counter})", option)
    print("(0)", exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    for label in list_labels:
        user_input = input(label + '\n' + f'{title} ')
        inputs.append(user_input)

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print("ERROR: " + message)
