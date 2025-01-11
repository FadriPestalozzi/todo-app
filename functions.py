FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return a list of items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the todo items list in the text file """
    with open(filepath, 'w') as file_Local:
        file_Local.writelines(todos_arg)


if __name__ == "__main__":
    print("script", __name__, "was run directly")