try:
    total_number = float(input("Enter the total value: "))
    value_number = float(input("Enter the value: "))

    percentage = (value_number / total_number) * 100
    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be zero.")
