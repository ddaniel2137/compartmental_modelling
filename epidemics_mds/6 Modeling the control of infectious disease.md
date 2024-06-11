# Modeling the control of infectious disease 


#### Abstract

In 1736 I lost one of my sons, a fine boy of four years old, by the small-pox, taken in the common way. I long regretted bitterly, and still regret that I had not given it to him by inoculation. This I mention for the sake of parents who omit that operation, on the supposition that they should never forgive themselves if a child died under it; my example showing that the regret may be the same either way, and that, therefore, the safer should be chosen.


From Benjamin Franklin's Autobiography, quoted by Best, Katamba, and Neuhauser

[184]

### 6.1 Modeling vaccination

The word "vaccination" comes from vacca, the Latin word for "cow." This is a poignant recapitulation of the history of vaccines. The first vaccine properly so called had, as its active ingredient, the cowpox virus, a close relative of smallpox that however was much less likely to cause severe, disfiguring, or lethal disease. Edward Jenner (1749-1823) observed that milkmaids, who were often exposed to cowpox, suffered a relatively mild disease, but would be immune to the much more serious smallpox. In an experiment that would unlikely pass muster in the modern world, he infected James Phipps, then an 8 -year-old, with cowpox. He suffered a mild and transient illness, but when he was later exposed to scabs from a smallpox patient, he proved immune [185]. Unlike the earlier practice of variolation, which was practised in late Song dynasty China [186] as a way to induce the cutaneous form of smallpox, variola minor, to protect against the more severe forms of smallpox (variola major), Jenner's vaccination used a different and less pathogenic virus. He relied on what would later be called "antigenic similarity," but which was at the time hardly understood.

Much has changed since Jenner's inoculations with cowpox. Vaccination has made smallpox extinct in the wild, as well as rinderpest, a relative of measles that affects cattle and buffalo, among others. Poliomyelitis, which has in its heyday killed and maimed millions of children and adults alike, is close to eradication, with fewer than 200 wild-type cases documented in 2020 . Vaccines are some of the most effective public health interventions against infectious disease. For this reason, we shall devote this section to modeling vaccination against infectious disease.

### 6.1.1 Case study: measles vaccination over the years

Measles is the Comeback Kid of infectious diseases. The measles morbillivirus $(\mathrm{MeV})$, which causes measles, is the most infectious known pathogen, with conservative estimates of its $\Re_{0}$ around 11-18 [175]. It emerged sometime between the 6 th century BCE and the mid-11th century CE from rinderpest, a morbillivirus of eventoed ungulates [187]. Unlike its ancestor, which holds the distinction of being the first animal disease eradicated using vaccination [188], measles is making a comeback. The recent years have seen increasing vaccine hesitancy specifically concerning the MMR vaccine [189], and consequently a number of localized outbreaks in the United States [190].

The overall vaccination rate in the United States is approximately $92 \%$, although this figure is much lower in some communities [191]. Studies have estimated the effectiveness of the vaccine to prevent clinical measles at approximately $95 \%$, and intrahousehold transmission in about $92 \%$ of cases [192].

The concern raised by localized outbreaks is that the protection that flows from collective immunity may be lost. Recall that a pathogen requires at least $\mathfrak{R}_{0}^{-1}$ susceptible fraction of population to be able to persist. For the higher estimates of $\Re_{0}$ for measles, this would correspond to around $5.5 \%$ of the population, in other words, as long as more than $5.5 \%$ of the population are susceptible, there is a constant risk of outbreaks. Susceptibility includes not only those who are not, or cannot be, vaccinated, but also those in whom the vaccination has, for whatever reason, failed to induce sufficient immunity. As such, $\mathfrak{R}_{0}^{-1}$ represents an optimistic upper bound, premised on the absence of vaccine failure, and thus, collective immunity might be lost at a much lower proportion of nonvaccinated individuals.

This section deals with modeling the effect of vaccines on populations. We will, in sequence, look at vaccines that are equally effective against illness and transmission, then move on to vaccines, where the effect on transmission is, as is the case for measles vaccines, different. Finally, we shall consider alternatives to mass vaccination that have proven their worth historically.

### 6.1.2 Modeling vaccines effective against both illness and transmission

### 6.1.2.1 Initial vaccination

Where a vaccine is equally effective against both illness and transmission, it is typically best modeled as a separate compartment that has, under the assumption of unlimited duration and full effectiveness of immunity, no outflows towards the infectious compartments. A simple model might assume a preexisting and static cohort of vaccinated.

Definition 6.1 (Initial vaccination). In initial vaccination, also called vaccination at recruitment, vaccinated individuals are present at the beginning of the model. The vaccination fraction $v$ is the fraction of susceptibles who are vaccinated at the initial point in time, and there are no accruals to the vaccinated compartment.

Given the vaccination fraction $\nu$, we initialize the model for $n_{I}$ initially infected as follows:

$$
\begin{align*}
S(0) & =1-R(0)-v \\
V(0) & =v \\
R(0) & =0  \tag{6.1}\\
I(0) & =1-S(0)-v
\end{align*}
$$

In other respects, the model is quite identical to a regular SIR model: the impact of the vaccination takes place before the infectious process begins, by way of "shielding" the vaccinated individual from being affected by the infectious process.

### 6.1.2.2 Fixed-rate vaccination

Process vaccination refers to time-dependent changes in the number of vaccinated individuals, by a fixed rate. Typically, a fixed vaccination rate is most appropriate when examining a relatively short period of time during which the vaccination rate is relatively steady, e.g., examining a single influenza epidemic. Another assumption is that the vaccine is given only to susceptible individuals.

$$
\begin{align*}
& \frac{d S}{d t}=-\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\nu S}_{\text {new vaccinations }} \\
& \frac{d V}{d t}=\underbrace{\nu S}_{\text {new vaccinations }} \\
& \frac{d I}{d t}=\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\gamma I}_{\text {recovery }}  \tag{6.2}\\
& \frac{d R}{d t}=\underbrace{\gamma I}_{\text {recovery }} .
\end{align*}
$$

In practice, fixed-rate vaccination is often applied in an age-regularized manner. Typically, most school-age children receive their vaccinations at the start of the school term, and in the Northern hemisphere, influenzavirus vaccination campaigns typically start around late September, when the annual vaccine is released. Where the rate of vaccination is deterministic but time-varying, it is possible to apply a time-varying forcing model, similar to the way we modeled annual peaks of epidemic processes in the vector-borne context Subsection 4.1.6.

### 6.1.2.3 Pulse vaccination

Vaccinating large numbers of individuals is expensive, time-consuming, and may at times not be practicable. Pulse vaccination is a "shortcut" of sorts to attain immunity at relatively lower rates of vaccination, carried out periodically in the form of "pulse" vaccination campaigns [193]. Barik, Chauhan, and Bhatia [194] demonstrated that in
certain circumstances, pulse vaccination may in fact be more effective than continuous vaccination.

At the heart of pulse vaccination is the fact that once $1-\mathfrak{R}_{0}^{-1}$ of all susceptibles have been vaccinated, the growth rate of the disease can only be negative. Thus pulse vaccination aims at limiting the fraction of $S$ (as a fraction of the total population) below $\Re_{0}^{-1}$ through periodic vaccination campaigns. This may be difficult to achieve in a single campaign, but feasible by multiple pulses.

Let us assume we vaccinate the proportion $\nu$ of the unvaccinated population every $\tau_{\nu}$ time (the pulse interval). Then, the vaccinated part of the population after $n$ pulses $\tau_{v}$ apart is

$$
\begin{equation*}
V(n)=v \sum_{i=0}^{n} S\left(i \tau_{v}-\epsilon\right) \delta\left(t-n \tau_{v}\right) \tag{6.3}
\end{equation*}
$$

where $S\left(n \tau_{v}-\epsilon\right)$ is the number of susceptible individuals an instant before the $n$-th pulse ( $\epsilon$ here stands for the infinitesimal time difference), and $\delta$ is the Dirac delta function. Then, given an equal rate of births and deaths $\mu$, we may represent this system's dynamics in the long run as

$$
\begin{align*}
\frac{d S}{d t} & =\mu-\beta S I-v \sum_{i=0}^{\infty} S\left(i \tau_{v}-\epsilon\right) \delta\left(t-n \tau_{v}\right)-\mu S \\
\frac{d I}{d t} & =\beta S I-\gamma I-\mu I \\
\frac{d R}{d t} & =\gamma I-\mu R  \tag{6.4}\\
\frac{d V}{d t} & =\nu \sum_{i=0}^{\infty} S\left(i \tau_{v}-\epsilon\right) \delta\left(t-n \tau_{v}\right)-\mu V
\end{align*}
$$

The disease-free mean numbers of $I$ and $S$ during the $n$-th pulse cycle, which is defined as $\left[(n-1) \tau_{\nu}, n \tau_{\nu}\right]$, are

$$
\begin{align*}
\bar{S}(t)= & 1-\frac{\nu e^{\mu \tau_{v}}}{e^{\mu \tau_{v}}-(1-v)} e^{-\mu\left(t-(n-1) \tau_{v}\right)} \\
& -\nu\left(1-\frac{\nu e^{\mu \tau_{v}}}{e^{\mu \tau_{v}}-(1-v)} e^{-\mu \tau_{v}}\right) \int_{(n-1) \tau_{v}}^{t} \delta\left(t-n \tau_{v}\right) \tag{6.5}
\end{align*}
$$

$\bar{I}(t)=0$.

The stability analysis of this model, which is due to Shulgin, Stone, and Agur [195], approaches this problem using Floquet theory, as one of small perturbations on stable level, where the current value of $S(t)$ and $I(t)$ are the sum of the pulse-wise means $\bar{S}(t)$ and $\bar{I}(t)$, respectively, plus a perturbation term $s$ or $i$. These are obtained by

Taylor expansion of Eq. (6.4), and discounting higher-order terms, it yields

$$
\begin{align*}
& \frac{d s}{d t}=-\mu s-\beta \bar{S}(t) i-\nu s\left(n \tau_{v}-\epsilon\right) \sum_{n=0}^{\infty} \delta\left(t-n \tau_{v}\right)  \tag{6.6}\\
& \frac{d i}{d t}=\beta \bar{S}(t) i-\gamma i-\mu i
\end{align*}
$$

Given the initial conditions

