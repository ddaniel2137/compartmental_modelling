from typing import Dict, Any, Callable
import numpy as np
from scipy.integrate import solve_ivp

class SEIRDVFModel:
    def __init__(self, params: Dict[str, float], initial_conditions: Dict[str, float], time_dependent_params: Dict[str, Callable] = None):
        self.params = params
        self.initial_conditions = initial_conditions
        self.time_dependent_params = time_dependent_params

    def _deriv(self, t, y):
        S, E, I, R, D, V, F = y
        N = S + E + I + R + D + V + F

        # Handle time-dependent parameters
        if self.time_dependent_params and 'beta' in self.time_dependent_params:
            beta = self.time_dependent_params['beta'](t)
        else:
            beta = self.params['beta']

        sigma = self.params['sigma']
        gamma = self.params['gamma']
        mu = self.params['mu']
        delta = self.params['delta']
        nu = self.params['nu']
        omega = self.params['omega']
        kappa = self.params['kappa']
        phi = self.params['phi']

        dSdt = mu * N - beta * S * (I + phi * F) / N - nu * S + omega * R + omega * V - mu * S
        dEdt = beta * S * (I + phi * F) / N - sigma * E - mu * E
        dIdt = sigma * E - gamma * I - delta * I - mu * I
        dRdt = gamma * I - omega * R - mu * R
        dDdt = delta * I - kappa * D
        dVdt = nu * S - omega * V - mu * V
        dFdt = kappa * D - phi * F

        print(f"t={t:.2f}, S={S:.2f}, E={E:.2f}, I={I:.2f}, R={R:.2f}, D={D:.2f}, V={V:.2f}, F={F:.2f}")
        print(f"dSdt={dSdt:.2f}, dEdt={dEdt:.2f}, dIdt={dIdt:.2f}, dRdt={dRdt:.2f}, dDdt={dDdt:.2f}, dVdt={dVdt:.2f}, dFdt={dFdt:.2f}")

        return [dSdt, dEdt, dIdt, dRdt, dDdt, dVdt, dFdt]

    def solve(self, t: np.ndarray) -> np.ndarray:
        y0 = list(self.initial_conditions.values())
        solution = solve_ivp(self._deriv, [t[0], t[-1]], y0, t_eval=t)
        return solution.y
