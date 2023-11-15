import unittest
from test_position_tracker import TestPositionTrackerInitialState

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestPositionTrackerInitialState))
    return test_suite

if __name__ == '__main__':
    testSuit=suite()
    runner=unittest.TextTestRunner()
    runner.run(testSuit)