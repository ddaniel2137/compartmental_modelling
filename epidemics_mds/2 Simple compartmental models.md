# Simple compartmental models The bedrock of mathematical epidemiology 

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-01.jpg?height=152&width=119&top_left_y=227&top_left_x=1248)


#### Abstract

The statistician knows ... that in nature there never was a normal distribution, there never was a straight line, yet with normal and linear assumptions, known to be false, he can often derive results which match, to a useful approximation, those found in the real world.


Box, "Science and Statistics", $1976[2]$

### 2.1 The intuition of compartmental models

Compartmental models are the bread and butter of infectious disease modeling. The development of compartmental models by Kermack and McKendrick, building on earlier work by Sir Ronald Ross (1857-1932) and Hilda Phoebe Hudson (1881-1965), represented the first rigorous mathematical treatment of infectious disease dynamics, transforming what was a mostly qualitative inquiry into a scientifically rigorous discipline. This section examines basic compartmental models as the building blocks of more complex structures in the modeling of infectious disease.

### 2.1.1 Case study: influenza A outbreak on Tristan da Cunha

The small British Crown dependency of Tristan da Cunha is one of the most isolated points on the planet. Over 1700 miles off the coast of South Africa, it is home to fewer than 300 permanent inhabitants. The island's capital, Edinburgh of the Seven Seas, is commonly considered to be the most remote permanent human settlement. Without suitable ground for a paved airstrip, Tristan da Cunha's only lifeline to the outside world is by sea.

In 1971, the supply ship Tristania brought an unwelcome stowaway to the island: the alphainfluenzavirus H3N2, known as the Hong Kong flu at the time. By winter's end, $96 \%$ of the population would contract influenza, with almost a third experiencing at least two distinct episodes of illness [43].

Isolated settings, such as Tristan da Cunha, are the closest reality ever tends to come to the simple compartmental models that take no account of migration, demographic changes (births and deaths) and other more complex processes. Though reality tends to be much more complicated than compartmental models give it credit for, such models are mathematically convenient and close enough to the real world to be valuable sources of illumination. We shall therefore use them to begin our journey through the mathematical and computational modeling of infectious disease.

In this section, we will be looking at the basic notions of a compartmental model. Such models are enticingly simple without being overly simplistic, and offer the
benefit of being quite easy to represent mathematically using systems of ordinary differential equations.

Compartmental models are in many ways the Lego bricks of quantitative epidemiology: they can be combined and almost endlessly expanded. For instance, a model that has a single compartment for "removed" cases can be expanded to include separate compartments for survival and mortality. This in turn can be broken down to characterize various forms of survival: survival with sequelae, survival without sequelae, and so on. The variety and complexity of compartmental models is limited only by imagination; SIDARTHE, for instance, is a model of COVID-19 transmission composed of eight compartments [44]. Yet no matter the complexity, compartmental models all follow the same basic mathematical notions, so that exploring an adequate but nonexhaustive sample of compartmental models suffices to provide infectious disease modelers with blueprints from which they can adapt and construct ever more ambitious models to fit specifications.

### 2.1.2 Defining compartments

The fundamental intuition of compartmental models is that if we define a number of mutually exclusive but jointly exhaustive states, we can characterize every individual's course through the disease process as state transitions at given times (e.g., from susceptible to infectious and from infectious to recovered) [13]. Given a population, then, we can estimate the rate at which these state transitions occur.

Definition 2.1 (Partition). A set of $n$ nonempty subsets $\mathcal{S}_{1 \ldots . n}$ is a partition of a set if every element of that set belongs to exactly one subset.

This gives us a very convenient mean-field model, so that instead of having to track each person individually, we may simply conceive of "flows" between compartments (states) at a given rate that reflects the approximate likelihood of subjects in one compartment to transition into another. In this way, we can characterize an entire pathogenic process in a population by the size of the compartments at the start (commonly denoted as $t_{0}$ ) and the volume of flow between those compartments. We can then represent the entire system as a set of ordinary differential equations (ODEs), which in turn lays the dynamics governing the system open to mathematical investigation and modeling. This is the "skeleton key" to much of the mathematical—and with that, computational—reasoning about infectious disease.

Compartments solve the thorny problem of relatively large populations, which would otherwise make such computations more difficult. The total population in a model may be a rather large figure; it was not until relatively recent days that the computing power required to operate large-scale agent-based models (which are discussed at length in Chapter 9) has become ubiquitous, and even so, there are limits to the size of agent-based models that can be feasibly run. It is often more efficient to look not at individuals but at populations and their mean-field governing statistical dynamics, just as statistical mechanics can make generalized statements about the whereabouts and behaviors of particles without having to account for each individual

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-03.jpg?height=242&width=763&top_left_y=226&top_left_x=383)

Figure 2.1 Flow diagram of a generic compartmental model with two compartments ( $C_{1}$ and $C_{2}$ ), a constant-rate influx and outflow ( $\mu$ ), and a loopback from $C_{1}$ to $C_{2}$ at the rate of $\rho$.

particle. The benefit of the compartmental formalism is that it is robust to the total population size; subject to the issue of value overflows, the time complexity of solving a system of ODEs is not computationally dependent on the number of individuals or the total quantities.

A compartment, in the context of infectious disease modeling, denotes both a state and the set of all individuals from the entire population (which by convention we shall refer to as $N$ ) that are in a particular state. Rather than tracking each member individually, we consider clinically coherent groups of patients-the compartments in question-and look at the sum total of "state changes" by patients through the lens of flows between compartments.

Definition 2.2 (Compartment). A compartment is a set of individuals in the population, who share a characteristic relevant for the modeling of infectious disease (e.g., all recovered alive persons). Every compartment is a subset of the set $N$ of all individuals in the model. The set of all compartments is a partition of $N$.

Fig. 2.1 is an example of a generic compartmental model. There are two compartments, $C_{1}$ and $C_{2}$. The rate of flow between $C_{1}$ and $C_{2}$ is governed by the parameter $\beta$, the rate of reflux is $\rho$. This example also hints at the fact that not all compartmental models are closed systems; the number of individuals within the system changes, through the parameters of $\mu$ and $\gamma$ (e.g., immigration/emigration, births and deaths). The representation adopted in Fig. 2.1 is called a flow diagram, in which we denote compartments by rectangles, flows by arrows, and the rate of flow by labels over the arrows.

Over the course of our journey through various models of infectious disease propagation, we will encounter a range of increasingly intricate flow diagrams of compartments. They will be our mappa mundi to help us understand anything from simple SIR models to multilayered host-pathogen interactions. At the heart of compartmental models lie three fundamental axioms:

Definition 2.3 (Closed system axiom). Subject to demographic change (immigration, emigration, deaths, and births), the sum of each compartment's cardinality at any given time $t$ is $N$. Subject to demographic change (immigration, emigration, deaths, and births), the sum of all flows is zero.

This follows from the fact that every patient in $N$ is accounted for in exactly one compartment at any given time, which in turn is a consequence of our definition of compartments in a way that the set of all nonempty compartments is a partition of $N$.

Definition 2.4 (Partition property axiom). The set of all nonempty compartments at time $t$ is a partition of $N(t)$, the population at time $t$.

From the partition property follows that every element of $N$ is in exactly one-no more, no fewer-compartment at any given time (or inversely, the sum of the cardinalities of the compartments is $N$ ). As such, we can comfortably represent individuals by flows between compartments without the risk of information loss (as would be the case if a person could be in multiple compartments at the same time).

Definition 2.5 (Markov property axiom). The cardinality of any compartment at any time $t \geq t_{0}$ can be determined from the state of the system at $t_{0}$ (its initial conditions) if the system can be described by an autonomous and deterministic ODE.

Definition 2.6 (Autonomous and nonautonomous systems of ODEs). A system of ODEs is autonomous if and only if its right-hand side is independent of $t$.

This can be proven by recursion. For discrete time, the Markov property means that the state of the system at $t+1$ is a function of the state of the system at $t$. That state, in turn, is a function of the state of the system at $t-1$, and so on until $t_{0}$. The corresponding proof for continuous time is left to the reader, but should not prove difficult. Compartmental models that fit the first two criteria but incorporate a Wiener process or some other source of stochasticity are known as stochastic compartmental models. Those that integrate a time-dependent function on the right-hand side are known as nonautonomous.

Definition 2.7 (Stochastic versus deterministic compartmental models). A compartmental model is deterministic if it strictly complies with the Markov property axiom, and otherwise stochastic.

We will generally not discuss stochastic compartmental models, because other highly stochastic compartmental models, such as agent-based models (see Chapter 9) often reflect stochasticity better. Keeling and Rohani [39] provide an outstanding survey of stochastic models that an interested reader might enjoy.

Together, these three axioms underlie our ability to represent the entire model as a system of ordinary differential equations. In the remainder of this chapter, we will be making use of these axioms in practice as we examine some basic compartmental models.

## Computational Note 2.1 ODE solvers

We reason about flows using ordinary differential equations (ODEs) and, in some cases, delay differential equations (DDEs) and partial differential equations (PDEs). The numerical solutions for ODEs are performed by the use of integrating ODE solvers. These solve a class of problems for ODEs known as initial value problems (IVPs): given some initial conditions (e.g., the sizes of the compartments at time zero), a set of parameters, and a system described by some
differential equations, what will the state of the system be at an arbitrary time $t>0$ ?

Until quite recently, the workhorse of such operations in Python was the scipy.integrate.odeint function, which wrapped around the venerable ODEPACK library written in FORTRAN. This has been significantly overhauled by the solve_ivp API, which incidentally also allows a number of different methods (mainly of the Runge-Kutta family, but also including backward differentiation) to be employed. In this text, we shall predominantly use the new API. An important practical difference is that whereas odeint takes a differential function of the form $\frac{d y}{d t}=f(y, t, \ldots)$, i.e., specifying $y$ first, solve_i vp takes a "time-first" specification $\frac{d y}{d t}=f(t, y, \ldots)$. Framing the derivative function with the arguments in the right order for the respective API is thus essential.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch02/ s ir_ models.

### 2.1.3 The principle of mass action

The fundamental assumption of compartmental models is that a fundamentally homogeneous mixing of the populations is occurring in a manner resembling Brownian motion, i.e., that every member of the population is in contact with every other one, and the likelihood of any person in any compartment interacting with any other is equal. Consequently, infection depends on the likelihood of transmission upon an encounter, and the likelihood of the encounter itself. The former is typically described as a parameter $\beta$. The latter results from the product of the proportion of susceptibles and the proportion of infectious individuals in the population. Together, they give us the transmission term or mass action term, $\beta S I$, which we will encounter repeatedly through our journeys across the realm of compartmental models.

Definition 2.8 (Mass action). By mass action, we denote the probabilistic nature of infectious disease transmission that depends on both the number of infected and the number of infectible individuals. Mathematically expressed, $\frac{d I}{d t} \propto S, I$. The proportionality is conditioned by the transmission coefficient $\beta$, which describes the likelihood of transmission upon an encounter eligible to create a transmission event, whereas SI describes the likelihood of such events occurring. The overall term $\beta S I$ represents the rate at which infectious $(I)$ and susceptible $(S)$ individuals encounter each other and transmission takes place. We refer to this as the mass action term.

It may be helpful to derive this term due to its fundamental nature. Let us assume a population of $\mathcal{N}$, of whom $\mathcal{S}$ are susceptible and $\mathcal{I}$ are infected (with $S$ and $I$, respectively, being the proportion of these compartments within $N$ ). Recall that we use the notation $\mathcal{C}$ for the absolute number of members in a compartment and $C$ for the fraction $\frac{\mathcal{C}}{N}$, the proportion of that compartment in the total model population. If a
susceptible individual meets $n$ individuals in unit time, some of these will be infectious. We know that $I=\frac{\mathcal{I}}{N}$ describes the proportion of individuals who are infectious, which under the assumption of homogeneous mixing equates to the likelihood that any randomly encountered individual will be infectious. For every encounter, the likelihood that the other party was infectious is $I$, and for $n$ encounters, it is $n I$. We may generalize this for any timespan $\Delta_{t}$ as $n I \Delta_{t}$.

Then, we assume that following a contact, there is a $p_{i}$ probability of infection. The likelihood thus of a contact not resulting in an infection is $1-p_{i}$. The likelihood that our susceptible person is infected after $\Delta_{t}$ time is

$$
\begin{equation*}
p_{S, I}=1-\left(1-p_{i}\right)^{n I t} \tag{2.1}
\end{equation*}
$$

If we substitute $\beta$ for $-n \log \left(1-p_{i}\right)$ and insert it into (2.1), we get

$$
\begin{equation*}
p_{S, I}=1-e^{-\beta I t} \tag{2.2}
\end{equation*}
$$

The limit of this expression is then

$$
\begin{equation*}
\lim _{t \rightarrow 0} \frac{1-e^{-\beta I t}}{t}=\beta I \tag{2.3}
\end{equation*}
$$

The above is often referred to as the force of infection, $\lambda$.

Definition 2.9 (Force of infection). The force of infection $\lambda$ is the likelihood of infection per unit time. It is often also expressed as the rate per capita of acquiring the infection.

Since the force of infection describes the per capita rate of acquiring the infection, we must multiply this by the amount of susceptibles $\mathcal{S}$ to obtain the rate of new infections. This term will have a negative sign, since it is a flow out of the pool of susceptible individuals and into the pool of infectious ones:

$$
\begin{equation*}
\frac{d S}{d t}=-\underbrace{\lambda}_{\text {force of infection susceptibles }} \underbrace{S} \tag{2.4}
\end{equation*}
$$

Since $\lambda=\beta I$, (2.4) becomes the mass action term

$$
\begin{equation*}
\frac{d S}{d t}=-\underbrace{\beta I}_{\text {mass action }} \underbrace{S}_{\text {force of infection susceptibles }} \tag{2.5}
\end{equation*}
$$

By convention, we write this in the order $\beta S I$. Beyond its mathematical importance, the mass action term tells us something important about infectious diseases, namely that the likelihood of their spread, under the assumption of homogeneous mixing, depends on the relative sizes of the infectious and the susceptible populations.

- There can be no epidemic without any infectious individuals; this is the idea at the heart of eradication and quarantines.

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-07.jpg?height=103&width=659&top_left_y=230&top_left_x=435)

Figure 2.2 Flow diagram of a basic SIR model. $\beta$ is the transmission coefficient, a term that accounts for the frequency of interactions between susceptible and infectious individuals. $\gamma$ is the removal rate; it reflects the rate at which infectious individuals become no longer infectious.

- There can also be no epidemic without any susceptible individuals, that is, the basic driving idea of vaccination and pre-exposure prophylaxis.
- Finally, there can be no epidemic without mixing of populations, which is the principle that underlies social distancing.

The principle of mass action provides a mathematical way of interpreting and analyzing the touchpoint between infectious and susceptible populations. As such, it is the cornerstone on which much of our subsequent compartmental modeling is built.

### 2.1.4 A basic SIR model

The simplest of all compartmental models is the SIR model for a closed population (i.e., a population with no demographic change). A flow diagram of such a model is presented in Fig. 2.2.

Definition 2.10 (Constant and closed populations). In a model with a constant population, the total population is a constant and always equal to the sum of the population of all compartments. Formally, in a closed population with $n$ compartments $C_{1 \ldots n}$, it holds for all $t$ that

$$
\frac{d N}{d t}=\sum_{i=1}^{n} \frac{d C_{i}}{d t}=0
$$

A population is closed if there are no inflows and no outflows.

This model is conditioned by two key parameters: the transmission coefficient $\beta$, which reflects the likelihood that an encounter between a susceptible and an infectious individual results in transmission, and the removal rate $\gamma$, which accounts for the rate at which infectious individuals are removed, i.e., become immune, deceased or otherwise inaccessible to the pathogen. Their relationship is encapsulated in the system of differential equations that represents SIR models:

$$
\begin{align*}
& \frac{d S}{d t}=-\underbrace{\beta S I}_{\text {mass action }}, \\
& \frac{d I}{d t}=\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\gamma I}_{\text {recovery }}, \tag{2.6}
\end{align*}
$$

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-08.jpg?height=663&width=1026&top_left_y=229&top_left_x=212)

Figure 2.3 Solution of a typical SIR model with $\Re_{0}=2.5$ and $\tau=8$.

$$
\frac{d R}{d t}=\underbrace{\gamma I}_{\text {recovery }}
$$

In the following, we are going to examine, first, the assumptions underlying the SIR model, followed by its key relationships, and concluding in analytical and numerical approaches.

## Computational Note 2.2 Solving ODEs in Python

Solving an initial value problem for a system of ODEs in Python generally proceeds in two stages. First, we need to describe the ODE as a function, then pass it onto the solver. The way of specifying a system of ODEs as a function might appear somewhat idiosyncratic at first. The overarching idea is that the function defining the ODEs will be called repeatedly with its own output passed to it as a tuple. For this reason, we will have to destructure the tuple input from the previous iteration.

Let us consider the system of differential equations from (2.6). As we transpose this to a Python function (by convention, the function describing the ODE is called deriv), we must consider this destructuring. The solver passes at least two arguments to the function describing the ODE. The first of these (again by convention, denoted $\mathrm{y}$ ), is a tuple containing the results of the previous iteration, which we will have to break down to be reused. The differential equation for a simple SIR model would thus be described as follows:

```
def deriv(t, y, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt
```

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch02/ sir_ models.

The simple SIR model makes four fundamental assumptions:

1. Static (or closed) population: $\mathcal{S}+\mathcal{I}+\mathcal{R}=N$ and consequently, $\frac{d S}{d t}+\frac{d I}{d t}+\frac{d R}{d t}=$ 0 . This holds for $\frac{d \mathcal{S}}{d t}, \frac{d \mathcal{I}}{d t}$ and $\frac{d \mathcal{R}}{d t}$, too.
2. Homogeneous mixing: every member of $S$ has the same likelihood (namely, $S I$ ) to encounter someone in $I$.
3. Equal outcomes: there is a single outcome of infection, and every infected person is equally likely to experience that outcome. This outcome is represented by the $\gamma$ term.
4. Survival confers immunity: it is assumed in this model that a removed person gains life-long immunity (or dies, which from the perspective of viral dynamics is altogether not all that different).

