from typing import Dict, Callable
import numpy as np
from scipy.integrate import solve_ivp

class SISIRDFModel:
    def __init__(self, params: Dict[str, float], initial_conditions: Dict[str, float], time_dependent_params: Dict[str, Callable] = {}):
        self.params = params
        self.initial_conditions = initial_conditions
        self.time_dependent_params = time_dependent_params
        self.N = sum(initial_conditions.values())  # Total population

    def _deriv(self, t, y):
        S_h, I_h, S_v, I_v, R, D, F = y
        N = self.N

        # Handle time-dependent parameters
        if self.time_dependent_params and 'beta_hh' in self.time_dependent_params:
            beta_hh = self.time_dependent_params['beta_hh'](t)
        else:
            beta_hh = self.params['beta_hh']

        if self.time_dependent_params and 'beta_hv' in self.time_dependent_params:
            beta_hv = self.time_dependent_params['beta_hv'](t)
        else:
            beta_hv = self.params['beta_hv']

        if self.time_dependent_params and 'beta_vh' in self.time_dependent_params:
            beta_vh = self.time_dependent_params['beta_vh'](t)
        else:
            beta_vh = self.params['beta_vh']

        if self.time_dependent_params and 'beta_vv' in self.time_dependent_params:
            beta_vv = self.time_dependent_params['beta_vv'](t)
        else:
            beta_vv = self.params['beta_vv']

        sigma = self.params['sigma']
        gamma_h = self.params['gamma_h']
        gamma_v = self.params['gamma_v']
        delta = self.params['delta']
        nu = self.params['nu']
        omega = self.params['omega']
        kappa = self.params['kappa']
        phi = self.params['phi']

        dS_hdt = -beta_hh * S_h * I_h / N - beta_hv * S_h * I_v / N
        dI_hdt = beta_hh * S_h * I_h / N + beta_hv * S_h * I_v / N - (gamma_h + delta) * I_h
        dS_vdt = nu - beta_vv * S_v * I_v / N - beta_vh * S_v * I_h / N - sigma * S_v
        dI_vdt = beta_vv * S_v * I_v / N + beta_vh * S_v * I_h / N - (gamma_v + sigma) * I_v
        dRdt = gamma_h * I_h - omega * R
        dDdt = delta * I_h
        dFdt = kappa * I_h + phi * I_v

        return [dS_hdt, dI_hdt, dS_vdt, dI_vdt, dRdt, dDdt, dFdt]

    def solve(self, t: np.ndarray) -> np.ndarray:
        y0 = list(self.initial_conditions.values())
        solution = solve_ivp(self._deriv, [t[0], t[-1]], y0, t_eval=t)
        return solution.y
