import unittest
from src.simulation import run_simulation

class TestSimulation(unittest.TestCase):
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

    def test_run_simulation(self):
        result = run_simulation(self.params, self.initial_conditions, days=10)
        self.assertEqual(len(result['t']), 10)
        self.assertEqual(result['S'].shape, (10,))

if __name__ == "__main__":
    unittest.main()