Definition 2.11 (Homogeneous mixing). Under homogeneous mixing, the likelihood of infection is identical for every infectious and every susceptible individual.

Let $S$ be the set of susceptible individuals $S_{1 \ldots m}$ and $I$ the set of all infectious individuals. $S$ and $I$ are said to be homogeneously mixed if the likelihood of encounter between any randomly selected members of $I$ and $S$ are equal, namely $S I$.

These assumptions are, of course, broad and sweeping generalizations that do not quite align with reality. Mixing, in practice, is far from homogeneous; we do not, in any meaningful sense, encounter every other individual in our population with equal likelihood. However, at a large enough scale, the actual patterns of encounters we do experience are adequately approximated by the homogeneity assumption. Thus the SIR model is a good first approximation of complex realities, and a good first step towards mathematically interpretable models of infectious disease.

## Computational Note 2.3 Phase portraits

A useful tool to characterize the population approaching equilibrium is the phase portrait. A phase portrait is a quite simple plot of two compartment values, typically $S$ and $I$, against each other. The following snippet plots a phase portrait from the output of the ODE solver:

```
fig = plt.figure(facecolor="w", figsize=(4, 4))
ax = fig.add_subp1ot(111, axisbelow=True)
ax.plot(S, I)
ax.set_ylabel("Fraction of infectious")
ax.set_x7abel("Fraction of susceptible")
plt.show()
```

The phase portrait can be understood as a view of how a dampened oscillation eventually converges upon an equilibrium. Fig. 2.4 shows the phase portrait of the SIR model we solved in Computational Note 2.2. The infectious process starts from the right lower corner and gradually converges on the equilibrium point. This type of phase portrait, with a gradually decreasing radius from a stable equilibrium point, is sometimes referred to as a spiral sink and suggests a process gradually converging on an equilibrium.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch02/ phase_ space.

### 2.1.5 The basic reproduction number $\mathfrak{R}_{0}$

As we have noted above, our basic SIR model has two main parameters: $\beta$, which is associated with the rate at which new cases are created, and $\gamma$, which is associated with the rate at which individuals cease to be infectious.

- If $\beta>\gamma\left(\frac{\beta}{\gamma}>1\right)$, the number of infections will increase.
- If $\beta=\gamma\left(\frac{\beta}{\gamma}=1\right)$, a case is lost by way of recovery for each new case gained by way of infection. The number of infectious individuals remains constant.
- If $\beta<\gamma\left(\frac{\beta}{\gamma}<1\right)$, more cases are lost by recovery than are gained through infection. The number of infectious will decrease and the infection will die out.

Thus the ratio between $\beta$ and $\gamma$ characterizes the long-term destiny of the pathogenic process. The ratio of $\beta$ to $\gamma$ describes the number of new cases that an infectious case produces, under the assumption that the entire population is immunologically naive (i.e., everyone except the index infectious patient is susceptible), it is a dimensionless quantity that characterizes the infectiousness of a pathogen. We term this fraction the basic reproduction number, represented by $\Re_{0}$ (pronounced "rnought" and not to be confused with $R(0)$ ). This relationship between $\beta, \gamma$ (by way of its inverse, $\tau$ ) and $\mathfrak{R}_{0}$ is illustrated in Fig. 2.5. Table 2.1 lays out the estimated $\mathfrak{R}_{0}$ values for some common pathogens.

Definition 2.12 (The basic reproduction number $\mathfrak{R}_{0}$ ). The basic reproduction number $\mathfrak{R}_{0}$ is the expectation of cases produced by an infectious case in a population, where every other individual is assumed to be susceptible.

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-11.jpg?height=1459&width=1073&top_left_y=222&top_left_x=226)

Figure 2.4 Phase portrait of the SIR model for $\mathfrak{R}_{0}=3.5, \tau=5$ and $\mu=0.02$ year. The red and blue dotted lines denote the $S$ and $I$ nullclines, respectively.

As a first approximation, it may be helpful to consider the forces governing $\Re_{0}$. Simply put, $\Re_{0}$ is the number of infections created during a person's infectious state We may thus conceptualize $\mathfrak{R}_{0}$ as proportional to the product of the encounter rate (encounters per unit time), the transmission ratio (transmissions per encounter), and the mean infectious period $\tau$ :

$$
\begin{equation*}
\mathfrak{R}_{0} \propto \frac{\text { encounters }}{\text { time }} \times \frac{\text { transmission }}{\text { encounters }} \times \tau \tag{2.7}
\end{equation*}
$$

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-12.jpg?height=1685&width=1184&top_left_y=280&top_left_x=135)

Figure 2.5 Simulations of epidemic curves for a range of $\Re_{0}$ and $\tau$ values under the assumption of a wholly susceptible population with 0.01 percent initial infected.

Table 2.1 $\mathfrak{R}_{0}$ values of some well-known pathogens.

| Pathogen | $\boldsymbol{\Re}_{\mathbf{0}}$ |  |
| :--- | :---: | :--- |
| Measles | $12.0-18.0$ | Guerra et al. [45] |
| Mumps | $4.0-10.0$ | Deeks et al. [46] |
| Smallpox | $3.0-5.0$ | Costantino et al. [47] |
| HIV | $3.6-4.7$ | Nishiura [48] |
| COVID-19, Delta variant | $2.3-7.0$ | Liu and Rocklöv [49] |
| COVID-19, ancestral strain | $1.4-3.1$ | Billah, Miah, and Khan [50], Mallela et al. |
|  |  | [51] |
| Zaire ebolavirus | $1.4-1.8$ | Khan et al. [52] |
| Influenza A, H1N1, recent | $1.4-1.6$ | Coburn, Wagner, and Blower [53] |
| Influenza A, H1N1, 1918-19 | $1.4-2.8$ | Coburn, Wagner, and Blower [53] |
| Nipah virus | $0.4-0.5$ | Royce and Fu [54] |
| Nipah virus, swine | 5.0 | Wongnak et al. [55] |
|  |  |  |

We may best derive $\mathfrak{R}_{0}$ mathematically by looking at a single infected individual. This person has, of course, the likelihood $\beta$ to create new infections (once again, assuming a naive population). Since we are interested not in a likelihood at a point in time to create new cases, but rather in the overall likelihood of a person creating new infections throughout their infectious state, we must multiply this figure by $\tau$, the mean infectious period. This, we note, is the inverse of $\gamma$, since $\gamma$ is the rate at which people are removed from the infectious ( $I$ ) compartment. Consequently,

$$
\begin{equation*}
\Re_{0}=\beta \tau=\beta \gamma^{-1}=\frac{\beta}{\gamma} \tag{2.8}
\end{equation*}
$$

### 2.1.6 The time-dependent reproduction number $\mathfrak{R}_{t}$

One of the urban legends of epidemiology is that the zero-index in $\Re_{0}$ exists to differentiate it from the compartment $R$. This, alas, is indeed an urban legend, but what exactly is zero in $\Re_{0}$ ?

There are two schools of thought on $\Re_{0}$ and $\Re_{t}$. One holds that $\Re_{0}$ is a theoretical figure, whereas $\Re_{t}$ is empirically ascertained. The other, perhaps somewhat more accurate, notion is that $\Re_{0}$ is the reproduction number at "time zero," that is, in the presence of a large pool of susceptibles, a single infectious individual and no recovered/resistant population.

$\mathfrak{R}_{0}$ is often explained as the number of secondary infections that flow from each case on average. Strictly speaking, that is not true. $\mathfrak{R}_{0}$ is the number of secondary infections that would flow from a case if the whole population were susceptible, except for the lone infectious index case. Because in the initial phases of an outbreak, the population of susceptible individuals is vastly larger than that of the infected, we may dispense with this strict formalism. However, the dynamics of an outbreak begin to follow more complex trajectories over time, and the $\mathfrak{R}_{0}$ notion becomes less viable.

Enter $\Re_{t}$, the time-dependent reproductive number. This figure is almost always used in the context of the empirical ascertainment of the reproduction number (on which see Section 2.5 in more detail).

Definition 2.13 (The time-dependent reproductive number $\Re_{t}$ ). The time-dependent reproductive number $\mathfrak{R}_{t}$ (also known as the effective reproductive number and sometimes abbreviated $R_{e}$ ) is the expectation of cases produced by an infectious case in a population at time $t$.

One might helpfully conceive of $\Re_{t}$ as the reproduction rate given the state of the system at time $t$. It thus reflects the system "as things are" at $t$, given $S(t)$ and $I(t)$. If a system has $I(t)$ infectious individuals at time $t$ and $I(t+\epsilon)$ after a short period of time $\epsilon$, then the number of cases created by the cases in existence at $t$ is $I(t+\epsilon)-I(t)$. From this, it follows that

$$
\begin{equation*}
\Re_{t}=\lim _{\epsilon \rightarrow 0} \frac{\overbrace{I(t+\epsilon)-I(t)}^{\text {new cases over } \epsilon}}{R(t+\epsilon)-R(t)} . \tag{2.9}
\end{equation*}
$$

Contact tracing efforts can often provide relatively accurate estimates of cases by generation, which allow for accurate calculation of $\mathfrak{R}_{t}$. Note, however, that such figures often do not take reporting lags into consideration, and the actual time to which a value of $\Re_{t}$ is related may be at variance with the time it was calculated. However, if the serial interval $\tau$ is known, $\Re_{t}$ can be calculated from a simple time series of infectious cases. The practical application of this is discussed in Subsection 2.5.4.

## Computational Note 2.4 Setting initial parameters

After defining the function, we will need to set the initial parameters. For this example, we will set the initial proportion of infectious persons at 0.01 percent, and assume that everyone who is not infected is susceptible. Then, we define $\mathfrak{R}_{0}$ at 2.5 and $\tau$ at 8 days. From this, we obtain $\gamma$ as $\tau^{-1}$ and $\beta$ as $\mathfrak{R}_{0} \gamma$.

```
I_0 = 0.0001
S_0 = 1 - I_0
R_0 = 0
y_0 = (S_0, I_0, R_0)
RO = 2.5
tau = 8
gamma = 1/tau
beta = R0 * gamma
```

Now, we can invoke the solver. For the purposes of this demonstration, we will set the interval of integration (t_span) at $0 \rightarrow 100$ and the maximum step size (max_step) to 1 ; in other words, we want a calculation for at least every day.

You do not have to specify max_step; the solver will try to guess an appropriate value. However, this typically is fairly parsimonious and the resulting curves can look quite choppy.

$$
\begin{aligned}
\text { res }=\text { solve_ivp( } & \text { fun=deriv, } \\
& \text { t_span }=(0,100), \\
& y 0=y \_0, \\
& \text { args=(beta, gamma), } \\
& \text { aax_step=1) }
\end{aligned}
$$

The solver returns an 0deResult object. This provides several attributes, the most important of which are the following:

1. success: True indicates that the solver managed to resolve the integration.
2. $t$ is an array with the points at which integration was performed.
3. y is a nested array (array of arrays), containing one array each for S, I and R.

We may now plot this result using our plotting tool of choice. Fig. 2.3 displays the result. This representation is, of course, population-agnostic. It is expressed in terms of a fraction of $N$, rather than real values of susceptible, infectious, and recovered patients. It is not difficult, however, to integrate those figures at the population level or at the level of plotting.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch02/ sir_ mode1s.

### 2.1.7 Threshold conditions of epidemics

Fig. 2.3 shows us the size (specifically, in terms of proportion of the entire population) of each compartment as plotted against time, for a given value of $\Re_{0}$ and $\tau$. In Fig. 2.4, we represent each value of $S(t)$ against the corresponding value of $I(t)$, a representation known as a phase portrait; it is discussed in more detail in Computational Note 2.3. Each of the lines refers to the same values of $\mathfrak{R}_{0}$ and $\gamma$, but different starting conditions in terms of starting values $S(0)$ and $I(0)$. We denote this family of curves as the characteristic curves of the SIR model with $\mathfrak{R}_{0}=2.5$ and $\tau=8$.

Definition 2.14 (Characteristic curves). The characteristic curves of a model refer to the family of curves for given values of $\{\beta, \gamma, \cdots\}$ in dependence of different values of $\{S(0), I(0)\}$.

Note that regardless of the starting conditions, as long as the dynamic parameters are identical, the maxima of the family of curves will lie at $S=\frac{1}{\Re_{0}}=\frac{\gamma}{\beta}$. Behind this intuition is a crucial mathematical relationship that governs the shape of an epidemic.

The phase plane (the $S / I$ plane in which the phase portrait is drawn) allows us to express $\frac{d S}{d t}$ and $\frac{d I}{d t}$ as a single equation, namely

$$
\begin{equation*}
\frac{d I}{d S}=\frac{-\overbrace{\beta S I}^{\text {new infections }}}{\underbrace{\beta S I}_{\text {new infections }}-\underbrace{\gamma I}_{\text {recoveries }}}=\frac{\gamma}{\beta S}-1=\frac{\mathfrak{R}_{0}^{-1}}{S}-1 \tag{2.10}
\end{equation*}
$$

In this equation, which is sometimes described as the phase portrait of the model, $\mathfrak{R}_{0}^{-1}$ is the threshold number for the parameters governing the model.

What we are in particular interested in is what happens around $\Re_{0}^{-1}$. Beginning with an almost entirely susceptible population $(S(0) \approx 1$ ), the ratio of infected versus susceptibles rises rapidly as individuals transfer from the susceptible to the infectious population. This persists until a point in time $t_{n}$, when $S\left(t_{n}\right)=\Re_{0}^{-1}$. Thereafter, the number of infectious individuals begins to decline sharply, leading to the eventual extinction of the infection.

Characteristic curves convey three fundamental truths about infectious processes. First, it explains a phenomenon called "epidemic burnout." Recall that we derived the mass action term from the fact that new infections require an infectious and a susceptible individual to meet. This is governed by the product of their relative proportions, and a constant (the coefficient of transmission, $\beta$ ). For a SIR model or some other model, where infectious cases do not revert to susceptibility (or do so with a significant delay), the infection eventually runs out of susceptible individuals and dies out. This receding stage of the infection begins once $S(t)$ reaches the critical value of $\Re_{0}^{-1}$.

Second, it indicates that an infection past that critical point is necessarily in decline. A consequence is that $S(0)<\mathfrak{R}_{0}^{-1}, I(t)$ will monotonically converge on zero. In other words, if $S(0) \Re_{0}<1$, then the corresponding $I(0)$ will be a global maximum, and the infection will monotonically decline.

Finally, and perhaps most importantly to us in our role as epidemiologists, is the fact that the time $t_{n}$ at which the maximum is reached is a function of $S(0), \beta$ and $\gamma$ :

- Interventions that reduce $S(0)$, such as vaccination, reduce both the duration of the overall outbreak and, if it is reduced below $\Re_{0}^{-1}$ (the threshold of collective immunity, on which Chapter 6 provides detail), outbreaks cannot sustain themselves.
- Interventions that reduce $\beta$, such as quarantine or social distancing, shift the critical point to the right, reducing the time during which the outbreak can grow.
- Interventions that increase $\gamma$ by shortening the mean recovery time $\tau$, such as early treatment with antimicrobials, reduces the overall extent of the disease.

An elegant analytical derivation of this is to be found in Li [41], but for our purposes, the principal takeaway is that $\Re_{0}$ does not only deal with the progress of an outbreak but also with the very fact of whether it will ever come to pass, in its relationship to $S(0)$. Thus an outbreak requires two indispensable factors:

- $I(0)>0$, that is, an initial (or "seed") population of infectious individuals, and
- $S(0)>\mathfrak{R}_{0}^{-1}$, that is, a suitable susceptible population through which to spread.

Together, these constitute the threshold criteria of epidemics, and the most remarkable results of Kermack and McKendrick's model of infectious disease.

### 2.1.8 Density-dependence, frequency-dependence, and other factors

The standard form of the SIR model discussed in Subsection 2.1.4 assumes that the rate of encounters $\varrho$ is governed by the relative densities of susceptible and infectious individuals. This assumption holds for many diseases, but not all of them:

- In frequency-dependent transmission, the encounter rate is not governed by population density, i.e., population density does not principally govern the encounter rate.
- In hybrid transmission, the interactions are nonlinear, i.e., neither purely frequencydependent nor purely density-dependent [56].

Definition 2.15 (Frequency and density dependence). Frequency-dependent transmission obtains where $\varrho \propto \mathcal{S} \mathcal{I}$. Density-dependent transmission obtains where $\varrho \propto S I$. Hybrid (or intermediate) transmission occurs where $\varrho \propto f(\mathcal{S}, \mathcal{I}, \mathcal{N})$, where $f$ may be a nonlinear function of relative densities.

It is worth noting that even for frequency-dependent transmission, density is often a secondary but nonetheless influential factor. Frequency dependence suggests that encounters are at a constant rate. This recapitulates the kind of dynamics where individuals seek out encounters from an available supply. For instance, for sexually transmitted infections, there is generally a large available supply and the number of encounters is governed by an individual's rate of sexual encounters over time. For this reason, many STIs, such as HIV, are considered frequency-dependent. However, at and beyond a critical low level of density, frequency-based processes become governed nonetheless by density, where the density is so low as to make it impossible for an individual to seek out the preferred volume of encounters.

Definition 2.16 (Hard critical point of frequency dependence). A frequency-dependent process becomes governed by density if and only if $S I<(S+I) \varrho^{-1}$, that is, where the density of available contacts makes it impossible for a frequency-dependent agent to maintain the specific constant number of encounters.

It is helpful to expand this to the situation where $S I>(S+I) \varrho^{-1}$, but approaches it. The cost of seeking out another individual to contact is a monotonously increasing function $J(S, I)$ of $S$ and $I$. As $S I$ converges to $(S+I) \varrho^{-1}$, the cost of obtaining $\varrho^{-1}$ contacts reaches a level beyond what an individual may be able to afford. For instance, an individual's attempts to find $\varrho^{-1}$ sexual partners will be frustrated if finding each partner requires a significant investment of time, energy, or risk from predators. Thus there is a soft critical point of frequency dependence that lies above the hard critical point.

