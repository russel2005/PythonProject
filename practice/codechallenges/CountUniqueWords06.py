"""
input() path to a text file
output: print() message with
-total number of words.
- top 20 most frequent words
- number of occurrences for each word

ignore case:
words contain:
 letter, numbers, apostrophes, hyphens
"""

import re
from collections import Counter

def count_words(path):
    with open(path, encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [all_words.lower() for all_words in all_words]
        print('\n Total Words: ', len(all_words))

        word_counts =  Counter()
        for word in all_words:
            word_counts[word] += 1

        print('\nTop 20 Words:')
        for word in word_counts.most_common(20):
            print(word[0], '=>', word[1])


count_words("file.txt")

