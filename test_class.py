import unittest
from selervy import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        name = [["lili","calisy",30000],["tom","steven",40000]]
        self.salery = Employee(name[0])
        self.result = [35000,40000]
    def test_give_default_raise():
        # up = self.salery.give_raise()
        self.assertEqual(self.result[0],self.salery.give_raise())
    # def test_give_custom_raise():
    #     self.assertEqual(self.result,self.salery.give_raise())
    unittest.main()




