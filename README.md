
# SEIRV Epidemiology Modeling Project

## Overview
This project models and analyzes various aspects of epidemic outbreaks using the SEIRV (Susceptible, Exposed, Infected, Recovered, Vaccinated) framework. It includes a rich graphical user interface (GUI) built with Streamlit and uses Gurobi for optimization. Users can explore various scenarios and compartments to understand the dynamics of disease spread.

## Project Structure
```
SEIRV_Modeling_Project/
│
├── data/
│   ├── synthetic_data.csv          # Synthetic data generated for model validation
│   ├── real_world_data.csv         # (Optional) Real-world data for model comparison
│
├── notebooks/
│   ├── exploration.ipynb           # Jupyter notebook for exploratory data analysis
│   ├── optimization.ipynb          # Jupyter notebook for testing optimization
│
├── src/
│   ├── __init__.py                 # Initialize the src package
│   ├── seirv_model.py              # SEIRV model implementation
│   ├── data_generation.py          # Data generation functions
│   ├── optimization.py             # Optimization functions using Gurobi
│   ├── visualization.py            # Functions for plotting and visualizations
│   ├── streamlit_app.py            # Main Streamlit app
│
├── tests/
│   ├── test_seirv_model.py         # Unit tests for the SEIRV model
│   ├── test_data_generation.py     # Unit tests for data generation
│   ├── test_optimization.py        # Unit tests for optimization functions
│
├── README.md                       # Project overview and instructions
├── requirements.txt                # Required libraries and dependencies
├── setup.py                        # Setup script for packaging and installation
└── LICENSE                         # License for the project
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd SEIRV_Modeling_Project
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scriptsctivate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

1. **Navigate to the `src` directory:**
   ```bash
   cd src
   ```

2. **Run the Streamlit app:**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Open your web browser and go to the provided URL (typically `http://localhost:8501`):**

## Usage

- **Adjust Model Parameters:** Use the sidebar in the Streamlit app to adjust the parameters such as transmission rate, progression rate, recovery rate, mortality rate, and vaccination rate.
- **Run Simulation:** Click the "Run Simulation" button to see the results of the SEIRV model with the specified parameters.
- **View Results:** The app will display the results in the form of interactive plots showing the dynamics of the different compartments (Susceptible, Exposed, Infected, Recovered, Vaccinated) over time.

## Project Components

- **`data/`:** Contains synthetic data generated for model validation and (optionally) real-world data for comparison.
- **`notebooks/`:** Jupyter notebooks for exploratory data analysis and optimization testing.
- **`src/`:** Source code for the model, data generation, optimization, visualization, and the Streamlit app.
- **`tests/`:** Unit tests for different components of the project.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

If you have any questions or need further assistance, please contact [Your Name] at [Your Email].
