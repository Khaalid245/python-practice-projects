todos=[]

while True:
    user_action =input("type add or to show : ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo= input("add a todo : ")
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.capitalize()
                print(item)
        case 'exit':
            break
print("bye")


