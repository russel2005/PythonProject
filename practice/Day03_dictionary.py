# dictionary is key and value pairs, no sequenced, no indexing > only Mapping, use {} brackets
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

# declare empty dictionary
d = {}
# adding value
d['one'] = 1
d['two'] = 2
print(d)


