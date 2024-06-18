import unittest
from graderutils import graderunittest
from graderutils.graderunittest import points
import numpy as np

data = np.random.randint(0, 100, 100)

class TestHelloPython(unittest.TestCase):

    @points(1)
    def test_return(self):
        """Check function return type"""
        # Calls the function and examines its return value.
        import functions
        self.assertTrue(type(functions.summary_statistics(data)) is dict)

    @points(1)
    def test_names(self):
        """Check the names of the return dictionary"""
        import functions
        self.assertEqual(set(functions.summary_statistics(data).keys()), set(["mean", "std", "min", "max"]))

    @points(2)
    def test_mean(self):
        """Check the value of the mean"""
        import functions
        self.assertAlmostEqual(functions.summary_statistics(data)["mean"], np.mean(data))

    @points(2)
    def test_std(self):
        """Check the value of the standard deviation"""
        import functions
        self.assertAlmostEqual(functions.summary_statistics(data)["std"], np.std(data, ddof=1))
    
    @points(2)
    def test_min(self):
        """Check the value of the min"""
        import functions
        self.assertAlmostEqual(functions.summary_statistics(data)["min"], np.min(data))

    @points(2)
    def test_max(self):
        """Check the value of the max"""
        import functions
        self.assertAlmostEqual(functions.summary_statistics(data)["max"], np.max(data))

if __name__ == '__main__':
    unittest.main(testRunner=graderunittest.PointsTestRunner(verbosity=2))