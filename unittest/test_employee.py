import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('russel', 'islam', 90000)
        emp_2 = Employee('arish', 'raheel', 50000)

        self.assertEqual(emp_1.email, 'russel.islam@email.com')
        self.assertEqual(emp_2.email, 'arish.raheel@email.com')

    def test_fullname(self):
        emp_1 = Employee('russel', 'islam', 90000)
        emp_2 = Employee('arish', 'raheel', 50000)

        self.assertEqual(emp_1.fullname, 'russel islam')
        self.assertEqual(emp_2.fullname, 'arish raheel')

    def test_apply_raise(self):
        emp_1 = Employee('russel', 'islam', 90000)
        emp_2 = Employee('arish', 'raheel', 50000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 103499)
        self.assertEqual(emp_2.pay, 57499)

if __name__ == '__main__':
    unittest.main()