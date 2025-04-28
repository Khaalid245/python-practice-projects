from os import remove

from pyexpat.errors import messages

while True:
    user_action = input("type, add,show edit, complete or exist: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("add todo: ") + "\n"

            with open('file/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open("file/todos.txt", 'w') as file:
                file.writelines(todos)

        case 'show':
            file = open('file/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index +1}-{item}'
                print(row)

        case 'edit':
            number = int(input("enter number of edit: "))
            number = number - 1

            with open('file/todos.txt', 'r') as file:
                todos = file.readlines()

            new_item = input("enter the new item: ")
            todos[number] = new_item + '\n'

            with open("file/todos.txt", 'w') as file:
                    file.writelines(todos)

        case 'complete':
            number =int(input("enter number of complete: "))


            index = number -1
            todo_to_remove = todos[index]

            message = f"todo {todo_to_remove } was removed from the list"
            print(message)

            todos.pop(number -1)

            with open('file/todos.txt', 'w') as file:
                file.writelines(todos)




        case 'exit':
            break

print('Bye')
