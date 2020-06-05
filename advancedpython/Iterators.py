"""
https://docs.python.org/3/library/itertools.html
"""

def main():
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    daysFr = ['Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam']

    ##### use iter to create an iterator over a collection
    # i = iter(days)
    # print(next(i))
    # print(next(i))
    # print(next(i))
    # print(next(i))
    ##### iterate using a function and a sentinel
    # with open("testfile.txt", "r") as fp:
    #     for line in iter(fp.readline, ''):
    #         print(line)
    ##### use regular interation over the days
    # for m in days:
    #     print(m)
    # #or
    # for m in range(len(days)):
    #     print(m+1, days[m])

    ####### using enumerate reduces code and provides a counter
    for i, m in enumerate(days, start=1):
        print((i, m))
    # use zip to combine sequences
    for m in zip(days, daysFr):
        print(m)
    #or
    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], "=", m[1], "in French")


if __name__ == "__main__":
    main()

