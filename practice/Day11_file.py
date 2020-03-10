"""
file IO
w > write
r > read
r+ > read and write
a > append
"""

###Write a file
my_list = [1,2,3]

my_file = open("firstfile.txt", "w")

for item in my_list:
    my_file.write(str(item))
    #my_file.write(str(item) + "\n")
    
my_file.close()

###Read a file
"""
Feading a file > .read()
reading line by line > .readline()
"""
my_file = open("firstfile.txt", "r")
print(str(my_file.read())) # whole file
my_file.close()

print("Line by line =============>")
my_file = open("firstfile.txt", "r")
print(str(my_file.readline())) #read firstline only
my_file.close()


############ using with don't need to worry about the close the file.
print("with as write start")
with open("firstfile.txt", "w") as with_as_write:
    with_as_write.write(" this an example of with as wrirte")


print("with as read start")
with open("firstfile.txt", "r") as with_as_read:
    print(str(with_as_read.read()))