Definition 2.17 (Soft critical point of frequency dependence). A frequency-dependent process tends towards being governed by density as $\varrho^{-1} J(S, I)$ approaches the individual's capacity to bear the costs of pursuing the encounters.

Thus pure frequency-dependent transmission does not really exist; after a critical point, density governs even ordinarily constant-frequency processes. In most cases, frequency-dependent dynamics converge towards a hybrid model that transitions from frequency dependence to density dependence as $S I$ converges the critical point.

### 2.1.9 Peak severity of epidemics

To those in charge of responding to an epidemic, from disaster management professionals through hospitals to governmental authorities, it is not merely the overall number of cases over the epidemic's lifetime that matters, but also how that number is distributed over time. Rapid epidemic spikes can overwhelm healthcare capacities and cause excess mortality from lack of care, both among the victims of the epidemic and from unaffected individuals who cannot avail themselves of adequate care due to acute overload of the hospital system. For this reason, we are interested in the maxima that we have explored previously in Subsection 2.1.10. We noted there that in an epidemic, $I(t)$ will approach a maximum, where $S=\mathfrak{R}_{0}^{-1}$. The value of this maximum will be

$$
\begin{equation*}
\max I=I(0)+S(0)+\Re_{0}^{-1}\left(\ln \Re_{0}^{-1}-1-\ln S(0)\right) \tag{2.11}
\end{equation*}
$$

Since $\mathfrak{R}_{0}=\beta S(0) \gamma^{-1}$, we can estimate maxima based on initial conditions and $\mathfrak{R}_{0}$. In practice, it may often be quite difficult to know the number of infectious populations at the outset. However, in many cases, $I(0)$ will be vanishingly small compared to $S(0)$. In such situations, well-informed guesswork yielding results that are accurate to an order of magnitude tend to be sufficient. Alternatively, as long as it is quite early in the outbreak (i.e., the number of infectious cases appears to follow an exponential increase), it is possible to simply set the first available data point to represent $S(0)$ and $I(0)$.

## Practice Note 2.1 A caveat about counting cases

It may be tempting to assume that the number of infected individuals is a knowable fact, and thanks to the advances of electronic medical records and integrated public health reporting systems, we might be closer to this than ever. At the same time, not all infectious patients come to the attention of healthcare services. This may be because of socio-economic factors, or because their symptoms are nonspecific or subclinical. For the former, it is often possible to compare local or regional presentation rates with the national average to estimate the relative likelihood of a symptomatic individual not seeking medical care. For the latter, serosurveys can be correlated against self-reported symptoms to calculate the likelihood of asymptomatic illness. Since asymptomatic individuals may be infectious, but also do not constitute part of the susceptible population, it is crucial to ascertain the ratio of asymptomatic infection vis-a-vis all infections. This may not always be a trivial exercise, as the intense controversy around the proportion
of asymptomatic infections during the early days of the COVID-19 pandemic has demonstrated. Nevertheless, estimates that might not be perfectly accurate are much better than no estimates at all.

### 2.1.10 The final size of epidemics

The final size of epidemics depends on the epidemic model. It is typical to specify these in an implicit manner, which makes them analytically unsolvable, but which can be numerically estimated. Recall that the phase portrait of $I$ and $S$ (see Eq. (2.10)) can be described as

$$
\begin{equation*}
\frac{d I}{d S}=\frac{\Re_{0}^{-1}}{S}-1 \tag{2.12}
\end{equation*}
$$

Consequently, we can take $I$ as a function of $S$ by taking the indefinite integral of the above, which yields

$$
\begin{align*}
I(S) & =\int \frac{\Re_{0}^{-1}}{S}-1  \tag{2.13}\\
& =\Re_{0}^{-1} \ln S-S+c
\end{align*}
$$

We can express the constant of integration as a function of $S$ and $I$, namely

$$
\begin{equation*}
\psi(S, I)=S+I-\mathfrak{R}_{0}^{-1} \ln S \tag{2.14}
\end{equation*}
$$

Because $N$ is constant, this has the same solution for every pair of $S$ and $I$ at any time. Consequently, for any $S(t)$ and $I(t)$,

$$
\begin{equation*}
\psi(S(t), I(t))=\psi(S(0), I(0)) \tag{2.15}
\end{equation*}
$$

We assume that $I(0)$ is vastly smaller than $S(0)$, and can be ignored. Therefore

$$
\begin{equation*}
S(\infty)-\mathfrak{R}_{0}^{-1} \ln S(\infty)=S(0)-\mathfrak{R}_{0}^{-1} \ln S(0) \tag{2.16}
\end{equation*}
$$

which simplifies to the implicit transcendental equation for the final size of the epidemic,

$$
\begin{equation*}
\Re_{0}\left(1-\frac{S(\infty)}{S(0)}\right)=\ln S(0)-\ln S(\infty) \tag{2.17}
\end{equation*}
$$

The same logic can be applied to any more complex models. An alternative is the model proposed by Heesterbeek and Dietz [57], which we also use in Subsubsection 2.5.3.3 in the inverse to estimate $\mathfrak{R}_{0}$. Consider a random member of the population. The likelihood that this individual will be susceptible at $t=0$ is, of course, $S(0)$. At any given time, the likelihood that this individual sustains infection is $\frac{\Re_{0}}{N}$.

Then, the likelihood that this individual will be infected at some point over the course of the epidemic,

$$
\begin{equation*}
I(\infty)=S(0)\left(1-\frac{\Re_{0}}{N}\right)^{I(\infty) N} \tag{2.18}
\end{equation*}
$$

For a sufficiently large $N$,

$$
\begin{equation*}
I(\infty)=\lim _{N \rightarrow \infty} S(0)\left(1-\frac{\mathfrak{R}_{0}}{N}\right)^{I(\infty) N}=1-S(0) e^{-\mathfrak{R}_{0} I(\infty)} \tag{2.19}
\end{equation*}
$$

Assuming $I(0)$ is quite small, $S(0)$ is approximately 1 , and consequently, Eq. (2.19) becomes

$$
\begin{equation*}
I(\infty)=1-e^{-\mathfrak{R}_{0} I(\infty)} \tag{2.20}
\end{equation*}
$$

In more complex models, deducing $I(\infty)$ from the likelihood of a notional individual's infection by the time the infectious process has concluded is often easier than the classical approach using the phase portrait.

## Practice Note 2.2 Population turnover

An inconvenient result of reality's staunch refusal to conform to the best of mathematical models is population turnover. People die and others are born, and statistically, a person being born is much more likely to be susceptible to a disease than a person dying, partly because absent maternal (vertical) immunity, newborns are generally immunologically naive, and partly because people are likely to die at older ages, which also correlates to the (time-dependent) lifetime likelihood of exposure to the pathogen. For this reason, counting on epidemic burnout to end an outbreak is rarely a wise idea. For very low population turnover and low likelihood of death from disease, counting on epidemic burnout to exhaust the pathogen's host population may be part of a multilimb strategy. However, population turnover makes reliance on epidemic burnout alone to be infeasible above an $\mathfrak{R}_{0}$ of approximately 5 in human populations, or where the disease has serious mortality risks or economic or social costs.

### 2.1.11 Epidemic burnout

The phenomenon of epidemic burnout is by far one of the most perplexing features of epidemic processes. We commonly talk of susceptibles as a vital "resource" for a pathogen, without which it cannot persist. This, and intuition, may give rise to the perception that epidemics "burn through" a population. This is correct, insofar as the absence of any susceptibles is a sufficient condition for the end of an infectious process. It is, however, incorrect in that it is not a necessary condition.

Let us consider Eq. (2.6), and divide the first and third equations:

$$
\begin{equation*}
\frac{d S}{d R}=\frac{-\beta S}{\gamma}=-\Re_{0} S \tag{2.21}
\end{equation*}
$$

Integrating this expression, we obtain

$$
\begin{equation*}
S(t)=S(0) e^{-R(t) R(0)} \tag{2.22}
\end{equation*}
$$

We know that $e^{-R(t) \Re_{0}}$ is always positive. Since $\mathrm{R}$ may, due to the partition prop-

erty $(S+I+R=1)$, assume only values in the domain $[0,1], S>e^{-\mathfrak{R}_{0}}$, which itself is above zero.

In biological terms, this means that for any $t$, there will be, at the end of the epidemic, $e^{-\mathfrak{R}_{0}}$ individuals who escape infection. Or, in other terms, epidemics cease, because they run out not of susceptibles but infected individuals. This is the phenomenon of epidemic burnout.

### 2.2 Modeling mortality and vital dynamics

So far, we have looked at models where the sum of all compartment cardinalities equaled a fixed quantity $N$. In this section, we are beginning to look at models in the space of vital dynamics: births and deaths.

Definition 2.18 (Vital dynamics). The vital dynamics (also termed population dynamics) of a population comprise changes in the population size, namely

- births,
- deaths,
- immigration, and
- emigration.


### 2.2.1 Case study: births and deaths in HIV

Where an infection lasts for a long time, births and disease-unrelated deaths become relevant for our calculations. As we move away from the closed-system models of the previous sections, we encounter the issue of allocation: we may know something about the growth or decrease of a population (births and deaths, correspondingly), but we need to identify which compartments these each fall into.

Definition 2.19 (Vertical transmission). Vertical transmission refers to the transmission of a pathogen to an offspring in utero (transplacental infection) or at time of birth.

Given that vertical transmission is more the exception than the rule, it is particularly prevalent in the case of certain viral infections. Vertical transmission is thus the reason why we cannot always assume that all births will fall into the immunologically naive

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-22.jpg?height=391&width=663&top_left_y=226&top_left_x=398)

Figure 2.6 A multioutcome SIR model with mortality. $\theta$ is the mortality fraction, which separates the deceased $(D)$ from the recovered $(R)$.

susceptible category. The reverse of this situation is, of course, maternal antibodybased immunity, which for structure's sake will be discussed with other models of immunity, in Subsection 2.3.4.

Human immunodeficiency virus infection is an example for a long-term infectious condition that is affected both by births and deaths. Thanks to modern antiretroviral therapy, the lifespan of patients with HIV has increased significantly, with many of them never progressing to full-blown AIDS. Consequently, a good proportion of them die with, rather than from, the disease, and population dynamics allows us to model that process. At the same time, vertical transmission of HIV is documented. This may be transplacental or occur at the time of birth. A recent survey by Forbes et al. found that vertical transmission occurs in about $3 \%$ of HIV positive mothers, and highly active antiretroviral therapy (HAART) reduces this to $1 \%$ or below [58].

In this section, we will examine the way vital dynamics affect a population. We will differentiate between the ordinary case of immunologically naive births, vertical transmission, and the effects of disease on fecundity; the special case of being born with a degree of immunity (maternal immunity) is discussed in Subsection 2.3.4.

### 2.2.2 A multioutcome SIR model: SIRD

Our first refinement of the SIR model will be by introducing differential outcomes (Fig. 2.6). This will be the foundation of later models, where these differential outcomes feed back into the system. For instance, in models that account for lapsing immunity, it is important to keep the deceased (who will never return to the pool of susceptibles) separate from the recovered (who will).

By far the most widely accounted-for differential outcome is short-term mortality. Fig. 2.7 shows a potential multioutcome model, in which after the course of illness, a fraction of patients recover, whereas others succumb to their illness. The mortality fraction $\theta$ denotes the fraction of removed cases that are allocated to the deceased $(D)$ compartment. This is from time to time referred to as the "mortality rate"; it is incorrectly so, since a rate is a time-denominated value. In the long run, $\theta$ equals the case-fatality ratio (CFR) of the infection.

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-23.jpg?height=710&width=1039&top_left_y=225&top_left_x=245)

Figure 2.7 Solutions of a typical SIRD model with $\mathfrak{R}_{0}=2.5, \tau=8$ and $\theta=0.2$.

The practical utility of a SIRD model is primarily as a building block for more complex models, in which recovered populations exhibit different behaviors from the deceased (typically, by virtue of being alive). A classical example of this is waning immunity; decedents cannot revert to the susceptible pool, but recovered immune patients can. Similarly, SIRD models are useful in modeling differential infection-fatality or case-fatality ratios between subpopulations, e.g., the characteristically higher mortality of the elderly in most infectious diseases. Finally, in models of funerary transmission (see Subsection 2.2.7), decedents are-for a certain period —-sources of infection, and thus part of the mass action term.

### 2.2.2.1 Governing equation

Just as the flow diagram of the SIRD model is quite similar to that of the simple SIR model outlined in Subsection 2.1.4, the system of differential equations that govern such circumstances is quite similar, too.

$$
\begin{align*}
\frac{d S}{d t} & =-\underbrace{\beta S I}_{\text {mass action }}, \\
\frac{d I}{d t} & =\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\gamma I}_{\text {removals to } R \text { and } D}  \tag{2.23}\\
\frac{d R}{d t} & =\gamma \underbrace{(1-\theta) I}_{\text {surviving part }},
\end{align*}
$$

$$
\frac{d D}{d t}=\gamma \underbrace{\theta I}_{\text {decedent part }}
$$

Note that the system of differential equations in (2.23) effectively apportions $\gamma$ into the two fractions, $\gamma \theta$ and $\gamma(1-\theta)$, which are allocated to the compartments $D$ and $R$, respectively. Conveniently, since this is a partition of $\gamma$, none of the other equations in the system need to be adjusted.

Definition 2.20 (Case-fatality ratio (CFR) and infection-fatality ratio (IFR)). The infection-fatality ratio $\mathrm{IFR}_{t}$ is the number of deaths divided by the number of infections at time $t$.

$$
\begin{equation*}
\mathrm{IFR}_{t}=\frac{D(t)}{\int_{0}^{t} I(u) d u} \tag{2.24}
\end{equation*}
$$

The idealized value of IFR is $\theta$.

The case-fatality ratio $\mathrm{CFR}_{t}$ is the number of deaths divided by the number of recognized cases.

$$
\begin{equation*}
\mathrm{CFR}_{t}=\frac{D(t)}{\int_{0}^{t} I(u) r d u} \tag{2.25}
\end{equation*}
$$

where $r$ is the ratio of recognized cases divided by all infections. Therefore $\mathrm{IFR}_{t}=$ $\mathrm{CFR}_{t} r$.

### 2.2.2.2 Blighted lives

Survivors of infectious diseases may escape short-term mortality but experience an elevated mortality risk, vis-a-vis their healthy counterparts. A 2021 study by Al-Aly, Xie, and Bowe [59] looked at survivors of COVID-19, and found that after a mean follow-up of 4 months, users of the Department of Veterans Affairs health system who were diagnosed with COVID-19 and survived for 30 or more days after their initial diagnosis still had an increased risk of mortality [59]. Similar results have emerged from long-term studies of survivors of the West African ebolavirus outbreak [60], and postviral syndromes are widely recognized in the aftermath of a range of other infectious diseases.

In a "blighted lives" model (illustrated in Fig. 2.8), $\theta_{s}$ determines the fraction of deceased versus recovered in the short term, much as $\theta$ simpliciter did for the simple SIRD model. However, in addition, we have the quantity $\mu_{l}$ to account for long-term mortality. We do so by subtracting the term $R \theta_{l}$ from $\frac{d R}{d t}$ and adding it to $\frac{d D}{d t}$, maintaining the closed system axiom's requirements. This gives us the following system of

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-25.jpg?height=396&width=710&top_left_y=226&top_left_x=414)

Figure 2.8 In this model, we are accounting for short-term mortality $\left(\theta_{s}\right)$ and long-term mortality $\left(\theta_{l}\right)$. Survivors experience increased mortality, in this case, for life. The long-term mortality coefficient $\theta_{l}$ reflects this by allocating a fraction of survivors to the deceased $(D)$ compartment.

differential equations:

$$
\begin{align*}
& \frac{d S}{d t}=-\underbrace{\beta S I}_{\text {mass action }}, \\
& \frac{d I}{d t}=\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\gamma I}_{\text {total removed }}, \\
& \frac{d R}{d t}=\underbrace{\left(1-\theta_{s}\right) \gamma I}_{\text {removed recovered }}-\underbrace{\theta_{l} R}_{\text {removed deceased }},  \tag{2.26}\\
& \frac{d D}{d t}=\underbrace{\gamma \theta_{s} I}_{\text {deceased from } I}, \underbrace{\theta_{1} R}_{\text {deceased from } R} .
\end{align*}
$$

### 2.2.3 Modeling births

Births and deaths affect the overall population under examination. Until now, this population has been steady, which was a convenient mathematical formalism but of course flew in the face of reality. In this chapter, notably, we are not concerned with diseaserelated deaths, but rather natural mortality. For this reason, infectious disease modelers should keep in mind that accounting for births and deaths is not necessary nor suitable for every disease. For short, fast-moving infections, births and natural mortality are generally negligible for anything beyond a trivial population. Longer-term models, however, may usefully take account of these variables. As a rule of thumb, for human populations, including births and deaths makes sense if the model is expected to reflect a process that runs over more than twice the human gestational interval, i.e., 1.5 years. One may wish to include births and deaths at shorter time periods if they are significantly unequal, such as where population growth vastly outpaces natural mortality or vice versa.

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-26.jpg?height=349&width=672&top_left_y=230&top_left_x=387)

Figure 2.9 In the naive births model, we assume all births to be susceptible, and thus credit them to the $S$ compartment. The rate of births over time is defined by the birth rate per population of $N$ per unit time, symbolized by $\phi$.

### 2.2.3.1 Naive births

In the naive birth model, we assume (as is in fact mostly the case) that anyone born is by definition susceptible at time of birth. We account for this by introducing the birth term, and assigning it entirely to $S$. For this, we assume that anyone who is in $N$ is equally fecund, and consequently the rate of change of $S$ attributable to new births is a function of the entire population size.

Definition 2.21 (Immunologically naive birth condition). The immunologically naive birth condition assumes that any individual born to the population will be neither infected nor immune, i.e., all births accrue to the susceptible $(S)$ compartment.

