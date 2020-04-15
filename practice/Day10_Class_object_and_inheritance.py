class Car(object):

    def __init__(self):
        print("You just created the car instance.")

    def drive(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("you just created the BMW instance")

    def drive(self):
        super(BMW, self).drive()
        # super().drive() # this line does the same but above one is more clear and standard
        print("you are driving a BMW, Enjoy....")
        # override the Car.drive method

    def headsup_display(self):
        print("this is unique feature")


c = Car()
c.drive()
c.stop()

b = BMW()
b.drive()
b.stop()
b.headsup_display()