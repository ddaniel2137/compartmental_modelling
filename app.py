import streamlit as st
import numpy as np
import pandas as pd
from src.simulation import run_simulation
from src.visualization import plot_results, plot_scenarios
from src.utils import generate_synthetic_data, estimate_parameters

def main():
    st.title("SI+SIRDF Model for Zoonotic Diseases")

    with st.expander("SI+SIRDF Model Documentation", expanded=False):
        st.markdown("""
        <style>
        .documentation {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        .documentation h2 {
            color: #2C3E50;
        }
        .documentation ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="documentation">
        <h2>SI+SIRDF Model Documentation</h2>
        <p>This app allows you to simulate the SI+SIRDF model for zoonotic disease spread. Adjust parameters using the sidebar and view the results in real-time.</p>
        <h3>Parameters</h3>
        <ul>
            <li><b>β_HH</b>: Human-to-human transmission coefficient</li>
            <li><b>β_HV</b>: Human-to-vector transmission coefficient</li>
            <li><b>β_VH</b>: Vector-to-human transmission coefficient</li>
            <li><b>β_VV</b>: Vector-to-vector transmission coefficient</li>
            <li><b>γ_H</b>: Human recovery rate</li>
            <li><b>γ_V</b>: Vector recovery rate</li>
            <li><b>δ</b>: Disease-induced death rate</li>
            <li><b>ν</b>: Vaccination rate</li>
            <li><b>ω</b>: Waning immunity rate</li>
            <li><b>κ</b>: Rate to funeral component</li>
            <li><b>φ</b>: Funeral transmission rate</li>
        </ul>
        <h3>Initial Conditions</h3>
        <p>Adjust the initial number of individuals in each compartment:</p>
        <ul>
            <li>Susceptible Humans (S_H)</li>
            <li>Infectious Humans (I_H)</li>
            <li>Susceptible Vectors (S_V)</li>
            <li>Infectious Vectors (I_V)</li>
            <li>Recovered (R)</li>
            <li>Deceased (D)</li>
            <li>Funeral (F)</li>
        </ul>
        <h3>Scenarios</h3>
        <p>Choose a scenario to explore:</p>
        <ul>
            <li><b>Hospital Capacity</b>: Ensure hospitals are not overwhelmed by the number of infected people.</li>
            <li><b>Seasonal Variation</b>: Investigate how the epidemic would evolve with seasonal variations in transmission rates.</li>
            <li><b>Custom Scenario</b>: Design a scenario that investigates an additional factor or intervention of your choice.</li>
        </ul>
        <h3>Model Equations</h3>
        <p>The SI+SIRDF model is described by the following system of ordinary differential equations (ODEs):</p>
        """)

        st.latex(r"""
        \begin{aligned}
        \frac{dS_H}{dt} &= - \beta_{HH} \frac{S_H I_H}{N} - \beta_{HV} \frac{S_H I_V}{N} \\
        \frac{dI_H}{dt} &= \beta_{HH} \frac{S_H I_H}{N} + \beta_{HV} \frac{S_H I_V}{N} - \gamma_H I_H - \delta I_H \\
        \frac{dS_V}{dt} &= - \beta_{VV} \frac{S_V I_V}{N} - \beta_{VH} \frac{S_V I_H}{N} \\
        \frac{dI_V}{dt} &= \beta_{VV} \frac{S_V I_V}{N} + \beta_{VH} \frac{S_V I_H}{N} - \gamma_V I_V \\
        \frac{dR}{dt} &= \gamma_H I_H - \omega R \\
        \frac{dD}{dt} &= \delta I_H \\
        \frac{dF}{dt} &= \kappa F \\
        \end{aligned}
        """)

        st.markdown("""
        <h3>How to Use</h3>
        <ol>
            <li>Adjust the parameters and initial conditions using the sidebar.</li>
            <li>Select a scenario from the dropdown.</li>
            <li>Click "Run Simulation" to see the results.</li>
        </ol>
        <h3>Visualization</h3>
        <p>The results are displayed as interactive plots. You can hover over the lines to see specific values and use the toolbar for zooming and panning.</p>
        </div>
        """)

    st.sidebar.header("Model Parameters")
    scenario = st.sidebar.selectbox("Select Scenario", ["Hospital Capacity", "Seasonal Variation", "Funerary Transmission", "Safe and Dignified Burials"])

    default_params = {
        "Hospital Capacity": {
            "beta_HH": 0.3,
            "beta_HV": 0.2,
            "beta_VH": 0.1,
            "beta_VV": 0.05,
            "gamma_H": 0.1,
            "gamma_V": 0.05,
            "delta": 0.05,
            "nu": 0.05,
            "omega": 0.01,
            "kappa": 0.05,
            "phi": 0.05
        },
        "Seasonal Variation": {
            "beta_HH": 0.3,
            "beta_HV": 0.2,
            "beta_VH": 0.1,
            "beta_VV": 0.05,
            "gamma_H": 0.1,
            "gamma_V": 0.05,
            "delta": 0.05,
            "nu": 0.05,
            "omega": 0.01,
            "kappa": 0.05,
            "phi": 0.05
        },
        "Funerary Transmission": {
            "beta_HH": 0.3,
            "beta_HV": 0.2,
            "beta_VH": 0.1,
            "beta_VV": 0.05,
            "gamma_H": 0.1,
            "gamma_V": 0.05,
            "delta": 0.05,
            "nu": 0.05,
            "omega": 0.01,
            "kappa": 0.05,
            "phi": 0.05
        },
        "Safe and Dignified Burials": {
            "beta_HH": 0.3,
            "beta_HV": 0.2,
            "beta_VH": 0.1,
            "beta_VV": 0.05,
            "gamma_H": 0.1,
            "gamma_V": 0.05,
            "delta": 0.05,
            "nu": 0.05,
            "omega": 0.01,
            "kappa": 0.05,
            "phi": 0.01
        }
    }

    params = default_params[scenario]

    st.sidebar.header("Adjust Parameters")
    param_explanations = {
        "beta_HH": "β_HH (Human-to-human transmission coefficient)",
        "beta_HV": "β_HV (Human-to-vector transmission coefficient)",
        "beta_VH": "β_VH (Vector-to-human transmission coefficient)",
        "beta_VV": "β_VV (Vector-to-vector transmission coefficient)",
        "gamma_H": "γ_H (Human recovery rate)",
        "gamma_V": "γ_V (Vector recovery rate)",
        "delta": "δ (Disease-induced death rate)",
        "nu": "ν (Vaccination rate)",
        "omega": "ω (Waning immunity rate)",
        "kappa": "κ (Rate to funeral component)",
        "phi": "φ (Funeral transmission rate)"
    }

    for param, value in params.items():
        params[param] = st.sidebar.slider(f"{param_explanations[param]}", min_value=0.0, max_value=1.0, value=value, step=0.01)
        st.sidebar.write(f"Current {param_explanations[param]}: {params[param]}")

    st.sidebar.header("Initial Conditions")
    initial_conditions = {
        "S_H": st.sidebar.number_input("Initial Susceptible Humans (S_H)", value=9990),
        "I_H": st.sidebar.number_input("Initial Infectious Humans (I_H)", value=10),
        "S_V": st.sidebar.number_input("Initial Susceptible Vectors (S_V)", value=9990),
        "I_V": st.sidebar.number_input("Initial Infectious Vectors (I_V)", value=10),
        "R": st.sidebar.number_input("Initial Recovered (R)", value=0),
        "D": st.sidebar.number_input("Initial Deceased (D)", value=0),
        "F": st.sidebar.number_input("Initial Funeral (F)", value=0)
    }

    days = st.sidebar.number_input("Number of Days for Simulation", value=160)

    if st.sidebar.button("Run Simulation"):
        if scenario == "Hospital Capacity":
            hospital_capacity = 0.1 * sum(initial_conditions.values())
            results = run_simulation(params, initial_conditions, days)
            peak_infections = max(results['I_H'])
            if peak_infections > hospital_capacity:
                st.warning(f"Warning: Peak infections ({peak_infections}) exceed hospital capacity ({hospital_capacity})")
            plot_results(results)
        elif scenario == "Seasonal Variation":
            time_dependent_params = {
                'beta_HH': lambda t: params['beta_HH'] * (1 + 0.3 * np.sin(2 * np.pi * t / 365)),
                'beta_HV': lambda t: params['beta_HV'] * (1 + 0.3 * np.sin(2 * np.pi * t / 365)),
                'beta_VH': lambda t: params['beta_VH'] * (1 + 0.3 * np.sin(2 * np.pi * t / 365)),
                'beta_VV': lambda t: params['beta_VV'] * (1 + 0.3 * np.sin(2 * np.pi * t / 365))
            }
            results = run_simulation(params, initial_conditions, days, time_dependent_params=time_dependent_params)
            plot_results(results)
        elif scenario == "Funerary Transmission":
            funerary_transmission_params = {
                'phi': 0.1
            }
            results = run_simulation(params, initial_conditions, days, time_dependent_params=funerary_transmission_params)
            plot_results(results)
        elif scenario == "Safe and Dignified Burials":
            sdb_params = {
                'phi': 0.01
            }
            results = run_simulation(params, initial_conditions, days, time_dependent_params=sdb_params)
            plot_results(results)
        plot_scenarios(scenario, params, initial_conditions)

    st.sidebar.header("Optimization")
    data_file = st.sidebar.file_uploader("Upload real-world data", type=["csv"])
    if data_file is not None:
        observed_data = pd.read_csv(data_file)
        st.session_state.observed_data = observed_data
        st.write("Real-world data uploaded.")

    if st.sidebar.button("Generate Synthetic Data"):
        synthetic_data = generate_synthetic_data(params, initial_conditions, days)
        st.session_state.synthetic_data = synthetic_data
        st.write("Synthetic data generated.")

    if st.sidebar.button("Estimate Parameters"):
        if 'observed_data' in st.session_state:
            observed_data = st.session_state.observed_data
            initial_guess = [params[key] for key in params]
            estimated_params = estimate_parameters(observed_data, initial_guess, initial_conditions)
            st.write(f"Estimated Parameters: {estimated_params}")
        else:
            st.write("Please upload real-world data first.")

    with st.expander("Tutorial"):
        st.write("""
        ### How to Use the SI+SIRDF Model App
        1. **Adjust Parameters**: Use the sliders and number inputs in the sidebar to set the parameters and initial conditions.
        2. **Select a Scenario**: Choose from Hospital Capacity, Seasonal Variation, or Custom Scenario.
        3. **Run Simulation**: Click the "Run Simulation" button to execute the model and visualize the results.
        4. **Generate Synthetic Data**: Click the "Generate Synthetic Data" button to create data for testing the optimization.
        5. **Estimate Parameters**: Click the "Estimate Parameters" button to optimize and find the best-fit parameters based on the synthetic data.
        6. **Interpret Results**: Examine the interactive plots to understand how the disease dynamics evolve over time.
        """)

if __name__ == "__main__":
    main()
