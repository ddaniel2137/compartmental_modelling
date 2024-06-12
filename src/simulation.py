import numpy as np
from typing import Dict, Callable
from src.models import SISIRDFModel

def run_simulation(params: Dict[str, float], initial_conditions: Dict[str, float], days: int = 160, time_dependent_params: Dict[str, Callable] = {}) -> Dict[str, np.ndarray]:
    t = np.linspace(0, days, days)
    model = SISIRDFModel(params, initial_conditions, time_dependent_params)
    results = model.solve(t)

    compartments = ['S_h', 'I_h', 'S_v', 'I_v', 'R', 'D', 'F']
    result_dict = {compartment: results[idx, :] for idx, compartment in enumerate(compartments)}
    result_dict['t'] = t
    return result_dict
