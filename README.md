
# SEIRDVF Epidemic Model Simulation

## Overview

This repository contains an implementation of the SEIRDVF compartmental model for simulating the spread of infectious diseases, particularly focusing on the Ebola epidemic. The SEIRDVF model includes the following compartments: Susceptible (S), Exposed (E), Infectious (I), Recovered (R), Deceased (D), Vaccinated (V), and Funeral (F).

This project aims to model complex transmission dynamics, including the effects of social behaviors, seasonal variations, vaccination strategies, and waning immunity. The implementation allows for advanced parameter estimation using real-world data and optimization techniques.

## Features

- **Dynamic Transmission Rates**: Incorporates detailed social interaction parameters and seasonal variations.
- **Advanced Parameter Estimation**: Utilizes optimization techniques such as `minimize`, `least_squares`, and `differential_evolution` for parameter estimation.
- **Real-World Data Integration**: Allows for uploading real-world data to validate and adjust model parameters.
- **Streamlit Interface**: Provides an interactive interface for adjusting parameters, running simulations, and visualizing results.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ddaniel2137/compartmental_modelling.git
    cd SEIRDVF_Model
    ```

2. Create a virtual environment:
    ```bash
    python3.12 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the Streamlit application, use the following command:
```bash
streamlit run app.py
```

You can access the application in your web browser at `http://localhost:8501`.

## Usage

### Adjust Parameters

- **Model Parameters**: Use the sidebar to adjust model parameters such as transmission coefficient (β), recovery rate (γ), vaccination rate (ν), etc.
- **Initial Conditions**: Set the initial number of individuals in each compartment (S, E, I, R, D, V, F).
- **Scenarios**: Select from predefined scenarios including High Transmission, Effective Vaccination, Seasonal Variation, High Natural Death Rate, and Waning Immunity.

### Running Simulations

1. Adjust the parameters and initial conditions using the sidebar.
2. Select a scenario from the dropdown.
3. Click "Run Simulation" to execute the model and visualize the results.

### Optimization

1. **Generate Synthetic Data**: Click the "Generate Synthetic Data" button to create data for testing the optimization.
2. **Upload Real-World Data**: Upload a CSV file containing real-world data for parameter estimation.
3. **Estimate Parameters**: Click the "Estimate Parameters" button to optimize and find the best-fit parameters based on the provided data.

## Model Description

The SEIRDVF model is defined by the following differential equations:

```
dS/dt = μN - βS(I + φF)/N - νS + ωR + ωV - μS
dE/dt = βS(I + φF)/N - σE - μE
dI/dt = σE - γI - δI - μI
dR/dt = γI - ωR - μR
dD/dt = δI - κD
dV/dt = νS - ωV - μV
dF/dt = κD - φF
```

### Parameters

- **β**: Transmission coefficient
- **σ**: Rate at which exposed individuals become infectious
- **γ**: Recovery rate
- **μ**: Natural death rate
- **δ**: Disease-induced death rate
- **ν**: Vaccination rate
- **ω**: Waning immunity rate
- **κ**: Rate at which deceased individuals are moved to the funeral component
- **φ**: Rate at which funerals contribute to new infections

