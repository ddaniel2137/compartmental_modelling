# Epidemiology modeling <br> Systems of $O D E$ 

## Intro

Your task is to explore and model various aspects of epidemic outbreaks using the SIR (Susceptible, Infected, Recovered) family of models. This project is aiming to use mathematical modeling to predict and control the spread of infectious diseases in a scenario and perspective of your choice. Here is an example article where one of many possible aspects of disease spread is modeled.

## Tasks list

## 1. Select an aspect of epidemic outbursts to explore.

Choose one of the following aspects to focus your modeling on:

- Age groups: Analyze how different age groups are affected by an epidemic.
- Contact rate variations: Examine how variations in contact rates (e.g., due to lockdowns or social distancing) influence the spread of the disease.
- Seasonal effects: Explore how seasonality impacts the transmission rates of the disease.
- Geographic differences: Study how the epidemic spreads differently in urban vs. rural areas.
- Hospitalized, ICU, and infrastructure availability: how the public health services can cope with epidemics. How to control the infection rate to control the accessibility of infrastructure?
- Severity and Mortality: Diseases have different severity levels and death is usually a possible outcome, explore how it changes the modeling process.
- Other options: You can investigate any other aspect of disease spread.


## 2. Description of your SIR model capturing the chosen aspect.

For any aspect you choose to explore, provide the aims and general properties of the model you plan to implement, including:

- Describe what you are trying to model, what are the strategies to capture the targeted aspects of the epidemic.
- What are the key elements of the model that you want to investigate? Which parameter or compartment change will be of interest to you, and why? What does it represent? (This is to ensure that we can interpret the model's behavior).
- In applications, what would be the potential sources of data to estimate the parameters of the model (e.g., age structure from national statistics, vaccine efficacy from clinical trial data, etc.)?
- any other important modeling decisions that you will make.


## 3. Introduce Model Parameters and Compartments.

Define all the parameters and compartments introduced in your model. Provide brief meaning/interpretations for each of them, explaining their significance and how they relate to the real world. Parameters might include:

- Transmission rate $(\beta)$ - is it a complex factor influenced by any social measures?
- Recovery rate $(\gamma)$ - is it influenced by anything? Introduction of the novel medicine that can boost the recovery process?
- if applicable, vaccination rate - can it be collected from any real data resources?
- if applicable, contact rate variations - how contact rates differ between subpopulations, and why? What is the source for these differences?


## 4. Discuss Initial conditions of your model.

Describe the initial conditions for your model, ensuring they are interpretable and realistic. This should include:

- Population size.
- Initial number of infected individuals.
- fixed parameters that you will not explore further explore.
- Any other relevant initial conditions specific to your chosen aspect.


## 5. Design Three Exploratory Scenarios.

Consider and explore three scenarios that question different realities regarding the data and forecasting of the epidemic:

Scenario 1: Hospital Capacity Assume the hospital capacity is $0.1 \times N$, where $N$ is the population size in your model. Determine the parameters that can be controlled by social restrictions (e.g., the $\beta$ parameter, which must be included in your model regardless of the SIR model extension you use) to ensure hospitals are not overwhelmed by the number of infected people (the peak of infections should not exceed the threshold).

Scenario 2: Seasonal Variation Investigate how the epidemic would evolve with seasonal variations in transmission rates (i.e., $\beta$ ) or any other parameter of your choice. One way to do this is to run the model iteratively with different parameter settings. Specifically, run the model for a given time interval, then take the values of all states and use them as initial values for the next run of the model with the different parameters. Consider at least three time points for parameters reset.

Scenario 3: Custom scenario Design a scenario that investigates an additional factor or intervention of your choice, based on your initial aspect of interest. It can cover variation of specific parameters value and its impact on scores of your choice.

For each of the above scenario present (visualize with trajectories) how parameters (especially contact rates $(\beta)$ influence the dynamics of the epidemic spread. Point out under which parameters' change the model is the most sensitive - meaning, small changes of values introduce strong qualitative changes. The descriptions do not need to be very extensive, however they need to exemplify and interpret how the general behavior of the model (trajectories) changes under the initial conditions/parameters shifts.

## 6. Data generation tool.

Use your system of equations to generate synthetic data. However, this data should be disturbed with:

- Seasonal variations (e.g., using a sinusoidal function),
- Random noise (e.g., Gaussian noise).

to simulate real-world data inaccuracies. Prepare functions that will allow you to set initial conditions and parameters and store the time series data, that you will use in the last task.

## 7. Prediction Using Optimization.

With the generated data, use optimization strategies (e.g., the minimize function from scipy.optimize) to predict the model's parameters and the time series values of different compartments, given the observable part of the generated data (e.g., number of infected individuals over time and/or number of vaccinated individuals over time).

Run example predictions on at least two out of the three scenarios considered in the previous steps. Present your estimation results and discuss how well your model fits the generated data. Did it work? How well? Are there any limitations of your model?

## Task grading

The solution to this computational problem is: (i) a python code with functions that can perform the above tasks, (ii) a presentation/report on your results with your comments regarding each task. Visualizations of trajectories, discussion over parameters, and formulation of conclusions (whenever a task requires that) are necessary for the report to be complete. Both should be dropped at your GitHub. Additionally, remember to fill-in the information about the repository in the Excel Sheet at the course's Moodle.

The programming part (implementation of the model) can be done in pairs, and this must be mentioned in the report. However, the final examples of trajectories selected to discuss the model dynamics in the report (see task 5. and 7.) should be done individually to ensure that everyone can interpret the model's outputs. To accomplish the task, you can use the materials from Moodle (see the 06_compex_generation.py Python script), resources from the internet, or assistance from GPT. Again, the most important part is that you are able to present, interpret, and discuss your work and results in the form of a written report.

The deadline for this Task is 04.06.2024, 23:59 - meaning any commit on GitHub after this deadline will receive up to $10-($ days_of _delay) points.

