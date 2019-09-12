import os
f1=open('test.md','w+')
for dirpath, dirnames, filenames in os.walk('./'):
    for file in filenames:
        if file.endswith('.md'):
            with open('./{}'.format(file),'r') as f:
                f1.write(f.read())