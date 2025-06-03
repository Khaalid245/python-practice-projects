from wheel.cli.convert import convert

contents = ['The American black bear is a native bear to North America.']
filenames = ['bear.txt']

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)
    file.close()

for filename in filenames:
    file = open(f"../files/{filename}", 'r')
    contents = file.read()
    converted = contents.title()
    num_characters = len(contents)
    print(converted,num_characters)
