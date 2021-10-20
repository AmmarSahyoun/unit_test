import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp1 = Employee("Ammar", "Sahyoun", 35000)
        emp2 = Employee("Jan", "Green", 60000)
        self.assertEqual(emp1.email, "Ammar.Sahyoun@email.com")
        self.assertEqual(emp2.email, "Jan.Green@email.com")

        emp1.first = "Anna"
        emp2.first = "Lars"
        self.assertEqual(emp1.email,  "Anna.Sahyoun@email.com")
        self.assertEqual(emp2.email,  "Lars.Green@email.com")

    def test_fullname(self):
        emp1 = Employee("Ammar", "Sahyoun", 35000)
        emp2 = Employee("Jan", "Green", 60000)
        self.assertEqual(emp1.fullnane, "Ammar Sahyoun" )
        self.assertEqual(emp2.fullnane, "Jan Green" )

        emp1.first = "Anna"
        emp2.first = "Lars"
        self.assertEqual(emp1.fullnane, "Anna Sahyoun")
        self.assertEqual(emp2.fullnane, "Lars Green")

    def test_apply_raise(self):
        emp1 = Employee("Ammar", "Sahyoun", 35000)
        emp2 = Employee("Jan", "Green", 60000)

        emp1.apply_raise()
        emp2.apply_raise()
        self.assertEqual(emp1.pay, 36750 )
        self.assertEqual(emp2.pay, 63000)

if __name__== '__main__':
    unittest.main()
