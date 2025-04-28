filename =["1.file data.txt","2.reporting.txt", "3.presentations.txt"]

for filename in filename:
    filename =filename.replace('.','-',1)
    print(filename)