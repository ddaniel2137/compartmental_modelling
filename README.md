# SISIRDF Epidemic Model Simulation

## Overview

This repository contains an implementation of the SISIRDF compartmental model for simulating the spread of infectious diseases. The SISIRDF model includes the following compartments: Susceptible Humans (S_h), Infectious Humans (I_h), Susceptible Vectors (S_v), Infectious Vectors (I_v), Recovered (R), Deceased (D), and Funerals (F).

This project aims to model complex transmission dynamics, including the effects of human-to-human, vector-to-human, human-to-vector, and vector-to-vector transmission. The implementation allows for time-dependent parameters and solving the model using scipy's `solve_ivp` function.

## Features

- **Time-Dependent Parameters**: Incorporates time-dependent transmission rates (beta_hh, beta_hv, beta_vh, beta_vv) to model varying transmission dynamics over time.
- **Numerical Integration**: Utilizes scipy's `solve_ivp` function for solving the system of differential equations.
- **Customizable Initial Conditions**: Allows setting initial conditions for each compartment.

## Installation

1. Clone the repository:

   git clone https://github.com/your-username/SISIRDF_Model.git
   cd SISIRDF_Model

2. Create a virtual environment:

   python -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`

3. Install the required packages:

   pip install -r requirements.txt

## Usage

To use the SISIRDF model, follow these steps:

1. Import the `SISIRDFModel` class from `models.py`:

   from models import SISIRDFModel

2. Create an instance of the `SISIRDFModel` class by providing the necessary parameters and initial conditions:

   params = {
       'beta_hh': 0.1,
       'beta_hv': 0.05,
       'beta_vh': 0.05,
       'beta_vv': 0.1,
       'sigma': 0.2,
       'gamma_h': 0.1,
       'gamma_v': 0.1,
       'delta': 0.01,
       'nu': 10,
       'omega': 0.01,
       'kappa': 0.1,
       'phi': 0.05
   }

   initial_conditions = {
       'S_h': 9990,
       'I_h': 10,
       'S_v': 10000,
       'I_v': 0,
       'R': 0,
       'D': 0,
       'F': 0
   }

   model = SISIRDFModel(params, initial_conditions)

3. Define the time points at which you want to solve the model:

   import numpy as np
   t = np.linspace(0, 100, 1000)

4. Solve the model using the `solve` method:

   solution = model.solve(t)

5. Access the solution for each compartment:

   S_h, I_h, S_v, I_v, R, D, F = solution

## Model Description

The SISIRDF model is defined by the following differential equations:

$
\begin{aligned}
\frac{dS_h}{dt} &= -\beta_{hh} \frac{S_h I_h}{N} - \beta_{hv} \frac{S_h I_v}{N} \\
\frac{dI_h}{dt} &= \beta_{hh} \frac{S_h I_h}{N} + \beta_{hv} \frac{S_h I_v}{N} - (\gamma_h + \delta) I_h \\
\frac{dS_v}{dt} &= \nu - \beta_{vv} \frac{S_v I_v}{N} - \beta_{vh} \frac{S_v I_h}{N} - \sigma S_v \\
\frac{dI_v}{dt} &= \beta_{vv} \frac{S_v I_v}{N} + \beta_{vh} \frac{S_v I_h}{N} - (\gamma_v + \sigma) I_v \\
\frac{dR}{dt} &= \gamma_h I_h - \omega R \\
\frac{dD}{dt} &= \delta I_h \\
\frac{dF}{dt} &= \kappa I_h + \phi I_v
\end{aligned}
$

### Parameters

- **β_hh**: Human-to-human transmission rate
- **β_hv**: Vector-to-human transmission rate
- **β_vh**: Human-to-vector transmission rate
- **β_vv**: Vector-to-vector transmission rate
- **σ**: Vector death rate
- **γ_h**: Human recovery rate
- **γ_v**: Vector recovery rate
- **δ**: Human disease-induced death rate
- **ν**: Vector birth rate
- **ω**: Waning immunity rate
- **κ**: Funeral transmission rate from humans
- **φ**: Funeral transmission rate from vectors
