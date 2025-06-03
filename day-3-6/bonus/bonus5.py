contents =['I have suspection for those two men',
           'what do you mean sir',
           'I will send to your email the evidence I have it ']

filenames =['doct.txt', 'report.txt', 'presentation.txt']

for contents, filenames in zip(contents, filenames):
    file = open(f"../files/{filenames}",'w')
    file.write(contents)