In the naive birth model (Fig. 2.9), we account for births by crediting them to the $S$ compartment. Thus for a rate of live births of $\phi$,

$$
\begin{align*}
& \frac{d S}{d t}=-\underbrace{\beta S I}_{\text {mass action }}+\underbrace{\phi}_{\text {births }} \\
& \frac{d I}{d t}=\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\gamma I}_{\text {recovery }}  \tag{2.27}\\
& \frac{d R}{d t}=\underbrace{\gamma I}_{\text {recovery }}
\end{align*}
$$

This model makes two significant assumptions:

1. All births are immunologically naive, i.e., neither infectious nor immune.
2. The population is equifecund, i.e., the compartment in which someone is unrelated to fertility.

We know that in reality, these assumptions do not hold. Some infections can be passed on from mother to child, by way of vertical transmission (Definition 2.19). Notable examples for the latter are the pathogens that make up the "TORCH complex," a group of infections that account for most transplacental transmission of infectious disease in humans, and are associated with perinatal infectious presentations. It includes the following diseases:

- toxoplasmosis
- other infections (HIV, chlamydia, parvovirus B19)
- rubella
- cytomegalovirus (CMV), and
- herpes simplex virus 2 (HSV-2)

Subsubsection 2.2.3.2 will discuss accounting for vertical transmission, whereas Subsubsection 2.2.3.3 shall deal with disease-related effects on fecundity.

## Practice Note 2.3 When to account for maternal immunity

Accounting for maternal immunity may be useful for populations (especially nonhuman populations), where the duration of maternal immunity is significant in relation to the overall lifespan or the period under examination. For a human life, the duration of maternal immunity is quite short. This may be different for short-lived animal species.

The duration of maternal immunity may also be more significant if we are only looking at a relatively short period of time. For instance, while maternal immunity to pertussis is relatively brief, it is a significant protective factor, because most severe cases of pertussis occur in very young children.

The naive birth model is a better, and mathematically more convenient, approximation when considering longer timespans in relation to the duration of maternal immunity.

### 2.2.3.2 Modeling vertical transmission of disease

In vertical transmission, offspring born to infected individuals have a certain probability $p_{I}$ of being infected themselves (see Definition 2.19). For this reason, we must account for population flows separately. We split the birth term, which until now we conceptualized as a single variable $\phi$, into separate birth terms:

- All births accruing to susceptible or recovered individuals are susceptible.
- $p_{I}$ of the births accruing to infected individuals are infected.
- $1-p_{I}$ of the births accruing to infected individuals are susceptible.

Therefore the birth term $\phi$ is separated into susceptible births ( $\phi_{S}$ ) and vertically infected births $\left(\phi_{I}\right)$ as follows:

$$
\begin{align*}
\phi_{S} & =\overbrace{(S+R) \phi}^{\text {births to }} S+\overbrace{I\left(1-p_{I}\right) \phi}^{S \text { and } R} \\
\phi_{I} & =\underbrace{I p_{I} \phi}_{\text {vertically infected births }}
\end{align*}
$$

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-28.jpg?height=347&width=863&top_left_y=226&top_left_x=298)

Figure 2.10 In the vertical transmission model, births in respect of $S$ and $R$ will be deemed susceptible, and credited to $S$. A fraction of births to infected individuals, $p_{I}$, will be born infected and be credited to $I$, whereas the remainder will be credited to $S$.

With that, we can adjust (2.27) to reflect vertical transmission to incorporate Eq. (2.28) (see Fig. 2.10):

$$
\begin{align*}
& \frac{d S}{d t}=-\underbrace{\beta S I}_{\text {mass action }}+\underbrace{\overbrace{(S+R) \phi}^{\text {births to }} S \text { and } R}_{\text {naive births }}+\overbrace{I\left(1-p_{I}\right) \phi}^{\text {uninfected births to } I}, \\
& \frac{d I}{d t}=\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\gamma I}_{\text {recovery }}+\underbrace{I p_{I} \phi}_{\text {vertically infected births }}  \tag{2.29}\\
& \frac{d R}{d t}=\underbrace{\gamma I}_{\text {recovery }}
\end{align*}
$$

### 2.2.3.3 Disease-related effects on fecundity (DREF)

Some infectious diseases cause a depression in the rate of live births, often by increasing the rate of miscarriages and stillbirths. We refer to these as disease-related effects on fecundity. Such effects are particularly often observed for infections of long duration, even if they are otherwise almost commensal (asymptomatic). A study of foragers in Bolivia by Blackwell et al. [61], for instance, found that gastrointestinal hookworm infection (Ancylostoma duodenale) reduced fertility by approximately $30 \%$ [61]. In the animal world, tsetse flies, who carry Trypanosoma brucei rhodesiense, have been found to suffer a $30 \%$ decrease in the number of offspring [62]. Disease-related effects on fecundity describe the cost, in terms of reduced fecundity, of an infectious disease.

Definition 2.22 (Disease-related effects on fecundity). A disease-related effect on fecundity is a temporary depression of the birth rate for individuals in an infected compartment in comparison to similar individuals in the susceptible compartment.

From time to time, such infections are described as "sterilizing," but this is a somewhat clumsy formulation. First, it is somewhat inaccurate in that often there's a depression of fecundity, rather than an outright sterilization. More importantly, it is liable to cause confusion with sterilizing treatments and vaccines, which describe treatments and vaccines that terminate infectious status upon administration.

We may account for DREF in our models by separating the birth rate attributable to infectious individuals and applying a discount factor $\rho_{i}$ that reflects this depression. Thus the number of total births will be

$$
\begin{equation*}
\frac{d N}{d t}=\underbrace{\phi}_{\text {birth rate }}(S+\underbrace{\left(1-\rho_{i}\right)}_{\text {births to infectious individuals }} I \quad+R)=\phi\left(N-\rho_{i} I\right) \tag{2.30}
\end{equation*}
$$

We may conceptualize $\phi \rho_{i} I$ as the number of births attributable to individuals in $I$ that would take place but for the disease-related reduction in fecundity. We may insert (2.30) into (2.27) for a naive births model that accounts for disease-related effects on fecundity:

$$
\begin{align*}
& \frac{d S}{d t}=-\underbrace{\beta S I}_{\text {mass action }}+\underbrace{\phi}_{\text {birth rate }}(N-\underbrace{\rho_{i} I}_{\mathrm{DREF}}) \\
& \frac{d I}{d t}=\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\gamma I}_{\text {recovery }}  \tag{2.31}\\
& \frac{d R}{d t}=\underbrace{\gamma I}_{\text {recovery }}
\end{align*}
$$

This assumes, of course, that the reduction in fecundity and infectiousness are coterminous. Where that is not the case, such as where there is an enduring depression of fecundity after resolution of symptoms and the end of infectiousness, the appropriate approach is to model this as a separate compartment $F$, with a rate of reversion to fertile immune recovery or fertile susceptibility of $\frac{1}{\overline{\tau_{F}}}$, where $\overline{\tau_{F}}$ is the mean duration of suppressed fertility. In that scenario, for the discount factor $\rho_{F}$ of the long-term suppressed fecundity compartment, population growth would be calculated not on the basis of $N$ but $N-\rho_{i} I-\rho_{F} F$.

### 2.2.4 Modeling natural mortality

We use the term natural mortality to distinguish the "background" rate of mortality (e.g., accidental deaths, suicide/homicide, deaths from other unconnected illnesses) from disease-related mortality. A good first approximation is that the natural death rate is the inverse of the host organism's average lifespan. Where the variance of this figure is relatively low, this assumption tends to hold quite well.

Definition 2.23 (Natural mortality). Natural mortality refers to mortality from all causes extraneous to the infectious disease under consideration. Notably, natural mortality does not coincide with the legal concept of death from natural causes. Homicides, suicides, and deaths from warfare and violence are, for the purposes of epidemiological modeling, considered "natural." Insofar as epidemiological modeling is
concerned, any births from any cause other than the infection under consideration is deemed "natural."

Natural mortality also assumes that recovered, infectious, and susceptible cases have the same mortality rate. We have seen in Subsection 2.2.2.2 that survivors of serious infectious diseases might often experience a depression in overall lifespans. However, for diseases that generally affect a large percentage of the population, such as influenza, we may consider these to be "factored into" life expectancy, and thus omit accounting for this term specifically.

Thus under the assumption that the risk of natural mortality is isotropic (equal across all compartments), we can break down the mortality term

$$
\begin{equation*}
\frac{d N}{d t}=\theta N \tag{2.32}
\end{equation*}
$$

in proportion to the size of each compartment:

$$
\begin{align*}
& \frac{d S}{d t}=\underbrace{\theta}_{\text {birth }}-\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\theta S}_{\text {deaths from } S}, \\
& \frac{d I}{d t}=\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\gamma I}_{\text {recovery }}-\underbrace{\theta I}_{\text {deaths from } I},  \tag{2.33}\\
& \frac{d R}{d t}=\underbrace{\gamma I}_{\text {recovery }}-\underbrace{\theta R}_{\text {deaths from } R} .
\end{align*}
$$

This is an isotropic model in which all births accrue to $S$, but deaths are distributed across the compartments according to their respective sizes. Since $S+I+R=1$, $\theta(S+I+R)=\theta$.

Definition 2.24 (Isotropy). A process or value is said to be isotropic over a compartmental model if it affects every compartment to the same degree.

## Practice Note 2.4 Estimating natural mortality

The inverse lifespan estimator $\left(\theta={\overline{\tau_{L}}}^{-1}\right.$, where $\overline{\tau_{L}}$ is the average life expectancy) is a convenient first guess of the mortality rate, but not always accurate. In particular, it is much less accurate where the risk of death is unevenly distributed.

In many developing countries, the likelihood of mortality is bimodal due to high infant mortality. Additionally, age-differential mortality factors, such as prolonged warfare (which affects young men more than older men and women), often interfere with this estimation. In affluent countries, where infant mortality is low and natural mortality is more or less a monotonously increasing function of age, the inverse lifespan estimator is likely to be adequate for most purposes.

Nevertheless, when modeling infectious disease over a longer period of time, we must be sensitive to the local circumstances, including how the population's demographics are distributed. Life tables are often available for populations, from which one may then infer precise population distributions.

### 2.2.5 Constant-population naive-birth isotropic mortality model

Many epidemiological models, especially those executed over longer timespans, benefit from introducing a term to reflect population turnover. This creates a supply of new susceptible individuals, while keeping the population constant. The constantpopulation naive-birth isotropic mortality model is a useful formalism to allow the long-term oscillatory dynamics that flow from a depletion of immune individuals (through waning or death) and an influx of susceptibles to manifest. Fig. 2.11 describes this distribution. By convention, since the birth rate and the death rate are equal, they are represented by the same symbol, $\mu$, representing the population's turnover rate.

Given a model of $n$ compartments, all births accrue to $S$, at a rate of $\mu$, and deaths occur in each compartment in proportion to its size, i.e., the mortality term for the $i$-th compartment is $C_{i} \mu$. Since $\sum_{i=1}^{n} C_{i} \mu=\mu$, the total mortality term will be the same as the birth term, and consequently, $\frac{d N}{d t}=0$.

$$
\begin{align*}
\frac{d S}{d t} & =\overbrace{\mu}^{\text {births }}-\ldots-\overbrace{\mu S}^{\text {deaths from } S} \\
\frac{d C_{i}}{d t} & =\ldots-\underbrace{\mu C_{i}}_{\text {deaths from } C_{i}} \tag{2.34}
\end{align*}
$$

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-31.jpg?height=574&width=674&top_left_y=1440&top_left_x=432)

Figure 2.11 In the naive birth-isotropic mortality model, all births accrue to $S$, whereas deaths flow proportionally from each compartment.

The beauty of this formalism is that it can be expanded to an arbitrary number of compartments without much change, with the caveat that if there are other sources of mortality, and these are treated as outflows without a separate compartment, the constant population constraint would require those to be offset by adding it to the birth term $\mu$ in $\frac{d S}{d t}$.

## Practice Note 2.5 When to account for vital dynamics

Vital dynamics do not play a significant role in every infectious disease. Especially in human populations, the rate of vital dynamics, when compared to the time dynamics of infectious diseases is tremendously slow. The human gestation period, at 270 days on average, is far from the longest in the mammalian world, but it is certainly very significantly longer than that of many other animals. It is over ten times longer than that of small rodents, such as hamsters and gerbils, and nine times as long as the gestation period of rabbits. Humans are also relatively long-lived. For this reason, in most human disease, vital dynamics have a negligible effect in the short term.

The practitioner must assess in devising the infectious disease model whether accounting for vital dynamics would have a meaningful impact on the results.

Cases where population dynamics ought to be typically modeled are

- infections in animals with relatively short gestation periods (a good rule of thumb is a maximum of $8-10 \tau$ as a cutoff point),
- infections of long or indeterminate duration (see Subsection 2.3.2), and
- significant heterogeneities in subpopulations with regard to population dynamics.


### 2.2.6 $\mathfrak{R}_{0}$ in combined demographic models

Given the constant population naive birth isotropic mortality formalism introduced in the previous section, we obtain for the SIR model the form

$$
\begin{align*}
& \frac{d S}{d t}=\underbrace{\mu}_{\text {births }}-\beta S I-\underbrace{\mu S}_{\text {deaths from } S} \\
& \frac{d I}{d t}=\beta S I-\gamma I-\underbrace{\mu I}_{\text {deaths from } I}  \tag{2.35}\\
& \frac{d R}{d t}=\gamma I-\underbrace{\mu R}_{\text {deaths from } R}
\end{align*}
$$

From this, we can derive $\Re_{0}$ for a model with births and deaths. If we denote the mean time spent in the infectious compartment as $\tau$, we can formulate it as the effect of two processes: for every unit of time spent in the infectious phase (every unit of $\tau$ ),
an infectious individual has $\gamma^{-1}$ chance to leave the compartment by way of recovery and $\mu^{-1}$ chance of leaving due to mortality. Together, $\tau=(\gamma+\mu)^{-1}$.

We know from our derivation of $\Re_{0}$ in Subsection 2.1.5 that $\Re_{0}$ is the total number of secondary cases that can be generated by a case during their infectious state. This is, of course, the product of their propensity to generate cases (the transmission coefficient $\beta$ ) and the time they spend in the infectious state $(\tau)$. Consequently,

$$
\begin{equation*}
\Re_{0}=\beta \tau=\frac{\beta}{\mu+\gamma} \tag{2.36}
\end{equation*}
$$

The consequence of this is that in short-lived host populations, a pathogen must be quite well-transmissible to persist. For humans, with a mean lifespan of seven decades, mortality is not going to be a particular concern when discussing an illness with the mean infectious period of 7-10 days. On the other hand, many vectors of infectious diseases, especially arthropods, are rather short-lived. Where $\mu$ is not very significantly smaller than $\gamma$, the infection must either be lifelong ( $\gamma=0$ therefore the infection will sustain itself if $\beta>\mu$ ) or significantly more contagious to offset it. As we shall see in Section 4.1, the former is quite often the case among short-lived vectors.

### 2.2.7 Funerary transmission

In recent years, increasing attention has been directed to funerary transmission, the phenomenon of infections generated by a deceased individual after death but before burial, especially in the context of Ebola haemorrhagic fever [63]. Tiffany et al. [64] estimated that on average, each unsafe burial during the 2013-2016 West African ZEBOV outbreak generated approximately 2.58 secondary cases.

Definition 2.25 (Funerary transmission). Funerary transmission denotes transmission of a pathogen from recently deceased individuals to susceptible individuals, typically during procedures that involve physical contact in funerary rituals.

Legrand et al. [65] first proposed a model that took account of funerary transmission. This model effectively considered the time pending burial a separate compartment within a SIRD model. Deceased individuals first move to the intermediate compartment (typically denoted $F$ ) of the unburied dead, from which they then transition, at a rate typically specified by the time to burial, to the ultimate compartment $(D)$. Fig. 2.12 illustrates the flow diagram of the Legrand et al. model's operation.

SIRFD models allow us to understand not only funerary transmission risk but also the impact that certain public health measures have, such as Safe and Dignified Burials (see Practice Note 2.6).

The effect of reducing the risk of funerary transmission is illustrated by Fig. 2.13. Assuming a time-dependent rate of infections, earlier funeral results in a significantly less severe infectious dynamic. Of course, in the same vein, we may use time as merely a proxy for overall encounters. Reducing the number of encounters during the burial process, e.g., by not embalming the body and by the use of barrier precautions in preparing the body for burial, has a similar effect.

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-34.jpg?height=398&width=954&top_left_y=227&top_left_x=246)

Figure 2.12 SIRFD model of funerary transmission. $\theta$ denotes the mortality fraction of removal. Deceased but unburied individuals $(F)$ remain infectious, at the rate of $\varphi$, for the time until burial, $\tau_{F}$.

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-34.jpg?height=837&width=1057&top_left_y=777&top_left_x=192)

Figure 2.13 Solutions of a SIRFD model for different values of $\tau_{F}$ (in days).

## Practice Note 2.6 Safe and dignified burials

Ceremonies and rites that mark the end of life and concern the disposition of the body are almost universal in all cultures and across all of human social evolution. Such ritual activity is often religiously and culturally sensitive, as well as highly emotive for the relatives and the wider community of the decedent. For this reason, funerary transmission raises important ethical and cultural dilem-
mas. Many funerary practices involve steps, such as ritual cleansing and ablution of the body, that expose the participants to contracting certain pathogens from the decedent, as has been documented, e.g., for haemorrhagic fever outbreaks in West Africa [66]. Funerals are also common social events, often involving geographically disparate family members, and may thus act as superspreader events (see Subsection 3.1.4) [67].

When addressing the contribution of funerary practices to pathogenic spread, it is important to act with understanding and sensitivity for the specific cultural context. During the 2013-2016 West African ebolavirus outbreak, the WHO developed the practice of Safe and Dignified Burials (SDB) [68]. which amended traditional funerary practices with steps intended to reduce the risk of funerary transmission [69]. The SDB guidelines had the benefit of being informed by a cross-cultural perspective and a deep anthropological understanding of the ways in which traditional rituals, especially the preparation of the body, could be altered, while retaining its ritual meaningfulness to the participants. For instance, the Islamic practice of ghusl, an ablution of the deceased, is replaced with tayammum or "dry ablution," which reduces the risk of pathogenic spread from the decedent.

