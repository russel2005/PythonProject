"""
small, anonymous fuctions
can be passed as arguments where you need a funcion
Typically used in place just when nedded
defined as:
   lambda (parameters) : (expression)
"""


def CelsisusToFahrenheit(temp):
    return (temp*9/5) + 32


def FahrenheitToCelsisus(temp):
    return (temp-32) * 5/9


def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]


    # use regular fuctions to convert temps
    print(list(map(FahrenheitToCelsisus, ftemps)))
    print(list(map(CelsisusToFahrenheit, ctemps)))

    # use lambdas to accomplish the same thing
    print('in lambda:')
    print(list(map(lambda t: (t-32) * 5/9, ftemps)))
    print(list(map(lambda t: (t*9/5) + 32, ctemps)))


if __name__ == "__main__":
    main()

