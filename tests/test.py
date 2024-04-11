# Automated testing is the act of writing a piece of software to test an original piece of software.
# Test case is a class that inherit unittest.TestCase.
# unittest is built-in module in python.
# Pytest is a third-party module.
# The unittest module provides an object oriented interface which follows the concepts of oop.
# unittest module provides the class called 'TestCase', which should be inherited to create a 'test case'.
# The module provides methods that can be used to do assertions.
# The naming convention of these methods follows the Java naming convention.


# unit test is a method in the test case, that tests a single unit of logic
# Method, Function :- then eachmethod of a class or function is considered a unit
# scenarios :- then a use case of a method or function will represent a unit

# TDD : write test  before developing code.

''' Test runner

The unittest 'Test Runner' is responsible for discoring all your tests
The runner works in 2 ways
    Discovery phase: Detect all test cases(classes that inherit the 'TestCase').In this test case
    Run phase
 '''
# Organizing
# Test packages or folders should have '__init__.py
# Test modules or .py files should start with 'test'
# Classes should inherit the 'TestCase'.
# The test case methods should start with test
# -v run with verbosity this means it provide information about 

import unittest

# create our test case

class MyTest(unittest.TestCase):  # <name>TestCase

    def test_one(self):  # A method of the test case should start with 'test'
        # Assertion
        self.assertTrue(True) # 

    def test_float_and_int(self):
        self.assertEqual(1,1.0)     # same as ==

    def test_float_and_str(self):
        self.assertEqual(1,"1")    

class MySecondTestCase(unittest.TestCase):
    def test_three(self):
        self.assertIsNone(None)        

if __name__ == '__main__': # python3 -m unittest and python3 -m unittest -k test_one
    unittest()       # start test runner