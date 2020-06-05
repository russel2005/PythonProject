## for loop
for i in range(1,11):
  print(i)

## find the occurance of char in string
test_str = "GeeksforGeeks"
freq_char = {} 

for ch in test_str:
  if ch in freq_char:
    freq_char[ch] +=1
  else:
    freq_char[ch] =1


# printing result  
print ("Count of all characters in GeeksforGeeks is : \n" +  str(freq_char)) 


##################list#################
numbers =[5,6,7,8,98]
numbers.append(30)# added last place in list
print(numbers)

numbers.insert(0,10)
print(numbers)

numbers.remove(98)
print(numbers)

numbers.pop() #delete last element on the list
print(numbers)

find_index = numbers.index(5)#return position of the given number in the list
print(find_index) #output: 1 because list [10,5,6,7,8]

#print(numbers.index(50)) #valueError: 50 is not in list

print(50 in numbers)#false but not throwing Error. retun boolean value

numbers.append(5)
print(numbers.count(5))#2

numbers.sort()
numbers.reverse()

print(numbers)#desceding order
numbers2 = numbers.copy()

print(numbers2)

"""
write a program to remove duplicates
"""
newNums = [5,6,7,8,6,8]
#01 
print(f"before delete duplicate:{newNums}")
newNums2 = newNums.copy()
for num in newNums2:
  if(newNums2.count(num) >1):
    newNums2.remove(num)
print(newNums2)

#02
uniques = []
for num in newNums:
  if num not in uniques:
    uniques.append(num)

print(uniques)

##############Dictionary##############
# >>> for key, value in a_dict.items():
# ...     print(key, '->', value)
# ...
# color -> blue
# fruit -> apple
# pet -> dog
#########################inheritance##############
class Dog:
  def walk(self):
    print("walk")


class Cat:
  def walk(self):
    print("walk")

#above two classes are define same method, in programming we called DRY=Dont Repeat Yourself
#how we can solve by inheritance
#################################
class Mammal:
  def walk(self):
    print("walk")


class Dog(Mammal):#dog class inheritace from Mammal class
  def bark(self):
    print("bark")


class Cat(Mammal):
  pass #if you dont have a class body use pass


dog1 = Dog()
dog1.walk()
dog1.bark()

####################fibonacci######################
def fib(num):
  a = 0 
  c, b = 1, 1
  #b = 1
  for i in range(0, num):
    yield("{}: {}".format(i+1, a))
    a = b
    b = c
    c = a + b

for item in fib(10):
  print(item)


### fibonacci number
a = 0
b, c = 1, 1

for i in range(0,10):
  print(a)
  a = b
  b = c
  c = a + b
  ##########################Class#################
  
  class Point:
  def move(self):
    print("move")

  def draw(self):
    print("draw")


#create obj or instance
point1 = Point()
point1.draw()

point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
#print(point2.x)#AttributeErorr because x didn't define in point2 object.
################create contructor####################

class PointC:
  def __init__(self,a, b):
    self.a = a
    self.b = b
  def move(self):
    print("move")

  def draw(self):
    print("draw")

point = PointC(10,20)
print(point.a)
###################################
class Person:
  def __init__(self, name):
    self.name = name
  def talk(self):
    print(f"hi, i am {self.name}")


russel = Person("Russel")
russel.talk()

arish = Person("Arish")
arish.talk()
  
##############################
  
