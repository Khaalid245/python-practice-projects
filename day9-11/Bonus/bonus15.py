def get_average():
    with open(".. /file/data.txt", "r") as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i)for i in values]

    average_local = sum(values) / len(values)
    return average_local


average=get_average()
print(average)