Though by no means perfect, the development of SDBs is an example of exercising cultural sensitivity and discarding both pure utilitarianism and Eurocentric biases in creating a new ritual that the population will accept. SDBs are also a model of shared decision-making in an epidemic context, allowing the decedent's family to be active participants in decision-making. Even though-in contrast with common ritual-they will not be preparing the decedent's body, the guidelines provide for a family-appointed observer, and adopt a participatory approach that integrates the grieving family [68], Thus although they may not be fulfilling their traditional roles in preparing the body, the SDB remains something that happens "with," rather than merely "to," the family and the community.

SDBs have been credited with avoiding up to 10,000 secondary cases in that outbreak through preventing community spread [64], and it is beyond doubt that this would have been hardly attainable had the practices that we now collectively call SDB not been formulated in a manner that fosters shared decision-making, respect for cultural and religious traditions, and open communication.

### 2.3 Models of immunity

Immunity is the permanent or temporary resistance of an organism to an infection. Our models until now assumed perfect and lifelong immunity in all survivors. In this section, we are examining more differentiated models of immunity.

In general, when it comes to immunity, we do not quite care as to the origins of the immunity. In the rare cases where there are clinical differences, e.g., the rate
of waning, there might be a good case to model, say, post-infectious and vaccineinduced immunity separately. On the other hand, we do care about the likelihood of immunity. Not everyone who is vaccinated or recovers from an illness develops immunity, and often, immunity has a shelf life, as Subsection 2.3.1 discusses in detail. In compartmental models, this is typically accommodated by discounting the rate of immune recovery, or providing for a "flowback" to reflect waning. This section will explore techniques to model immunity in detail, whereas Section 6.1 discusses vaccine-induced immunity specifically in more depth.

### 2.3.1 Case study: periodicity in syphilis incidence

Syphilis is a bacterial infection caused by Treponema pallidum spp. pallidum, which is most often spread through sexual activity, though vertical transmission (see Subsubsection 2.2.3.2) has also been documented (congenital syphilis). In the United States, Grassly, Fraser, and Garnett observed that the peak spectral density of syphilis incidence was around 10 years [70]. Spectral density determines the contribution of individual frequencies to a time series, and its peak determines the frequency of the dominant periodic process. Grassly, Fraser, and Garnett also observed that unlike syphilis, gonorrhoea did not exhibit a similar periodicity.

Syphilis exhibits an oscillating pattern because of waning immunity over time. As we have seen in Subsection 2.1.5, epidemics need a suitably large pool of susceptible individuals to be viable. An infectious disease that engenders immunity will eventually exhaust this pool of susceptibles, and "burn out." However, if immunity gradually wanes, the pool of susceptibles is gradually refilled, and when $S$ once again reaches the critical mass, the epidemic will flare up.

Definition 2.26 (Waning immunity). Waning immunity denotes the reduction of immune response against the same pathogen as a function of time.

Biologically, waning immunity refers to the reduction in the effectiveness of the immune response over time.

In epidemiology, we primarily consider waning immunity as a binary-distributed variable over a population. As such, waning immunity denotes the reversion of immune individuals to susceptibility.

Waning immunity thus explains why certain epidemics, absent any external intervention, may recur with astonishing regularity, following multiyear cycles. In this section, we will examine the effect of immunity on our models. Until now, we generally assumed full immunity, i.e., everyone who survived infection was indefinitely immune. This section looks at what happens in the absence of that assumption.

### 2.3.2 No-immunity models (SI)

Previously examined models have generally assumed that survival bestowed indefinite immunity. We will depart from this assumption in the present section. In fact, we will do so by examining the polar opposite of indefinite immunity, namely pathogens that
induce no immunity at all, but rather result in lifelong infection. The classic example of such pathogens is herpes simplex (HSV). HSV infection is widely prevalent and lasts a lifetime. SI models (which some texts, such as Keeling and Rohani [39], refer to as SIS models) allow us to model such infections.

### 2.3.2.1 SI models with no vital dynamics and no recovery

First, let us consider SI models without vital dynamics and without recovery, i.e., where an infected person remains infected for the duration of the model. We may describe such a model by the system of differential equations:

$$
\begin{gather*}
\frac{d S}{d t}=-\underbrace{\beta S I}_{\text {mass action }} \\
\frac{d I}{d t}=\underbrace{\beta S I}_{\text {mass action }} \tag{2.37}
\end{gather*}
$$

It follows from the above that under the assumption of homogeneous mixing, and in the absence of vital dynamics, the entire population will eventually be infected:

$$
\begin{align*}
\lim _{t \rightarrow \infty} S(t) & =0 \\
\lim _{t \rightarrow \infty} I(t) & =1  \tag{2.38}\\
\lim _{t \rightarrow \infty} \mathcal{I}(t) & =N \lim _{t \rightarrow \infty} I(t)=N
\end{align*}
$$

### 2.3.2.2 SI models with clearance (SIS models)

SI models with clearance are models where the population alternates between an infectious state and susceptibility. These models are common, where surviving an infection does not result in an appreciable length or degree of immunity, but also where antigenic drift is so significant that immunity developed at one time is unlikely to have a protective effect for all but a trivial time period. This is often observed with rapidly mutating viruses, such as influenzaviruses, which necessitates annual re-immunization due to significant antigenic drift.

Definition 2.27 (Clearance). Clearance refers to the reversion from infectiousness into a nonimmune susceptible state. Unlike in the case of recovery, no immunity is built up.

In a SIS model with clearance, the $\gamma$ parameter, which ordinarily reflects transition from infectious to recovered state, will refer to clearance, that is, return to the susceptible pool. (See Figs. 2.14 and 2.15.)

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-38.jpg?height=231&width=381&top_left_y=232&top_left_x=539)

Figure 2.14 In the SI model with clearance, the population moves between the infectious and susceptible state.

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-38.jpg?height=606&width=1024&top_left_y=578&top_left_x=211)

Susceptible - Infectious

Figure 2.15 Solutions of a SI model with clearance for $\mathfrak{R}_{0}=4$ and $\tau=6$. The dashed line represents the separation between the oscillatory phase (left) and equilibrium phase (right).

We may characterize this model by the following differential equations:

$$
\begin{align*}
& \frac{d S}{d t}=-\underbrace{\beta S I}_{\text {new infections }}+\underbrace{\gamma I}_{\text {clearance }}  \tag{2.39}\\
& \frac{d I}{d t}=\underbrace{\beta S I}_{\text {new infections }}-\underbrace{\gamma I}_{\text {clearance }}
\end{align*}
$$

### 2.3.3 Modeling loss of immunity

At the heart of immunity is an organism's ability to create an enduring immunological memory against a pathogen. The mechanisms of immunological memory are quite complex, and include both cellular and humoral immunity. Humoral immunological memory results from the persistence of antibodies against the pathogen, even after the effector $\mathrm{T}$ cells that have responded to the initial infection have died off. This is

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-39.jpg?height=275&width=672&top_left_y=227&top_left_x=435)

Figure 2.16 Waning immunity is the gradual loss of immune competence against a pathogen. $\omega$ denotes the rate of waning immunity, which is inversely related to the duration of immunity $\tau_{R}$. The dotted lines denote peaks of epidemic waves.

relatively short-lived but highly effective. Cellular immunological memory relies on memory $\mathrm{T}$ cells and memory $\mathrm{B}$ cells that are long-lived and indeed in some cases confer lifelong immunity.

Waning immunity denotes the process of a loss of immunity over time (see Definition 2.26). In other words, recovered individuals "trickle back" to the susceptible compartment at a certain rate. Our first approximation is to consider this a fixed rate, $\omega$, which is the inverse of the mean duration of immunity engendered by infection (sometimes denoted as $\tau_{R}$ ).

Definition 2.28 (Waning rate). The waning rate $\omega$ is the time-denominated rate at which immunity is lost. It corresponds to the inverse of the duration of immunity.

We may articulate this term by adding it to $S$ and removing it from $R$, throughout. Thus the governing system of equations becomes

$$
\begin{align*}
& \frac{d S}{d t}=\mu-\underbrace{\beta S I}_{\text {new infections }}+\underbrace{\omega R}_{\text {reversal of waned }}-\mu S \\
& \frac{d I}{d t}=\underbrace{\beta S I}_{\text {new infections }}-\underbrace{\gamma I}_{\text {recovery }}-\mu I  \tag{2.40}\\
& \frac{d R}{d t}=\underbrace{\gamma I}_{\text {recovery }}-\underbrace{\omega R}_{\text {waning }}-\mu R .
\end{align*}
$$

The formula can, of course, be adapted to take account of vital dynamics similar to (2.35).

A consequence of waning immunity is that the pool of susceptibles is gradually replenished time and time again. We have seen in Subsection 2.1.5 that an epidemic requires a proportion of susceptible individuals to persist in a population. As immunity waxes and wanes, a periodic pattern of "seesaw" infections or "waves" may emerge, with the period of infectious waves coinciding with the time for sufficient replenishment of the susceptible pool. The case study at the beginning of this section (see Subsection 2.3.1) illustrates such a periodic recurrent epidemic. (See Figs. 2.16 and 2.17.)

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-40.jpg?height=706&width=1057&top_left_y=227&top_left_x=192)

Figure 2.17 Solutions of a SIRS model for $\Re_{0}=2.5, \tau=4$ and $\tau_{R}$ (duration of immunity) of 50 days.

## Computational Note 2.5 Waning immunity

By far the most commonly modeled aspect of immunity is periodicity due to waning immunity (as described in Subsection 2.3.3). Fundamentally, a SIRS model is no different in its computational execution than the previous compartmental models. We begin by defining the key initial characteristics, including $\omega$, the rate of waning immunity. It is generally more convenient to represent $\omega$ as $\overline{\tau_{R}}-1$, the inverse of the duration of immunity.

```
I_0 = 1e-2
S_0 = 1 - I_0
R_0 = 0
y_0 = (S_0, I_0, R_0)
RO = 2.5
tau = 4
gamma = 1/tau
tau_R = 50
omega = 1/tau_R
beta = RO * gamma
```

We can then use the approach used for prior ODE solutions to arrive at a numerical result.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder I ch02/ sir_ models.

In practice, however, waning is not a homogeneous rate process. Often, a better approximation is to assume that immunity lasts a certain time $\omega^{-1}$. Instead of defraying a fraction of the immune population at every step, we can use a delay differential equation (DDE) that simply returns the quantity of individuals who have become immune at $t-\omega^{-1}$ to susceptibility:

$$
\begin{align*}
\frac{d S_{t}}{d t} & =\mu-\beta S(t) I(t)+\gamma I\left(t-\omega^{-1}\right)-\mu S(t) \\
\frac{d I_{t}}{d t} & =\beta S(t) I(t)-\gamma I(t)-\mu I(t)  \tag{2.41}\\
\frac{d R_{t}}{d t} & =\gamma I(t)-\gamma I\left(t-\omega^{-1}\right)-\mu R(t)
\end{align*}
$$

Ordinary ODE solvers cannot solve delay differential equations, which makes them computationally somewhat more demanding and less convenient than simple ODE models. However, they are computationally solvable using DDE solvers. Computational Note 6.2 lays out the use of a DDE solver for waning of vaccination-induced immunity, which can be trivially adapted to cover waning of post-infectious immunity, as detailed in this subsection, too.

### 2.3.4 Maternal immunity

Maternal immunity, sometimes called vertical immunity, is the immunity counterpart to vertical transmission of disease (on which see Subsection 2.2.3.2). Unlike the forms of immunity we have considered until now, maternal immunity is a form of passive immunity. There are multiple mechanisms for developing maternal immunity. In primates and humans, as well as other mammals that have a haemochorial placenta, the main method of acquiring maternal immunity is through placental transfer, where maternal IgG passes to the foetus through the close contact between the fetal capillary endothelium and the maternal chorionic endothelium. In a number of other animals important for infectious disease, especially canines and chiropterans (bats), this is not the case. These animals have an endotheliochorial placenta, in which the contact between maternal and foetal circulation is less proximate, and consequently, does not offer an avenue for the efficient transfer of $\operatorname{IgG}$. For this reason, offspring of these species typically acquire $\operatorname{IgG}$ through the gastrointestinal tract from colostrum [71].

Regardless of how it was obtained, maternal immunity shares two principal features:

1. It is present $a b$ initio, i.e., the child is not born into the susceptible compartment.

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-42.jpg?height=635&width=676&top_left_y=223&top_left_x=385)

Figure 2.18 The SIRM model with waning immunity allocates births to an intermediate compartment $M$ of maternally immune individuals, whose immunity wanes at the rate of $\omega$.

2. It is relatively short-lived, offering protection for the first months to a year of the child's life $[72]$.

Where maternal immunity is relevant (including by way of maternal vaccination, as is the case for maternal TDaP vaccination), and where infants in their first years of their lives are a significant part of the population, we must therefore reflect this in our models. (See Fig. 2.18.)

A SIRM model does so by reserving a compartment for newborns, who are presumed to be born with some degree of immunity that wanes after a while. The flow rate from $M$ to $S$ is defined by $\omega$, which in turn is the inverse of the mean duration of maternal immunity $\overline{\tau_{M}}$. We may thus describe this model by the system of differential equations in Eq. (2.42).

$$
\begin{align*}
\frac{d M}{d t} & =\underbrace{\phi N}_{\text {vertically immune births }} \\
\frac{d S}{d t} & =-\underbrace{\beta S I}_{\text {mass action }}+\underbrace{\omega M}_{\text {waning of vertical immunity }}  \tag{2.42}\\
\frac{d I}{d t} & =\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\gamma I}_{\text {recovery }}, \\
\frac{d R}{d t} & =\underbrace{\gamma I}_{\text {recovery }} .
\end{align*}
$$

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-43.jpg?height=531&width=954&top_left_y=229&top_left_x=292)

Figure 2.19 Key events in the timeline of an infectious process. The latent period (yellow) denotes the period between infection and infectiousness. Note that the symptomatic period does not exactly coincide with the infectious period. In many, but not all, infectious diseases, the abatement of symptoms tends to coincide with the end of infectiousness. Equally, some diseases may not be accompanied by a noticeable symptomatic period.

### 2.4 Models with latent periods, asymptomatic infection, and carrier states

So far, we have assumed that an infected individual becomes immediately infectious. (See Fig. 2.19.) We break with this assumption in this section, and look at ways to account for three different scenarios:

- latent periods (the time between infection and onset of infectiousness),
- asymptomatic infections (where a part of the infected population does not experience symptoms), and
- carrier states, where the person recovers from clinical infection but remains infectious.

Definition 2.29 (Latent period). The latent period (also known as the latency period) denotes the timespan between infection and onset of infectiousness.

## Practice Note 2.7 Asymptomatic infection

The notion of asymptomatic infection is sometimes a little muddled, due to confusion with the latent period (Definition 2.29). True asymptomatic infection occurs when a patient transits into the infectious compartment and subsequently leaves it, without showing clinically appreciable symptoms. Strictly speaking, this may include biomarkers (such as elevated leukocyte counts), but in practice, we consider a patient asymptomatic if the condition resolves (into susceptibil-
ity, immunity, or some other post-infectious status) without a noticeable clinical picture.

Asymptomatic patients pose two main concerns:

- Because illness often limits a person's interactions with society, asymptomatic patients are more likely to go about their ordinary business and infect others than symptomatic infectious individuals, who are both aware of their status and potentially prevented from pursuing their ordinary activities thereby.
- On the other hand, where symptoms of the illness are intrinsically connected to the mode of transmission, as is the case, e.g., for droplet infections, asymptomatic patients may have a lower infectiousness.

It is, in addition, not easy to identify asymptomatic carriers. Seroprevalence studies are costly, and often yield little information. Antibody seroprevalence studies do not indicate when the patient had the disease (although the ratio of IgG to IgM may differentiate acute phase infection from a resolved infection). Antigen seroprevalence studies, on the other hand, only return positive results for a relatively short period of time. Where asymptomatic transmission is a significant part of a pathogen's life in a population, antigen seroprevalence studies should be carried out and correlated with clinical symptoms to elicit the ratio of asymptomatic patients.

### 2.4.1 Case study: the true story of "typhoid Mary"

Mary Mallon was born in 1869 in Cookstown, County Tyrone, then part of Britishruled Ireland. Like many of her countrymen, she immigrated to the United States at a young age, where she eventually found employment as a cook. During her lifetime, it was suspected that she has unintentionally (albeit perhaps negligently) infected over fifty people with typhoid [73].

Typhoid fever is a bacterial disease caused by gastrointestinal infection by Salmonella enterica serovar Typhi. In most patients, it causes an unpleasant but manageable disease that resolves fully. However, as many as one in twenty patients become chronic carriers, who continue to be infectious for their lifetimes. Mary Mallon was one of the unfortunate few who fell into that category. It is hypothesized today that she contracted typhoid at birth.

Her case, which involved prolonged quarantine on North Brother Island for almost half her life, raises complex moral and ethical questions about reconciling the interests of public health with the moral imperative to respect individual liberties and treating the sick (even if asymptomatic) with compassion [74]. However, it also highlights the difficulties of modeling infectious diseases, where some patients recover into an asymptomatic carrier state. This is the subject of the present section.

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-45.jpg?height=108&width=941&top_left_y=227&top_left_x=294)

Figure 2.20 In a SEIR model, patients go through an exposed $(E)$ phase, during which they are considered to be infected but not yet infectious.

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-45.jpg?height=695&width=1035&top_left_y=450&top_left_x=247)

Figure 2.21 Solutions of a SEIR model for $\Re_{0}=6.0, \tau=12$ and $\sigma=0.1$.

### 2.4.2 Modeling the latent period: SEIR models

