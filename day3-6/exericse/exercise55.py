# List of filenames
filenames = ['a.txt']

# Loop through each filename
for filename in filenames:
    # Open each file in read mode
    file = open(f"../files/{filename}", 'r')

    # Read and print the content of the file
    content = file.read()
    print(content)

    # Close the file
    file.close()
