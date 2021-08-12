"""
Author: Manivannan
Testing class for the helper module

This contains unit test to mock and validate max string occurance
"""

import unittest
import helper

class TestHelper(unittest.TestCase):
    
    mock_response = {'g': 1, 'e': 2, 't': 1, 'o': 1, 'c': 3, 'u': 1, 'r': 1, 'a': 1, 'n': 1, '2': 1, '3': 1, '4': 1}
    mock_response1 = {'c':2,'a':2,'h':1}
    mock_response2 = {}
    mock_input = 'get occurance 234#@'
    mock_input1 = ' '

    def test_get_occurance(self):
        '''
            Test case for get_occurance method for valid input
        '''
        response = helper.get_occurance(TestHelper.mock_input)
        self.assertIsNotNone(response)
        self.assertDictEqual(TestHelper.mock_response,response)

    def test_get_occurance_space(self):
        '''
            Test case for get_occurance method for space input
        '''
        response = helper.get_occurance(TestHelper.mock_input1)
        self.assertIsNotNone(response)        
        self.assertDictEqual({},{})

    def test_get_max_occuranc(self):
        '''
            Test case for get_max_occurance
        '''
        response1,response2 = helper.get_max_occurance(TestHelper.mock_response)
        self.assertIsNotNone(response1)
        self.assertIsNotNone(response2)
        self.assertEqual(3,response2)
        self.assertEqual(['c'],response1)

    def test_get_max_occurance_more_than_one(self):
        '''
            Test case for get_max_occurance
        '''
        response1,response2 = helper.get_max_occurance(TestHelper.mock_response1)
        self.assertIsNotNone(response1)
        self.assertIsNotNone(response2)
        self.assertEqual(2,response2)
        self.assertEqual(['c','a'],response1)

    def test_get_max_occurance_no_occurance(self):
        '''
            Test case for get_max_occurance
        '''
        response1,response2 = helper.get_max_occurance(TestHelper.mock_response2)
        self.assertIsNotNone(response1)
        self.assertIsNotNone(response2)
        self.assertEqual(0,response2)
        self.assertEqual([],response1)
        
