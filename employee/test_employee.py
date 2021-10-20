import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):


    def setUp(self): # run before each test
        print('setUp')
        self.emp1 = Employee("Ammar", "Sahyoun", 35000)
        self.emp2 = Employee("Jan", "Green", 60000)

    def tearDown(self): # run after each test
        print('tearDown\n')

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp1.email, "Ammar.Sahyoun@email.com")
        self.assertEqual(self.emp2.email, "Jan.Green@email.com")

        self.emp1.first = "Anna"
        self.emp2.first = "Lars"
        self.assertEqual(self.emp1.email,  "Anna.Sahyoun@email.com")
        self.assertEqual(self.emp2.email,  "Lars.Green@email.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp1.fullnane, "Ammar Sahyoun" )
        self.assertEqual(self.emp2.fullnane, "Jan Green" )

        self.emp1.first = "Anna"
        self.emp2.first = "Lars"
        self.assertEqual(self.emp1.fullnane, "Anna Sahyoun")
        self.assertEqual(self.emp2.fullnane, "Lars Green")

    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp1.apply_raise()
        self.emp2.apply_raise()
        self.assertEqual(self.emp1.pay, 36750 )
        self.assertEqual(self.emp2.pay, 63000)

if __name__== '__main__':
    unittest.main()

# python -m unittest