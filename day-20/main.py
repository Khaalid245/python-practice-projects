from modules.function import get_todos, write_todos

while True:
    user_input = input("Choose: add, show, edit, complete, or exit: ").strip()

    # ADD: Add a new note
    if user_input.lower().startswith("add"):
        note = user_input[4:].strip()  # Slice after 'add '
        todos = get_todos()
        todos.append(note + '\n')
        write_todos(todos, "file/book.txt")
        print("Note saved.")

    # SHOW: Display all notes
    elif user_input.lower().startswith("show"):
        todos = get_todos("file/book.txt")
        for index, item in enumerate(todos):
            print(f"{index + 1} - {item.strip()}")

    # EDIT: Edit a note by number
    elif user_input.lower().startswith("edit"):
        try:
            number = int(user_input[5:].strip()) - 1
            todos = get_todos("file/book.txt")
            new_note = input("Enter the new note: ")
            todos[number] = new_note + '\n'
            write_todos(todos, "file/book.txt")
            print("Note updated.")
        except (ValueError, IndexError):
            print("Invalid input. Use: edit <number>")

    # COMPLETE: Remove a completed note
    elif user_input.lower().startswith("complete"):
        try:
            number = int(user_input[9:].strip()) - 1
            todos = get_todos("file/book.txt")
            removed = todos.pop(number).strip()
            write_todos(todos, "file/book.txt")
            print(f"Note '{removed}' was removed.")
        except (ValueError, IndexError):
            print("Invalid input. Use: complete <number>")

    # EXIT: Stop the loop
    elif user_input.lower() == "exit":
        print("Goodbye!")
        break

    else:
        print("Invalid command. Try: add, show, edit, complete, or exit.")