In a SEIR model, we split the hitherto monolithic compartment of infected individuals into exposed $(E)$, who are infected but not infectious, and infectious $(I)$, who are infectious as well. Consequently, patients will flow from $S$, initially, into $E$. The rate of transition $\sigma$ from $E$ to $I$ is the inverse of $\overline{\tau_{l}}$, the average duration of the latency period. (See Figs. 2.20 and 2.21.)

It is important to remember that the governing mass action is still between the susceptible and the infectious population (see Subsection 2.1.3). Consequently, the flow from $S$ to $E$ is determined by $S$ and $I$, and largely independent from $E$.

The system of governing differential equations is thus

$$
\begin{align*}
& \frac{d S}{d t}=-\underbrace{\beta S I}_{\text {mass action }} \\
& \frac{d E}{d t}=\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\sigma E}_{\text {exposure }} \\
& \frac{d I}{d t}=-\underbrace{\sigma E}_{\text {exposure }}-\underbrace{\gamma I}_{\text {recovery }} \tag{2.43}
\end{align*}
$$

$$
\frac{d R}{d t}=\underbrace{\gamma I}_{\text {recovery }}
$$

Because the $E$ compartment acts as an "anteroom" to infectiousness, SEIR models tend to result in a slower development of the pathogenic dynamics. The reverse of the model is that during the latent period, the infection might be much harder to detect. Since by definition the latent period precedes the onset of symptoms, individuals are typically asymptomatic and unaware that they have been infected. For this reason, in spatial models of dissemination and diffusion, longer latent periods may result in wider spatial spread.

## Practice Note 2.8 Privacy-preserving exposure tracing

One of the new tools in the public health toolbox that came to be tested for the first time during the COVID-19 pandemic is privacy-preserving exposure tracing [75]. This is a technique that depends upon the ubiquity of smartphones that can use Bluetooth to send signals to nearby devices without the need for an organized network. Devices send anonymous random identifiers to all nearby devices. The low power and thus spatial limitation of Bluetooth is, in this context, a feature, rather than a bug; the limited range corresponds to a fairly good estimate of exposure for a droplet infection. Upon a positive test result, users can then "report" their status to the public health authorities anonymously using their random identifier. The authorities can then trigger exposure notifications on all devices that have been in contact with the infected user's device recently.

This technique is not foolproof, and abounds in false negatives and false positives alike. For instance, since radio waves can propagate in different ways from infectious droplets, a person working on a different floor of the same building could get an exposure notification when in fact actual exposure would not have occurred. At the same time, exposure notifications rely greatly on a cooperative userbase, who report positive tests and maintain tracking throughout. Nevertheless, it is a cost-effective solution that is technologically easy to implement and imposes minimal social burdens in return for the benefits of relatively reliable exposure notifications.

## Computational Note 2.6 Solving SEIR models

The functional definition for SEIR models is quite analogous to previous models, namely:

```
def deriv(t, y, beta, gamma, sigma):
    S, E, I, R = y
    dSdt = - beta * S * I
    dEdt = beta * S * I - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt
```

The versatility of compartmental epidemic models and their representationand solution-as systems of ODEs is that these models can be expanded with ease, by simply changing the derivative function's definition. Other than ensuring that the sigma parameter is taken, solving a SEIR model's IVP computationally is no different from a SIR model.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch02/ sir_ mode7s.

### 2.4.3 Models of recovery into carrier state

In the preceding models, recovery might have conferred immunity, but it was in any case the end of infectiousness. In carrier state models, a proportion of infectious patients recover into asymptomatic carriers, who remain infectious potentially for life, even though their symptoms have subsided. SIRC models allow us to characterize such situations.

Definition 2.30 (Carrier). A carrier is an individual who is asymptomatic but capable of transmitting the disease, typically, where this period of time lasts relatively long compared to acute symptomatic infection. Depending on the model, the carrier compartment may include the primary asymptomatic infected, who never develop symptoms, or be limited only to recoveries into a carrier state.

### 2.4.3.1 Recovery into carrier state with equal infectiousness

The SIRC model assumes that carriers eventually clear the infection and become immune, in $\overline{\tau_{c}}$ time. We will denote the rate of carriers who become immune as $\omega=\bar{\tau}_{c}-1$, in line with the way we denoted waning immunity. (See Figs. 2.22 and 2.23.)

From the perspective of mass action, a susceptible individual may contract the infection from a carrier or an infectious individual. Therefore we have to treat $I$ and $C$ as a single compartment for the mass action term, assuming for this iteration of the model that infectiousness is identical for symptomatic and asymptomatic carriers. We denote the fraction of individuals who recover into a carrier state $(C)$, rather than immune recovery $(R)$ by $\theta$. Finally, we use the transfer term $\omega C$ to denote the rate at which carriers recover. This gives us the system of differential equations

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-48.jpg?height=694&width=1024&top_left_y=229&top_left_x=211)

Figure 2.22 Solutions of a SIRC model for $\Re_{0}=6.0, \tau=12$, the waning rate $\omega=0.005$ and the fraction of carriers $\theta=0.25$. Note the elongation of the infectious curve due to carriers.

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-48.jpg?height=391&width=670&top_left_y=1088&top_left_x=386)

Figure 2.23 The SIRC model results in a carrier state $C$ and a recovered state $R . \theta$ denotes the proportion of infected who go on to be carriers. $\omega$ is the rate at which carriers convert to noninfectious, immune recovery.

$$
\begin{align*}
& \frac{d S}{d t}=-\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\beta S C}_{\text {from infected }}, \\
& \frac{d I}{d t}=\underbrace{\beta S(I+C)}_{\text {mass action }}-\underbrace{\gamma I}_{\text {recovery }}, \\
& \frac{d R}{d t}=\underbrace{(1-\theta) \gamma I}_{\text {recovery into } R}+\underbrace{\omega C}_{\text {recovery from } C}, \tag{2.44}
\end{align*}
$$

$$
\frac{d C}{d t}=\underbrace{\theta \gamma I}_{\text {recovery into carrier state }}-\underbrace{\omega C}_{\text {recovery to } R}
$$

## Computational Note 2.7 Solving SIRC models

Numerical solutions for SIRC models are arrived at much the same way as previous ODEs. The functional definition of the ODE in (2.44) is

```
def deriv(t, y, beta, gamma, omega, theta):
    S, I, R, C = y
    dSdt = - beta *S*(I + C)
    dIdt = beta * S * (I + C) - gamma * I
    dRdt = (1 - theta) * gamma * I + omega * C
    dCdt = theta * gamma * I - omega * C
    return dSdt, dIdt, dRdt, dCdt
```

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch02/ sir_ mode1s.

### 2.4.3.2 Accounting for reduced infectiousness

In the model above, we have assumed that symptomatic and asymptomatic carriers are equally infectious. This is not always warranted; symptoms of infectious disease are not mere epiphenomena, they are often evolutionary adaptations by the pathogen to accelerate its spread. A pathogen does not intrinsically benefit from causing a violent cough or nasal discharge, for instance, except that such activities enable it to be transmitted more easily. The consequence is that asymptomatic carriers, by reason of their asymptomatic state, might have a lower infectious propensity. We will use a discount factor $\alpha$ to reflect this.

The overall structure of a model that accounts for reduced infectiousness is the same as that of the equiinfectious model discussed in Subsection 2.4.3.1, with the exception that the infection term attributable to $C$ is multiplied by the correction factor $\alpha$. We implement this compensation by amending the mass action term to take account of the reduced rate of transmission, so that it becomes $\beta S(I+\alpha C)$. Including that into Eq. (2.44) yields

$$
\frac{d S}{d t}=-\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\beta S \alpha C}_{\text {from } I}
$$

$$
\begin{align*}
& \frac{d I}{d t}=\underbrace{\beta S(I+\alpha C)}_{\text {mass action }}-\underbrace{\gamma I}_{\text {recovery }},  \tag{2.45}\\
& \frac{d R}{d t}=\underbrace{(1-\theta) \gamma I}_{\text {recovery into } R}+\underbrace{\omega C}_{\text {recoveries from } C} \\
& \frac{d C}{d t}=\underbrace{\theta \gamma I}_{\text {recovery into } C}-\underbrace{\omega C}_{\text {recoveries from } C} .
\end{align*}
$$

## Computational Note 2.8 Solving SIRC models with reduced infectiousness

To adapt the solution for Eq. (2.44) for Eq. (2.45), we simply add the factor a 1 pha to represent the discount factor $\alpha$ :

```
def deriv(t, y, beta, gamma, omega, theta, alpha):
    S, I, R, C = y
    dSdt = - beta * S * (I + (C * alpha))
    dIdt = beta * S * (I + (C * alpha)) - gamma * I
    dRdt = (1 - theta) * gamma * I + omega * C
    dCdt = theta * gamma * I - omega * C
    return dSdt, dIdt, dRdt, dCdt
```

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch02/s ir_ models.

### 2.4.3.3 $\mathfrak{R}_{0}$ in models with a carrier state

Where a pathogen has a clinically significant infectious asymptomatic carrier state, the $\mathfrak{R}_{0}$ will have to be adjusted to reflect this. We do so by adding a term to $\frac{\beta}{\gamma}$ to reflect the infected who become carriers. We know that carriers are less efficient at producing secondary infections, therefore the numerator term will have to be multiplied by the adjustment factor $\alpha$. We multiply this by $\theta$ to reflect the relative proportion of carriers and divide it by $\omega$ to reflect the loss over time of carriers to the waning of the carrier state. Putting it all together, we may calculate $\mathfrak{R}_{0}$ as

$$
\mathfrak{R}_{0}=\underbrace{\frac{\beta}{\gamma}}_{\mathfrak{R}_{0} \text { without carrier state }}+\underbrace{\frac{\theta \overbrace{\alpha}^{\text {adjustment factor }} \beta}{\omega}}_{\text {carrier state }}=\beta\left(\frac{1}{\gamma}+\frac{\theta \alpha}{\omega}\right)
$$

### 2.5 Empirical parameter estimation

Many parameters of an infectious disease model lend themselves to easy, or at least feasible, measurement or inference:

- the length of the infectious period $\tau$ can be ascertained from studies of the serial interval,
- the recovery rate $\gamma$ can be calculated from $\tau$,
- the case-fatality ratio (CFR) can be derived from case reports and mortality reports, and
- the duration of the latency interval can be ascertained from contact tracing studies.

$\mathfrak{R}_{0}$, however, is a derived quantity, and it is not amenable to direct measurement. For this reason, we need ways to estimate it in practice, and ways to identify it in relation to the model's conditioning variables in complex models.

### 2.5.1 Case study: early estimation of the $\mathfrak{R}_{0}$ of Covid-19

In the waning years of 2019, a new respiratory infection surfaced in Wuhan, People's Republic of China. Within a few short weeks, it attained global spread, and by the end of January 2021, twenty-seven countries were affected. The WHO declared this new respiratory disease a Public Health Emergency of International Concern on 30 January 2020 and a pandemic six weeks later, on 11 March. The rest, of course, is history.

The early days of the COVID-19 pandemic highlight the fast-moving, dynamic nature of infectious disease outbreaks. To adequately support public health responses to rapidly developing outbreaks, it is important to have methods that allow us to ascertain key parameters from real-world data that we can then fit models onto. First and foremost among these is, of course, $\mathfrak{R}_{0}$.

A systematic review by Alimohamadi, Taghdir, and Sepandi [76] has surveyed statistical and probabilistic models of COVID-19 in China. The 29 models examined by the authors found values ranging between 1.90 and 6.49. Exponential growth-based models alone ranged between 1.90 and 6.30 [76]. The authors arrived at a pooled estimate of 3.32 ( $95 \% \mathrm{CI}$ : $2.81-3.82$ ), but what is more revealing is the wide variance. Even based on the same data, there were significant disparities in $\Re_{0}$ based on the particular implementations and algorithms.

The attempts to quantify the $\mathfrak{R}_{0}$ of COVID-19 are an instructive example of the sensitivity of $\Re_{0}$ to methods used to estimate it. $\Re_{0}$ is often seen as a convenient encapsulation of a pathogen's behavior in a population, but it is rarely recognized how malleable it is as a guiding figure for interventions. It is an instructive tool to illustrate pathogenic dynamics and a useful value to characterize some parts of the infectious process, but it should not become the subject of exaggerated focus. Nor should it be presented uncritically, without clearly conveying that its value greatly depends on the method used to ascertain it.

In a 2020 article, Pandit pointed out the paradox of $\mathfrak{R}_{0}$ : it is "relatively easy to explain, more complicated to understand (even graphically), and very difficult to calculate" [77]. We will concentrate on $\mathfrak{R}_{0}$, because unlike other variables in simple
compartmental models, it is not directly ascertainable or trivially related to a variable that is (the way, e.g., $\gamma$ is trivially related to the mean infectious period $\tau$ by way of being its inverse).

## Practice Note 2.9 Communicating $\Re_{0}$

$\Re_{0}$ is one of the more descriptive parameters of an infectious disease. It is surprisingly easy to explain relatively accurately what it accomplishes. However, the $\Re_{0}$ is not a trivially measurable quantity.

In fact, as we shall see throughout this chapter, how we measure $\mathfrak{R}_{0}$ affects its value greatly. For this reason, excessive attention devoted to $\Re_{0}$ might mislead the public. The transmission of infections and the dynamics of infectious diseases are complex and multifactorial. They depend on more than a single figure, and using $\Re_{0}$ alone to illustrate pertinent facts about an infectious disease might not be sufficient. It is up to disease modelers not only to know how to calculate $\Re_{0}$, but also to know which calculation to use when, and in their communications guard against undue attention directed at $\mathfrak{R}_{0}$ (and, by extension, $\mathfrak{R}_{t}$ ).

### 2.5.2 Next-generation matrices

The next-generation matrix is by far the most popular method of determining the $\Re_{0}$ of a complex model, as we shall encounter increasingly often in later steps. We proceed in three steps to calculate $\Re_{0}$ using the next-generation method:

1. We divide the model into infected and noninfected subsystems. We denote these as the vectors $x$ and $y$, which are vectors comprising infected and noninfected compartments, respectively.
2. We construct the vector $F(x, y)$, which comprises flows into $x$, and the vector $V$, which comprises flows out of $x$. Note the nomenclature here: $F$ is a vector-valued function, whereas $\mathbf{F}$ is a matrix (some texts use $\mathcal{F}$ for the vector-valued functions and $F$ for the matrix, but this may altogether muddy the waters). These, together, make up $\frac{d x}{d t}$.

$$
\begin{equation*}
\frac{d x}{d t}=F(x, y)-V(x, y) \tag{2.47}
\end{equation*}
$$

We can represent this change as the Jacobian matrices $\mathbf{F}$ and $\mathbf{V}$ :

$$
\begin{align*}
\mathbf{F} & =\left(\frac{\partial F}{\partial x}\right) \\
\mathbf{V} & =\left(\frac{\partial V}{\partial x}\right) \tag{2.48}
\end{align*}
$$

3. The $\mathfrak{R}_{0}$ of the system is obtained by taking the spectral radius of $\mathbf{F} \mathbf{V}^{-1}$.

Definition 2.31 (Next-generation matrix). The matrix $\mathbf{F V} \mathbf{V}^{-1}$ is called the next generation matrix. Its spectral radius (see Definition 2.32), as evaluated at the disease-free equilibrium, equals the $\Re_{0}$.

Consider, for instance, the SIR model described in (2.6). Our $x$ and $y$ vectors are, of course,

$$
\begin{equation*}
x=(I), \quad y=\binom{S}{R} \tag{2.49}
\end{equation*}
$$

The vector-valued functions can then be evaluated as

$$
\begin{align*}
\vec{F}(I) & =\beta S I \\
\vec{V}(I, S, R) & =\gamma I \tag{2.50}
\end{align*}
$$

Taking the partial differentials and evaluating it at the disease-free equilibrium, we get

$$
\begin{align*}
& \mathbf{F}=\left.\left(\frac{\partial \beta S I}{\partial I}\right)\right|_{(1,0,0)}=\beta \\
& \mathbf{V}=\left.\left(\frac{\partial \gamma I}{\partial I}\right)\right|_{(1,0,0)}=\gamma \tag{2.51}
\end{align*}
$$

And thus, we obtain $\mathfrak{R}_{0}$ as the spectral radius $\varrho\left(\mathbf{F} \mathbf{V}^{-1}\right)$, which in this case is of course $\frac{\beta}{\gamma}$.

Next-generation matrices can be helpful in understanding the dynamics of complex systems. In practice, the next-generation matrix is most useful in estimating the $\mathfrak{R}_{0}$ of multicompartmental models, as we will encounter them in Chapter 4 , in which there are separate compartments for hosts and vectors, or in Chapter 3, where we separate individuals by their behavioral risk into high- and low-risk groups. Symbolic evaluation is often helpful in making sense of such models. Computational Note 2.9 discusses the use of symbolic computation for such a scenario.

Definition 2.32 (Spectral radius and dominant eigenvalue). Let $\Lambda(\mathbf{A})$ be the set of all eigenvalues $\lambda_{1 \ldots i}$ of $\mathbf{A}$.

The spectral radius of $\mathbf{A}$ is the eigenvalue of $\mathbf{A}$ with the largest absolute value. We denote this as $\varrho(\mathbf{A})$. Every matrix has a defined spectral radius.

If there exists an eigenvalue $\lambda_{d}$ in $\Lambda(\mathbf{A})$ so that its absolute value is larger than any other eigenvalue in $\Lambda(\mathbf{A})$, it is a dominant eigenvalue of $\mathbf{A}$. Not every matrix has a dominant eigenvalue. Every dominant eigenvalue, where it exists, is equal to the spectral radius of the matrix.

## Computational Note 2.9 Symbolic computation of $\Re_{0}$ in a complex model

So far, we have used computational tools to give us numerical solutions to problems. However, we can use computational tools to solve analytical problems, too. Symbolic computation deals with arriving at analytical solutions using the manipulation of symbols (which in this case is just a fancy term for functions, variables, operators, and anything else mathematics is "made of"). Computer algebra systems (CAS), from the simple solvers on a graphing calculator to complex automated theorem-provers, do exactly that.

