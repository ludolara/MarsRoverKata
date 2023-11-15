import unittest
from test_mars_rover import TestMarsRover
from test_planet import TestPlanetInitialState
from test_position_tracker import TestPositionTrackerInitialState
from test_command_handler import TestCommandHandler

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestPositionTrackerInitialState))
    test_suite.addTest(unittest.makeSuite(TestCommandHandler))
    test_suite.addTest(unittest.makeSuite(TestMarsRover))
    test_suite.addTest(unittest.makeSuite(TestPlanetInitialState))
    return test_suite

if __name__ == '__main__':
    testSuit=suite()
    runner=unittest.TextTestRunner()
    runner.run(testSuit)