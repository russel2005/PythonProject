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

### sub class ######
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


dev_1 = Developer('russel', 'islam', 4000, 'python')
dev_2 = Developer('arish', 'islam', 5000, 'java')

print(dev_1.email)
print(dev_2.prog_lang)

### sub class #####

class Manager (Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
    
mgr_1 = Manager('Sue', 'smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

#######  build in  isinstance() method, issubclass()

print(isinstance(mgr_1, Manager) # True
print(isinstance(mgr_1, Developer) # False
      
print(issubclass(Developer, Employee) # True
print(issubclass(Manager, Developer) # False