In Python, we can make use of the SymPy package to perform symbolic manipulations. Consider a SEIR model with births and mortality:

$$
\begin{align*}
\frac{d S}{d t} & =-\beta S I-\mu S+\phi(S+E+I+R) \\
\frac{d E}{d t} & =\beta S I-(\sigma+\mu) E  \tag{2.52}\\
\frac{d I}{d t} & =\sigma E-\gamma I-\mu I \\
\frac{d R}{d t} & =\gamma I-\mu R
\end{align*}
$$

We can obtain a neat symbolic solution for this using SymPy. First and foremost, we need to import SymPy, and define our symbols:

```
import numpy as np
from sympy.interactive.printing import init_printing
init_printing(use_unicode=True, wrap_1ine=True)
from sympy.matrices import Matrix
from sympy import symbols
from sympy import factor
S, E, I, R, beta, mu, phi, sigma, gamma
    = symbols("S E I R beta mu phi sigma gamma")
```

Next, we define $x$ :

$X=$ Matrix(np.array([E, I]).T)

We can now define the vector-valued functions $F$ and $V$ :

Fvec $=$ Matrix(np.array([beta $*$ S $*$ I, O]).T)

```
Vvec = Matrix(np.array([(mu + sigma) * E, -sigma * E
    + (gamma + mu) * I]).T)
```

We evaluate Fvec at $S=1$ :

Fvec $=$ Fvec.subs(\{S: 1$\})$

Vvec $=$ Vvec.subs(\{S: 1\})

SymPy has a convenient function to calculate the Jacobian of a vector-valued function. Recall that the next-generation matrix $\mathbf{F} \mathbf{V}^{-1}$ is the product of the Jacobian of $F$ with respect to $x$ multiplied by the inverse of the Jacobian of $V$ in respect of $x$. We may write this as

ngm $=$ Fvec.jacobian(X) * Vvec.jacobian(X).inv()

The function .eigenvals() returns the spectrum (the list of all eigenvalues) of the matrix. Unfortunately, SymPy cannot automatically determine the dominant eigenvalue, but this should not be difficult manually.

Factoring the dominant eigenvalue gives us a nice-looking output:

factor(1ist(ngm.eigenvals().keys())[0])

$$
\frac{\beta \sigma}{(\gamma+\mu)(\mu+\sigma)}
$$

Symbolic application of the next-generation matrix may often be your best choice to obtain $\Re_{0}$ from the description of a compartmental model as a differential equation. This is so in particular if the system has many compartments and a large number of variables, as we will indeed encounter later on in models of more complex disease.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch02/ symbol ic_ ro.

### 2.5.3 Determining $\mathfrak{R}_{0}$ from epidemiological data

$\mathfrak{R}_{0}$ is by far one of the most useful parameters to obtain from epidemiological data, as it holds within itself the values of both $\beta$ and $\gamma$, but unlike both of those variables, it is more amenable to measurement. Together with information about the length of the infectious period, which is also measurable, the $\mathfrak{R}_{0}$ can help fit a SIR model, or any of the variations on that theme, onto a real-world epidemic.

### 2.5.3.1 Contact tracing

In practice, contact tracing is one of the most widespread methods of estimating $\mathfrak{R}_{0}$. The idea of contact tracing is to identify secondary cases by asking confirmed cases

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-56.jpg?height=806&width=1189&top_left_y=230&top_left_x=135)

Figure 2.24 Network of sexual interactions among 40 homosexual men, based on Auerbach et al. [78]. Nodes are colored by their degree, i.e., the number of nodes connected to them.

to list potential contacts, then surveilling those contacts for symptoms and/or seroconversion. Though contact tracing is time-consuming, resource-intensive, and depends greatly on patient cooperation for its success, it is nonetheless the most effective ways of ascertaining $\Re_{0}$.

Consider the study by Auerbach et al. , one of the most famous examples of network analysis used in epidemiology [78]. This study was one of the early examinations of HIV/AIDS, proceeding by identifying the sexual contacts of 40 homosexual men. It is also the source of the colloquialism "patient zero" to mean what ought more appropriately be called the index case of an infection. If we conceive of the results of contact tracing as the directed graph $\mathcal{G}(V, E)$, then $\Re_{0}$ will be the average outdegree of $\mathcal{G}$.

This network is visualized in Fig. 2.24. The mean outdegree is approximately 1.026 , which almost definitely underestimates the actual $\Re_{0}$ figure by as much as a factor of two. This highlights a fundamental fact about using contact tracing data to get to an $\mathfrak{R}_{0}$ estimate: the result is only going to be as good as the contact tracing exercise itself. It is difficult to remember everyone one has been in contact with on a given day, never mind over the span of years (could you list everyone you were within $6 \mathrm{ft}$ of in the last 48 hours, everyone you touched in the last 30 days, and everyone you were intimate with over the last five years?). In this case, the matter was complicated by the fact that many of the persons were, sadly, deceased by the time contact tracing was carried out, and the researchers had to rely on information from friends and partners. In other contexts, a person might not be aware of all the
other individuals they have interacted with, or at least not be able to provide their details. This latter case has been a particular issue during the early AIDS epidemic due to anonymity of homosexual encounters, where such encounters were legally or socially unacceptable at the time, and it continues to be an issue for airborne infections, where contact tracing might have to extend to a surprisingly large number of people, many of whom we never have a profound enough social interaction with to even know their names. Such studies therefore are bound to underestimate $\mathfrak{R}_{0}$ by some degree. Nevertheless, contact tracing is the most concrete and direct approach to identifying $\mathfrak{R}_{0}$, and for that reason, it remains an important pillar of epidemic surveillance.

## Computational Note 2.10 Contact tracing data with NetworkX

In this example, we will be using NetworkX to estimate $\mathfrak{R}_{0}$ from contact tracing data.

We begin by instantiating a directed graph (DiGraph) object:

## $G=n x . D i G r a p h()$

There are many ways to build up a graph object in NetworkX, but where we do not intend to attach complex properties, the easiest is by far to provide edges, and let NetworkX create the nodes for us.

To make data entry easier, it is often a good idea to build a dictionary object, where the keys are the source and the values are a list of destinations of the directed edges.

```
EDGES = {"O": ["LA3", "LA8", "LA6", "NY15", "NY9", "NY4", "NY3",
        "LA9"],
    "LA3": ["LA2", "FL1"],
    "FL1": ["TX1", "GA2", "GA1", "FL2"],
    "GA1": ["PA1"],
    "LA2": ["LA1", "LA4"],
    "LA4": ["LA5"],
    "LA6": ["LA7", "SF1"],
    "NY9": ["NY18", "NY1", "NY17"],
    "NY18": ["NY20"],
    "NY17": ["NY22", "NY21", "NY14", "NY7"],
    "NY7": ["NY6", "NY16"],
    "NY11": ["SF1", "NY13"],
    "NY13": ["NY12"],
    "NY14": ["NY5", "NJ1"],
    "NJ1": ["NY21"],
    "NY5": ["NY2", "NY19"],
```

```
"NY2": ["NY19"],
"NY19": ["NY8"]}
```

We can then merge this into the graph using a simple nested iterator:

```
for o in EDGES:
    for d in EDGES[o]:
    G.add_edge(o, d)
```

Finally, we can obtain the mean outdegree, which is our estimator for $\mathfrak{R}_{0}$, by obtaining the outdegree of each node (which is what G.out_degree returns), slice the array to get an array only of the outdegree values, then obtain the average:

np.mean(np.array(1ist(G.out_degree))[:,1].astype("uint8"))

>> 1.0256410256410255

### 2.5.3.2 Wallinga-Lipsitch method

The most popular way of estimating $\Re_{0}$ in early infection is the method outlined by Wallinga and Lipsitch [79]. This method is most useful in the early phases of an outbreak, when $S$ largely approximates 1, i.e., almost everyone is susceptible. Under such conditions, the disease spreads exponentially, so that after $n$ generations, $\sum_{i=0}^{n} R_{0}^{i}$ have been infected at some point. Note that this assumption does not hold for long, or, indeed, mathematically strictly speaking, it does not hold at all, but is in the very beginning of an epidemic an acceptable approximation.

The basis of the Wallinga-Lipsitch approach is that early enough in an epidemic, growth is exponential. This exponential growth rate $r$ governs initial spread so that at least in the beginning, $I(t)=c e^{r t}$. We can, of course, obtain $c$ and $r$ by fitting an exponential model to the data. In practice, it is often simpler to apply a log transformation to the data, then apply a simple linear regression.

Next, we must determine the moment generating function $M$ of the generation time distribution $g(t)$. We can obtain this from epidemiological field studies that compared the symptom onset time of the index case and their secondaries.

Definition 2.33 (Generation time). The generation time or generation interval of a case is the time between the index case's infection and the secondary case's infection.

For instance, if Alice (the secondary case) is infected on Friday by Bob (the index case), who was infected on Monday, the generation time with respect to Alice is 4 days.

Some texts define the generation interval as the time between symptom onsets. Under the assumption that the latency period is largely the same for everyone, the two definitions are equivalent.

Table 2.2 Moment generating functions of distributions frequently used in modeling infectious diseases.

|  | Distribution | Moment-generating function $M(t)$ |
| :---: | :---: | :---: |
| Normal | $\operatorname{Normal}(\mu, \sigma)$ | $e^{t \mu+\frac{1}{2} \sigma^{2} t^{2}}$ |
| Chi-squared | $Q_{k}^{2}$ | $(1-2 t)^{-\frac{1}{2} k}$ |
| Gamma | $\Gamma(k, \theta)$ | $(1-t \theta)^{-k}\left(t<\theta^{-1}\right)$ |
| Exponential | $\operatorname{Exp}(\lambda)$ | $\left(1-t \lambda^{-1}\right)^{-1} \quad(t<\lambda)$ |
| Poisson | $\operatorname{Poisson}(\lambda)$ | $e^{\lambda\left(e^{t}-1\right)}$ |
| Laplace | $\operatorname{Laplace}(\mu, b)$ | $\frac{e^{t \mu}}{1-b^{2} t^{2}}\left(\|t\|<b^{-1}\right)$ |

$\mathfrak{R}_{0}$ is then calculated as the inverse of the moment-generating function evaluated at $-r$, i.e.,

$$
\begin{equation*}
\Re_{0}=\frac{1}{M(-r)} \tag{2.53}
\end{equation*}
$$

Table 2.2 lays out the moment-generating functions of commonly used distributions.

## Computational Note 2.11 Symbolic determination of the momentgenerating function

SciPy's optimize subpackage offers a very useful function, curve_fit, which can fit an arbitrary function to data. Given a time series, we can fit the model $I(t)=c e^{r t}$ to our actual data. First, we define the function that represents this model:

def exp_model(t, c, r):

return $c * n p . \exp (r * t)$

Note that this is equivalent to applying a logarithm transform and fit a simple linear model. We will, however, for the sake of clarity, use the exponential formulation.

Next, we fit this model to a time series. In this example, we will be using a COVID-19 data set for the United States during the first wave (March-June 2020), using pd.read_csv():

```
data = pd.read_csv("https://raw.githubusercontent.com/nytimes/\
    covid-19-data/master/rol1ing-averages/us.csv",
    usecols=["date", "cases"],
    dtype={"date": str, "cases": int})
```

Next, to control for weekly variations in reporting, we take the seven-day moving average:

data["cases"] = data.cases.rol1ing(7).mean()

We filter the time series for our desired dates:

```
data = data[(data.date >= "2020-02-01")
    & (data.date <= "2020-04-11")]
```

Now, we can fit our model against the time series to obtain the growth rate:

```
popt, pcov = optimize.curve_fit(exp_model,
    data.index,
    data.cases,
    p0=(1e-2, 1e-6),
    maxfev=10000)
```

The resulting popt object is a 2-length array that contains the values of $c$ and $r$ obtained by fitting the model against the data. Fig. 2.25 shows actual case counts during the period under examination and the exponential fit using the parameters we obtained through the above.

We now have $r$ (as popt[1]), which allows us to calculate the momentgenerating function at $-r$. We know from metaanalyses (e.g., Griffin et al. [80]) that $\operatorname{Normal}(5,1.15)$ a good estimate of the parameters for the generation time of COVID-19. We can symbolically evaluate the moment-generating function

$$
M(t)_{\mu, \sigma}=e^{t \mu+\frac{1}{2} \sigma^{2} t^{2}}
$$

using SymPy. First, we initialize the variables:

mu, sigma, t, blamda = sympy.symbols("mu sigma t lambda")

Next, we express the moment-generating function in those terms:

```
mgf_norma1 = E ** (t * mu + (sigma ** 2 * t ** 2)/2)
```

In the above, E is the constant $e$, which is imported from SymPy. We can now estimate the $\mathfrak{R}_{0}$ by evaluating the moment-generating function at $\mu=5$ and $\sigma=1.15$, at $-t$. $-t$, of course, is -1 * popt[1].

```
1/mgf_norma1.subs({"t": -1 * popt[1],
    "mu": 5,
    "sigma ": 1.15})
```

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-61.jpg?height=638&width=1077&top_left_y=226&top_left_x=226)

Figure 2.25 Exponential fit on a time series of COVID-19 in the United States in early 2020. Data from The New York Times, based on reports from state and local health agencies.

The . subs( ) method provided by SymPy applies to all kinds of symbolic objects. .subs () takes a dictionary of symbols and replaces them with a specified value, essentially parametrically evaluating the expression.

Notably, our result of an $\Re_{0}$ of 1.49 is rather lower than what is commonly understood to be the $\Re_{0}$ of COVID-19. This is for a number of reasons, which highlight some of the shortcomings of the Wallinga-Lipsitch method. Our estimate is only as good as our fit for the growth rate and the distribution of the generation time. Obtaining the generation time is often nontrivial in practice, and often depends on the availability of monitoring and tracing tools, which might not be available at the very beginning of the epidemic, just when this model is at its most powerful.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch02/ symbo 7 ic_ mgf.

The Wallinga-Lipsitch solution is a convenient method in the very beginning to obtain the value of $\mathfrak{R}_{0}$ as long as there is some information about the generation time or serial interval, but its accuracy hinges greatly on the adequacy of this information. In other words, the wrong distribution fit over the data will yield erroneous results. Regardless of distribution used, it is crucial to document the assumptions employed when describing a Wallinga-Lipsitch estimate of $\Re_{0}$.

## Practice Note 2.10 Using the Wallinga-Lipsitch method

The Wallinga-Lipsitch method ultimately provides us a very convenient way of easily estimating $\mathfrak{R}_{0}$ in the earliest days of an outbreak. As it relies greatly on the exponential nature of early epidemics, it is not suitable for the modeling of endemic disease. Keeling and Rohani [39] note two additional difficulties with the Wallinga-Lipsitch approximation:

1. The model assumes that at time 0 , there will be a negligibly small number of infected individuals amidst a susceptible population, with no part of the population immune. This may hold true for a truly novel pathogen or a hitherto isolated population (as is the case, e.g., when a new disease is introduced to a geographically and epidemiologically isolated group), but in general, even naive populations have some small number of immune individuals owing to cross-immunity with similar pathogens.
2. In the early days of an epidemic, owing to the low number of cases, the epidemic dynamics may be quite turbulent due to stochastic effects, and by the time such stochastic effects subside, the epidemic might no longer be following an exponential growth pattern.

For this reason, $\Re_{0}$ figures estimated from the exponential model are best treated with a degree of caution.

### 2.5.3.3 Hesterbeek-Dietz (final epidemic size) method

A relatively simple method of estimating $\Re_{0}$ from empirical data relies on the difference of the initial state and the state at the end of an epidemic. We have noted earlier that most epidemics reach an equilibrium, where some of the population remains susceptible and some of the population is immune and recovered. We denote this as the final state $S(\infty), I(\infty), R(\infty)$.

In the absence of demographic change, and with some initial immunity (which is almost always a warranted assumption, even for a novel pathogen),

$$
\begin{equation*}
\Re_{0}=\frac{\log S(0)-\log S(\infty)}{S(0)-S(\infty)} \tag{2.54}
\end{equation*}
$$

The main drawback of this approach is that it assumes constant behavior throughout the epidemic, from beginning to the end. This is, however, manifestly not the case in most outbreaks. As time moves on, public health authorities as well as individuals respond to an outbreak, which means that the dynamics are not homogeneous throughout, and consequently this method typically overestimates $\Re_{0}$. In addition, this method is strictly retrospective; it only works where a final state has been established.

### 2.5.3.4 Mean age at infection

Another method that commends itself by easily ascertainable inputs is discussed by Mollison [81] and Dietz and Schenzle [82]. This model assumes a population of naive
births and recovery to immunity, along with perfectly homogeneous mixing, in particular with regard to age.

Definition 2.34 (Mean age of infection). The mean age of infection $A$ is the population mean of the age at which individuals become infected.

Then, $\mathfrak{R}_{0}$ is proportional to the fraction of the mean lifetime $L$ divided by the mean age of acquiring the disease, $A$.

$$
\begin{equation*}
\mathfrak{R}_{0}=1+\frac{L}{A} \tag{2.55}
\end{equation*}
$$

and conversely,

$$
\begin{equation*}
A=\frac{L}{\Re_{0}-1} \tag{2.56}
\end{equation*}
$$

The mean age at infection method is widely used where the mean age of an individual is easy to measure, but other methods, especially contact tracing, are prohibitive. In the wildlife veterinary setting, for instance, information about the mean age of animals and the age of any individual (especially in a "tagged" or otherwise observed cohort) is much easier to come by than any other form of information.

### 2.5.4 Estimating $\mathfrak{R}_{t}$

Similarly to $\mathfrak{R}_{0}$, the time-dependent reproduction number $\mathfrak{R}_{t}$ also permits a number of methods of estimation. Harvey and Kattuman [83] proposed a particularly convenient estimator for $\Re_{t}$, namely

