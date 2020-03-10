class Employee:
    raise_amount = 1.04 #instance variable
    num_of_emps = 0 #class variable, if we want to increase empy by instance then we should use class name instead of self.

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1  #we should not use self because we want to increase class level.
  
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
      
    def apply_raise(self):
       self.pay = int(self.pay * self.raise_amount) #use instance variable with self.
       #self.pay = int(self.pay * Employee.raise_amount) 
       #above line will raise pay by all employee
       
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
   
emp_1 = Employee('russel', 'islam', 4000)
emp_2 = Employee('arish', 'islam', 5000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

#################
"""
we have employee info seperated by hiphen '-'
"""
emp_str_1 = 'john-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-9000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)

print(new_emp_1.pay)


###########but here every time split and get the value is painful, so just create class method.

@classmethod
def from_string(cls, emp_str)
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.pay)

##############
@classmethod
def fromtimestamp(cls, t):
    y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
    return cls(y, m, d)

###################  static method ##############

import datetime
my_date = datetime.date(2016, 7, 10)

@staticmethod
def is_workday(day):
    if day.weekday() == 5 or if day.weekday() == 6:
        return False
    return True

print(Employee.is_workday(my_date))
