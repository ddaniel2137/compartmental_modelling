import numpy as np
from scipy.optimize import minimize, least_squares, differential_evolution
from src.simulation import run_simulation

def generate_synthetic_data(params, initial_conditions, days, noise_level=0.1):
    results = run_simulation(params, initial_conditions, days)
    for key in results.keys():
        if key != 't':
            results[key] += noise_level * np.random.normal(size=results[key].shape)
    return results

def estimate_parameters(observed_data, initial_guess, initial_conditions, method='minimize'):
    def objective(params):
        params_dict = {
            'beta': params[0], 'sigma': params[1], 'gamma': params[2], 'mu': params[3],
            'delta': params[4], 'nu': params[5], 'omega': params[6], 'kappa': params[7], 'phi': params[8],
            'beta_HV': params[9], 'beta_VH': params[10], 'gamma_b': params[11]
        }
        simulated_data = run_simulation(params_dict, initial_conditions)
        
        error = 0
        for key in observed_data.keys():
            if key != 't':
                error += np.sum((observed_data[key] - simulated_data[key])**2)
        return error

    if method == 'minimize':
        result = minimize(objective, initial_guess, method='Nelder-Mead')
    elif method == 'least_squares':
        result = least_squares(objective, initial_guess)
    elif method == 'differential_evolution':
        bounds = [(0, 1) for _ in initial_guess]
        result = differential_evolution(objective, bounds)
    else:
        raise ValueError("Unsupported method")
    
    return result.x
