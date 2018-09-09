# try:
#     fh = open('fear.txt') #rt default
#
#     for line in fh:
#         print(line.strip()) # remove whitespace and print
# finally:
#     fh.close()

with open('fear.txt') as fh:
    for line in fh:
        print(line.strip())
