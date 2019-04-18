import unittest
from custom_functions import temperature_methods


class TestCollectionMethods(unittest.TestCase):

    def test_Departamentprom(self):
        Total= temperature_methods.Departamentprom(12,12,12,12,12,12,12,12,12,12,12,12)
        self.assertEqual(Total, 13)

    def test_DepartamentMax(self):
        Total = temperature_methods.DepartamentMax(450,12,12,12,12,12,12,12,12,12,12,12)
        self.assertEqual(Total, 450)



    def test_DepartamentMaximus(self):
        Total = temperature_methods.DepartamentMaximus(12, 25, 14,)
        self.assertEqual(Total, 25)

    def test_DepartamentDes(self):
        Total = temperature_methods.DepartamentDes(12, 12,12,12,12,12,13,12,12,12,12,12)
        self.assertEqual(Total, 0)


if __name__ == '__main__':
    unittest.main()
