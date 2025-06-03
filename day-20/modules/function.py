FILEPATH = "../file/book.txt"
def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        return file.readlines()

def write_todos(todos, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos)
