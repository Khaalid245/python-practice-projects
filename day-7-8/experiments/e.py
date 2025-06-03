with open('../file/docs.txt', 'w') as file:
    file.writelines('hwllow khalid ')

with open("../file/docs.txt", 'r') as file:
    read= file.readlines()
    print(read)
    

with open('../file/docs.txt', 'a') as file:
    file.write(' Hello again Khalid!\n')
