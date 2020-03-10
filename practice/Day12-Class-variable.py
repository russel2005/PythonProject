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
   
emp_1 = Employee('russel', 'islam', 4000)
emp_2 = Employee('arish', 'islam', 5000)

emp_1.raise_amount = 1.05 
print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employeee.num_of_emps)
