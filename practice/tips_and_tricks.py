condition = True

if condition:
	x = 1
ele:
	x = 0

print(x)

#==============Ternary operator==========
condition = True
x = 1 if condition else 0
print(x)



#--------------------------------------
num1 = 10000000000
num2 = 100000000

total = num1 + num2
print(total)
#==================use underscore for readability========
num1 = 10_000_000_000 # 10 billion
num2 = 100_000_000    # 100 million
total = num1 + num2
print(total) #10100000000
print(f'{total:,}') # 10,100,000,000

#----------------------------------------
open a file and close
f = open('test.txt, 'r')
file_contents = f.read()
f.close()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)
#=================using context manager==========
with open('test.txt, 'r') as f:
	file_contents = f.read()
#we dont need to close manually file

words = file_contents.split(' ')
word_count = len(words)
print(word_count)


#--------------print list by index--------------------------------
names = ['russel' , 'arish', 'momo']

index = 0
for name in names:
	print(index, name)
	index += 1
#====================using enumerate function==============
names = ['russel' , 'arish', 'momo']

for index, name in enumerate(names, start=1):
	print(index, name)	

#---------------------loop thru two lists--------------------
names = ['russel' , 'arish', 'momo', 'nazrul']
heroes = ['spiderman', 'superman', 'deadpool', 'batman']

for index, name in enumerate(names):
	hero = heroes[index]
	print(f'{name} is actually {hero}')
#================using ZIP function to use two list===========
for name, hero in zip(names, heroes):
	print(f'{name} is actually {hero}')

#using ZIP in 3 lists
names = ['russel' , 'arish', 'momo', 'nazrul']
heroes = ['spiderman', 'superman', 'deadpool', 'batman']
universes = ['marvel', 'dc', 'marvel', 'dc']

for name, hero, universe in zip(names, heroes, universes):
	print(f'{name} is actually {hero} from {universe}')

#or using Tuple
for value in zip(names, heroes, universes):
	print(value)

#--------------------unpacking values----------------
a, b = (1,2)
#if we not use b then we can use underscore and tell compiler that b is not using now as variable
a, _ = (a, 2)

#if we use more variable than value then get >value error
a, b, c = (1,2)

#if we use more values than variable then get >value error too
a, b, c = (1,2,3,4,5)

#how we can over come using asterik *
a, b, *c =(1,2,3,4,5) #> here c will take all after 2 
a, b, *c, d =(1,2,3,4,5) #>here d will be the last value

#---------------------input sensative value------------------
username = input('Username: ')
password = input('Password: ')

print('Logging In...')

#======================above code will display the password when user type===========
from getpass import getpass
username = input('Username: ')
password = getpass('Password: ') # > it will hide the input text from display
-----------------------------------------------------------------