$$
\begin{equation*}
\hat{R}_{k, \tau, t}=\frac{\overbrace{\tau-1}^{\sum_{j=0}^{k-1} y_{t-j}}}{\sum_{\tau=\text {-shifted }}^{k-\text { length moving average }} y_{t-\tau-j}^{k-1}}, \tag{2.57}
\end{equation*}
$$

where $\tau$ is the generation interval, and $k$ is a smoothing constant. Harvey and Kattuman notes that setting $k$ to 7 eliminates intra-week variations, whereas a value used for $\tau$ depends on the infectious process. Conveniently, the fraction in Eq. (2.57) can be expressed as the fraction of a $k$-day rolling sum and a second $k$-day rolling sum shifted by $\tau$ days. We shall use this to our advantage in Computational Note 2.12.

## Computational Note 2.12 Estimating $\Re_{t}$

As noted above, Eq. (2.57) for $\Re_{t}$ can be expressed as the fraction of the $k$-day rolling sum and the $k$-day rolling sum at $t-\tau$. Following Harvey and Kattuman [83], we will be using a $k$-value of 7 to smooth out intra-week variations in reporting. In addition, we will be using data on COVID-19 incidence in the United States from Ritchie et al. [84], and in accordance with common modeling practice (as mentioned, e.g., in Harvey and Kattuman [83]), we will use a value of 4 for $\tau$.

We begin, after ingesting our data into a Pandas data frame, by creating a column for the 7 -day rolling sum:

$d f[" 7 m s "]=d f . n e w \_c a s e s . r o 11 i n g(7) . s u m()$

We assign another column to represent the denominator, which is essentially the $7 \mathrm{~ms}$ column shifted back by $\tau$ :

$d f\left[" 7 m s \_t a u "\right]=d f[" 7 m s "] . s h i f t(4)$

Finally, we obtain our $\mathfrak{R}_{t}$ by dividing the two columns:

$d f[$ "Rt"] = df["7ms"]/df["7ms_tau"]

The result of this calculation is shown in Fig. 2.26. Note that because of the rolling sum and the shift, as well as because of rapid initial dynamics, there is often an unrealistically high spike in the earliest days of an outbreak. It may be worthwhile to limit $\Re_{t}$ plots to the period once the epidemic is no longer in its earliest phases.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch02/rt_ estimation.

### 2.5.5 Estimating recovery rate

The recovery rate $\gamma$ is the inverse of the mean duration of illness $\bar{\tau}$, i.e., $\gamma=\bar{\tau}^{-1}$. For simple SIR models, the best estimate in practical settings is from empirical studies. As a first line of departure, we may consider the mean duration of illness to be the time between onset and resolution of symptoms. However, this is not always quite accurate. Recall that $\gamma$ describes the rate at which individuals transit out of the infectious compartment. Therefore what is actually at concern is the time between onset and end of infectiousness.

A problem with duration of illness data is that it is often difficult to come by in the early stages of an outbreak. Where the pathogen is relatively well-characterized,

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-65.jpg?height=1318&width=1042&top_left_y=229&top_left_x=246)

Figure 2.26 Cases, 7-day rolling sum of cases and $\mathfrak{R}_{t}$ of COVID-19 in the United States between April 2021 and January 2022 estimated using the estimator in Eq. (2.57). Note the prominent increases in $\Re_{t}$ in mid-2021 (Delta) and late 2021/early 2022 (Omicron). Incidence data obtained from Ritchie et al. [84].

typically from previous outbreaks, information from those cases is a good starting point. Ascertaining the mean duration of illness is helped by contact tracing, which can illuminate the length, if any, of a latent or asymptomatic but infectious period. It is worth noting however that such data typically excludes individuals who do not seek medical care, either because it is not accessible to them, because they do not exhibit sufficiently severe symptoms (or indeed any symptoms at all) or, in rare cases, because they succumb to the disease before they find medical attention.

### 2.5.6 Estimating vital dynamic parameters

Demographic change affects epidemiological modeling in a handful of ways:

- With very few exceptions (which we discussed in Subsection 2.2.3.2), the birth rate determines the accrual of new susceptibles. Growing populations can support pathogens, because they face a much lower risk of "running out of room to spread," i.e., depleting the pool of susceptibles necessary to sustain chains of transmission.
- Mortality (by which we generally mean mortality from causes other than the infectious disease under consideration) may reduce the proportion of immune individuals. If infection provides lifelong immunity, the likelihood of immunity is a strictly monotonously increasing function of age. Since natural mortality in adults also increases with age, immune-recovered individuals are disproportionately represented among those dying of natural causes.
- Emigration generally decreases the pool of immune individuals and immigration increases the pool of susceptible individuals. We are more likely to be immune to the pathogens that are endemic where we live, because we have spent our lives around those pathogens. The reverse of this phenomenon, pathogenic invasion (where a population affected by a pathogen comes into proximity with a susceptible population), is relatively rare (for a description of such an event, see Huag and Nilssen [85]'s description of phocine morbillivirus outbreaks due to an invading population of harp seals, Phoca groenlandica, sparking off an episodic in the immunologically naive population of harbor seals, Phoca vitulina).

Migration is generally not the subject of compartmental models; spatial and agentbased modeling is often much more appropriate to examine the effect of migrational population flows. On the other hand, births and deaths do affect the balance of pathogenic spread at nontrivial timeframes. For this reason, we must now turn our attention to the way to quantify these.

### 2.5.6.1 Mortality

The normal mortality rate is typically considered to be the inverse of the mean life expectancy. Actuarial tables, also known as life tables, contain much additional information in addition to life expectancy. Reading life tables is something of a practiced skill, but as epidemiologists, we are principally concerned only with two numbers:

- $q(x)$ is, by convention, the first (leftmost) value column of a life table. It shows an $x$-aged person's probability of dying within the index period, typically a year. These probabilities can be averaged, or they can be used to construct a statistical distribution.
- $e(x)$ is typically on the rightmost side of the table, and indicates the average number of "remaining" years expected for a person of age $x$. Thus $e(18)$ is the time remaining to reach the mean life expectancy for a person aged 18 today.

It is often important to use the right life tables. Life tables should be reflective of the population under consideration. This requires obtaining life tables for the right population.

## Practice Note 2.11 Avoiding bias by weighting demographic parameters

Often, researchers use national figures for $e(x)$ and $q(x)$, commonly referred to as "total populations." This approach loses its validity when considering subpopulations, whose distribution is significantly different from that of the general population. The consequence is that the inherent differences in life expectancies between ethnicities and genders-often mediating complex socio-economic determinants of health-are ignored. For this reason, if the population being modeled differs from the national average, it may need to be re-weighted.

Re-weighting consists of calculating a proportion-weighted average of values. Thus for a population consisting of $K$ segments (e.g., "Caucasian males," "Caucasian females," "African-American males," and so on), where $p(k)$ is the proportion of a segment $k$ in the entire population,

$$
\begin{equation*}
\overline{e(x)}=\frac{\sum_{i=1}^{K} p(i) e_{k}(x)}{\sum_{i=1}^{K} p(i)} \tag{2.58}
\end{equation*}
$$

and

$$
\begin{equation*}
\overline{q(x)}=\frac{\sum_{i=1}^{K} p(i) q_{k}(x)}{\sum_{i=1}^{K} p(i)} \tag{2.59}
\end{equation*}
$$

### 2.5.6.2 Birth rate

The birth rate, also known as natality, is the person-time-denominated number of births per unit population per unit time. Typically, the crude birth rate (i.e., the birth rate that is not adjusted to reflect differences in age groups) is reported in births per 1000 persons per year.

Ordinarily, the birth rate is by far the preferred metric from which to infer demographic change in a compartmental model with vital dynamics. In some cases, where the population is significantly imbalanced with regard to gender, it may be helpful to use an adjustment. For instance, the birth rate in the US in 2020 was approximately 11 births per year per 1000 persons, whereas the fertility rate was 56.0 births per 1000 women aged 15-44 years. If there are 70\% women aged 15-44 years in a population and $30 \%$ men, the effective birth rate will be 39.2 births per year per 1000. Typically, the world population is approximately $3-6 \%$ weighted towards males. Where the difference between genders in a population is over $10 \%$, rebalancing using the weighted average method might be indicated.

### 2.5.7 Estimating waning rate

The waning rate is the inverse of the duration of immunity. In general, our metric of concern is the duration of effective immunity. This is not necessarily the same as the
decrease in biomarkers evidencing immunity, such as antibody levels, and it is crucial to look at real-world data, i.e., studies of effective duration of protection, alongside biomarkers.

The mean waning rate is, of course, the inverse of the mean duration of immunity. This is generally quite simple to apply. However, in practice, one should not forget to take into account the variance, which can be quite significant. Human and nonhuman animals' immune systems are equally unique and complex. For instance, we know that certain MHC haplotypes are associated with inferior immune response to the Hepatitis B vaccine [86]. Similarly, it is relatively well understood that individuals suffering from immune suppression (e.g., long term users of steroids or immunosuppressive medications) and older individuals typically develop weaker immune responses (quantified as the number of antibodies per unit volume of serum), and their immune responses are often short-lived in comparison to the general population [87].

## Practice Note 2.12 Acquired vs. induced immunity: effects on duration and waning rate

In general, there tends to be no significant difference between acquired immunity (through infection and recovery) and vaccine-induced immunity (through vaccination) in terms of duration and strength of immune response. That being said, there exist well-documented outliers, with Vibrio cholerae infection being the most significant from a public health perspective. As Wrammert et al. demonstrated, vaccine-induced immunity to $V$. cholerae wanes quite rapidly, whereas acquired immunity is much broader and endures for up to a decade [88]. Though equal waning rates for vaccinated and recovered individuals are typically a good starting assumption, infectious disease modelers must be ready to adapt their models if real-world data indicates a meaningful divergence.

### 2.5.8 Multiparameter estimation by nonlinear curve fitting

Curve fitting is a general method that covers a multitude of things. In general, curve fitting methods converge in their overall aim: given a series $y$ and a function $\hat{y}=f_{t}(\theta)$, find $\theta$ so as to minimize a distance metric or "loss" between $\hat{y}$ and $y$. By far, the most frequent method for this is least-squares estimation, i.e.,

$$
\begin{equation*}
\underset{\theta}{\arg \min } \sum_{i=1}^{k}\left(y(i)-f_{i}(\theta)\right)^{2} \tag{2.60}
\end{equation*}
$$

This is mathematically convenient, because the minimum of the expression above occurs where the gradient is zero. This obtains where for all $j \in \theta$,

$$
\begin{equation*}
\sum y(i)-f_{i}(\theta) \frac{\partial\left(y(i)-f_{i}(\theta)\right)}{\partial \theta_{j}}=0 \tag{2.61}
\end{equation*}
$$

For nonlinear systems, this is rarely an easily ascertainable figure, but can be numerically approximated with relative ease.

The caveat of least-squares solvers is that they are the sledgehammers of parameter estimation: highly effective but rather crude. Among the most significant shortcomings of curve fitting algorithms is the fact that outbreaks do not neatly conform to the simple compartmental model's neat sinusoidal curves. It may be somewhat unfair to lay blame for that at the door of curve fitting algorithms, since the root of the issue lies not with the curve fitting algorithm itself but with compartmental models in general, and their inability to accommodate more complex nonlinearities, such as successive waves of infection with accuracy. Curve fitting algorithms are, however, very effective where there is relatively little data and speed is prioritized over accuracy. Thus, a curve-fitting approach can yield useful estimates of multiple parameters in a single outbreak, but would typically struggle with aperiodic waves from emergent strains, as we witnessed with, e.g., the Delta and later the Omicron VOCs of COVID-19.

## Computational Note 2.13 Multiparameter estimation with Imfit and Emcee

The advantage of multiparameter estimation is that-as the name suggests-it estimates multiple parameters contemporaneously and in relation to each other. This is particularly useful if we have information about more than one compartment (e.g., number of infectious cases and number of decedents). In this computational example, we are using a SEIRD model to estimate a whole host of parameters all at once: $\beta, \gamma, \sigma$, and $C F R$. We do so in three steps:

1. First, we define the model, our starting conditions, and our best guesses as to the parameters.
2. Next, we obtain a best estimate for $\beta, \gamma, \sigma$, and $C F R$ by performing a Nelder-Mead minimization with $1 \mathrm{mfit}$. This is often better than the more commonly used Levenberg-Marquardt algorithm, which tends to have a somewhat more difficult time with exponential processes, which is of course the kind of problem that describes epidemics.
3. Finally, we use a Markov chain Monte Carlo (MCMC) simulation to get an idea of how good our estimates are.

Once we have obtained the data (in this case, from Ritchie et al. [84], for the United States, between 06 March 2020 (the first day when cases exceeded a hundred new diagnoses per day) and the end of July 2021) and cut it down to the columns on cases and deaths, we calculate a ten-day rolling sum of cases as a rough estimate of active cases at any one time. From this, we create our $X$ and $Y$ vectors (in keeping with the convention in scientific Python as to what the dependent and independent variable vectors ought to be named):

```
Y = df[["total_cases", "total_deaths"]].dropna().to_numpy()
```

```
X = np.array(list(range(0, len(Y))), dtype=float)
```

Next, we define our SEIRD model:

```
def SEIRD_model(t, y, beta, gamma, sigma, CFR):
    S, E, I, R, D = y
    dSdt = - beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = (1 - CFR) * gamma * I
    dDdt = CFR * gamma * I
    return dSdt, dEdt, dIdt, dRdt, dDdt
```

We also need to define some sensible starting values. We have data on $I(0)$ and $D(0)$. We assume (somewhat naively) that $E(0)=2 I(0)$. Since it is early in the epidemic, we assume there are no recovered individuals yet. This gives us the initial conditions:

```
N = 329.5e6
E0 = 2 * Y[0, 0]
IO = Y[0, 0]
RO = 0
DO = Y[0, 1]
SO = N - EO - IO - DO
starting_values = (SO, E0, IO, RO, DO)
```

Next, we need to describe our parameters, i.e., the vector $\theta$. The "values" we provide here actually matter rather little; their primary purpose is to give the fitting algorithm somewhere to start.

```
theta = 1mfit.Parameters()
theta.add("beta", value=0.5, min=0, max=5)
theta.add("gamma", value=1/10, min=0, max=1)
theta.add("sigma", value=1/3, min=0, max=1)
theta.add("CFR", value=0.05, min=0, max=1)
```

Now, we need to provide the solver with a quantification of how good a fit is, given $X, Y$, the starting conditions, and $\theta$. 1mfit expects a function that, given $X, \theta$, the starting conditions, and $Y$, returns $\hat{y}_{i, j}-Y_{i, j}$ as a one-dimensional array. We obtain this by taking any given value of $\theta$ and performing the integration, then taking the third and fifth columns (corresponding to the $I$ and $D$
compartments, for which we have observed data) and subtracting the predicted from the observed value. This is our residual function, which allows $1 \mathrm{mfit}$ to evaluate each proposed value for $\theta$ :

```
def residual(theta, X, Y, starting_values=starting_values):
    parvals = theta.valuesdict()
    beta, gamma, sigma, CFR = parvals["beta"], parvals["gamma"], \
            parvals["sigma"], parvals["CFR"]
    res = solve_ivp(fun=SEIRD_model,
        t_eva]=X,
        t_span=(X[0], X[-1]),
        y0=starting_values,
        args=(beta, gamma, sigma, CFR))
    return (Y.T - res.y[[2, 4], : ]).ravel()
```

Note that we need to deconstruct the Parameters object theta. Ordinarily, iterating over a Parameters object yields the keys, i.e., the names of the parameters as strings. Since that is not all that helpful to us, we obtain a dictionary of values with the .valuesdict() method, and obtain each of the values by their key.

Now, we can call 1mfit.minimize on the residual, and the parameter set theta:

```
fit = lmfit.minimize(residual,
    theta,
    method="ne1der",
    args=(X, Y, starting_values))
```

Calling the fit object will provide a quite helpful short summary of the values, including the estimates with their standard error. Our model seems to indicate, for this period, a best fit for $\beta=0.492, \gamma=0.408$, and a CFR of 0.006 (i.e., $0.6 \%$ ). These suggest a $\Re_{0}$ of around 1.2 , which is a quite reasonable approximation if we consider that case recognition and reporting in the early days of the pandemic was rather imperfect.

We are finally interested in how good our fit is. Out of the box, calling a fit object or the report_fit() function in $1 \mathrm{mfit.printfuncs,} \mathrm{provides} \mathrm{a} \mathrm{range} \mathrm{of}$ standard metrics ( $Q^{2}$, Akaike's information criterion and Bayesian information criterion), but a much better and more illuminating way is to obtain the posterior probability distribution of the parameters, given observed data. For this, we create a fit with Emcee, a package for Markov chain Monte Carlo sampling:

```
res = 1mfit.minimize(1ambda x: residual(x, X, Y, starting_values),
    method="emcee",
```

```
burn=300,
steps=1_500,
thin=20,
params=theta,
is_weighted=False,
progress=True)
```

Note that this is not really a fit; we are not fitting anything, and this only works if the results have already been fit once, as we did above. Rather, this uses the fitting API to estimate the posterior distributions. From this, we can construct a corner plot as seen in Fig. 2.27. The corner plot shows the posterior distributions of the parameters with respect to each other. This allows us to reason about the degree to which our estimates for one value are contingent on the value of another, and their relationship.

Since we did not weight our data (we assume that measurement uncertainty is equal for all measurements of the residual), Emcee will try to encapsulate it as the parameter $\ln (\varsigma)$ (which is not the same as $\sigma$, the inverse duration of the latent period; unfortunately, we are limited in our choices of symbols far beyond our needs). This appears as the last row of the corner plot, serving as the estimate of uncertainty in the data.

Reading corner plots is nontrivial and requires some experience, but it is a helpful tool to understand how the parameters were estimated and what the effect of an error into a particular direction would be on the other parameters.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch02/mu1 tiparameter.

![](https://cdn.mathpix.com/cropped/2024_06_11_fe9fdebf2e9671e7e798g-73.jpg?height=1189&width=1185&top_left_y=232&top_left_x=172)

Figure 2.27 Corner plot of the fitted SEIRD model from Computational Note 2.13.

