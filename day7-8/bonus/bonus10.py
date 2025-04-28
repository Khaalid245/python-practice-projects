data = input("enter here your data: ")
journal = input("how do you rate your mood from 1 to 10: ")
thought = input("let your thought flow:\n ")
with open(f"../bonus/{data}.txt","w") as file:
    file.writelines(journal +"\n")
    file.writelines(thought)