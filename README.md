
# SEIRDVFB Epidemic Model Simulation

## Overview

This repository contains an implementation of the SEIRDVFB compartmental model for simulating the spread of infectious diseases, particularly focusing on the Ebola epidemic. The SEIRDVFB model includes the following compartments: Susceptible (S), Exposed (E), Infectious (I), Recovered (R), Deceased (D), Vaccinated (V), Funeral (F), Susceptible Bats (S_b), Infectious Bats (I_b), and Recovered Bats (R_b).

This project aims to model complex transmission dynamics, including the effects of social behaviors, seasonal variations, vaccination strategies, and waning immunity. The implementation allows for advanced parameter estimation using real-world data and optimization techniques.

## Features

- **Dynamic Transmission Rates**: Incorporates detailed social interaction parameters and seasonal variations.
- **Advanced Parameter Estimation**: Utilizes optimization techniques such as `minimize`, `least_squares`, and `differential_evolution` for parameter estimation.
- **Real-World Data Integration**: Allows for uploading real-world data to validate and adjust model parameters.
- **Streamlit Interface**: Provides an interactive interface for adjusting parameters, running simulations, and visualizing results.

## Installation

1. Clone the repository:

   git clone https://github.com/ddaniel2137/compartmental_modelling.git
   cd SEIRDVFB_Model

2. Create a virtual environment:

   python3.12 -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`

3. Install the required packages:

   pip install -r requirements.txt

## Running the Application

To run the Streamlit application, use the following command:

streamlit run app.py

You can access the application in your web browser at `http://localhost:8501`.

## Usage

### Adjust Parameters

- **Model Parameters**: Use the sidebar to adjust model parameters such as transmission coefficient (β), recovery rate (γ), vaccination rate (ν), etc.
- **Initial Conditions**: Set the initial number of individuals in each compartment (S, E, I, R, D, V, F, S_b, I_b, R_b).
- **Scenarios**: Select from predefined scenarios including Hospital Capacity, Seasonal Variation, Funerary Transmission, and Safe and Dignified Burials.

### Running Simulations

1. Adjust the parameters and initial conditions using the sidebar.
2. Select a scenario from the dropdown.
3. Click "Run Simulation" to execute the model and visualize the results.

### Optimization

1. **Generate Synthetic Data**: Click the "Generate Synthetic Data" button to create data for testing the optimization.
2. **Upload Real-World Data**: Upload a CSV file containing real-world data for parameter estimation.
3. **Estimate Parameters**: Click the "Estimate Parameters" button to optimize and find the best-fit parameters based on the provided data.

## Model Description

The SEIRDVFB model is defined by the following differential equations:

## Model Description

The SEIRDVFB model is defined by the following differential equations:

## Model Description

The SEIRDVFB model is defined by the following differential equations:

$$
\begin{aligned}
\frac{d\mathrm{S}}{dt} &= - \beta \frac{\mathrm{S} (\mathrm{I} + \phi \mathrm{F})}{\mathrm{N}} - \nu \mathrm{S} + \omega \mathrm{R} + \omega \mathrm{V} - \beta_{HV} \frac{\mathrm{S} \mathrm{I_b}}{\mathrm{N}} \\
\frac{d\mathrm{E}}{dt} &= \beta \frac{\mathrm{S} (\mathrm{I} + \phi \mathrm{F})}{\mathrm{N}} - \sigma \mathrm{E} \\
\frac{d\mathrm{I}}{dt} &= \sigma \mathrm{E} - \gamma \mathrm{I} - \delta \mathrm{I} \\
\frac{d\mathrm{R}}{dt} &= \gamma \mathrm{I} - \omega \mathrm{R} \\
\frac{d\mathrm{D}}{dt} &= \kappa \mathrm{F} \\
\frac{d\mathrm{V}}{dt} &= \nu \mathrm{S} - \omega \mathrm{V} \\
\frac{d\mathrm{F}}{dt} &= \delta \mathrm{I} - \kappa \mathrm{F} \\
\frac{d\mathrm{S_b}}{dt} &= - \beta_{VH} \frac{\mathrm{S_b} \mathrm{I}}{\mathrm{N}} \\
\frac{d\mathrm{I_b}}{dt} &= \beta_{\mathrm{VH}} \frac{\mathrm{S_b} \mathrm{I}}{\mathrm{N}} - \gamma_b \mathrm{I_b} \\
\frac{d\mathrm{R_b}}{dt} &= \gamma_b \mathrm{I_b} \\
\end{aligned}
$$

### Parameters

- **β**: Transmission coefficient
- **σ**: Rate at which exposed individuals become infectious
- **γ**: Recovery rate
- **δ**: Disease-induced death rate
- **ν**: Vaccination rate
- **ω**: Waning immunity rate
- **κ**: Rate at which deceased individuals are moved to the funeral component
- **φ**: Rate at which funerals contribute to new infections
- **β_HV**: Human-to-bat transmission rate
- **β_VH**: Bat-to-human transmission rate
- **γ_b**: Bat recovery rate
