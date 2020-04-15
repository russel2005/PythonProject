names = ['russel' , 'arish', 'momo', 'nazrul']
heroes = ['spiderman', 'superman', 'deadpool', 'batman']
universes = ['marvel', 'dc', 'marvel', 'dc']

zipped = list(zip(names, heroes))

print(zipped)

unzipped = list(zip(*zipped))

print(unzipped)


items = ['apple', 'banana', 'orange']
counts = [3, 12, 6]
prices = [.99, .25, .50]

sentences = []
for (item, count, price) in zip(items, counts, prices):
    item, count, price = str(item), str(count), str(price)
    sentence = 'I bought ' + count + ' ' + item + 's at $' + price + ' .'
    sentences.append(sentence)

print(sentences)
