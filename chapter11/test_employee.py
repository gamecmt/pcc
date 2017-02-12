import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        firstname='fly'
        lastname='pig'
        annual_salary='50000'
        self.top_raise='8000'
        self.my_employee=Employee(firstname,lastname,annual_salary)        
        
    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertIn('5000',self.my_employee.properties)
    def test_give_custom_raise(self):
        self.my_employee.give_raise(self.top_raise)
        self.assertIn('8000', self.my_employee.properties)

unittest.main()