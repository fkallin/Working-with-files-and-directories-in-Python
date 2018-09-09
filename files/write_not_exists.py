with open('write_x.txt', 'x') as fw:
    fw.write('Writing Line 1') #This succeeds

with open('write_x.txt', 'x') as fw:
    fw.write('Writing Line 2') #This failes
