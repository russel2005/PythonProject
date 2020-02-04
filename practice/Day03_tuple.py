#tuple is immutable 

person1 = ("russel", 35, "pizza")
person2 = ("momo", 25, "chicken")
people = [person1, person2]

name, age, favfood = person1
name, age, favfood = person2


for name, age, favfood in people:
    print(name)
    print(age)
    print(favfood)
    print()


