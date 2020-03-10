"""
file IO
w > write
r > read
r+ > read and write
a > append
"""

my_list = [1,2,3]

my_file = open("firstfile.txt", "w")

for item in my_list:
    my_file.write(str(item))
    
my_file.close()


