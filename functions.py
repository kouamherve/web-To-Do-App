FILEPATH = "toDo.txt"


def get_todolist(filepath=FILEPATH):
    """Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todolist_local = file_local.readlines()
    return todolist_local


def write_todolist(todolist_local, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todolist_local)


if __name__ == "__main__":
    print("hello")
    print(get_todolist())
