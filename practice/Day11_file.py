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
## If you’re not using the with keyword, then you should call f.close() to close the file and immediately free up any system resources used by it.

##For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:
for line in f:
    print(line, end='')  #If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().
    
with open('text.txt', 'r') as f:
    #print(f.readline()) ### read one line
    #print(f.read()) ### read all lines
    for line in f:
        if line.__contains__('two'):
            print(line, end='')
