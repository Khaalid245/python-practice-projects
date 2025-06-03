from os import remove
from pyexpat.errors import messages  # Note: This import is not used, can be removed

while True:
    user_action = input("Type: add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # ADD: Add a new todo item to the list
    if 'add'  in user_action:
        todo = user_action [4:] # Extract the todo after 'add '

        # Read existing todos
        with open('file/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo+ '\n')  # Add new item with newline

        # Write updated todos back to file
        with open("file/todos.txt", 'w') as file:
            file.writelines(todos)

    # SHOW: Display all todo items
    elif 'show' in user_action:
        with open('file/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')  # Remove newline character
            row = f'{index + 1} - {item}'
            print(row)

    # EDIT: Edit an existing todo item by index
    elif 'edit' in user_action:
        number = int(user_action[5:])
        print(number)

        number = number -1

        with open('file/todos.txt', 'r') as file:
            todos = file.readlines()

        new_item = input("Enter the new item: ")
        todos[number] = new_item + '\n'  # Replace item with new content

        with open("file/todos.txt", 'w') as file:
            file.writelines(todos)

    # COMPLETE: Remove a completed todo item
    elif 'complete' in user_action:
        number = int(user_action[9:])
        index = number - 1

        # Read current todos
        with open('file/todos.txt', 'r') as file:
            todos = file.readlines()

        todo_to_remove = todos[index]
        print(f"Todo '{todo_to_remove.strip()}' was removed from the list.")

        # Remove item
        todos.pop(index)

        # Write back updated list
        with open('file/todos.txt', 'w') as file:
            file.writelines(todos)

    # EXIT: Quit the program
    elif 'exit' in user_action:
        break

print('Bye')
