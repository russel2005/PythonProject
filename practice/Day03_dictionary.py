# dictionary is key and value pairs
# python 3.7 by default added order list
groceries = {'banana': .29, 'orange': 1.29, 'apple': 1.49}

print(groceries['banana'])

print(groceries.get('carrot'))
# get method not throw KeyErro when key not found in dictionary

add_item = {'lemon': 3.99}
groceries.update(add_item)

print(groceries)
groceries.pop('apple')
print(groceries)

#groceries.keys()
#groceries.values()
#groceries.popitem()


#print order by values

print(list(groceries.values()).sort())
contacts ={
    'russel': {'phone': '212-311-1222', 'email':'russel@gmail.com'},
    'arish': ['212-345-3333', 'arish@gmail.com']
}

def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])


save_user(id=1, name="admin") # this is dictionary


#count value in hashtable/dictionary  how many times occured
items = ["apple", "pear", "orange", "banana", "apple",
"apple", "orange", "banana", "apple", "pear", "orange",
"banana", "apple", "pear", "banana", "grape", "orange"]

count = dict()

for item in items:
    if item in count.keys():
        count[item] += 1
    else:
        count[item] = 1

print(count)

