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