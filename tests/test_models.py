import unittest
from src.models import SEIRDVFModel
import numpy as np

class TestSEIRDVFModel(unittest.TestCase):
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

    def test_model_initialization(self):
        model = SEIRDVFModel(self.params, self.initial_conditions)
        self.assertIsInstance(model, SEIRDVFModel)

    def test_model_solution(self):
        model = SEIRDVFModel(self.params, self.initial_conditions)
        t = np.linspace(0, 10, 10)
        result = model.solve(t)
        self.assertEqual(result.shape, (7, 10))

if __name__ == "__main__":
    unittest.main()
