import turtle
russel_turtle = turtle.Turtle()
# this is square

def square():
    russel_turtle.forward(100)
    russel_turtle.right(90)
    russel_turtle.forward(100)
    russel_turtle.right(90)
    russel_turtle.forward(100)
    russel_turtle.right(90)
    russel_turtle.forward(100)


square()
russel_turtle.forward(200)
square()

"""
>>> str = "Messi is the best soccer player"
>>> "soccer" in str
True
>>> "football" in str
False

>>> str = "Messi is the best soccer player"
>>> str.find("soccer")
18
>>> str.find("Ronaldo")
-1
"""
