# f = open("file.txt")
# print(f.read())
# f.close()

# The same can be written using with statement like this:
with open(r"F:\for data transfer\repo-for-data-transfer\chapter9\file.txt") as f:
    print(f.read())

# You dont have to explicitly close the file