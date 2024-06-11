import numpy as np
from scipy.optimize import minimize
from src.simulation import run_simulation


def generate_synthetic_data(params, initial_conditions, days, noise_level=0.1):
    results = run_simulation(params, initial_conditions, days)
    for key in results.keys():
        if key != 't':
            results[key] += noise_level * np.random.normal(size=results[key].shape)
            results[key] += 0.1 * np.sin(2 * np.pi * results['t'] / 365)
    return results


def estimate_parameters(observed_data, initial_guess, initial_conditions):
    def objective(params):
        params_dict = {
            'beta': params[0], 'sigma': params[1], 'gamma': params[2], 'mu': params[3],
            'delta': params[4], 'nu': params[5], 'omega': params[6], 'kappa': params[7], 'phi': params[8]
        }
        simulated_data = run_simulation(params_dict, initial_conditions)
        
        error = 0
        for key in observed_data.keys():
            if key != 't':
                error += np.sum((observed_data[key] - simulated_data[key]) ** 2)
        return error
    
    result = minimize(objective, initial_guess, method='Nelder-Mead')
    return result.x
