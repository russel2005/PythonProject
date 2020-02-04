# set contain unique list and ignore duplicates


l = [1,2,4,5,4,2,9,7,9]

no_duplicate = set(l)
print(no_duplicate)


lib1 = {'harry potter', 'hanger games', 'lord of the rings'}
lib2 = {'harry potter', 'romeo and juliet', 'lord of the rings'}

all_books = lib1.union(lib2)
common_book = lib1.intersection(lib2)
diff_book = lib1.difference((lib2))

clear_book = lib1.clear()


print(all_books)
print(common_book)
print(diff_book)
print(clear_book)