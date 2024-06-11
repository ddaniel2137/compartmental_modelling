import streamlit as st
from src.models import SEIRDVFModel
from src.simulation import run_simulation
from src.visualization import plot_results, plot_scenarios
from src.utils import generate_synthetic_data, estimate_parameters
import numpy as np


def main():
    st.title("SEIRDVF Epidemic Model Simulation")
    
    st.markdown("""
    # SEIRDVF Model Documentation
    This app allows you to simulate the SEIRDVF model for epidemic spread. Adjust parameters using the sidebar and view the results in real-time.
    ## Parameters
    - **β**: Transmission coefficient
    - **σ**: Rate at which exposed individuals become infectious
    - **γ**: Recovery rate
    - **μ**: Natural death rate
    - **δ**: Disease-induced death rate
    - **ν**: Vaccination rate
    - **ω**: Waning immunity rate
    - **κ**: Rate to funeral component
    - **φ**: Funeral transmission rate

    ## Initial Conditions
    Adjust the initial number of individuals in each compartment:
    - Susceptible (S)
    - Exposed (E)
    - Infectious (I)
    - Recovered (R)
    - Deceased (D)
    - Vaccinated (V)
    - Funeral (F)

    ## Scenarios
    Choose a scenario to explore:
    - **High Transmission**: High transmission and low recovery rate.
    - **Effective Vaccination**: High vaccination rate.
    - **Seasonal Variation**: Seasonal variations in transmission rates.
    - **High Natural Death Rate**: High natural death rate.
    - **Waning Immunity**: Significant waning immunity.

    ### How to Use
    1. Adjust the parameters and initial conditions using the sidebar.
    2. Select a scenario from the dropdown.
    3. Click "Run Simulation" to see the results.

    ### Visualization
    The results are displayed as interactive plots. You can hover over the lines to see specific values and use the toolbar for zooming and panning.
    """)
    
    st.sidebar.header("Model Parameters")
    scenario = st.sidebar.selectbox("Select Scenario",
                                    ["High Transmission", "Effective Vaccination", "Seasonal Variation",
                                     "High Natural Death Rate", "Waning Immunity"])
    
    if scenario == "High Transmission":
        params = {
            "beta": 0.8,
            "sigma": 0.2,
            "gamma": 0.05,
            "mu": 0.01,
            "delta": 0.1,
            "nu": 0.01,
            "omega": 0.01,
            "kappa": 0.05,
            "phi": 0.05
        }
    elif scenario == "Effective Vaccination":
        params = {
            "beta": 0.3,
            "sigma": 0.2,
            "gamma": 0.1,
            "mu": 0.01,
            "delta": 0.05,
            "nu": 0.3,
            "omega": 0.01,
            "kappa": 0.05,
            "phi": 0.02
        }
    elif scenario == "Seasonal Variation":
        params = {
            "beta": 0.5,
            "sigma": 0.2,
            "gamma": 0.1,
            "mu": 0.01,
            "delta": 0.05,
            "nu": 0.05,
            "omega": 0.01,
            "kappa": 0.05,
            "phi": 0.05
        }
        time_dependent_params = {
            'beta': lambda t: 0.5 * (1 + 0.3 * np.sin(2 * np.pi * t / 365))
        }
    elif scenario == "High Natural Death Rate":
        params = {
            "beta": 0.3,
            "sigma": 0.2,
            "gamma": 0.1,
            "mu": 0.05,
            "delta": 0.05,
            "nu": 0.05,
            "omega": 0.01,
            "kappa": 0.05,
            "phi": 0.05
        }
    elif scenario == "Waning Immunity":
        params = {
            "beta": 0.4,
            "sigma": 0.2,
            "gamma": 0.1,
            "mu": 0.01,
            "delta": 0.05,
            "nu": 0.05,
            "omega": 0.1,
            "kappa": 0.05,
            "phi": 0.05
        }
    
    st.sidebar.header("Initial Conditions")
    initial_conditions = {
        "S": st.sidebar.number_input("Initial Susceptible (S)", value=9990),
        "E": st.sidebar.number_input("Initial Exposed (E)", value=10),
        "I": st.sidebar.number_input("Initial Infectious (I)", value=0),
        "R": st.sidebar.number_input("Initial Recovered (R)", value=0),
        "D": st.sidebar.number_input("Initial Deceased (D)", value=0),
        "V": st.sidebar.number_input("Initial Vaccinated (V)", value=0),
        "F": st.sidebar.number_input("Initial Funeral (F)", value=0),
    }
    
    if st.sidebar.button("Run Simulation"):
        if scenario == "Seasonal Variation":
            results = run_simulation(params, initial_conditions, time_dependent_params)
        else:
            results = run_simulation(params, initial_conditions)
        plot_results(results)
        plot_scenarios(scenario, params, initial_conditions)
    
    st.sidebar.header("Optimization")
    if st.sidebar.button("Generate Synthetic Data"):
        synthetic_data = generate_synthetic_data(params, initial_conditions, 160)
        st.session_state.synthetic_data = synthetic_data
        st.write("Synthetic data generated.")
    
    if st.sidebar.button("Estimate Parameters"):
        if 'synthetic_data' in st.session_state:
            observed_data = st.session_state.synthetic_data
            initial_guess = [params[key] for key in params]
            estimated_params = estimate_parameters(observed_data, initial_guess, initial_conditions)
            st.write(f"Estimated Parameters: {estimated_params}")
        else:
            st.write("Please generate synthetic data first.")
    
    with st.expander("Tutorial"):
        st.write("""
        ### How to Use the SEIRDVF Model App
        1. **Adjust Parameters**: Use the sliders and number inputs in the sidebar to set the parameters and initial conditions.
        2. **Select a Scenario**: Choose from Default, Hospital Capacity, Seasonal Variation, or Custom scenarios.
        3. **Run Simulation**: Click the "Run Simulation" button to execute the model and visualize the results.
        4. **Generate Synthetic Data**: Click the "Generate Synthetic Data" button to create data for testing the optimization.
        5. **Estimate Parameters**: Click the "Estimate Parameters" button to optimize and find the best-fit parameters based on the synthetic data.
        6. **Interpret Results**: Examine the interactive plots to understand how the disease dynamics evolve over time.
        """)


if __name__ == "__main__":
    main()
