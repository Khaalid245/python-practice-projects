
while True:
    user_action = input("type, add,show edit, complete or exist: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("add todo: ") + "\n"

            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f'{index +1}-{item}'
                print(row)

        case 'edit':
            number = int(input("enter number of edit: "))
            number = number - 1
            new_item = input("enter the new item: ")
            todos[number] = new_item

        case 'complete':
            number =int(input("enter number of complete: "))
            todos.pop(number -1)



        case 'exit':
            break

print('Bye')
