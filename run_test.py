import unittest
from test_mars_rover import TestMarsRover, TestMarsRoverObstacleDetector
from test_planet import TestPlanetInitialState, TestPlanetWithObstacle
from test_position_tracker import TestPositionTrackerInitialState
from test_command_handler import TestCommandHandler

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestPositionTrackerInitialState))
    test_suite.addTest(unittest.makeSuite(TestCommandHandler))
    test_suite.addTest(unittest.makeSuite(TestMarsRover))
    test_suite.addTest(unittest.makeSuite(TestMarsRoverObstacleDetector))
    test_suite.addTest(unittest.makeSuite(TestPlanetInitialState))
    test_suite.addTest(unittest.makeSuite(TestPlanetWithObstacle))
    return test_suite

if __name__ == '__main__':
    testSuit=suite()
    runner=unittest.TextTestRunner()
    runner.run(testSuit)