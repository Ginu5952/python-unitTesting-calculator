
import unittest
from typing import NoReturn

from src.calculator import Calculator
from src.custom_ex import IncorrectInputError

class CalculatorAddTestCase(unittest.TestCase):

    def test_add_3_correct_input(self) -> None | NoReturn:  # unit
       
        # Arrange
        calculator = Calculator()
        x = 4
        y = 3
        z = 1
        expected_result = 8

        # Act
        result = calculator.add(x,y,z)

        # Assert
        self.assertEqual(result,expected_result)

    def test_add_with_no_args(self) -> None | NoReturn:

        # Arrange
        calculator = Calculator()
        expected_result = 0

        #Act
        result = calculator.add()

        #Assert
        self.assertEqual(result,expected_result)

    def test_add_with_incorrect_input(self) -> NoReturn:

        # Arrange
        calculator = Calculator()
        x = '6'
        y = [4,5]

        # Act/Assert
        with self.assertRaises(TypeError):
            calculator.add(x,y)

#---------------------------------------------------------------------------------

class CalculatorMultTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_mult_with_correct_input(self):
       
        # Arrange
        
        x = 1
        y = 2
        z = 3
        expected_result = 6

        #Act
        result = self.calculator.multiply(x,y,z)  

        # Assert
        self.assertEqual(result,expected_result)    

    def test_mult_with_incorrect_input(self):    

     # Arrange
    
        x = []
        y = (1,2) 
        z = '4'

        # Act/Assert
        with self.assertRaises(IncorrectInputError):
            self.calculator.multiply(x,y,z)       

    def tearDown(self):
        pass

#-------------------------------------------------------------------------------------------------

class CalculatorDivTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_div_with_correct_input(self):

        # Arrange

        x = 100
        y = 2
        expected_result = 50

        # Act
        result = self.calculator.division(x,y)     

        # Assert
        self.assertEqual(result,expected_result)   

    def test_div_with_incorrect_input(self):

        # Arrange
        x = 100
        y = 0    

        # Act/Assert
        with self.assertRaises(ZeroDivisionError):
            self.calculator.division(x,y) 

#------------------------------------------------------------------------------------------------------------

class CalculatorSubTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_sub_with_correct_input(self):

        # Arrange

        x = 10
        y = 2
        expected_result = 8

        # Act
        result = self.calculator.substraction(x,y)     

        # Assert
        self.assertEqual(result,expected_result)   

    def test_sub_with_incorrect_input(self):

        # Arrange
        x = 100
        y = []    

        # Act/Assert
        with self.assertRaises(IncorrectInputError):
            self.calculator.substraction(x,y) 

  
