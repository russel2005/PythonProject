names = ['arish','momo','russel','nazrul']

l =[]
for person in names:
    l.append(person)
print(l)

#below line are same as above 4 lines, conprehensive
print([person for person in names])


x = []
for person in names:
    x.append(person + ' dump')
print(x)
#or
print([person+' clever' for person in names])
#######################################
movies_ratings = {'interstellar': 9, 'dark nights': 8, '50 shades of darker': 3, 'lord of the rings': 10, 'helo': 2}

best_ratings = []
for movie in movies_ratings:
    if movies_ratings[movie] > 6:
        best_ratings.append(movie)
print(best_ratings)
#or
print([movie for movie in movies_ratings if movies_ratings[movie] > 6])
###############################


# find max value

items = [6, 20, 8, 19, 23, 87, 41, 49, 53]

def find_max(items):
    if len(items) == 1:
        return items[0]
    op1 = items[0]
    op2 = find_max(items[1:])

    if op1 > op2:
        return op1
    else:
        return op2

print(find_max(items))