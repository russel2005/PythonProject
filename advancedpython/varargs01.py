def addition(*args):
    result = 0;
    for arg in args:
        result += arg;
    return result


def main():
    # pas different arguments
    print(addition(5, 10, 15, 20))

    # pass an existing list
    myNums = [5,10,20,15]
    print(addition(*myNums))

if __name__ == '__main__':
    main()
