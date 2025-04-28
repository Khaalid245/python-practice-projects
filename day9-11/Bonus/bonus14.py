try:
    width = float(input("enter rectangle width: "))
    length =float(input("enter length:"))
    if width == length:
        exit("that looks life square.")

    area = width*length
    print(area)
except ValueError:
    print("please enter number ")