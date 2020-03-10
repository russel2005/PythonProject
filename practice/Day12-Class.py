class Employee:

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'
  
  def fullname(self):
      return '{} {}'.format(self.first, self.last)
    
emp_1 = Employee('russel', 'islam', 4000)
emp_2 = Employee('arish', 'islam', 5000)

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname)
