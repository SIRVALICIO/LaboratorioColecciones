import unittest
from custom_functions import temperature_methods


class TestCollectionMethods(unittest.TestCase):

    def test_Departamentprom(self):
        Total= temperature_methods.Departamentprom(12,25,14,28,36,27,39,40,24,14,13,25)
        self.assertEqual(Total, 3.75)

    def test_DepartamentMax(self):
        Total = temperature_methods.DepartamentMax(12, 25, 14, 28, 36, 27, 39, 40, 24, 14, 13, 25)
        self.assertEqual(Total, 3.75)



    def test_DepartamentMaximus(self):
        Total = temperature_methods.DepartamentMaximus(12, 25, 14,)
        self.assertEqual(Total, 3.75)

    def test_DepartamentDes(self):
        Total = temperature_methods.DepartamentDes(12, 25, 14, 28, 36, 27, 39, 40, 24, 14, 13, 25)
        self.assertEqual(Total, 3.75)


if __name__ == '__main__':
    unittest.main()
