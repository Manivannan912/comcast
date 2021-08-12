'''
Author: Mani
Unit test driver
'''

import logging
import unittest

from test.test_helper import TestHelper



if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR,format='[%(levelname)s] - %(message)s')
    unittest.main()