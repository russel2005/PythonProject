class Employee:
    raise_amount = 1.04 
   
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
          
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
      
    def apply_raise(self):
       self.pay = int(self.pay * self.raise_amount) 
       
class Developer(Employee):
  pass


dev_1 = Developer('russel', 'islam', 4000)
dev_2 = Developer('arish', 'islam', 5000)

print(dev_1.email)
print(dev_2.email)
