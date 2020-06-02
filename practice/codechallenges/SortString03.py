"""
write a function to sort words in a string
input: string of words, separated by spaces
output: string of words, sorted alphabetically
ignore case when sorting

example:
sort_words('string of words')
output: 'of string words'
"""
def sort_words(input):
    words = input.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return ' '.join(words)


print(sort_words("banana ORANGE apple"))
