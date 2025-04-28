
password = input("enter here password: ")

result =[]
if len(password)>=7:
    result.append(True)
else:
    result.append(False)

if all(result)==True:
    print("strong password")
else:
    print("your password is week")