$$
\left\{\begin{array}{l}
s_{1}(0)=1  \tag{6.7}\\
i_{1}(0)=0 \\
s_{2}(0)=0 \\
i_{2}(0)=1
\end{array}\right.
$$

we obtain the fundamental matrix of the system in Eq. (6.6),

$$
\mathbf{F}(t)=\left(\begin{array}{ll}
s_{1}(t) & s_{2}(t)  \tag{6.8}\\
i_{1}(t) & i_{2}(t)
\end{array}\right)
$$

The Floquet multipliers are the eigenvalues $\lambda_{1}$ and $\lambda_{2}$ of $\mathbf{F}\left(\tau_{v}\right)$, namely

$$
\begin{equation*}
\lambda_{1}=(1-v) e^{-\mu \tau_{v}} \lambda_{2}=e^{\int_{0}^{\tau_{v}} \beta(t) \bar{S}(t) d t-\mu \tau_{v}-\gamma \tau_{v}} \tag{6.9}
\end{equation*}
$$

The solution in Eq. (6.5) is stable if both of the Floquet multipliers in Eq. (6.9) have absolute values less than one. This is necessarily the case for $\lambda_{1}$ and true for $\lambda_{2}$ if

$$
\begin{equation*}
\frac{1}{\tau_{v}} \int_{0}^{\tau_{v}} \bar{S}(t) d t<\frac{\mu+\gamma}{\beta} \tag{6.10}
\end{equation*}
$$

By integrating the stability condition, we get

$$
\begin{equation*}
\frac{\left(\mu \tau_{v}-\nu\right)\left(e^{\mu \tau_{v}}-1\right)+\mu \nu \tau_{v}}{\mu \tau_{v}\left(\nu-1+e^{\mu \tau_{v}}\right)}<\frac{\mu+\gamma}{\beta} . \tag{6.11}
\end{equation*}
$$

For pulses that are much shorter than the mean lifespan and assuming that the duration of the disease, $\frac{1}{\gamma}$ is also shorter than the mean lifespan, we may approximate the critical maximum value of $\tau_{v}$, which we will call $\tau_{\max }$, as

$$
\begin{equation*}
\tau_{\max }=\frac{\gamma \nu}{\beta \mu\left(1-\frac{\nu}{2}-\frac{\gamma}{\beta}\right)} \tag{6.12}
\end{equation*}
$$

This allows us to calculate the minimum safe pulse frequency. Note that this approach makes several major assumptions, in particular that

- vaccines do not wane in effect, and
- vaccines do not fail.

We know from practice that this is not the case, and it may be necessary to account for these. A common method of accounting for the effect of vaccine failure is to multiply the vaccination rate $v$ by the vaccine efficacy $V E$, essentially discounting a fraction of vaccinated individuals to represent those in whom no protective effect is attained.

### 6.1.2.4 Seasonally rate-varying vaccination

In practice, many diseases for which we vaccinate occur seasonally. Sinusoidal forcing, which we discuss in rather more detail in Subsection 7.3.2, is a technique to model diseases with periodically (seasonally) oscillating transmission rates. We can then rewrite Eq. (6.4) in a time-dependent form:

$$
\begin{align*}
\frac{d S}{d t} & =\mu-\beta(t) S I-v \sum_{n=0}^{\infty} S\left(n \tau_{v}-\epsilon\right) \delta\left(t-n \tau_{v}\right)-\mu S \\
\frac{d I}{d t} & =\beta(t) S I-\gamma I  \tag{6.13}\\
\frac{d R}{d t} & =\gamma I \\
\frac{d V}{d t} & =v \sum_{n=0}^{\infty} S\left(n \tau_{v}-\epsilon\right) \delta\left(t-n \tau_{v}\right)
\end{align*}
$$

where $\beta(t)$ denotes the time-varying contact rate, which is composed of a background rate $\beta_{0}$ and a factor $\beta_{1}$, which describes the amplitude of the seasonal variation above the background rate. Specifically,

$$
\begin{equation*}
\beta(t)=\beta_{0}+\beta_{0} \beta_{1} \cos \left(2 \pi t+\psi_{0}\right) \tag{6.14}
\end{equation*}
$$

where $\psi_{0}$ is the phase offset between the vaccination and the seasonal variations of $\beta$.

Using the same Floquet techniques that yielded us the stability condition in Eq. (6.10), we get the Floquet multipliers

$$
\left\{\begin{array}{l}
\lambda_{1}=(1-v) e^{-\mu \tau_{v}}  \tag{6.15}\\
\lambda_{2}=e^{\int_{0}^{\tau_{v}} \beta(t) \bar{S}(t) d t-\mu \tau_{v}-\gamma \tau_{v}}
\end{array}\right.
$$

If $\left|\lambda_{2}\right|<1$, the periodic infection-free solution is stable. This is the case if

$$
\begin{equation*}
\frac{1}{\tau_{v}} \int_{0}^{\tau_{v}} \beta(t) \bar{S}(t) d t<\mu+\gamma \tag{6.16}
\end{equation*}
$$

Under the Taylor expansion of Eq. (6.16), and the assumptions we have made previously, as well as the assumption that $\mu<2 \pi$, we obtain $\tau_{\max }$ in the presence of forcing as

$$
\begin{equation*}
\tau_{\max }=\frac{\gamma \nu}{\beta_{0} \mu\left(1-\frac{\nu}{2}-\frac{\gamma}{\beta_{0}}\right)}+\frac{\nu \beta_{1}\left(\mu \cos \psi_{0}-2 \pi \sin \psi_{0}\right)}{4 \pi^{2}\left(1-\frac{\nu}{2}-\frac{\gamma}{b_{0}}\right)} \tag{6.17}
\end{equation*}
$$

The first part, which ought to be rather familiar from Eq. (6.12), represents the maximum safe pulse period in the absence of temporal forcing, whereas the second part represents the effect of seasonal forcing via $\beta_{1}$. The relative value of the temporally forced and the temporally unforced component determines the degree to which a pathogen's temporally forced dynamics affect pulse vaccination. This is the effect of forcing $\zeta$, which we calculate as

$$
\begin{equation*}
\zeta=\frac{\beta_{0} \beta_{1} \mu\left(\mu \cos \psi_{0}-2 \pi \sin \psi_{0}\right)}{4 \pi^{2} \gamma} \tag{6.18}
\end{equation*}
$$

By evaluating the maximum of $\zeta$, we can calculate the likely effect of phase differences: the greater the maximum of $\zeta$ is, the greater the impact of $\psi_{0}$ (i.e., the phase difference between peak infections and vaccinations).

## Practice Note 6.1 When to schedule vaccinations

Shulgin, Stone, and Agur [195] estimate that for their infectious parameters of measles, $\zeta$ would take a value of approximately 0.02 , meaning that for all intents and purposes, it does not quite matter when a pulse vaccination is initiated with respect to the peak infectious period. On the other hand, $\zeta$ might be quite considerable, especially where $\gamma$ is small. When advising on pulse vaccination schedules, it is crucial for infectious disease modelers to take into account the expected impact of setting a mathematically more appropriate pulse vaccination schedule vis-a-vis other considerations. Pulse vaccination of school age children, for instance, is difficult outside of term-time, and a suboptimally scheduled vaccination campaign with high vaccination rates ( $v$ ) might often be superior to a better timed but less thorough one. In addition, pulse vaccinations may create hard-to-predict long-term nonlinear effects. These are discussed in detail in Subsection 7.3.5.

### 6.1.3 Risk-targeted vaccination

As we have learned in Chapter 3, in epidemiology, all are not created equal. Vaccine targeting is the conscious determination of particular segments of the population to achieve optimum effects.

It is known, for instance, that vaccines are generally less effective in people with suppressed immune systems, whether as a consequence of immunosuppressive therapy (e.g., for autoimmune disorders), as a consequence of illness (e.g., AIDS or congenital conditions affecting the immune system, such as DiGeorge syndrome) or are too young or too old to mount effective immunity. Given a limited number of vaccines, the strategy of targeting the first-degree contacts (such as household members and caregivers) of persons less likely to respond to the vaccine can create an effect sometimes described as "cocooning," reducing the risk of infection among close contacts to avoid infection [196].

This strategy is widely used to protect newborns from, among others, pertussis. In addition to maternal immunization during pregnancy with the $\mathrm{TDaP}$ vaccine, immunizing the child's close contacts can significantly reduce the risk of pertussis [197].

Risk-targeted vaccination, on the other hand, is an a priori approach, in which vaccines are targeted at individuals who are more likely to contract the infection in the first place. Looking back at Chapter 3, we recall that populations may be stratified by their risk. One of the consequences of such a stratification is that the overall impact of vaccination on different strata might yield different results. We know that random vaccination will eradicate the infection (under the assumption of perfectly effective vaccines), where $1-\frac{1}{\Re_{0}}$ of the population is vaccinated. This is the collective immunity threshold ${ }^{\Delta}$.

Definition 6.2 (The critical threshold of collective immunity). A pathogen cannot persist in a population where a fraction of $1-\frac{1}{\Re_{0}}$ or more of the population are immune, whether by vaccination or post-infectious immunity. We call this value the critical threshold of collective immunity or herd immunity threshold ${ }^{\Delta} v$ for short.

However, where risk is heterogeneous (see Definition 3.2), who gets vaccinated may matter more than how much of the population ends up vaccinated. The consequence is that the infection can be controlled at less than ${ }^{\Delta} \nu$ vaccinated, as long as higher-risk strata are vaccinated to a sufficient degree.

Let us consider the scenario from Subsection 3.1.2, with two strata (see Definition 3.1): high-risk $(H)$ and low-risk $(L)$, with $n_{H}$ and $n_{L}$ denoting the fractions of each stratum as part of the population. We account for differential vaccination through the vaccination rate parameters $v_{H}$ and $v_{L}$ (Fig. 6.1). We can computationally estimate a curve at which the disease is eradicated by determining the area on a coordinate space defined by the total percentage vaccinated and the percentage of high-risk individuals vaccinated, where $\Re_{0} \leq 1$. As Keeling and Rohani [39] note, such issues are not quite amenable to analytical solutions in most cases, but computational optimization can often get us the results we need. Computational Note 6.1 lays out a computational approach to solving such problems, creating a nomogram of control.

## Computational Note 6.1 Targeted vaccination

Let us consider a population with characteristics identical to the example in Computational Note 3.1, namely a WAIFW matrix of

$$
\mathbf{b}=\left(\begin{array}{cc}
10 & 0.5 \\
0.5 & 2
\end{array}\right)
$$

and $20 \%$ of the population belonging to the high-risk category. Furthermore, we shall assume a $\gamma$ of $\frac{1}{20}$. Recall from Computational Note 3.1 that the infectious subsystem was given by

![](https://cdn.mathpix.com/cropped/2024_06_11_144605289bea1fda3a26g-09.jpg?height=912&width=916&top_left_y=225&top_left_x=311)

Figure 6.1 A model of differential vaccination in a population with two risk strata. $v_{H}$ and $v_{L}$ are the vaccination rates of the high and low risk strata, respectively.

```
d_Is = Matrix(np.array([(beta_HH * n_H - gamma_H) * I_H
    + (beta_HL * n_H) * I_L,
    beta_LH * n_L * I_H
        + (beta_LL * n_L - gamma_L) * I_L]).T)
```

We obtained the Jacobian of d_Is as

coeffs = d_Is.jacobian(infectious_system)

namely

$$
\left[\begin{array}{cc}
\beta_{H H} n_{H}-\gamma_{H} & \beta_{H L} n_{H} \\
\beta_{L H} n_{L} & \beta_{L L} n_{L}-\gamma_{L}
\end{array}\right]
$$

and calculated $\Re_{0}$ by inserting values into this matrix.

We are slightly amending our approach in the present case. What we are specifically interested in is what the expected value of $\mathfrak{R}_{0}$ would be, given a
certain percentage of vaccination of each of the strata. We consider initial vaccination only, and we are simply treating it as removing a fraction of $n_{H} *$ or $n_{L} *$ (the initial population fractions), so that $n_{H}=\left(1-v_{H}\right) n_{H} *$ and, correspondingly, $n_{L}=\left(1-v_{L}\right) n_{L} *$. We then perform a grid search by estimating the value of $\Re_{0}$ for any permutation of $\nu_{H}$ and $\nu_{L}$.

We begin by setting up the grid, using NumPy's meshgrid function:

```
nx, ny = (100, 100)
x = np.1inspace(0.01, 1, nx)
y = np.1inspace(0.01, 1, ny)
xx, yy = np.meshgrid(x, y)
```

Next, we use lambdify to "bake in" the eigenvalues of the Jacobian subject to certain values that are not going to change. 1 ambdify is a function of SymPy that turns a particular expression into a function subject to certain variables.

```
f = 1ambdify([v_H, v_L], coeffs.subs({"beta_HH": 10,
    "beta_HL": 0.5,
    "beta_LH": 0.5,
    "beta_LL": 2,
    "n_H": 0.2 * (1-v_H),
    "n_L": 0.8 * (1-V_L),
    "gamma_H": 0.05,
    "gamma_L": 0.05}).eigenva1s())
```

This essentially turned the eigenvalues of a matrix of coefficients into a function callable with two parameters ( $\nu_{H}$ and $\nu_{L}$, respectively). We turn our code seeking the dominant eigenvalue into a vectorized form that we can then directly apply to array objects from NumPy, like our grid:

```
@np.vectorize
def get_rO(v_H, v_L):
    return max([abs(i) for i in f(v_H, V_L)])
```

Finally, we can call this function in conjunction with Matplotlib's contour plotting functions to create estimates of $\Re_{0}$ at different levels of high- and lowrisk vaccination:

```
fig, ax = plt.subplots(constrained_layout=True, figsize=(10, 6))
origin = "lower"
fi11 = ax.contourf(xx,
```

yy,

```
get_r0(xx, yy),
                    15,
                    cmap=plt.cm.rainbow,
                    origin=origin)
critical_optimum = ax.contour(xx,
                    yy,
                    get_r0(xx, yy),
                    leve1s=[1.0],
                    origin=origin)
ax.set_ylabel("Vaccination rate, low-risk ($\\nu_L$)")
ax.set_xlabel("Vaccination rate, high-risk ($\\nu_H$)")
cbar = fig.colorbar(fil1)
cbar.ax.set_y1abe1("$\mathfrak{R}_0$")
cbar.add_1ines(critical_optimum)
```

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch06/ rt $v$.

Fig. 6.2 shows the most important feature of risk-dependent vaccination. The L-shaped contour separates circumstances where epidemic spread is possible (leftbelow) from circumstances where $\Re_{0}$ is pushed below 1 , and consequently epidemic spread is not possible. The $\mathrm{L}$-shape of the curve indicates two salient points.

First, once a relatively small percentage of high-risk individuals are vaccinated, the population comes quite close to immunity. Once about half of the high-risk individuals are vaccinated (i.e., $10 \%$ of the total population), the epidemic potential is greatly diminished. Targeting a high-risk subpopulation means that only a relatively small part (in this case, about $35 \%$ ) of the low-risk population need to be vaccinated to eliminate the pathogen's epidemic potential.

Second, as Keeling and Rohani [39] point out, though vaccinating the high-risk group above their threshold yields no further benefits and is in fact an ineffective use of vaccines, overvaccinating may be more advantageous than undervaccinating. This is because, as the steepness of the "stem" of the L-shaped curve (the vertical component) indicates, the critical point, a $5 \%$ decrease in vaccination rates of the high-risk subpopulation, can plunge the entire population into the risk of a reemergent epidemic.

### 6.1.4 Game theoretical perspectives on vaccination

Game theory is the study of individual decision-making in the face of competing boundedly rational actors. We may conceive of vaccination as a sequential multiplayer game, with two strategies open to each agent.

- If an agent chooses to vaccinate, they will be immune, at least to some extent, from the consequences of a particular infectious disease, for some time going forward.

![](https://cdn.mathpix.com/cropped/2024_06_11_144605289bea1fda3a26g-12.jpg?height=776&width=1167&top_left_y=227&top_left_x=137)

Figure 6.2 Nomogram of control indicating risk-dependent vaccination optima for $\mathbf{b}=$ $\left(\begin{array}{cc}10 & 0.5 \\ 0.5 & 2\end{array}\right)$ and $\gamma=0.05$. The solid line shows the critical vaccination optimum at $\mathfrak{R}_{0}=1$.

However, they incur some small but nonzero risk of suffering adverse effects from the vaccine. The latter is fixed, whereas the former is a function of what proportion of the population is already vaccinated.

- If an agent chooses not to vaccinate, they do not suffer the fixed cost of the nonzero risk of suffering adverse effects from the vaccine, but risk contracting the disease. Once again, how high that risk is depends on how many people have already been vaccinated.

This leads to a clear paradox: we know, from our study of herd immunity, that it is not necessary to vaccinate an entire population to elicit immunity. Thus once a certain percentage of a population is already immune, nothing is there to gain from vaccination. In fact, not vaccinating becomes the dominant strategy somewhat below that threshold, specifically, at the inflection point, where the risk of disease is lower than the risk of adverse effects. This results in an apparent paradox: at a particular level of vaccination, the dominant individual strategy is to not vaccinate, but if everyone does so, the overall utility is decreased. This notion is widely referred to as the "tragedy of the commons": it is in the interest of each farmer, seen individually, to exploit the common pasture to its maximum extent, but if every farmer adopts that strategy, the overall results are going to be rather unfavorable. Liu et al. [198] note that quite often, the level of vaccination above which it is no longer in an individual's self-interest to vaccinate (Nash vaccination) is well below what is required to elicit collective immunity.

Bauch and Earn [199] propose a general scheme for analyzing the "vaccination game." Individuals adopt a strategy $P$, which is their general likelihood to vaccinate. For the entire population $N$, the population-level vaccination fraction $\nu$ will be

$$
\begin{equation*}
v=\frac{1}{|N|} \sum_{i \in N} P_{i} \tag{6.19}
\end{equation*}
$$

- If an individual vaccinates, they incur the risk of adverse effects, $J_{v}$.
- If an individual does not vaccinate, they incur the risk of infection, $J_{i}$. Since this depends on the mass action term, i.e., the number of infectious (nonvaccinated) individuals, we multiply this by $\pi_{\nu^{\prime}}$, the likelihood of sustaining infection if the population-level vaccination fraction is $v^{\prime}$.

If we conceptualize the relative risk $J$ as $\frac{J_{v}}{J_{i}}$, the expected payoff for a strategy $P$ given the population-level vaccination fraction $\nu$ may be expressed as

$$
\begin{equation*}
E(P, v)=-J P-\pi_{\nu^{\prime}}(1-P) \tag{6.20}
\end{equation*}
$$

since the strategies of vaccinating and not vaccinating are partitions (i.e., mutually exclusive and jointly exhaustive). If a large part of the population adopts $P$, we call $P$ a Nash equilibrium if anyone choosing any strategy other than $P$ (which we shall call $\neg P)$ will receive a lower payoff. If, for any value of $\nu, E(P, \nu)>E(\neg P, \nu), P$ is a convergently stable Nash equilibrium (CSNE).

## Practice Note 6.2 Game theory, rationality and information asymmetry

Notably, agents make decisions based on their own understanding of the risk. This may not, actually, correspond to the true risk, either of the vaccine or of the illness. "Vaccine scares" are episodic events during which, owing often to exaggerated media interest, the public perception of the risks associated with a vaccine exceed the actual risk. Similarly, agents may overestimate or underestimate the risk from the disease. Incidents such as that following the unexpected adverse effects of a dengue vaccine in the Philippines [200] or the vaccine scare in France following the media interest in a now disproven association between the hepatitis B vaccine and multiple sclerosis [201] affect the perception of risk. As such, it is crucial to understand not only real risks but also the risks as they are understood and evaluated by boundedly rational agents, whose understanding of risks and benefits might be colored by subjective perception and by individual interpretations of the concept of risk.

For simplicity's sake, let us assume a population split into two segments: those vaccinating with probability $P$ and those vaccinating with probability $Q$, with $\rho$ being the fraction of those adopting $P$ and, since the strategies are mutually exclusive, $1-\rho$ being the fraction of those who adopt $Q$. Based on these strategies, the population's
vaccination fraction is the product of the proportions and their individual vaccination properties:

$$
\begin{equation*}
v=\rho P+(1-\rho) Q \tag{6.21}
\end{equation*}
$$

This gives us the payoffs for $P$ and $Q$ strategists, $E_{P}$ and $E_{Q}$ respectively, as

$$
\left\{\begin{array}{l}
E_{P}(P, Q, \rho)=E(P, \rho P+(1-\rho) Q)  \tag{6.22}\\
E_{Q}(P, Q, \rho)=E(Q, \rho P+(1-\rho) Q)
\end{array}\right.
$$

For any $P$ strategist, the benefit of switching to $Q$ would be

$$
\begin{equation*}
\Delta_{E}(P \rightarrow Q)=E_{P}(P, Q, \rho)-E_{Q}(P, Q, \rho)=(P-Q)\left(\pi_{\nu P+(1-\nu) Q}-J\right) \tag{6.23}
\end{equation*}
$$

Bauch and Earn [199] proved that for any relative risk $J$, there exists a strategy $P^{*}$ so that for any strategy $\neg P^{*}$ and any value $\rho, \Delta_{E} P \rightarrow Q>0$. The term $\pi_{\rho P+(1-\rho) Q}$ describes the likelihood of infection if $\rho$ part of the population adopt $P$ and $1-\rho$ adopt $Q$. There are three possible Nash equilibria for the above: the pure equilibria $P^{*}=0$ and $P^{*}=1$, and a mixed equilibrium of $0<p^{*}<1$. If $J \geq \nu P+(1-\nu) Q$, then the Nash optimal response is to never to vaccinate. If $J<\nu P+(1-v) Q$, the Nash optimal strategy is to vaccinate at a nonzero rate of $\nu^{*}$ so that $\pi_{\nu^{*}}=J$.

It is crucial to examine the ramifications of this last statement. A Nash rational agent keeps vaccinating until the $\pi^{\nu^{*}}=J$, that is, until the risks of sustaining the illness no longer outweigh the risks of the vaccination itself. If $v=1-\frac{1}{\Re_{0}}$, the disease has been effectively eradicated, and $\pi_{\nu}$ is by definition zero. Recall that we defined $J$ as the fraction of risks from the vaccine $J_{v}$, and risks from infection $J_{i}$. It follows from the existence of the mixed equilibrium $0<v^{*}<1$ that

$$
\begin{equation*}
\lim _{v \rightarrow v^{*}} \frac{J_{v}}{J_{i}(v)}=\infty \tag{6.24}
\end{equation*}
$$

It may be assumed that $v^{*}=1-\frac{1}{\Re_{0}}$, i.e., the threshold of collective immunity, would be a Nash equilibrium, since there would be no additional benefit to vaccinating (or "unvaccinating," a mathematically possible but biologically nonsensical strategy). However, this is not the case for any case where $J_{v}$ is nonzero. For all nonzero values of $J_{v}$, as $\nu$ approaches $1-\frac{1}{\Re_{0}}, J_{i}$ approaches zero and the risk approaches infinity. Consequently, for all nonzero $J_{v}$, there exists a value $\epsilon$ so that $1-\frac{1}{\Re_{0}}=v^{*}+\epsilon$.

The consequence of $\epsilon$ is to denote a "band," in which Nash strategy and prosocial vaccination, which aims at providing the greatest protection for the population, are different: because $\epsilon$ is nonzero if $J_{v}$ is nonzero, in every such case, the CSNE at $\nu^{*}$ is attained before collective immunity. The value of $\epsilon$ is solely a function of $J_{v}$, the risks of the vaccine, or more specifically, their perception (on which see Practice Note 6.2). It is not, however, a function of the risks from the disease or its severity. Once $v^{*}$ has been reached, the impact of the disease is already nullified for the individual, vis-a-vis the risks from the vaccination, and the vaccine does not provide a direct benefit for
the individual, only for the collective. As such, effective communication about vaccination needs to shift, as $v^{*}$ is approached, away from individual benefit and towards prosocial and altruistic objectives.

### 6.2 Duration and effectiveness of vaccine-induced immunity

Similarly to post-infectious immunity, vaccine-induced immunity may decrease over time. Some vaccinations provide a lifelong protective effect, whereas others need to be boosted periodically, reinforcing immunity. Equally, the degree of immunity created by vaccination may be variable between individuals, between vaccines, and over time. This section deals with the way we conceptualize the limits on the duration and effectiveness of vaccine-induced immunity.

1. A vaccine may prevent severe illness, but not necessarily mild illness. This is sometimes referred to as a nonsterilizing vaccine. Such vaccines nevertheless affect infectiousness indirectly, by reducing the pathogenic load in the body and/or alleviating the symptoms that contribute to the pathogen's spread. For instance, the rotavirus vaccine does not eliminate the pathogen completely, but prevents severe illness. A secondary effect of that is that milder (and shorter) infection generally results in fewer secondary cases. In the same vein, the COVID-19 vaccines' reduction of severe symptomatic illness has resulted in improved control.
2. A vaccine may be ineffective in an individual, by which we mean to say it fails to obtain the protective effect that it has in the population at large. In certain subpopulations, vaccine failure is more common due to decreased immunogenicity. This includes, in particular, the elderly. For certain vaccines, a more immunogenic preparation is available for such subpopulations, which is typically an adjuvanted version of a nonadjuvanted vaccine.
3. Finally, a vaccine typically induces temporary immunity. Similarly to postinfectious immunity, vaccine-induced immunity may not last indefinitely, and typically wanes in a way that can be approximated as a deterministic process.

## Practice Note 6.3 "Natural" immunity

The term "natural immunity" has been often used to express post-infectious immunity and differentiate it from vaccine-induced immunity. In practice, this is not necessarily helpful. There is nothing fundamentally "unnatural" in vaccineinduced immunity, and whereas the minutiae of natural infection and vaccineinduced immunity might differ, this is a quintessentially unhelpful notion.

In addition to encouraging the naturalistic fallacy, whereby "natural" immunity is seen as less risky (when in practice, surviving an infection is almost
always more dangerous than a vaccine) and more "appropriate," it is also bound to create public misperceptions, e.g., confusion with passive immunization via convalescent plasma or antibodies. A preferable terminology is "post-infectious" or "post-infection" immunity, which highlights that the process leading to immunity was infection rather than immunization.

### 6.2.1 Case study: Marek's disease

Marek's disease is an alphaherpesvirus-mediated oncogenic disease in chickens caused by the Marek's disease virus (MDV). Infected animals present with T cell lymphomas and lymphocytic tumors [202]. In chicken flocks, Marek's disease has been largely controlled using vaccines. However, the vaccine is not perfect, in fact, because the vaccine does not provide sterilizing immunity [203], vaccinated animals continue to spread the infection. As a result, vaccines have actually increased the virulence of Marek's disease [203].

A vaccine is, in the end, an evolutionary pressure on a pathogen. If the vaccine does not eliminate the pathogen's ability to infect new hosts (i.e., if it is not a sterilizing vaccine), vaccination may increase overall virulence by selecting for the most virulent strain of the pathogen, where virulence and transmissibility are related in any way (as it is where herpesviruses are concerned). The result of the vaccine against Marek's disease has been clearly beneficial in reducing disease from an economically costly disease of poultry, but its evolutionary pressure has made it a much more lethal pathogen.

This is, of course, not an argument against vaccination. Contributing to pathogenic evolution towards higher virulence is, even in extreme cases as Marek's disease, the lesser of two evils. It does, however, call attention to the need to understand the impact that interventions to control disease have on the ecology and evolution of the disease itself. Pathogens do not exist in isolation but exist in a space of competition for hosts and the ability to spread.

### 6.2.2 Incomplete effect of vaccines

For modeling the incomplete effect of vaccines, preventing severe illness but not mild disease, it is helpful to conceptualize it as the interplay of three variables:

- $p_{s}$ is the likelihood of severe disease, i.e., the probability that an infected case, from $S$ or $V$ alike, flows into $I_{s}$ rather than $I_{m}$.
- $\epsilon_{I}$ is the vaccination penalty on infection. It reflects the reduction in $\beta$ as a consequence of vaccination, and is confined to the range $[0,1]$.
- $\epsilon_{S}$ is the vaccination penalty on virulence. This reflects the reduction that vaccination confers to the likelihood of developing serious illness, and is equally confined to the range $[0,1]$.

Using the shorthand $I$ for $I_{m}+I_{s}$, we may write

$$
\begin{aligned}
& \frac{d S}{d t}=-\underbrace{\beta S I}_{\text {infections }}-\underbrace{v}_{\text {vaccinations }},
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2024_06_11_144605289bea1fda3a26g-17.jpg?height=185&width=542&top_left_y=424&top_left_x=265)

$$
\begin{align*}
& \frac{d I_{m}}{d t}=\beta\left(1-p_{s}\right)(\underbrace{S I}_{\text {from } S}+\underbrace{V\left(1-\epsilon_{s}\right) \epsilon_{i} I}_{\text {from } V})-\gamma_{m} I_{m},  \tag{6.25}\\
& \frac{d I_{s}}{d t}=\beta p_{s}(\underbrace{S I}_{\text {from } S}+\underbrace{V \epsilon_{i} \epsilon_{s} I}_{\text {from } V})-\gamma_{s} I_{s}
\end{align*}
$$

The beauty (and utility) of this representation is that $\epsilon_{I}$ is the relative risk (RR) between vaccinees and nonvaccinated with respect to infection, and $\epsilon_{S}$ is the same quantity with respect to severe disease. They are also related to the vaccine efficacy $\alpha$, the proportional reduction in the attack rate of the disease, by way of $\alpha=1-\epsilon$. This connection to the population impact numbers that are typically obtained during clinical and early post-marketing testing of a vaccine enable us to reason about infections in view of the vaccine. Moreover, it allows us to determine the requisite vaccination rate $v$ to achieve a certain maximum number of severe cases, which is critical for planning vaccinations to protect hospital capacity.

### 6.2.3 Waning immunity

As we have seen in Subsubsection 2.3.3, post-infectious acquired immunity often wanes after a given period of time. The same is true for vaccine-induced immunity, which is the rationale behind boosting immunizations periodically (see Subsection 6.2.5). In the SIRS model, persons who recovered into an immune state relapsed into susceptibility at the waning rate $\omega=\frac{1}{\tau_{R}}$, where $\tau_{R}$ is the mean duration of immunity. SVIRS is a variation on the theme of the SIRS model that takes account of vaccination rates $v$, as well as waning immunity of the vaccinated. (See Fig. 6.3.)

We may express this as the set of differential equations:

$$
\begin{align*}
& \frac{d S}{d t}=-\underbrace{\beta S I}_{\text {mass action }}+\underbrace{\omega R}_{\text {reversion from } R}+\underbrace{\omega V}_{\text {reversion from } V}-\underbrace{\nu S}_{\text {new vaccinations }} \\
& \frac{d V}{d t}=\underbrace{\nu S}_{\text {new vaccinations }}-\underbrace{\omega V}_{\text {waning of vaccinated }},  \tag{6.26}\\
& \frac{d I}{d t}=\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\gamma I}_{\text {recovery }},
\end{align*}
$$

![](https://cdn.mathpix.com/cropped/2024_06_11_144605289bea1fda3a26g-18.jpg?height=567&width=863&top_left_y=226&top_left_x=298)

Figure 6.3 SVIRS model accounting for homogeneous waning immunity of the vaccinated. Homogeneity of waning means that post-infectious immunity and post-vaccination immunity are subject to the same waning rate $\omega$.

$$
\frac{d R}{d t}=\underbrace{\gamma I}_{\text {recovery }}-\underbrace{\omega R}_{\text {reversion from } R}
$$

This presupposes, of course, that vaccine-induced and post-infectious immunity (on which see Practice Note 6.3) wane at an equivalent rate of $\omega$.

This model's main shortcoming is that waning is not ordinarily a continuous process. Immunity typically wanes after a given amount of time, and not at all before then. Delay differential equations can help us model this situation. Consider vaccination of susceptibles at rate $\nu$. The number vaccinated by time $t$ is

$$
\begin{equation*}
\int_{0}^{t} \nu S(u) d u \tag{6.27}
\end{equation*}
$$

At first approximation, the vaccination has a lifetime of $\tau_{\omega}$, after which it invariably vanes to zero. Biologically, $\tau_{\omega}$ is the inverse of the waning rate or the mean period of protection. For values of $t>\tau_{\omega}$, the reversion to susceptibility at time $t$ will be equal to the number vaccinated at the point in time $t-\tau_{\omega}$ (the principle of "first in, first out" applies here). That, of course, is $v S\left(t-\tau_{\omega}\right)$. Combining these yields the system of delay differential equations described as

$$
\begin{align*}
& \frac{d S}{d t}=\mu-\underbrace{\beta S I}_{\text {mass action new vaccinations }}+\underbrace{-\nu S}_{\text {reversion }}+\underbrace{\nu S\left(t-\tau_{\omega}\right)}_{\text {mass action }}-\mu S, \\
& \frac{d I}{d t}=\underbrace{\beta S I}_{\text {recovery }}-\underbrace{\gamma I}-\mu I, \tag{6.28}
\end{align*}
$$

$$
\begin{aligned}
\frac{d V}{d t} & =\underbrace{v S}_{\text {new vaccinations }}-\underbrace{v S\left(t-\tau_{\omega}\right)}_{\text {reversion }}-\mu V \\
\frac{d R}{d t} & =\underbrace{\gamma I}_{\text {recoveries from } I}-\mu R
\end{aligned}
$$

Delay differential equations are more computationally expensive to solve than ODEs, but there exist accelerated optimizing solvers for DDEs; their use is discussed in Computational Note 6.2.

## Computational Note 6.2 Solving delay differential equations computationally

A delay differential equation (DDE) differs from an ODE in that it has at least one term represented as a function of the system's state at a previous time. The term $\nu S\left(t-\tau_{\omega}\right)$ in Eq. (6.28), wherein the value of $\frac{d S}{d t}$ at time $t$, is a function of its value at time $t-\tau$. This makes integration significantly more challenging, and not quite feasible with much accuracy at all for an initial period (about twice the length of the delay). However, we can usefully integrate DDEs to elicit a system's long-term behavior.

JiTCDDE is an efficient solution for DDEs that is related to the JiTCODE project used in some other applications in this text (see, e.g., Computational Note 7.7) [204]. After importing jitcdde and explicitly importing the symbols $t$ and $y$, we can specify our DDE:

```
f = [
    mu - beta * y(0, t) * y(1, t) - (nu + mu) * y(0, t) \
        + nu * y(0, t - tau),
    beta * y(0, t) * y(1, t) - (gamma + mu) * y(1, t),
    nu * (y(0, t) - y(0, t-tau)) - mu * y(2, t),
    gamma * y(1, t) - mu * y(3, t)
]
```

Unlike in previous instances where we defined differential equations as Python functions of $y, t$, and its parameters, JiTCDDE expects a more formal definition. This is because JiTCDDE performs a symbolic analysis of the function to interpret it and render it as optimized $\mathrm{C}$ code.

In JiTCDDE, the system state is represented as the vector $y$, which in this case is a vector of length 4 , each element corresponding to $S, I, V$, and $R$. In addition, JiTCDDE can take a time parameter. By default, $y(2)$ refers to the third (zero-indexed) element of the state vector, but in addition, we can specify a time relation. Thus $y(2, t-t a u)$ means "the value of the third element of the state
vector at the time $t-\tau^{\prime \prime}$. It is not strictly necessary to specify the time if it is $t$, although this is good practice to keep in mind which of the parameters are delay-contingent and which are not.

Next, we initialize the JiTCDDE solver by providing it with the system of differential equations we defined above, as well as the delay parameters. In this case, we have a single static delay parameter: we assume that $\tau$ days after vaccination, the vaccine's effect completely disappears in all cases. This is not strictly reflective of practical realities, which is why a waning function is often helpful. Nevertheless, it is a useful approximation of reality especially for short-lived vaccines, or where the pathogen's rate of mutation is high enough to render the previous season's immunity ineffective (as is the case with influenza vaccination).

Subsequently, we need to tell JiTCDDE about the past. For the first $\tau$ time, JiTCDDE will be asked to look into a past before we started integration, that is, a past that, strictly speaking, does not exist. JiTCDDE supports a number of ways this could be specified, but by far the simplest is "constant past":

DDE.constant_past([0.95, 0.05, 0, 0], time=tau)

Here, we essentially declare the starting parameters (much as we provided $S(0), I(0)$, and so on to other solvers), and tell JiTCDDE that up until $t=\tau$, it should assume those values for each of the four quantities.

Finally, we will have to deal with the fact that our definition of the starting parameters results in a discontinuity in the case of constant past, essentially a straight line, up until integration begins, where it discontinuously assumes the first integrated value. The trivial solution is to initialize with DDE.step_on_discontinuities(), which adaptively integrates at discontinuities. We now have everything we need to run our DDE integrator with a simple iteration:

```
res = []
for time in np.arange(DDE.t, DDE.t + 30000, 1):
    res.append(DDE.integrate(time))
```

The results of a run of this DDE integrator are displayed as Fig. 6.4. JiTCDDE is an enormously powerful tool for exploring the long-term dynamics of systems, and this simple example can be expanded easily with a more complex waning function or varying delays. A caveat is that since JiTCDDE (along with the entire JiTCODE project) relies on symbolic optimization, many frequently used numeric functions (such as np.pi to obtain the value of $\pi$ or np.exp to perform exponentiation to $e$ ), are not available. Instead, symengine, which is at the backend of JiTCODE, and is thus installed at the same time, must be imported, and
the relevant symbols be explicitly sourced from symengine (e.g., for exponentiation, the symbol exp must be imported from symengine).

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch06/waning_ dde.

Fig. 6.4 shows three critical effects of waning immunity:

1. Waning creates periodicities. As the disease process depletes the population of suitable hosts, it begins to decline. Waning replenishes the pool of susceptibles, allowing an epidemic to once again spread. This is, of course, a result of the phenomena explored in the beginning of Chapter 2.
2. Eventually, waning results in an equilibrium state, where the disease becomes endemic, so that for each recovery, there will be an infection. In Fig. 6.4, the system converges onto an equilibrium point at around $S=0.0475$ and $I=0.003$. At this point, the disease may persist indefinitely.
3. Where vaccination for a particular pathogen is rolled out to a large population in a single large campaign (as was the case for the SARS-CoV-2 vaccine), it is often helpful to keep the periodic dynamics of waning in mind. Scheduling booster or follow-up campaigns at the right time (preferably before, or around the time of, local minima) may often suppress the infection to levels that eliminate the pathogen's ability to spread. This is analogous to pulse vaccination (see Subsubsection 6.1.2.3) at the pulse frequency equal to the inverse of the typical waning period.

Models of waning immunity are helpful in understanding how the interactions between a pathogen's dynamics and human intervention result in new equilibria, and may be powerful tools for the planning of disease eradication.

## Practice Note 6.4 DDEs and the terms of dynamics

DDEs are uniquely powerful tools to mathematically explore systems, whose right hand side at $t$ depends on an earlier state. The tradeoff is that in the beginning, DDEs operate on an assumption of what the past was before the first moment of integration. Since this is rarely easy to specify, in the overwhelming majority of cases, DDEs are not very useful in the very beginning.

Eventually, dynamical systems converge to states that are no longer governed by their initial states (see Subsection 7.3.5 for an important qualification to this statement). The initial discontinuities of a DDE are eventually subsumed into the system's wider dynamics. As tools for exploring the long-term evolution of a system (past $2-4 \tau$ ), DDEs are uniquely powerful. For predicting short-term effects, they should be handled with care, if at all.

![](https://cdn.mathpix.com/cropped/2024_06_11_144605289bea1fda3a26g-22.jpg?height=786&width=1112&top_left_y=240&top_left_x=171)

Susceptible

Infectious

![](https://cdn.mathpix.com/cropped/2024_06_11_144605289bea1fda3a26g-22.jpg?height=760&width=1094&top_left_y=1191&top_left_x=158)

Figure 6.4 Periodicities induced by the waning of vaccine-induced immunity. Integral and phase portrait of a delay-differential system with $\tau_{\omega}=180, \beta=1.5, \gamma=\frac{1}{14}, \mu=2 \times 10^{-5}$, and $\nu=10^{-6}$ per day.

![](https://cdn.mathpix.com/cropped/2024_06_11_144605289bea1fda3a26g-23.jpg?height=1155&width=1185&top_left_y=220&top_left_x=172)

Figure 6.5 Two strains of a pathogen with a vaccine that only protects against one strain. This diagram shows the state space of two pathogens in the state representation, i.e., $C_{1}, C_{2}$ describes the compartment of individuals who are in $C_{1}$ with respect to pathogen 1 and $C_{2}$, with respect to pathogen 2 . Red boxes denote the infectious subsystem of pathogen 1 and blue boxes that of the pathogen 2, respectively. Arrows that transition into infectious states are colored based on which infectious subsystem governs the mass action term.

### 6.2.4 Mutating out of immunity

In the vast majority of cases, in particular where there is no significant divergence between strains or epitopic subtypes of the pathogen, immunity is more or less constant. In creating an infectious disease model, one needs to be aware of the particular circumstances (major mutations, geographic dispersal, and separate evolution) that yield significantly (i.e., antigenically/epitopically) different variants.

Let us consider a pathogen with two strains in the presence of a vaccine protective against strain 1 , but not against strain 2 . We can analyze this as essentially a special case of two-pathogen competition with no coinfection and with no cross-immunity
(since cross-immunity would mean that vaccine-induced immunity would be protective against both strains). Fig. 6.5 lays out such a scenario, where a vaccine protects against the first, but not the second, pathogen. The result of such a system, assuming a constant vaccination rate $\nu$, can be described as the following system of differential equations (where strain 1 is susceptible to the vaccine, but strain 2 is not):

$$
\begin{align*}
& \frac{d N_{S, S}}{d t}=N_{S, S}(-\underbrace{\beta_{1} I_{1}-\beta_{2} I_{2}}_{\text {infections }}-\underbrace{v}_{\text {vaccinations }}), \\
& \frac{d N_{V, S}}{d t}=\underbrace{v\left(N_{S, S}+N_{I, S}+N_{R, S}\right)}_{\text {new vaccinations }}-\underbrace{\beta_{2} N_{V, S} I_{2}}_{\text {infections with resistant strain }} \\
& \frac{d N_{I, S}}{d t}=\underbrace{\beta_{1} N_{S, S} I_{1}}_{\text {new infections }}-N_{I, S}(\underbrace{\gamma_{1}}_{\text {recoveries }}+\underbrace{v}_{\text {vaccinations }}) \\
& \frac{d N_{R, S}}{d t}=\underbrace{\gamma_{1} N_{I, S}}_{\text {recoveries from } 1}-N_{R, S}(\underbrace{\beta_{2} I_{2}}_{\text {infections with } 2 \text { from } R, S}+\underbrace{v}_{\text {vaccinations }}) \\
& \frac{d N_{S, I}}{d t}=\underbrace{\beta_{2} N_{S, S} I_{2}}_{\text {infections with } 2 \text { from } S . S}-N_{S, I}(\underbrace{\gamma_{2}}_{\text {recoveries }}+\underbrace{v}_{\text {vaccinations }}) \\
& \frac{d N_{S, R}}{d t}=\underbrace{\gamma_{2} N_{S, I}}_{\text {recoveries from } S, I}-N_{S, R}(\underbrace{\beta_{1} I_{1}}_{\text {infections with 1 }}+\underbrace{v}_{\text {vaccinations }})  \tag{6.29}\\
& \frac{d N_{I, R}}{d t}=\underbrace{\beta_{1} N_{S, R} I_{1}}_{\text {infections with } 1 \text { from } S, R}-N_{I, R}(\underbrace{v}_{\text {vaccinations }}+\underbrace{\gamma_{1}}_{\text {recoveries }}) \\
& \frac{d N_{R, I}}{d t}=\underbrace{\beta_{2} N_{R, S} I_{2}}_{\text {infections with } 2 \text { from } R, S}-N_{R, I}(\underbrace{v}_{\text {vaccinations }}+\underbrace{\gamma_{2}}_{\text {recoveries }}), \\
& \frac{d N_{R, R}}{d t}=\underbrace{\gamma_{1} N_{I, R}}_{\text {recoveries from } I, R}+\underbrace{\gamma_{2} N_{R, I}}_{\text {recoveries from } R, I}-\underbrace{v N_{R, R}}_{\text {vaccinations }}, \\
& \frac{d N_{V, R}}{d t}=\underbrace{v\left(N_{R, R}+N_{V, I}+N_{S, R}+N_{S, I}\right)}, \\
& \text { vaccinations } \\
& \frac{d N_{V, I}}{d t}=\underbrace{\beta_{2} N_{V, S} I_{2}}_{\text {infections from } V, S}+\underbrace{v\left(N_{R, I}+N_{S, I}\right)}_{\text {vaccinations }}-\underbrace{\gamma_{2} N_{V, I}}_{\text {recoveries }}
\end{align*}
$$

$I_{1}$ and $I_{2}$ describe the infectious subsystems of the pathogens, respectively; they are made up of $N_{I, S}+N_{I, R}$ on one hand and $N_{R_{I}}+N_{S, I}+N_{V, I}$ on the other. The susceptible subsystem in respect of pathogen 2 , that is, the proportion of the population available for infection by pathogen 2 , consists of $\sum N_{*, S}$, i.e., the sum of all states with state vectors, where the second element is $S$. This amounts to $N_{S, S}+N_{I, S}+N_{V, S}+N_{R, S}$. On the other hand, for pathogen 1, this system only
includes $N_{S, S}+N_{S, I}+N_{S, R}$. Denoting the two subsystems as $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$, respectively, we obtain the difference $N_{I, S}+N_{V, S}+N_{R, S}-N_{S, I}-N_{S, R}$, which we shall call $\Delta S_{\nu}$, or the difference between susceptibles between the two strains given the vaccination rate of $\nu$. We can calculate it as

$$
\begin{equation*}
\Delta S_{v}=\beta_{1} I_{1}\left(N_{S, S}+N_{S, R}\right)-\beta_{2} I_{2}\left(N_{R, S}+N_{S, S}\right)+v\left(N_{S, S}+N_{S, R}+N_{S, I}\right) \tag{6.30}
\end{equation*}
$$

We may be interested in the overall evolutionary effect of mutating out of protection. Kennedy and Read [205] correctly note that antimicrobial resistance is much more frequent than resistance to vaccination, which they attribute to two factors:

1. vaccines are prophylactic, and immunity is thus often preexistent by the time of pathogenic exposure, consequently there is no initial period before treatment during which the pathogen can establish a large enough seed population from which to mutate, and
2. vaccines target a wider range of epitopes, whereas antimicrobials typically target a single cellular function or enzyme.

A counterexample that strengthens the rule is, of course, Marek's disease (see Subsection 6.2.1).

In the example of Eq. (6.29), the mutated pathogen gains a fitness advantage in terms of being able to access a larger pool of susceptibles than the vaccine-susceptible strain. We denote this fitness advantage vis-a-vis vaccination as $\Delta F_{v}^{+}$, and calculate it as

$$
\begin{equation*}
\Delta F_{v}^{+}=\frac{\sum N_{*, S}}{v \sum N_{S, *}} \tag{6.31}
\end{equation*}
$$

Since the denominator $v \sum N_{S, *}$ increases strictly monotonically with increasing values of $\nu$, whereas $\sum N_{*, S}$ is not dependent on $\nu$ at all, $\Delta F_{\nu}^{+}$increases at higher vaccination rates $\nu$.

On the other hand, it is common to see a resistant pathogen pay a fitness cost in terms of reduced transmissibility, so that

$$
\begin{equation*}
\Delta F^{-}=\frac{\mathfrak{R}_{0,2}}{\mathfrak{R}_{0,1}}=\frac{\beta_{2} \gamma_{1}}{\beta_{1} \gamma_{2}} \tag{6.32}
\end{equation*}
$$

In this case, $\Re_{0}$ is analogous to the way competitive fitness studies use the number of offspring as an indicator of the fitness cost of resistance [206]. This gives us the overall fitness criterion

$$
\begin{equation*}
\Delta F_{v}=\frac{\sum N_{*, S}}{v \sum N_{S, *}}-\frac{\beta_{2} \gamma_{1}}{\beta_{1} \gamma_{2}} \tag{6.33}
\end{equation*}
$$

Consequently, the resistant strain will become dominant once

$$
\begin{equation*}
v \sum N_{S, *}>\frac{\beta_{1} \gamma_{2} \sum N_{*, S}}{\beta_{2} \gamma_{1}} \tag{6.34}
\end{equation*}
$$

Since the system of ODEs we are considering is autonomous, the time at which this condition is met, given a value of $\nu$ and initial conditions, can be calculated numerically. This gives us a quantitative tool of immense value with which to analyze the evolutionary effect of vaccination on a pathogen, and where a vaccine-resistant strain exhibits other clinically relevant features, such modeling may inform considerations of vaccination policy.

### 6.2.5 Boosting

Boosting refers to the use of an additional exposure to an antigen to prolong or reinforce immunity. The classical model by Alexander et al. [207] conceives of boosters as conferring final immunity, so that the vaccinated compartment is essentially in an anteroom of immunity. This model is appropriate where immunity indeed becomes life-long after the booster vaccination, but fails to reflect cases where the booster prolongs temporary immunity, rather than conferring indefinite immunity. This was the case with the COVID-19 vaccine, where multiple boosters were required to prolong and increase immunity [208]. Most variants of the boosting problem, e.g., Carlsson et al. [209], adopt some form of "stacking" approach, where there are $n$ compartments that each represent $1,2, \ldots, n$ boosters. Such situations are perhaps more adequately modeled by a differential outcome model.

Let us assume that the duration of immunity is $\tau_{e}$, that is, $\tau_{e}$ time after the last booster, an individual must receive another booster or revert to susceptibility. For simplicity's sake, we will assume that the vaccination rate for the entire process is constant (v) and regardless of the number of boosters received, the likelihood to boost is $p_{b}$. Then, we obtain the following system of delay-differential equations:

$$
\begin{align*}
& \frac{d S}{d t}=\mu-\beta S I-\underbrace{\nu S}_{\text {vaccinations }}+\underbrace{\left(1-p_{b}\right) \nu S\left(t-\tau_{e}\right)}_{\text {lapsed, unboosted vaccinees }}-\mu_{s} \\
& \frac{d I}{d t}=\beta S I-\gamma I-\mu I  \tag{6.35}\\
& \frac{d V}{d t}=\nu S-\underbrace{\left(1-p_{b}\right) \nu S\left(t-\tau_{e}\right)}_{\text {lapsed, unboosted vaccinees }}-\mu V \\
& \frac{d R}{d t}=\gamma I-\mu R
\end{align*}
$$

Lifelong boosting is relatively rare, however. In most cases, a limited number of boosters establishes final immunity. For this case, we may adapt Eq. (6.35) with a given initial vaccianted compartment $V$, and vector $p$, which has the number of elements corresponding to booster stages, so that $p_{i}$ is the likelihood of a person who has had the $n-1$ th booster to receive the $i$-th booster (with the 0 th booster being the initial vaccination and governed by $\nu$ ). The $|p|$-th booster is the terminal booster, which
confers terminal immunity.

$$
\begin{align*}
\frac{d V}{d t}= & \nu S-\mu V-\mu S\left(t-\tau_{e}\right) \\
\frac{d B_{i}}{d t}= & \left(\prod_{m=1}^{i} p_{m}\right) \nu S\left(t-i \tau_{e}\right)-\mu_{B_{i}}-\left(\prod_{n=1}^{i+1} p_{n}\right) \nu S\left(t-(i+1) \tau_{e}\right) \\
\frac{d S}{d t}= & \mu-\beta S I-v S+\sum_{k=1}^{|p|}\left(\left(\prod_{m=1}^{k}\left(1-p_{m}\right)\right) \nu S\left(t-k \tau_{e}\right)\right.  \tag{6.36}\\
& \left.-\left(\prod_{n=1}^{k+1}\left(1-p_{n}\right)\right) \nu S\left(t-(k+1) \tau_{e}\right)\right)
\end{align*}
$$

### 6.3 Isolation and quarantine

Isolation and quarantine are the oldest methods in the arsenal of public health [210]. The word itself hints at its origins: a quarantena was the forty-day period ships had to spend in anchorage before entering Venice to avoid the transmission of infectious diseases [211]. Quarantines may be enforced or voluntary (self-quarantining): though the public perception of quarantine is principally a restrictive measure, voluntary quarantine has also long history. Boccaccio's Decamerone is one of the immortal legacies of self-quarantine, describing the story of ten affluent young people from Florence, who shelter in the seclusion of a villa outside the city from the 1348 outbreak of the Black Death $[212,213]$.

Throughout history, both general quarantines and specific quarantines have been used to prevent the spread of disease. A general quarantine applies to a population on the whole, regardless of health status. For instance, several countries require companion animals (pets) to be quarantined-usually in their country of origin-for a given amount of time before entry [214]. A specific quarantine applies to people who exhibit the symptoms of a particular disease, or to people who are particularly vulnerable (reverse quarantine or shielding).

It is sometimes common in the literature of public health to see the quarantine refer to identified infectious cases and prophylactic medical isolation to exposed suspected cases. However, since from a quantitative perspective, this distinction is not necessarily useful, we shall use these terms interchangeably. Table 6.1 attempts to provide an overview of the most frequently used nonpharmacological interventions.

We can explain quarantines mathematically by reference to the mass action term (see Subsection 2.1.3). Transmission is a function of the product of a constant $\beta$, the proportion of infectious, and the proportion of susceptibles. Separating either some of the infectious or some of the susceptible (or, indeed, both) into a compartment that cannot communicate with the rest of the population decreases the mass action term:

Table 6.1 The most common forms of isolation, quarantine, and related nonpharmaceutical interventions.

|  | Applied to | Limitations |
| :--- | :--- | :--- |
| Isolation <br> Barrier isolation | Exposed individuals <br> Exposed or vulnerable individuals | Movement, interaction <br> Direct physical <br> interaction <br> Movement, interaction |
| Quarantine <br> Reverse <br> quarantine | Symptomatic individuals <br> Groups, up to entire populations, of <br> generally susceptible individuals | Interaction, movement <br> of individuals from <br> outside the quarantine <br> zone |
| Cordon sanitaire | Areas surrounding (and sometimes in- <br> cluding) the source of an infection <br> Regions or wider populations, regard- <br> less of infectious status (exemptions of <br> essential workers are common) <br> Regions or wider populations, regard- | Movement, interaction, <br> presence |
| less of infectious status (exemptions of |  |  |

- by reducing the ability of some of the infectious individuals to come in contact with susceptible individuals (quarantine, isolation); or
- by reducing the likelihood of susceptible individuals to come in contact with infectious individuals (reverse quarantine, protective isolation, shielding).

In either case, the effect is to decrease the overall mass action term.

Despite this similarity, not all forms of quarantine are made equal. Computational modeling can help us understand how, why, and when quarantines work, and assist in decision-making in a public health emergency.

### 6.3.1 Case study: nonpharmaceutical interventions against Covid-19

SARS-CoV-2 and the viral syndrome it causes, COVID-19, made their world debut in the late days of 2019. Until the emergence of COVID-19 vaccines in late 2020, nonpharmacological interventions (NPIs) were the mainstays of the public health response. Despite its time-honored provenance, quarantine measures have been at the forefront of the initial measures aimed at combating the spread of SARS-CoV-2. The scale of these measures was truly unprecedented: by late 2021, almost all countries (with the notable exceptions of Sweden, Japan, South Korea, and some US states) have imposed a form of lockdown.

Lockdowns are highly effective responses to an epidemic threat, but also constitute significant limitations of individual freedoms of movement and the exercise of associated rights. Economically, lockdowns are costly and disproportionally affect certain disadvantaged groups, who may not have the financial wherewithal to sustain themselves over a period of enforced business closures.

A strategy for minimizing such costs, while achieving a comparable effect, is the "circuit breaker," first deployed in Singapore [215] and later adopted in the UK and other states [216]. The "circuit breaker" is a short period of lockdown triggered by an objective indicator, such as a rise in test-positivity ratios or a spike in healthcare capacity utilization. Circuit breakers can achieve favorable public health objectives at lower economic costs.

## Practice Note 6.5 Health equity and NPIs

It is important to consider nonpharmacological interventions as what they are: fundamental (albeit justified) limitations of individual liberties. Connected to that are a range of economic and social interests, including serious concerns of equity and social solidarity. For instance, the impact of lockdowns is significantly stronger on hourly workers with little to no savings than it is to salaried employees, who may be able to work from home. Equally, public health measures can be abused as a method of "justified" exercise of prejudice: it is hard to consider the lifelong imprisonment of Mary Mallon (better known as Typhoid Mary) to be entirely separate from the prevailing anti-Irish sentiment at the time [74]. For this reason, it is crucial to see quarantines, lockdowns, and similar measures not in isolation but as a combined social, legal, and epidemiological intervention that needs to be justified in each of those three dimensions.

Socially, lockdowns are justified by appealing to the public's overriding benefit and the importance of public health. A cornerstone of this process is ensuring that the social justification is clearly laid out and communicated in clear, intelligible terms, avoiding both panic and downplaying the risks. Legally, lockdowns will often need to rely on specialized emergency legislation. Such legislation might have to comply with superordinate norms (e.g., constitutional legislation
and civil liberties). This often requires lockdowns to be articulated in the least onerous way possible.

Finally, lockdowns must be epidemiologically sound. Gaining and maintaining public trust in the epidemiological and public health professions is paramount. For this reason, disease modelers must be prepared to communicate the risks of the pathogen, as well as the effects of the lockdown, taking into account wider social and socio-economic effects. Decision-makers in a crisis situation are often suffering from a bias of "tunnel vision," focusing on the most urgent problem at hand. Epidemiologists can assist in alleviating the detrimental effects of NPIs on social equity and the situation of disadvantaged populations by highlighting the effect of NPIs on society's most vulnerable and advocating for measures to minimize the detrimental impact.

### 6.3.2 General quarantine

A general quarantine is not selective to the class of individuals, and for this reason, everyone enters and exits the quarantine at the same time. The easiest way to characterize general quarantine is to conceive of it as a time-dependent depression of $\beta$ by a discount factor $\chi$ (where $0 \leq \chi \leq 1$ ). For a $\tau_{q}$-day quarantine starting on $t_{q}$,

$$
\beta(t)=\left\{\begin{array}{l}
\beta \chi \text { if } t \in\left[t_{q}, t_{q}+\tau_{q}\right]  \tag{6.37}\\
\beta \text { otherwise }
\end{array}\right.
$$

This model is somewhat akin to the time-varying $\beta$ models that utilize a step function, e.g., term-time forcing (on which see Subsection 7.3.3), except that we are modeling a single, nonrecurrent event. A welcome convenience of this approach is that it does not introduce a new compartment. Though this would ordinarily make analytical solutions rather more elusive than a simple transfer function to another compartment, it makes numerical solutions almost trivially easy, as we shall see in Computational Note 6.3.

## Computational Note 6.3 Modeling the effect of different quarantine regimes

A SIR model can be adapted to take account of a quarantine period rather easily. Since we define our derivative function as a Python function, any Python construct operating on its parameters is fair game. This includes conditionals:

```
def deriv_with_quarantine(t, y, beta, gamma, chi, tau_q, t_q):
    S, I, R = y
```

```
if t_q<t<t_q + tau_q:
    beta_eff = beta * chi
e1se:
    beta_eff = beta
dSdt = -beta_eff * S * I
dIdt = beta_eff * S * I - gamma * I
dRdt = gamma * I
return dSdt, dIdt, dRdt
```

It is often quite practical to integrate over a range of parameters. solve_i vp is particularly useful for this purpose, because it returns a lot of parameters in a single object. Different parameters often lead to the function being evaluated at different points in time, and for this reason, they need to be plotted with their own times of evaluation. For the derivative above, we can obtain the times of evaluation (the property .t of the result object) and the corresponding result vector (the property .t).

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch06/ quarant ine.

## Practice Note 6.6 The ethics of quarantines

Quarantines restrict fundamental human freedoms we recognize as inherent rights of every human being. As such, they are prima facie infringements on human rights and civil liberties. The American Medical Association's Code of Medical Ethics Opinion 8.4 concerning the ethical use of quarantine and isolation lays down some fundamental rules that could be considered good practice for all of public health [217]:

- Quarantine and isolation must be scientifically and ethically sound.
- The least restrictive means that are sufficient to control disease must be used.
- Quarantine and isolation must be exercised equitably, without bias against classes or groups of patients.

The power to quarantine individuals is perhaps the most extensive power over another human being available to the state without a judicial process. Like the criminal justice system, it is empowered to deprive people of their liberty temporarily, yet it is not subject to many of the safeguards that protect a defendant in a criminal trial. Unequal or discriminatory application of quarantines, or, indeed, even the perception of it, as Desclaux et al. [218] note, may vitiate a quarantine's
perception as a measure for the public good. Complex social and economic contexts, as were evidenced both during the West African EBOV outbreak and, later, during the COVID-19 crisis (see for example Hesselman et al. [219] for energy poverty, Crawford and Waldman [220] for period poverty, Ahmed et al. [221] for race, Phillips et al. [222] and Sachdeva et al. [223] for the LGBTQ+ community), factor into these perceptions.

The quarantine power may be enforceable by the state's policing powers, but this is not the case indefinitely. Quarantines require civil cooperation, and such cooperation is easily lost if the measures appear biased, inequitable, or calculated to affect some groups more harshly than others. A general quarantine is an emergent and extraordinary option, and wherever possible, alternative mechanisms, such as circuit breakers (see Subsection 6.3.4), should be considered. There will always be a "next pandemic," and errors of judgment in the present can jeopardize adherence in the future.

### 6.3.3 Quarantines and healthcare capacity

As Fig. 6.6 demonstrates, different quarantine regimes have a profound effect on the long-term dynamics of the disease. Importantly, longer quarantine times slow down the spread and reduce the maxima of infections. The consequence is that appropriate quarantines can reduce the demand on healthcare services and prevent overloading.

This is instructively demonstrated by a model with contingent mortality. Let $\mu_{T}$ be the base mortality rate of the disease with treatment and $\mu_{U}$ the untreated mortality rate, both denominated in terms of deaths per person per day. Let $c$, furthermore, be the carrying capacity of the healthcare system, expressed as new infections per day.

![](https://cdn.mathpix.com/cropped/2024_06_11_144605289bea1fda3a26g-32.jpg?height=569&width=1184&top_left_y=1396&top_left_x=135)

Figure 6.6 Results of a SIR model with quarantines of various lengths commencing on day 35 and a quarantine effectiveness of $\chi=0.3$. The model was initialized with $\Re_{0}=2.5, \gamma=\frac{1}{8}$ and an initial infected population of $1 \times 10^{-4}$.

![](https://cdn.mathpix.com/cropped/2024_06_11_144605289bea1fda3a26g-33.jpg?height=577&width=1182&top_left_y=230&top_left_x=174)

Figure 6.7 The effect of quarantines on capacity-dependent mortality regimes for a model identical to that in Fig. 6.6, with a carrying capacity $c=0.15, \mu_{T}=0.5$, and $\mu_{U}=0.15$. Regimes where $I$ exceeds $c$ are marked and shaded in red.

A critical phenomenon occurs at $I=c$, at which point excess cases above $c$ will receive lower level care, or no care at all. We may approximate this by separating treated and untreated mortality rates, where the first $c$ patients at any given time experience the treated mortality rate $\mu_{T}$ and the remainder experiences the untreated mortality rate $\mu_{U}$. This allows us to formulate overall illness-related mortality (i.e., ignoring natural mortality) as

$$
\begin{equation*}
\frac{d D}{d t}=(\underbrace{\mu_{T} \max (I, c)}_{\text {first } c \text { patients }}+\underbrace{\mu_{U} \max (I-c, 0)}_{\text {overload }}) I \tag{6.38}
\end{equation*}
$$

Fig. 6.7 highlights the effects of quarantines in preserving a healthcare system's ability to care for patients. Not only is the overall mortality lower due to the attenuated epidemic curve witnessed in Fig. 6.6, but the periods during which the healthcare system is beyond the critical point, and mortality occurs at the over-capacity regime are drastically shortened, until they are eliminated altogether in the case of the 35-day quarantine.

## Practice Note 6.7 Mortality below, at, and above capacity

In much of the section above, we discussed mortality that sets in once healthcare capacity is exceeded. This is largely discontinuous: receiving care is largely a binary variable, splitting the population into two cohorts, whose clinical outcomes will be governed to a great extent by the difference between mortality with versus without treatment.

There is another and entirely distinct source of mortality that is related to hospital capacity. Rossman et al. [224] examined mortality rates of patients with COVID-19 in Israel depending on patient load, and found that under increased but moderate patient load (at approximately $60 \%$ of the Israeli Ministry of Health's estimate of the maximum capacity), mortality rates were $22.1 \%$ to $27.2 \%$ higher than in periods with lower patient loads. Strålin et al. [225] found similar results in Sweden with respect to 60-day all-cause mortality following COVID-19 diagnosis. This phenomenon has been observed in other infectious diseases (e.g., by Maciás et al. [226] in the context of dengue) and noninfectious phenomena (e.g., Kayiga et al. [227] in the context of obstetric care and Crandall et al. [228] in respect of trauma care).

This suggests that in addition to the critical phenomenon once $I=c$, there is a continuous subcritical phenomenon as $I$ converges on the capacity constraint. As Rossman et al.'s study showed, this phenomenon appears at a rather disconcertingly early stage. Exploring the capacity envelope of the healthcare system in an epidemic should, if at all possible, be avoided. Even subcritical excess loads present a cost in terms of mortality, and recommendations on quarantine length should take this into account.

### 6.3.4 Circuit breakers

A circuit breaker is a form of generalized, short-term quarantine that is triggered by a sentinel variable, such as the number of new infections or hospitalized individuals. The term originates from a type of safety mechanism in stock exchanges, notably the New York Stock Exchange (NYSE), which automatically applies a trading halt when an indicator declines more than a certain preset value over a trading day. Circuit breakers were introduced during the COVID-19 pandemic in Singapore, and have been quite successful in attenuating the early dynamics of COVID-19 [229,230]. A key benefit of circuit breakers is that they are highly efficient: the effect of a circuit breaker policy is comparable, if not superior, to a longer general quarantine, without the economic and social costs of sustained quarantining.

Circuit breakers can be modeled most conveniently by using a time-dependent coefficient of transmission:

$$
\beta(t)= \begin{cases}\beta_{1} & \text { if circuit-breaker is active at } t  \tag{6.39}\\ \beta_{0} & \text { otherwise }\end{cases}
$$

Circuit breakers are activated if a sentinel indicator reaches a particular threshold value. Where the key objective is preserving the healthcare capacity, the number of hospitalized cases is a good sentinel indicator, as it is quite easy to ascertain from hospital information systems. This was, indeed, the approach adopted in Singapore [229]. Though the example in Computational Note 6.4 uses the size of the infectious com-
partment as the sentinel variable, this figure is in practice much more difficult to ascertain.

## Practice Note 6.8 Choosing a sentinel indicator

The circuit breaker strategy is only as good as its sentinel indicator. Good sentinel indicators meet the three As: ascertainability, availability and accuracy.

- Ascertainability means that the indicator can be calculated or at least very accurately estimated. The number of infectious individuals, for instance, is relatively hard to ascertain, especially if the pathogen is novel, its presentation is nonspecific and/or there is a nontrivial asymptomatic period.
- Availability means that the sentinel indicator should be accessible and updated frequently. Any indicator with a less than daily temporal resolution is generally not a suitable candidate. Hospital admissions data, perhaps the most widely available potential sentinel indicator in resource-rich settings, where electronic medical records (EMRs/EHRs) are common, are connected to a reporting system maintained by the public health authorities, and cases can be reported in near real time. In resource-constrained settings, including in the aftermath of natural disasters, communications may not be sufficient to support a circuit breaker strategy at all.
- Accuracy means that the indicator reasonably closely reflects reality. This can be rather challenging, especially in the context of a novel emerging pathogen. Often, a more sensitive but less specific indicator, such as the total number of presentations with any type of respiratory illness, might be preferable to a more specific but less sensitive metric, e.g., COVID-19 diagnoses.

Circuit breakers are powerful tools that limit the time spent in quarantine, while providing benefits comparable to a longer quarantine period. Quarantines have economic [231], social [232], and emotional [233,234] costs of which one must remain mindful. Circuit breakers have the potential to reduce the scale of these effects without losing the public health benefits of quarantines, but are strongly dependent on the availability of the right kind and quality of data to support it. It is not a "one size fits all" solution, and its relative success during COVID-19 must be weighed against its specific resource requirements.

Circuit breakers work best when their duration $\tau_{q}$ is relatively long compared to the mean infectious period. Singapore's two circuit breakers lasted a little less than two months each. Byrne et al. [235] estimated the median infectious period of COVID-19 as 6.5 to 9.5 days for asymptomatic cases and the median maximal infectious period as 18.1 days. Singapore's circuit breakers were thus approximately 3 times as long as the median maximal infectious period. The simulation in Computational Note 6.4 and Fig. 6.8 uses a quarantine period 1.75 times the mean infectious period, and shows a positive impact. The length of the quarantine period is bounded on the lower end by the maximal infectious period; any shorter and an infectious case may still transmit

![](https://cdn.mathpix.com/cropped/2024_06_11_144605289bea1fda3a26g-36.jpg?height=576&width=1187&top_left_y=224&top_left_x=134)

Figure 6.8 A model of a circuit breaker quarantine for a pathogen with $\mathfrak{R}_{0}=2.5$ and $\gamma=\frac{1}{8}$. The transmission coefficient is $\beta_{0}=0.3125$ outside the circuit breaker and $\beta_{1}=0.0625$ during the circuit breaker's activity. The circuit breaker is triggered at $I(t)=0.1$ and lasts for 14 days.

disease when emerging from the circuit breaker quarantine. The minimum safe values of $\frac{\tau_{q}}{\tau}$ for circuit breakers have not been determined, but Singapore's example suggests that for a highly efficient (and restrictive) quarantine, a factor of 3 is appropriate. For lower effectiveness, higher time factors are likely to be necessary.

## Computational Note 6.4 Iterative stateful evaluation

ODE integrators are powerful tools, but generally do not accommodate nonintegrated state variables too well. It is possible to model circuit breakers as delay differential equations with a conditional function for $\beta$, but in practice, computationally ascertaining the result is much easier by way of iterative evaluation.

Since a differential equation describes the state of change of a system, an initial value problem can be computationally solved by iterating over a span of time $t_{0} \rightarrow t_{n}$ and in each step, applying the differential equation's terms to the previous step's results. We implement the circuit breaker through four main steps:

- an array that keeps track of whether the circuit breaker is active or not for each time step,
- a variable that retains the last time the circuit breaker was triggered,
- an expression that adjusts $\beta$, depending on whether the circuit breaker is in effect, and
- an expression that turns the circuit breaker on and off.

We shall take these in turn.

We initialize a two-dimensional array with a row for each day (given by the integration period t_span) and four columns, three for each compartment and one for the current state of the circuit breaker. The rationale for using an array rather than an expanding list is due to the memory benefits of changing values in an existing and predefined array over consistently reshaping the array, which would require the array to be re-mapped over memory.

We initialize the first row with the vector y_0, comprising $S(0), I(0)$, and $R(0)$, and 0 to represent that we initialize the system with the circuit breaker off:

```
y = np.zeros(shape=(t_span, 4))

```

![](https://cdn.mathpix.com/cropped/2024_06_11_144605289bea1fda3a26g-37.jpg?height=42&width=299&top_left_y=689&top_left_x=213)

Thus $S(t), I(t)$, and $R(t)$ correspond to y[t, 0], y[t, 1], and y[t, 2], respectively, whereas $y[t, 3]$ gives the state of the circuit breaker. The destructuring assignment in $[* y 0,0]$ is a quick and efficient way to create the initial state that is partly provided by an iterable ( $\mathrm{y} 0$, for $S, I$ and $R$ ) and partly by a concrete value ( 0 , for the state of the circuit breaker).

Next, we initialize a variable to store the start of the circuit breaker:

```
circuit_breaker_start = None
```

The iterative execution will loop through each day, from 0 to $t$ span, and calculate the integral by adding the differential, evaluated at the previous time step, to the value at the previous time step:

```
for i in range(1, t_span):
    beta = beta_0 if y[i - 1, 3] == 0 else beta_1
    y[i, :3] = y[i-1,:3] + (
        - beta * y[i - 1, 0] * y[i - 1, 1],
    beta * y[i - 1, 0] * y[i - 1, 1] - gamma * y[i - 1, 1],
    gamma * y[i - 1, 1]
    )
```

The step function for $\beta$ is defined here, too: if the circuit breaker was off in the previous time step, $\beta=\beta_{0}$, otherwise $\beta=\beta_{1}$.

Finally, we need to perform some housekeeping in each step with respect to the state of the circuit breaker:

- If the circuit breaker is on and it has been more than $\tau_{q}$ days since the initiation of the circuit breaker, it is switched off.
- If the circuit breaker is off and the sentinel value (in this example, $I$ ) exceeds the threshold (defined as threshold), the circuit breaker is turned on. The time is noted by setting circuit_breaker_start equal to the current time.

All put together, the function reads as follows:

```
def model_with_circuit_breaker(t_span:int,
                    y0: tup7e,
                    beta_0: float,
                    beta_1: float,
                    gamma: float,
                    tau_q:float,
                    threshold:float) -> np.array:
    y = np.zeros(shape=(t_span, 4))
    y[0, :] = [*y0, 0]
    circuit_breaker_start = None
    for i in range(1, t_span):
        beta = beta_0 if y[i - 1, 3] == 0 else beta_1
        y[i, :3] = y[i - 1, :3] + (
            - beta * y[i - 1, 0] * y[i - 1, 1],
            beta * y[i - 1, 0] * y[i - 1, 1] - gamma * y[i - 1, 1],
            gamma * y[i - 1, 1]
        )
        if y[i - 1, 3] == 1:
            if i > circuit_breaker_start + tau_q:
                y[i, 3] = 0
            else:
                y[i,3] = 1
    if y[i - 1, 3] == 0 and y[i, 1] > threshold:
        y[i, 3] = 1
        circuit_breaker_start = i
    return y
```

Fig. 6.8 shows the number of an infected population with a trigger value of $I \geq 0.1$, showing the way circuit breakers can flatten the epidemic curve, and thus preserve healthcare capacity.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch06/ circuit_ breaker.

### 6.3.5 Quarantine of the infectious

As the name suggests, in the quarantine of the infectious, only individuals who are infectious are placed in quarantine. Often, this is not entirely accurate; typically, infectious individuals are selected by serological markers, and depending on the methodology of testing, an infectious individual may not immediately test positive. This is the case in particular where tests look for antibodies, which take a few days to emerge, rather than the antigen, which is typically present immediately, but may be harder to test for. A system of delay differential equations can characterize this dynamic as

$$
\begin{align*}
\frac{d S}{d t} & =\mu-\beta S I-\mu S \\
\frac{d I}{d t} & =\beta S I-\gamma I-\mu I-\int_{t-\tau}^{t-\tau_{d}} p_{c} I\left(u-\tau_{d}\right) d u \\
\frac{d Q}{d t} & =\int_{t-\tau}^{t-\tau_{d}} p_{c} I\left(u-\tau_{d}\right) d u-\int_{t-\left(\tau+\tau_{q}\right)}^{t-\left(\tau_{d}+\tau_{q}\right.} p_{c} I\left(v-\left(\tau_{d}+\tau_{q}\right)\right) d v-\mu Q  \tag{6.40}\\
\frac{d R}{d t} & =\gamma I+\int_{t-\left(\tau+\tau_{q}\right)}^{t-\left(\tau_{d}+\tau_{q}\right)} p_{c} I\left(v-\tau_{d}-\tau_{q}\right) d v-\mu R
\end{align*}
$$

where $\tau_{q}$ is the fixed duration of the quarantine, $\tau_{d}$ is the diagnostic or symptomatic delay (i.e., the time before an infectious individual becomes symptomatic and/or diagnosable, and thus amenable to capture by quarantine) and $\tau$ is, of course, the length of the entire infectious period. The capture of infectious individuals is described by the integral

$$
\begin{equation*}
\int_{t-\tau}^{t-\tau_{d}} p_{c} I\left(u-\tau_{d}\right) d u \tag{6.41}
\end{equation*}
$$

In other words, at time $t$, quarantine can capture individuals who have contracted the infection no earlier than $t-\tau$ (since anyone who has obtained the infection earlier would by $t$ be recovered) and no later than $t-\tau_{d}$ (since anyone who has obtained the infection later would not be symptomatic or have a detectable infection).

- Individuals are liable to capture throughout their symptomatic period, which is $\tau-\tau_{d}$ long. Their capture likelihood is the constant $p_{c}$.
- Quarantinees are released $\tau_{q}$ time after their quarantine. This is so regardless of their time of infection, or how far into the infection they were captured. Thus the number of individuals released on $t$ equals the inflow into quarantine on $t-\tau_{q}$,
namely

$$
\begin{equation*}
\int_{t-\left(\tau+\tau_{q}\right)}^{t-\left(\tau_{d}+\tau_{q}\right)} p_{c} I\left(u-\left(\tau_{d}+\tau_{q}\right)\right) d u \tag{6.42}
\end{equation*}
$$

The benefit of the delay integro-differential formulation of the model is that it provides a stateful memory to specify quantities with respect to the past. Thus though a simple delay-differential formulation might give the quarantine system a "single bite of the cherry" (one chance to recognize and capture a symptomatic individual at $\tau_{d}$ days after the infection), this model of quarantine reflects the reality that individuals can in fact be captured throughout their infectious career. The computational approach outlined in Computational Note 6.2 can be applied to this model, mutatis mutandis.

The delay differential equation in (6.40) can be vastly simplified in many cases, most appropriately where quarantine is not of a fixed duration, but is rather contingent on biomarkers (testing negative) or the clinical course. Instead of using a delay, we simply use a transfer term that considers the mean rate of moving out of the quarantined compartment, which is the inverse of the mean time spent in quarantine, $\tau_{\bar{q}}$ :

$$
\begin{align*}
& \frac{d Q}{d t}=\underbrace{p_{c} I}_{\text {capture }}-\underbrace{\frac{1}{\tau_{\bar{q}}} Q}_{\text {release }} \\
& \frac{d R}{d t}=\underbrace{\gamma I}_{\text {recovered from } I}+\underbrace{\frac{1}{\tau_{\bar{q}}} Q}_{\text {released from } Q} . \tag{6.43}
\end{align*}
$$

The effect of quarantine on $\Re_{t}$ deserves mention. An analysis of the simplified model's next generation matrix (see Subsection 2.5.2) reveals that given a quarantine of identified infectious individuals with the capture probability $p_{c}$,

$$
\begin{equation*}
\Re_{t}=\frac{\beta}{\gamma+p_{c}} \tag{6.44}
\end{equation*}
$$

Solving the above for $\Re_{t}=1$ reveals that the capture rate of a quarantine system must be larger than $\beta-\gamma$ if it is to control the infection. We may use this finding to understand the effect of lags. Let us consider a single patient, who experiences the illness for $\tau=\frac{1}{\gamma}$ days. On each of these, he stands a $p_{c}$ chance of being captured and quarantined. For $\tau_{d}<\tau$, we can conceive of each of the days in $\tau_{d}$ to be a "missed opportunity" to detect him. Thus a delay of $\tau_{d}$ days reduces the effective value of $p_{c}$ by $\frac{\tau_{d}}{\tau}$. This means that Eq. (6.44) now becomes

$$
\begin{equation*}
\mathfrak{R}_{t}=\frac{\beta}{\gamma\left(1-\tau_{d} p_{c}\right)} \tag{6.45}
\end{equation*}
$$

The maximum value of capture is, of course, unity, representing perfect capture. Setting $p_{c}=1$ and $\Re_{t}=1$, we can solve for $\tau_{d}$. This gives us an important finding: if
$\tau_{d}>\frac{\beta-\gamma}{\gamma}$ (under the assumption that $\frac{1}{\gamma}>>\tau_{d}$ ), then even perfect control of detected cases will be ineffective at curbing the disease, since the time to detection will suffice to provide enough secondary cases for the pathogen's survival.

## Practice Note 6.9 Time and life

The consequence of this limitation of quarantine is that for diseases with a higher $\Re_{0}$ (in general), control through quarantine of the infectious becomes increasingly difficult. If we consider that the vast majority of infectious diseases rarely show initial symptoms for days (and even then, the symptoms may be nonspecific), control through quarantine of the infectious becomes an increasingly tenuous proposition. For this reason, quarantine of the infectious is rarely a sufficient mainstay of public health response to an epidemic.

This is not to say quarantining the infectious is not an important measure. Together with general quarantine and other NPIs, it can fulfill an important role. Moreover, in many settings, infection is presumed rather than substantiated. This is the rationale of human and animal quarantines at ports of entry. This eliminates the potential risk of missing an infection for too long until it moves beyond control, but comes with serious economic and social costs. As in so many cases of public health, the best option is often a mix of judiciously applied options rather than a single policy.

### 6.3.6 Post-exposure quarantine

Post-exposure quarantine refers to quarantine models, where the quarantine process is triggered by an exposure event. Often, this is described not as quarantine but as asymptomatic medical isolation, but the essence is the same: individuals subject to post-exposure quarantine will be restricted to an isolation unit or their place of residence.

An interesting feature of this model is that one can be infectious and quarantined at the same time. Since this is not compatible with the fundamental properties of a compartmental model discussed in Chapter 2, we will consider quarantined status to supervene infection. We can do so safely if $\tau_{q}>>\tau$, as long as we assume that the quarantined do not take part in the infectious process, and therefore do not need to be considered in the mass action term. Given a latency period of $\tau_{d}$ days, the model may be specified as

$$
\begin{aligned}
\frac{d S}{d t} & =-\underbrace{\beta S I}_{\text {mass action }} \\
\frac{d E}{d t} & =\underbrace{\beta S I}_{\text {mass action }}-\underbrace{\tau_{d}^{-1}}_{\text {lapse of latency }}
\end{aligned}
$$

$$
\begin{align*}
\frac{d I}{d t}=\underbrace{\left(1-p_{c}\right) \tau_{d}^{-1}}_{\text {non-captured exposures }}-\underbrace{\gamma I}_{\text {recovery }}  \tag{6.46}\\
\frac{d Q}{d t}=\underbrace{p_{c} \tau_{d}^{-1}}_{\text {captured exposures }}-\underbrace{\tau_{q}^{-1} Q}_{\text {released from } Q} \\
\frac{d R}{d t}=\underbrace{\tau_{q}^{-1}}_{\text {released from } Q}+\underbrace{\gamma I}_{\text {recovered from } I}
\end{align*}
$$

In this model, the exposed compartment's outflow $\left(\tau_{d}^{-1} E\right)$ is partitioned into those who are captured (the fraction ${ }^{\Delta} \mathcal{v}$ ) and those who are not, and therefore go on to constitute the infectious compartment $\left(1-p_{c}\right)$.

### 6.3.7 Shielding (quarantine of high-risk susceptibles)

Shielding is a form of reverse quarantine, where a segment of the susceptible population is separated to protect them from infection. However, in addition to traditional self-quarantine, we have an intermediate group of "shielders," who are not at high risk but take special additional measures to avoid infection, because they are in frequent contact with vulnerable individuals. Thus we have three strata: the general population $G$, the shielders $S$, and the vulnerable $V$. The vulnerable are only in contact with shielders, whereas shielders are in contact with the vulnerable and the general population, albeit at a lower rate.

It may be useful to reutilize the WAIFW matrix concept from Eq. (3.1), for

$$
\mathbf{b}=\left(\begin{array}{lll}
\beta_{G \rightarrow G} & \beta_{G \rightarrow S} & \beta_{G \rightarrow V}  \tag{6.47}\\
\beta_{S \rightarrow G} & \beta_{S \rightarrow S} & \beta_{S \rightarrow V} \\
\beta_{V \rightarrow G} & \beta_{V \rightarrow S} & \beta_{V \rightarrow V}
\end{array}\right)
$$

Under the assumption of perfect shielding, there are no direct interactions between the general population and the vulnerable population, therefore $\beta_{G \rightarrow V}$ and $\beta_{V \rightarrow G}$ are both zero. We may describe the model as a classical SIR model with $n$ subpopulations $\{G, S, V\}$, i.e.,

$$
\begin{align*}
\frac{d S_{i}}{d t} & =-S_{i} \sum_{j=1}^{n} \mathbf{b}_{i, j} I_{j} \\
\frac{d I_{i}}{d t} & =S_{i} \sum_{j=1}^{n} \mathbf{b}_{i, j} I_{j}-\gamma I_{i}  \tag{6.48}\\
\frac{d R_{i}}{d t} & =\gamma I_{i}
\end{align*}
$$

The overall impact of this is not only to reduce the mass action term $\beta S I$, but also to selectively protect a subset of susceptible individuals. The "cost" of shielding is
the shielders' reduced ability to interact with others. Shielding is only effective if $\beta_{S}$ is quite significantly lower than $\beta_{G}$ [236]. Experience from the COVID-19 pandemic suggests that a $\frac{\beta_{G}}{\beta_{S}}$ of between 2.0 and 4.9 is most effective [236].

## Practice Note 6.10 Stratified shielding

The example above approaches shielding as a monolithic concept, but that need not be so. Precision shielding or stratified shielding is an approach that balances the risk to the shielded individual with the extent of shielding [237]. The difficulty is that risk stratification is often quite individual, and creating a "permissible activities framework" for shielders depending on the shielded vulnerable person's individual degree of vulnerability is often quite complicated and not necessarily amenable to analytically sound assessment.

It is also important, however, to keep the economic aspects of shielding in mind. Shielding affects not only the vulnerable person but also the shielders. The ability of households to be able to sustain shielding over a prolonged period of time depends on economic and societal factors. Stratification may be imperfect, but even a rough stratification may reduce the overall economic burden on shielders, and thus, overall, benefit the vulnerable, too.

