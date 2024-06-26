from typing import Dict, Callable
import numpy as np
from scipy.integrate import solve_ivp

class SEIRDVFModel:
    def __init__(self, params: Dict[str, float], initial_conditions: Dict[str, float], time_dependent_params: Dict[str, Callable] = {}):
        self.params = params
        self.initial_conditions = initial_conditions
        self.time_dependent_params = time_dependent_params
        self.N = sum(initial_conditions.values())  # Total population

    def _deriv(self, t, y):
        S, E, I, R, D, V, F = y
        N = self.N

        # Handle time-dependent parameters
        if self.time_dependent_params and 'beta' in self.time_dependent_params:
            beta = self.time_dependent_params['beta'](t)
        else:
            beta = self.params['beta']

        if self.time_dependent_params and 'phi' in self.time_dependent_params:
            phi = self.time_dependent_params['phi']
        else:
            phi = self.params['phi']

        sigma = self.params['sigma']
        gamma = self.params['gamma']
        delta = self.params['delta']
        nu = self.params['nu']
        omega = self.params['omega']
        kappa = self.params['kappa']

        dSdt = -beta * S * (I + phi * F) / N - nu * S + omega * R + omega * V
        dEdt = beta * S * (I + phi * F) / N - sigma * E
        dIdt = sigma * E - gamma * I - delta * I
        dRdt = gamma * I - omega * R
        dDdt = kappa * F
        dVdt = nu * S - omega * V
        dFdt = delta * I - kappa * F

        return [dSdt, dEdt, dIdt, dRdt, dDdt, dVdt, dFdt]

    def solve(self, t: np.ndarray) -> np.ndarray:
        y0 = list(self.initial_conditions.values())
        solution = solve_ivp(self._deriv, [t[0], t[-1]], y0, t_eval=t)
        return solution.y
