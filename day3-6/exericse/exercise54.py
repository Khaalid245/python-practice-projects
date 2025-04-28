from bonus.bonus5 import filenames

content_text =['hello', 'world', 'how is ai']

filenames =['hello.txt', 'world.txt', 'Ai.txt']

for content_text, filenames in zip(content_text, filenames):
    file = open(f"../files/{filenames}", 'w')
    file.write(content_text)
    file.close()

