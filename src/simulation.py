import numpy as np
from typing import Dict, Any
from src.models import SEIRDVFModel

def run_simulation(params: Dict[str, float], initial_conditions: Dict[str, float], days: int = 160) -> Dict[str, np.ndarray]:
    t = np.linspace(0, days, days)
    model = SEIRDVFModel(params, initial_conditions)
    results = model.solve(t)

    compartments = ['S', 'E', 'I', 'R', 'D', 'V', 'F']
    result_dict = {compartment: results[idx, :] for idx, compartment in enumerate(compartments)}
    result_dict['t'] = t
    return result_dict
