while True:
    user_action = input("Type: add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # ADD: Add a new todo item to the list
    if user_action.startswith("add"):
        todo = user_action[4:]  # Extract the todo after 'add '

        # Read existing todos
        with open('file/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')  # Add new item with newline

        # Write updated todos back to file
        with open("file/todos.txt", 'w') as file:
            file.writelines(todos)

    # SHOW: Display all todo items
    elif user_action.startswith("show"):
        with open('file/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')  # Remove newline character
            row = f'{index + 1} - {item}'
            print(row)

    # EDIT: Edit an existing todo item by index
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open('file/todos.txt', 'r') as file:
                todos = file.readlines()

            new_item = input("Enter the new item: ")
            todos[number] = new_item + '\n'  # Replace item with new content

            with open("file/todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    # COMPLETE: Remove a completed todo item
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number - 1

            # Read current todos
            with open('file/todos.txt', 'r') as file:
                todos = file.readlines()

            todo_to_remove = todos[index].strip()
            todos.pop(index)

            # Write back updated list
            with open('file/todos.txt', 'w') as file:
                file.writelines(todos)

            print(f"Todo '{todo_to_remove}' was removed from the list.")
        except (ValueError, IndexError):
            print("Invalid number. Please try again.")

    # EXIT: Quit the program
    elif user_action.startswith("exit"):
        break

print("Bye!")
