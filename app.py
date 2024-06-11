import streamlit as st
from src.models import SEIRDVFModel
from src.simulation import run_simulation
from src.visualization import plot_results, plot_scenarios
from src.utils import generate_synthetic_data, estimate_parameters
import numpy as np
import pandas as pd

def main():
    st.title("SEIRDVF Epidemic Model Simulation")

    with st.expander("SEIRDVF Model Documentation", expanded=False):
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
        <h2>SEIRDVF Model Documentation</h2>
        <p>This app allows you to simulate the SEIRDVF model for epidemic spread. Adjust parameters using the sidebar and view the results in real-time.</p>
        <h3>Parameters</h3>
        <ul>
            <li><b>β</b>: Transmission coefficient</li>
            <li><b>σ</b>: Rate at which exposed individuals become infectious</li>
            <li><b>γ</b>: Recovery rate</li>
            <li><b>δ</b>: Disease-induced death rate</li>
            <li><b>ν</b>: Vaccination rate</li>
            <li><b>ω</b>: Waning immunity rate</li>
            <li><b>κ</b>: Rate to funeral component</li>
            <li><b>φ</b>: Funeral transmission rate</li>
        </ul>
        <h3>Initial Conditions</h3>
        <p>Adjust the initial number of individuals in each compartment:</p>
        <ul>
            <li>Susceptible (S)</li>
            <li>Exposed (E)</li>
            <li>Infectious (I)</li>
            <li>Recovered (R)</li>
            <li>Deceased (D)</li>
            <li>Vaccinated (V)</li>
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
        <p>The SEIRDVF model is described by the following system of ordinary differential equations (ODEs):</p>
        """, unsafe_allow_html=True)

        st.latex(r"""
        \begin{aligned}
        \frac{dS}{dt} &= - \beta \frac{S (I + \phi F)}{N} - \nu S + \omega R + \omega V \\
        \frac{dE}{dt} &= \beta \frac{S (I + \phi F)}{N} - \sigma E \\
        \frac{dI}{dt} &= \sigma E - \gamma I - \delta I \\
        \frac{dR}{dt} &= \gamma I - \omega R \\
        \frac{dD}{dt} &= \kappa F \\
        \frac{dV}{dt} &= \nu S - \omega V \\
        \frac{dF}{dt} &= \delta I - \kappa F \\
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
        """, unsafe_allow_html=True)

    st.sidebar.header("Model Parameters")
    scenario = st.sidebar.selectbox("Select Scenario", ["Hospital Capacity", "Seasonal Variation", "Funerary Transmission", "Safe and Dignified Burials"])

    default_params = {
        "Hospital Capacity": {
            "beta": 0.3,
            "sigma": 0.2,
            "gamma": 0.1,
            "delta": 0.05,
            "nu": 0.05,
            "omega": 0.01,
            "kappa": 0.05,
            "phi": 0.05
        },
        "Seasonal Variation": {
            "beta": 0.3,
            "sigma": 0.2,
            "gamma": 0.1,
            "delta": 0.05,
            "nu": 0.05,
            "omega": 0.01,
            "kappa": 0.05,
            "phi": 0.05
        },
        "Funerary Transmission": {
            "beta": 0.3,
            "sigma": 0.2,
            "gamma": 0.1,
            "delta": 0.05,
            "nu": 0.05,
            "omega": 0.01,
            "kappa": 0.05,
            "phi": 0.05
        },
        "Safe and Dignified Burials": {
            "beta": 0.3,
            "sigma": 0.2,
            "gamma": 0.1,
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
        "beta": "β (Transmission coefficient)",
        "sigma": "σ (Rate at which exposed individuals become infectious)",
        "gamma": "γ (Recovery rate)",
        "delta": "δ (Disease-induced death rate)",
        "nu": "ν (Vaccination rate)",
        "omega": "ω (Waning immunity rate)",
        "kappa": "κ (Rate to funeral component)",
        "phi": "φ (Funeral transmission rate)"
    }

    for param, value in params.items():
        if scenario == "Hospital Capacity" and param not in ["beta"]:
            st.sidebar.write(f"{param_explanations[param]}: {value}")
        elif scenario == "Seasonal Variation" and param not in ["beta"]:
            st.sidebar.write(f"{param_explanations[param]}: {value}")
        else:
            params[param] = st.sidebar.slider(f"{param_explanations[param]}", min_value=0.0, max_value=1.0, value=value, step=0.01)
            st.sidebar.write(f"Current {param_explanations[param]}: {params[param]}")

    st.sidebar.header("Initial Conditions")
    initial_conditions = {
        "S": st.sidebar.number_input("Initial Susceptible (S)", value=9990),
        "E": st.sidebar.number_input("Initial Exposed (E)", value=10),
        "I": st.sidebar.number_input("Initial Infectious (I)", value=1),
        "R": st.sidebar.number_input("Initial Recovered (R)", value=0),
        "D": st.sidebar.number_input("Initial Deceased (D)", value=0),
        "V": st.sidebar.number_input("Initial Vaccinated (V)", value=0),
        "F": st.sidebar.number_input("Initial Funeral (F)", value=0),
    }

    days = st.sidebar.number_input("Number of Days for Simulation", value=160)

    if st.sidebar.button("Run Simulation"):
        if scenario == "Hospital Capacity":
            hospital_capacity = 0.1 * sum(initial_conditions.values())
            results = run_simulation(params, initial_conditions, days)
            peak_infections = max(results['I'])
            if peak_infections > hospital_capacity:
                st.warning(f"Warning: Peak infections ({peak_infections}) exceed hospital capacity ({hospital_capacity})")
            plot_results(results)
        elif scenario == "Seasonal Variation":
            time_dependent_params = {
                'beta': lambda t: params['beta'] * (1 + 0.3 * np.sin(2 * np.pi * t / 365))
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
        ### How to Use the SEIRDVF Model App
        1. **Adjust Parameters**: Use the sliders and number inputs in the sidebar to set the parameters and initial conditions.
        2. **Select a Scenario**: Choose from Hospital Capacity, Seasonal Variation, or Custom Scenario.
        3. **Run Simulation**: Click the "Run Simulation" button to execute the model and visualize the results.
        4. **Generate Synthetic Data**: Click the "Generate Synthetic Data" button to create data for testing the optimization.
        5. **Estimate Parameters**: Click the "Estimate Parameters" button to optimize and find the best-fit parameters based on the synthetic data.
        6. **Interpret Results**: Examine the interactive plots to understand how the disease dynamics evolve over time.
        """)

if __name__ == "__main__":
    main()
