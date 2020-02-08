import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('russel', 'islam', 90000)
        self.emp_2 = Employee('arish', 'raheel', 50000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'russel.islam@email.com')
        self.assertEqual(self.emp_2.email, 'arish.raheel@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'russel islam')
        self.assertEqual(self.emp_2.fullname, 'arish raheel')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 103499)
        self.assertEqual(self.emp_2.pay, 57499)

if __name__ == '__main__':
    unittest.main()