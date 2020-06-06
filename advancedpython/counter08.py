from collections import Counter


def main():
    #list of students in class 1
    class1 = ["Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah"
              "Kevin", "James", "James", "Melanie", "Penny", "Steve"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

    # Create a counter for class1 and class2
    c1 = Counter(class1)
    c2 = Counter(class2)

    # how many students in class1 named James?
    print(c1["James"])

    # how many students are in class1?
    print(sum(c1.values()), " students in class1")

    # combine the two classes
    c1.update(class2)
    print(sum(c1.values()), " students in class1")

    # what the most common name in the two classes?
    print(c1.most_common(3))

    # Separate the classes again
    c1.subtract(class2)
    print(c1.most_common(3))

    # what the common between the two classes?
    print(c1 & c2)


if __name__ == "__main__":
    main()