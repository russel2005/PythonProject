"""
advanced iteration functions in the itertools package
"""
import itertools


def testFunction(x):
    return x < 40


def main():
    # cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))


    # use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    # accumulate creates an iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30]
    acc = itertools.accumulate(vals)
    print(list(acc))
    #output: [10, 30, 60, 100, 150, 190, 220]

    # use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x))
    #output: ['A', 'B', 'C', 'D', '1', '2', '3', '4']

    # dropwhile and takewhile will return values until a certain condition is met that stops them
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))

    list_item= [0,0j, None,"0"]
    print(any(list_item))


if __name__ == "__main__":
    main()