import unittest
from calculator import calculator
from CSVReader import CSVReader

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data_add = CSVReader("C:/Users/sahil/PycharmProjects/CalculatorPythonProject_1/src/UnitTest_Addition.csv").data
        for row in test_data_add:
            result = int(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_sub_method_calculator(self):
        test_data_sub = CSVReader("C:/Users/sahil/PycharmProjects/CalculatorPythonProject_1/src/UnitTest_Subtraction.csv").data
        for row in test_data_sub:
            result = int(row['Result'])
            self.assertEqual(self.calculator.sub(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_mul_method_calculator(self):
        test_data_mul = CSVReader("C:/Users/sahil/PycharmProjects/CalculatorPythonProject_1/src/UnitTest_Multiplication.csv").data
        for row in test_data_mul:
            result = int(row['Result'])
            self.assertEqual(self.calculator.mul(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_div_method_calculator(self):
        test_data_div = CSVReader("C:/Users/sahil/PycharmProjects/CalculatorPythonProject_1/src/UnitTest_Division.csv").data
        for row in test_data_div:
            result = float(row['Result'])
            self.assertEqual(self.calculator.div(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

if __name__ == '__main__':
    unittest.main()
