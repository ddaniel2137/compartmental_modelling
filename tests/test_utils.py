import unittest
from src.utils import generate_synthetic_data
from src.simulation import run_simulation

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.params = {
            "beta": 0.3,
            "sigma": 0.2,
            "gamma": 0.1,
            "mu": 0.01,
            "delta": 0.05,
            "nu": 0.05,
            "omega": 0.01,
            "kappa": 0.1,
            "phi": 0.05
        }
        self.initial_conditions = {
            "S": 9990,
            "E": 10,
            "I": 0,
            "R": 0,
            "D": 0,
            "V": 0,
            "F": 0
        }

    def test_generate_synthetic_data(self):
        data = generate_synthetic_data(self.params, self.initial_conditions, 160)
        self.assertTrue('t' in data)
        self.assertTrue('S' in data)
        self.assertTrue(len(data['S']) == 160)

if __name__ == "__main__":
    unittest.main()
