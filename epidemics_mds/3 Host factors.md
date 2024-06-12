# Host factors Who gets sick and why 

[A]ll good things (e.g., stability) are more fragile than bad things. It seems that in good situations a number of requirements must hold simultaneously, while to call a situation bad even one failure suffices.

Arnol'd, Catastrophe theory, 1986 [89]

The term "host factors" denotes those aspects of infectious disease transmission that are inherent in the potential host. Simply put, host factors are what sets an individual apart from others in the context of contracting an infectious disease. Because we are modeling populations, we need to represent host factors often as groups of individuals who share meaningfully similar values of a particular host factor (e.g., age groups, binned numbers of sexual partners, binned values of an exposure variable). We refer to these groupings as strata.

Definition 3.1 (Strata). A stratum ( $p l$. strata) is a modifier that sets individual types of compartment apart by a population characteristic.

For instance, in a model that has separate strata for high- and low-risk behaviors, the high-risk stratum would comprise high-risk susceptible and infectious compartments ( $S_{H}$ and $I_{H}$, respectively), whereas the low-risk stratum would comprise low-risk susceptible and infectious compartments ( $S_{L}$ and $I_{L}$, respectively).

This chapter deals with situations of heterogeneous populations. In computational epidemiology, strata are our way of representing sets of compartments that "belong together" as members of groups with groupwise heterogeneity, such as higher transmission risk. It is sometimes common to refer to such models as "structured," e.g., "age-structured" for an age stratified model, but in what follow, we will use the term stratification, where risks are represented as categories and strata.

### 3.1 Heterogeneity of transmission risk

In models where transmission risk is heterogeneous, we are no longer assuming that the transmission likelihood between every individual is the same. Recall that the mass action term $\beta S I$ assumed homogeneous mixing and equal risk of transmission from any member of $I$ to any member of $S$ (see Subsection 2.1.3). In this section, we will be breaking the first half of that symmetry. In reality, when it comes to passing on or sustaining infections, all are not created equal. For reasons that are not as well understood as their practical importance would warrant, a small number of infected individuals are often responsible for a disproportionately large number of infectious
events (see Subsection 3.1.4). On the other hand, some factors of the clinical course may reduce the likelihood of infecting others, such as isolation and hospitalization (see Subsection 3.1.6). This section describes the mathematical models we can use to make sense of these heterogeneities.

## Practice Note 3.1 Meaningful heterogeneity

To an extent, all populations are heterogeneous when it comes to the transmission of infectious disease. When creating models, it is up to you to know whether these differences are relevant. For instance, though women are somewhat more likely to acquire influenzaviral infections, as noted by e.g. Klein, Hodgson, and Robinson [90], the difference is rarely large enough to justify modeling.

As a guideline, heterogeneity is meaningful if

- there is a significant difference in terms of infection between strata $(\mathrm{RR} \geq$ 1.5 ), or
- there is a significant difference in terms of outcomes between strata $(\mathrm{RR}\geq$ 1.5 ), or
- there is a significant issue of health equity involved, e.g., an underserved stratum with a much higher risk.


### 3.1.1 Case study: determinants of hepatitis C transmission

Hepatitis C virus (HCV) affects approximately $2 \%$ of the global population. It is one of the leading causes of liver failure worldwide, and curative treatment is expensive [91].

In the United States and most developing nations, the majority of HCV infection are attributable to intravenous drug use (IVDU), where the pathogen is spread through the reuse and sharing of hypodermic needles. Shiffman [92] notes that over half of intravenous drug users have been exposed to $\mathrm{HCV}$, driving a new epidemic of hepatitis C, especially among younger people.

The additional risk from a certain behavior (in this case, IVDU) may put a subpopulation at a significantly higher risk for exposure. Where such differences in exposure or transmission risk are meaningful, it may be useful to consider accommodating this risk difference in our models. In such cases, we denote the population as riskheterogeneous.

Definition 3.2 (Risk heterogeneity). A population is risk-heterogeneous if a part of the population has a significantly higher or lower risk of acquiring, transmitting, or carrying an infectious disease (i.e., a higher or lower risk of transitioning out of the susceptible, and into an infected, compartment).

Heterogeneities may come in one of three forms:

- behavioral heterogeneities (e.g., high-risk sexual behaviors),
- exposure heterogeneities (e.g., working in a profession where exposure to bloodborne pathogens is more likely, such as EMTs and emergency physicians), and
- susceptibility heterogeneities (e.g., iatrogenic immunosuppression or old age).


## Practice Note 3.2 Avoiding undue stigma

Discussing higher and lower risk behaviors can easily move into the territory of stigmatizing people who engage in what we epidemiologically regard as "higher risk." Not only is this analytically unhelpful, it is also counterproductive from a public health perspective. When we speak of high-risk behaviors, we must understand that some-indeed, many!-of these behaviors are not voluntary choices. Although we use the terminology of behaviors, these are often the consequence of givens and circumstances, such as certain socioeconomic determinants of health.

When writing about risk heterogeneity, remember to be sensitive to the subject and avoid stigmatising language wherever possible.

Heterogeneities of multiple sources may often coexist. For HCV, the main heterogeneity is, of course, behavioral (i.e., IVDU). For other pathogens, however, there may be multiple risk factors. For HIV, for instance, high-risk sexual behaviors constitute a behavioral heterogeneity in the population. On the other hand, some alleles of the CCR5 protein (specifically, CCR5- $\triangle 32$ ) have a protective effect against infection by macrophagotropic strains of HIV-1, because they interfere with viral entry. The latter is a susceptibility heterogeneity, present in the protective homozygous form in about $0.1 \%$ of the population. When encountering a large number of heterogeneities, it is often useful to assess whether they are meaningful enough to be modeled (see Practice Note 3.1).

### 3.1.2 Modeling risk-heterogeneous populations

A risk-heterogeneous population has two or more distinct subgroups that exhibit risk heterogeneity (see Definition 3.2).

Let us consider a simple case of a population made up of two groups, high-risk and low-risk, denoted by the subscripts $H$ and $L$, respectively (see Fig. 3.1). We know from our examination of the mass action term (in Subsection 2.1.3) that the infectious effect is the product of the transmission coefficient $\beta$, the susceptible population, and the infected population. There are four distinct processes going on in our model of two separate risk groups: transmissions inside the groups (high-risk to other high-risk individuals and low-risk to low-risk individuals) and transmissions between groups (high-risk to low-risk individuals and low-risk to high-risk individuals). We may conveniently represent this as a matrix $\mathbf{b}$ of transmission probabilities, where by convention $\mathbf{b}_{i, j}$ means the likelihood of transmission from $j$ to $i$

$$
\mathbf{b}=\left(\begin{array}{ll}
\beta_{H, H} & \beta_{H, L}  \tag{3.1}\\
\beta_{L, H} & \beta_{L, L}
\end{array}\right)
$$

![](https://cdn.mathpix.com/cropped/2024_06_11_7acef27a50e7509ebe89g-04.jpg?height=514&width=903&top_left_y=226&top_left_x=276)

Figure 3.1 A SIR model with two differential risk classes. $\beta_{i, j}$ denotes the transmissibility from $j$ to $i$.

This matrix is sometimes referred to as a WAIFW (who acquires infection from whom) matrix.

Definition 3.3 (WAIFW matrix). A WAIFW (who acquires infection from whom) matrix $\mathbf{b}$ for a model with $m$ strata is an $m \times m$ matrix, where $\mathbf{b}_{i, j}=\beta_{j \rightarrow i}$.

The WAIFW matrix is a convenient mathematical shorthand for the values of $\beta$ within the separate differential equations for the infectious subsystem $\left\{I_{H}, I_{L}\right\}$ in a $S I_{H, L} R$ model:

$$
\begin{align*}
& \frac{d I_{H}}{d t}=\overbrace{\beta_{H, H} S_{H} I_{H}}^{H \rightarrow H}+\overbrace{\beta_{H, L} S_{H} I_{L}}^{H \rightarrow L}-\overbrace{\gamma I_{H}}^{\text {recovery }} \\
& \frac{d I_{L}}{d t}=\underbrace{\beta_{L, H} S_{L} I_{L}}_{L \rightarrow H}+\underbrace{\beta_{L, L} S_{L} I_{L}}_{L \rightarrow L}-\underbrace{\gamma I_{L}}_{\text {recovery }}
\end{align*}
$$

Eq. (3.2) corresponds, given the matrix $\mathbf{b}$ from Eq. (3.1) and a vector $\vec{\gamma}=\binom{\gamma_{H}}{\gamma_{L}}$, to

$$
\begin{equation*}
\frac{d I_{i}}{d t}=\underbrace{S_{i} \sum_{j=1}^{n} \overbrace{\mathbf{b}_{i, j}}^{\text {WAIFW matrix }} I_{j}}_{\text {mass action }}-\overbrace{\gamma_{i}}^{\text {vector of recovery rates by stratum }} I_{i} \text {. } \tag{3.3}
\end{equation*}
$$

Where there are multiple subpopulations of each of the compartments, it may often be a sensible choice to represent different transitions between those populations as WAIFW matrices and nondirectional subpopulation-dependent factors (such as $\gamma$ or $\mu$, which depend solely on the subpopulation to which they relate) as vectors.

### 3.1.2.1 Analysis of the WAIFW matrix

In our previous models, we assumed homogeneous mixing (see Definition 2.11), and thus we had a single compartment $S$ and a single compartment $I$, with a single coefficient $\beta$. The WAIFW matrix breaks down $\beta$ into components. Thus where the WAIFW matrix's elements have been empirically ascertained, we can obtain some insights about the underlying process.

- The symmetry of $\mathbf{b}$ indicates the equality of response. If $\mathbf{b}_{i, j}=\mathbf{b}_{j, i}$, then the response is not directionally dependent. This is the case where belonging to a risk group affects the likelihood of transmission and exposure, but not the likelihood of becoming infected upon exposure. We refer to this as equiresponse (see Definition 3.4). Conversely, where being in a particular risk group is associated with risk factors that also make infection upon exposure more likely (e.g., the ratio of persons suffering from immune deficiencies is higher among intravenous drug users than the general population), the matrix will not be symmetrical, because the risk groups are not equirespondent.
- The dominance of the diagonal (see Definition 3.5) indicates the degree of assortative mixing. In general, members of risk groups tend to mix among each other. In fact, for behaviorally defined risk groups, interacting with a high-risk individual is part of the way high-risk behaviors are defined (e.g., needle sharing in the context of IVDU). The degree to which the diagonal is dominant indicates the degree of assortative mixing.
- The relative values of b's columns indicate the overall "spreading potential" of the pathogen. The out-of-group spreading of a risk group indicates the exposure hazard to which a compartment's members of that group expose the other groups.

Definition 3.4 (Equiresponse). The risk groups $P$ and $Q$ are said to be equirespondent to the infection in question if $\beta_{P, Q}=\beta_{Q, P}$ (i.e., if the likelihood of acquiring infection upon interaction is the same, regardless of which of the equirespondent risk groups an individual belongs to).

Definition 3.5 (Diagonal dominance). A matrix $\mathbf{b}$ is diagonally dominant if for all $i, j, \sum_{i \neq j}\left|\mathbf{b}_{i, i}\right| \geq\left|\mathbf{b}_{i, j}\right|$.

### 3.1.2.2 Coupled dynamics in risk-heterogeneous models

Infectious processes in risk-heterogeneous models go through three distinct phases, as shown in Fig. 3.2:

1. Initially (1), the proportions of the model are driven by the initial distributions of high- and low-risk individuals within the initially infected population.
2. In the next period (2), the number of infected individuals rises exponentially.
3. In the asymptotic phase (3), the model converges on the endemic equilibrium $\lim _{t \rightarrow \infty} I(t)$.

During the second phase, both risk groups follow the same dynamics, determined entirely by $\mathfrak{R}_{0}$. The risk groups in this state are said to be coupled (or, in some texts, such as Keeling and Rohani [39], slaved).

![](https://cdn.mathpix.com/cropped/2024_06_11_7acef27a50e7509ebe89g-06.jpg?height=701&width=1059&top_left_y=225&top_left_x=193)

Figure 3.2 Solutions for the infectious compartment in a SIR model with two risk classes. The stages of the model's evolution are noted above the plots.

### 3.1.3 $\Re_{0}$ for risk-heterogeneous populations

As we have seen, $\mathfrak{R}_{0}$ determines the dynamics in the coupled phase of the infection's evolution. However, unlike in previous models, there is not a single value of $\beta$, and hence, of $\Re_{0}$ (recall that $\Re_{0}=\frac{\beta}{\gamma}$ ). Consequently, we will have to adjust our calculation of $\Re_{0}$.

During the coupled phase, $\Re_{0}$ is driving the dynamics of both $I_{H}$ and $I_{L}$ :

$$
\begin{align*}
I_{H}(t) & \propto e^{\Re_{0} t} \\
I_{L}(t) & \propto e^{\Re_{0} t} \tag{3.4}
\end{align*}
$$

Note that because of the coupling, $\mathfrak{R}_{0}$ is the same for both risk groups.

Given the WAIFW matrix and population proportions of each risk group, as well as reasonable approximations for $\gamma$, we can use symbolic computation followed by numerical evaluation to characterize the dynamics of the infectious process during the coupled phase (see Computational Note 3.1).

## Computational Note 3.1 Calculating the $\mathfrak{R}_{0}$ of complex stratified models

Calculating the $\Re_{0}$ of a stratified model, even one apparently quite simple, can lead to extremely complex (and mathematically ugly) results. Symbolic computation with later evaluation can be used in this situation with great effect.

Consider the system described in (3.2). We will primarily consider the infected subsystem, i.e., $I_{H}$ and $I_{L}$.

Let us first define our variables:

```
import numpy as np
from sympy.interactive.printing import init_printing
init_printing(use_unicode=True, wrap_line=True)
from sympy.matrices import Matrix
from sympy import symbols
I_H, I_L, beta_HH, beta_HL, beta_LH, beta_LL, gamma_H, gamma_L,
    n_H, n_L =
    symbols("I_H I_L beta_HH beta_HL beta_LH beta_LL \
        gamma_H gamma_L n_H n_L")
```

Next, we need to define the ODE of the infectious system as two column vectors: one containing the compartments and one containing their definitions.

```
infectious_system = Matrix(np.array([I_H, I_L]).T)
d_Is = Matrix(np.array([(beta_HH * n_H - gamma_H) * I_H \
        + (beta_HL * n_H) * I_L,
        beta_LH * n_L * I_H \
        + (beta_LL * n_L - gamma_L) * I_L]).T)
```

Now, we can take the Jacobian of the compartments to get the matrix of coefficients:

```coeffs = d_Is.jacobian(infectious_system)```

$$
\left[\begin{array}{cc}
\beta_{H H} n_{H}-\gamma_{H} & \beta_{H L} n_{H} \\
\beta_{L H} n_{L} & \beta_{L L} n_{L}-\gamma_{L}
\end{array}\right]
$$

We could, technically, proceed entirely symbolically from here onwards. However, the number of variables means that the resultant expression will be inevitably rather messy. Fortunately, SymPy allows us to replace symbols with actual values using the . subs method, which takes a dictionary of symbol keys paired to the values that are to be substituted for them. We will be using a rather reasonable WAIFW matrix, namely

$$
\mathbf{b}=\left(\begin{array}{cc}
10 & 0.5 \\
0.5 & 2
\end{array}\right)
$$

Alongside that, we will assume that $20 \%$ of the population belonging to the high risk group, and we will also assume that both groups have the same removal rate of 0.05 . We create the matrix $J$ through substitution using . subs on the Jacobian created in the previous step:

```
J = coeffs.subs({beta_HH: 10,
    beta_HL: 0.5,
    beta_LH: 0.5,
    beta_LL: 2,
    n_H: 0.2,
    n_L: 0.8,
    gamma_H: 0.05,
    gamma_L: 0.05})
```

$\left[\begin{array}{cc}1.95 & 0.1 \\ 0.4 & 1.55\end{array}\right]$

Now, we can calculate an approximation of $\Re_{0}$ for the coupled period. This is best accomplished by creating a list of the absolute values of the spectrum (returned by J.eigenvals()) and taking the maximum:

```
R_0 = max([abs(i) for i in J.eigenvals()])
>> 2.03284271247462
```

Thus we can now characterize the infectious dynamics during the coupled phase as proportional to the term $e^{\Re_{0} t}$.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder /ch03/stratified_r0.

The computational approach outlined above is particularly useful, because it gives us insights about the eventual fate of the pathogen in the population. $\Re_{0}$ alone does not determine the dynamics of the whole disease process, especially not the transient interval in the beginning, which is largely governed by initial population ratios and, in real-world use cases, stochasticity, but it does determine the long-term fate of the infectious process. As such, if the overall $\mathfrak{R}_{0}$ as calculated using the method in Computational Note 3.1 is below zero, the infection will eventually die out. This can be accelerated through targeted interventions, in particular vaccinating the strata that have a higher stratum-wise $\Re_{0}$.

### 3.1.4 Superspreading and supershedding

During the SARS outbreak, it was observed that a relatively small number of infected persons were responsible for a relatively large number of secondary cases. In epidemiology, groups of individuals with a significantly higher likelihood to infect others are called "supershedders," although the term does not really have a settled definition. For instance, the WAIFW matrix

$$
\mathbf{b}_{1}=\left(\begin{array}{ccc}
10 & 3 & 1  \tag{3.5}\\
9 & 3 & 2 \\
9 & 2 & 3
\end{array}\right)
$$

suggests supershedding by the first compartment (first column). Note that supershedding merely indicates higher likelihood to transmit the disease, not to acquire it. Supershedding is primarily a biological phenomenon and only relatively weakly behavioral.

On the other hand, there also exist individuals who are both more likely to be infected and to pass on infection. Consider the WAIFW matrix

$$
\mathbf{b}_{1}=\left(\begin{array}{ccc}
10 & 7 & 8  \tag{3.6}\\
9 & 3 & 2 \\
9 & 2 & 3
\end{array}\right)
$$

which indicates that people in the first compartment are more likely not only to pass on the infection but also to be infected in the first place. We call these individuals superspreaders.

Lloyd-Smith et al. [93] define superspreading in a statistically rigorous way as instances drawn from the right-hand tail of a continuous probability distribution centered around $\mathfrak{R}_{0}$. In other words, there will be individuals who are significantly more likely to spread the infection, just as there will be individuals who are significantly less so. The latter, of course, generally escape epidemiological notice. An often used metric of superspreading likelihood is the $t_{20}$ proportion, which plots the part of transmission that is attributable to the most infections $20 \%$ of cases. As Lloyd-Smith et al. [93] have shown, the often-cited Pareto " $20 / 80$ " relationship, where $20 \%$ of cases cause $80 \%$ of transmission [94] does not universally hold. In other words, the dispersion parameter of the probability distribution from which an individual's propensity to cause secondary cases is drawn varies from disease to disease and outbreak to outbreak. Table 3.1 shows the $t_{20}$ values of a number of outbreaks, illustrating the wide disparity that exists between diseases in their potential to cause superspreading events. Interpretation and discussion of "superspreading" must therefore be in light of the limitations, both definitional and practical, of the concept.

Table 3.1 $t_{20}$ of some infectious diseases at vaccination rates, based on Lloyd-Smith et al. [93].

| Pathogen | \% vaccination level | $\boldsymbol{t}_{\mathbf{2 0}}$ |
| :--- | :--- | :--- |
| SARS | $0 \%$ | 0.88 |
| Measles | $95 \%$ | 0.82 |
| Smallpox | $20-70 \%$ | 0.74 |
| Smallpox | $80 \%$ | 0.71 |
| Monkeypox | $70 \%$ | 0.62 |
| Pneumonic plague | $0 \%$ | 0.47 |
| Hantavirus | $0 \%$ | 0.45 |
| ZEBOV | $0 \%$ | 0.34 |

Practice Note 3.3 Superspreaders and superspreader events

There is an unhelpful tendency to regard superspreaders and events where superspreading has occurred as anomalies out of the ordinary. This contributes relatively little to our understanding of infectious dynamics and is bound to exacerbate the stigmatization of individuals, as it has, e.g., during the early years of AIDS, when much sensationalistic and unjustified blame was laid at the feet of early HIV patient Gaëtan Dugas (see McKay [95]). Rather, superspreading is one "tail" of a distribution prominent mainly because it is noticeable: statistical models predict that there are generally an equal number of "greatly inferior spreaders" who are particularly ineffective in spreading the illness. The significance of "superspreading" therefore is peculiar to the pathogen, the population and a wide range of other factors.

It should not be assumed, absent evidence, to apply to any pathogen. Nor is superspreading particularly predictable. While all things being equal, events with close physical proximity and no barrier precautions are more likely to become superspreader events, there exists no scientifically sound methodology to extrapolate the likelihood of this occurring purely from the number of attendees or the manner an event is organized. The heavy-tailed distribution of superspreading indicates that the right (or, rather, wrong) person at the right time can turn an intimate family gathering into a superspreader event. It is therefore crucial not to equate superspreading with large-scale events and be aware of the superspreading risk at small events. Superspreaders can create vast numbers of secondaries, even without meeting larger groups of people at any point. Thus avoiding mass gatherings, though a sensible precaution amidst an epidemic, is no guarantee against falling victim to superspreading.

When discussing superspreading, infectious disease modelers should refrain from assigning blame or engaging in moral discourse. Superspreading is frequently not within the patient's control, and especially amidst an epidemic, branding individuals as particularly infectious or even reckless may elicit hostil-
ity, exclusion, and even violence. Many superspreader events continue to elude a clear causal explanation, and approaching the issue from a clear scientific perspective is paramount, as is avoiding stigma and steering clear of moral discourse.

### 3.1.5 Treatment effect

For many infectious diseases, treatment is largely supportive. This is the case in particular for those viral diseases that do not have a specific antiviral therapy. For other diseases, treatment may affect transmission rates. In those cases, it may be important to account for the effect of treatment as a separate compartment.

We consider a hypothetical treatment that, upon initiation, reduces transmission by a given percentage. We reflect this in the value $\beta_{T}$. Furthermore, treatment lasts $\tau_{T}$ days, after which patients are cured (recovered). For the sake of simplicity, we will assume furthermore that this treatment has a uniform effect and perfect effectiveness. Fig. 3.3 illustrates this model structure.

This gives us the system of ordinary differential equations outlined in Eq. (3.7).

$$
\begin{align*}
& \frac{d I}{d t}=\underbrace{\beta S I}_{\text {from untreated}}+\underbrace{\beta _{T} S T}_{\text {from treated }}-\underbrace{\gamma I}_{\text {untreated}}-\underbrace{\theta I}_{\text {treated}}, \\
& \frac{d T}{d t}=\underbrace{\theta I}_{\text {treatment influx }}-\underbrace{\frac{1}{\tau_{T}} T}_{\text {treated recoveries }},  \tag{3.7}\\
& \frac{d R}{d t}=\underbrace{\gamma I}_{\text {recovery }}+\underbrace{\frac{1}{\tau_{T}} T}_{\text {treated recoveries }} .
\end{align*}
$$

![](https://cdn.mathpix.com/cropped/2024_06_11_7acef27a50e7509ebe89g-11.jpg?height=415&width=708&top_left_y=1603&top_left_x=415)

Figure 3.3 A SIRT model of differential treatment. $\theta$ is the rate at which patients are treated. $\beta_{T}$ is the value of $\beta$ specific to the treated.

|  | $G$ | $H$ |
| :---: | :---: | :---: |
| $G$ | 10 | 5 |
| $H$ | 0 | 6 |

Figure 3.4 WAIFW matrix with hospitalized and community transmission. $G$ denotes the general population, $H$ denotes the hospitalized population. Dark red indicates community transmission, dark blue denotes nosocomial transmission. Since only infected persons are in the hospitalized compartment, there is no $G \rightarrow H$ transmission.

It emerges from this model that a higher rate of treatment, as well as a higher treatment efficacy $\theta$, can suppress the overall intensity of an outbreak.

A variant of this model is the delayed-effect treatment model. This model accounts for the fact that initiation of therapy does not immediately stop infectiousness. How long this period is, and consequently how meaningful it is to model such a period, depends both on the disease and the treatment. Bactericidal antibiotics typically result in a faster suppression of infectiousness than bacteriostatic agents, and some diseases have significantly longer post-treatment infectious periods than others.

### 3.1.6 Hospitalization

Where a part of infectious cases are hospitalized, the transmission dynamics change. Hospitalized cases have relatively few interactions with the general population, and as a consequence, the two main routes of transmission are within the general population and within the hospitalized population (nosocomial transmission). Fig. 3.4 shows a typical WAIFW matrix for such a scenario.

- The general population is usually relatively more likely to transmit (community transmission) than in-hospital transmission (nosocomial transmission). There are some exceptions to this assumption, however: some pathogens are relatively more frequent in healthcare settings than "in the wild." The classic example is, of course, methicillin-resistant Staphylococcus aureus (MRSA).
- Nosocomial spread tends to be lower than spread in a general population: patients are often confined spatially, to wards or treatment units. Indeed, this is largely the governing principle in the organization of SITTUs (severe infectious temporary treatment units) and Ebola treatment units (ETUs) [96].
- $H \rightarrow G$ spread involves transmission from hospitalized individuals to the general population who come into contact with them. By far, the largest category of $H \rightarrow G$ spread is infection of healthcare workers. The COVID-19 pandemic has highlighted the risk healthcare workers are exposed to in the course of their work, and their contacts with the community in turn can spark off tertiary chains of transmission.

Hospitalization models can, of course, be combined with treatment models. In recent years, especially in the context of the COVID-19 pandemic, multitiered hos-
pitalization models have also been widely used. These distinguish between patients by level of care, e.g., ICU, medical wards, and ER/urgent care. Such models are useful to chart healthcare utilization and remaining capacity. For this reason, models of hospitalization are often useful, even where only a small fraction of individuals suffering from a particular infectious disease ever seek care or are hospitalized.

### 3.1.7 Vulnerability estimation from WAIFW matrices

A vulnerability score is an individual metric of a particular population's risk relative to others. With other factors, a vulnerability score might form part of a vulnerability index, an overall estimate of a population's risk. For instance, during the COVID-19 pandemic, the pandemic vulnerability index (PVI) was used to aggregate risk from infectious dynamics (number of cases), public health interventions (social distancing and testing), interaction factors (population density), and exogenous variables (air pollution, comorbidities) [97]. In the WAIFW matrix, the $n$-th row represents the transmission risk of the $n$-th stratum from all strata (including itself). We will call this the stratal exposure of the $n$-th stratum given the WAIFW matrix $\mathbf{b}$.

Definition 3.6 (Stratal exposure). The stratal exposure of the $n$-th stratum, given the $m \times m$ WAIFW matrix $\mathbf{b}$, denoted $\mathcal{E}_{n}(\mathbf{b})$, is the sum of the $n$-th row of $\mathbf{b}$, i.e.,

$$
\mathcal{E}_{n}(\mathbf{b})=\sum_{j=1}^{m} \mathbf{b}_{n, j}
$$

We can now represent each stratum's risk score as the fraction

$$
\frac{\mathcal{E}_{n}(\mathbf{b})}{\sum_{k=1}^{m} \mathcal{E}_{k}(\mathbf{b})}
$$

This is the proportionate share of the overall risk that the $n$-th stratum is exposed to.

### 3.2 Continuous and semicontinuous heterogeneities

Some heterogeneities are discrete; for instance, a person may or may not engage in intravenous drug use. On the other hand, heterogeneities may also be continuous. Consider, for instance, the number of distinct sexual partners per unit time. This may take any nonnegative real value. Clearly a higher number of distinct sexual partners puts one at a higher risk, statistically speaking, of sexually transmitted infections. However, this may not be particularly easy to model. In practice, three approaches have emerged: semidiscrete heterogeneities, discretization, and continuous modeling. Discretization is by far the most widely used method in the computational realm. Many continuous variables are amenable to discretize modeling, and the most frequently used continuous variable, age, is particularly so.

### 3.2.1 Case study: age-dependent transmission heterogeneities

Age is a crucial factor in epidemiology, because it mediates a range of factors that affect infectious processes in populations.

Age affects mixing affinity. In assortativity of subpopulations, the rule "like attracts like" holds true. Most people spend a considerable part of their time with others who are, roughly, within the same age group. A high school student's time away from the family home will be spent almost entirely with others who are within a few years' of their age. Moreover, age mediates behaviors and social interactions: young children spend relatively little time interacting with others, and reaching the age of mandatory schooling (typically around the 6th year of life) rapidly increases one's number of social encounters. Departure from the active workforce, as is typical towards the 6th to 7 th decade of life in Western societies, has the reverse effect.

Age also affects immune response, however, and consequently, the likelihood that an infection will lead to transmission. The very young and the very old are less likely to mount robust immune responses to a pathogen, and consequently more likely to suffer prolonged illness (decreasing $\gamma$ and increasing the mean infectious period). They are also less likely to have effective immunity; some children may be too young to immunize, and a reduced immune response is common among the elderly and is addressed, e.g., by using vaccines that are more immunogenic, such as adjuvanted influenzavirus vaccines. Meanwhile, young children are often less able to perform the fundamental hygiene behaviors that keep older humans healthy.

### 3.2.2 Semidiscrete heterogeneities

The power (and beauty) of computational epidemiology is that it can leverage computation to easily solve what would otherwise be quite difficult. Consider the simulated network of sexual contacts created by Rocha, Liljeros, and Holme [98].

This simulation comprises 50,632 sexual encounters between over 16,000 simulated individuals, whose number of distinct sexual partners ranges from one to 615 . We could, of course, stratify this into a number of sexual risk classes. However, we may be able to do better if we consider every person's degree (the number of distinct individuals they are connected to) as a risk stratum of its own.

The problem is, of course, that would yield a 149-by-149 sized WAIFW matrix, which is unwieldy to manage at the best of times. Fortunately, we do not need to. We can compute the WAIFW matrix for a vast problem space quite easily based on empirical data.

## Practice Note 3.4 Patient zero

"Patient zero" is one of the most widely known terms of epidemiology, which is startling, in view of the fact that epidemiologists do not use it, the correct term being "index case." In fact, its origins lie in a report on a sexual contact
network in the early days of the HIV/AIDS pandemic, included in this book as Fig. 2.24 [78]. This study denoted the node in the middle of the transmission network as "O," since he had a number of sexual contacts in California but was out-of-state (hence "O"). Through a misreading, "O" became "zero," and linked the tragic fate of a young man to a perception of being the "source" of HIV in America.

Nothing could be further from the truth. In fact, the Canadian flight attendant Gaëtan Dugas, the person behind the moniker, was neither an extraordinarily prolific spreader of HIV, nor a particularly early case. A phylogenetic study by Worobey et al. conclusively disproves the claim that Dugas was a "first" in any sense [99]. In fact, the numbering is not in temporal order, but rather order of receiving reports from state health agencies. The alleged "zero" was, in fact, the fifty-seventh reported case [99]. And a decade and a half prior to Auerbach et al.'s 1984 paper, a 15 -year-old male has succumbed to what today is rather unambiguously considered to be the first case of AIDS in the United States [100].

The lesson of Patient "Zero" is that networks are rarely comprehensive. The networks we examine are often subsets of larger networks, and thus notions of origin and centrality are often limited to this subset of data, rather than being reflective of wider realities.

We assume that $\mathbf{b}_{i, j}=\frac{\mathbf{M}_{i, j}}{n_{i} n_{j}}$, where $\mathbf{M}$ is the degree mixing matrix, that is, $M_{i, j}$ is the number of individuals of the $i$ th degree who are connected to an individual of the $j$ th degree. Note that our matrix does not include compartments that have no members. Therefore the $i$ th column or row might not necessarily denote degree $i$, but rather the $i$ th in the ascending list of degrees. The computational approach to this is outlined in Computational Note 3.2.

## Computational Note 3.2 Calculating the mixing matrix from a contact network

In this computational example, we will be using networkx, a widely used Python package for network analysis, with the data set from Rocha, Liljeros, and Holme [98]. This data set is available as a CSV file as supporting information (S1) to the article, which can be read into NetworkX by first reading it into a Pandas data frame (using the pd.read_csv function), then creating a graph object:

```
import pandas as pd
import numpy as np
import networkx as nx
df = pd.read_csv("pcbi.1001109.s001.csv",
    skiprows=24,
    header=None,
    sep=";")[[0, 1]]
df = df.rename(columns={0: "F", 1: "M"})
n = nx.convert_matrix.from_pandas_edgelist(df,
    source="F",
    target="M",
    create_using=nx.MultiGraph)
```

Now that we have our graph object $n$, we can determine the two parts of the matrix b: the mixing matrix (numerator) and the outer product of the number of individuals in each of the "risk groups," i.e., the number of nodes by the number of their sexual partners.

We calculate the mixing matrix using NetworkX's built-in functionality:

```
mixing_matrix = nx.degree_mixing_matrix(n, normalized=False)
```

And we calculate the sizes of the risk groups by counting distinct values of sexual encounters (i.e., the degree list of the graph $n$ ):

```
number_by_degree = pd.DataFrame(list(n.degree),
    columns=["id", "degree"]).\
    groupby("degree").\
    count().\
    rename(columns= {"id": "count"})
```

Now, we can obtain our matrix b by dividing the mixing matrix by the outer product:

betas = mixing_matrix / np.outer(number_by_degree, number_by_degree)

Because this uses NumPy's built-in vector arithmetic, it is remarkably fast; results are in a few seconds.

This example illustrates how we can gain insights from very complex models. Transmission networks are particularly important for STIs and for contact tracing in the initial phases of an outbreak. The $\mathbf{b}$ matrix we obtained can be used to parameterize any of the compartmental models we have discussed previously, with highly granular and individualized data.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder /ch03/contact_waifw.

The calculation of a mixing matrix with hundreds of classes illustrates a profound point about computational methods: for large problem sizes that would be difficult to

![](https://cdn.mathpix.com/cropped/2024_06_11_7acef27a50e7509ebe89g-17.jpg?height=1037&width=1009&top_left_y=224&top_left_x=260)

Figure 3.5 WAIFW matrix for the simulated network of sexual contacts in Rocha, Liljeros, and Holme [98] stratified by number of sexual partners.

tackle with analytical methods, computational approaches can provide highly detailed and accurate models. (See Fig. 3.5.)

### 3.2.3 Discretized continuous heterogeneities

In some cases, there is a meaningful transition in terms of a property to stratify. An example is age: individuals only age in one direction, that being forward. It is possible, especially if age groups typically mix only between themselves as is the case in the context of pediatric infectious disease in school-age children, to create a model that discretizes the continuous heterogeneity of age.

Unlike previous discrete models, a crucial difference is that we have to account for "natural" transitions between age groups. Consider, for instance, a Sixth Form house at a boarding school (Sixth Form comprises Upper Sixth and Lower Sixth, corresponding to years 12 and 13, in the British educational system). Pupils in the Lower Sixth typically associate with others in the Lower Sixth, and vice versa. Nevertheless, there is some interaction between them, being under the same roof, and consequently
the mass action term for each group will have to include infectious individuals from both age groups. We account for natural aging-out (transitioning from Lower to Upper Sixth) by the rate $\nu_{L}$ and additions to the population (enrollment) by $\mu$, noting that the two tend to be largely equal.

We can now extend the SIR model with heterogeneous risks (see Subsection 3.1.2) with age progression. (3.8) describes such a model, for the rate of aging $\nu$ (the rate of transitioning from Lower to Upper Sixth), a population growth rate $\mu$ and a population leaving rate $\theta$ (which are typically the class size over a year).

$$
\begin{align*}
& \frac{d S_{L}}{d t}=-\overbrace{S_{L}(\overbrace{\beta_{L, L} I_{L}}^{L \rightarrow L}+\overbrace{\beta_{L, U} I_{U}}^{L \rightarrow U}}^{\text {mass action }}-v_{L} S_{L}+\mu\left(S_{L}+I_{L}+R_{L}\right), \\
& \frac{d S_{U}}{d t}=-\underbrace{S_{U}(\underbrace{\beta_{U, U} I_{U}}_{U \rightarrow U}+\underbrace{\beta_{U, L} I_{L}}_{U \rightarrow L})}_{\text {mass action }}+v_{L} S_{L}, \\
& \frac{d I_{L}}{d t}=\underbrace{S_{L}\left(\beta_{L, L} I_{L}+\beta_{L, U} I_{U}\right)}_{\text {new infections }}-\underbrace{v_{L} I_{L}}_{\text {aging }}-\underbrace{\gamma I_{L}}_{\text {recovery }}, \\
& \frac{d I_{U}}{d t}=\underbrace{S_{U}\left(\beta_{U, U} I_{U}+\beta_{U, L} I_{L}\right)}_{\text {new cases }}+\underbrace{v_{L} I_{L}}_{\text {aging }}-\underbrace{\gamma I_{U}}_{\text {recovery }},  \tag{3.8}\\
& \frac{d R_{L}}{d t}=\underbrace{\gamma I_{L}}_{\text {recoveries }}-\underbrace{v_{L} R_{L},}_{\text {aging }} \\
& \frac{d R_{L}}{d t}=\underbrace{\gamma I_{U}}_{\text {recoveries }}-\underbrace{\theta R_{U},}_{\text {graduation}}.
\end{align*}
$$

## Computational Note 3.3 A simple age-heterogeneity model

In this computational example, we will use the tried and true methods from previous applications to solve the scenario from (3.8). For this, we will use the WAIFW matrix

$$
\mathbf{b}=\left(\begin{array}{ll}
8 & 4 \\
4 & 8
\end{array}\right)
$$

The symmetricity of the WAIFW matrix suggests that there will largely be a coupled behavior, but the differential equations from (3.8) indicate that a lot of the dynamics are highly dependent on population change. Because all popula-
tion growth initially accrues to the Lower Sixth, and because these are deemed immunologically naive, the relative proportion of recovered will decrease over time as the population grows.

We begin by initializing our parameters $\mu=0.01, v=0.02$ and $\theta=0.015$, with $\gamma=\frac{1}{20}$. Next, we implement the differential equations above as the differential function. For convenience, this functional definition tracks recovered groups separately for Upper and Lower Sixth, but of course there is no reason why they could not be considered jointly.

```
def deriv(t, y, beta, gamma, mu, nu, theta):
    S_L, I_L, S_U, I_U, R_U, R_L = y
    dSLdt = - S_L * (beta[0] * I_L + beta[1] * I_U) - nu * S_L \
        +mu*(S_L + I_L + R_L)
    dSUdt = - S_U * (beta[2] * I_L + beta[3] * I_U) + nu * S_L \
    dILdt = S_L * (beta[0] * I_L + beta[1] * I_U) - nu * I_L \
        gamma * I_L
    dIUdt = S_U * (beta[2] * I_L + beta[3] * I_U) + nu * I_L \
        gamma * I_U
    dRLdt = gamma * I_L - nu * R_L
    dRUdt = gamma * I_U + nu * R_L - theta * R_U
    return dSLdt, dILdt, dSUdt, dIUdt, dRUdt, dRLdt
```

Now, we can solve this as an ordinary initial value problem.

```
res = solve_ivp(fun=deriv,
    t_span = (0, 100),
    y0=y_0,
    args=(beta, gamma, mu, nu, theta),
    max_step=1,
    method="BDF")
```

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder /ch03/age_differential_sir.

As Fig. 3.6 shows, the proportion of individuals who are immune in the Lower Sixth is gradually decreasing, while the proportion of individuals who are immune in the Upper Sixth grows steadily. The reason behind that is that all population growth accrues to $S_{L}$, since the only way to access the Upper Sixth compartments is to go through the Lower Sixth. Consequently, the Lower Sixth stratum is fed a constant stream of immunologically naive individuals.

![](https://cdn.mathpix.com/cropped/2024_06_11_7acef27a50e7509ebe89g-20.jpg?height=699&width=1041&top_left_y=226&top_left_x=209)

Figure 3.6 Solutions of the SIR model with age strata from Eq. (3.8).

On the other hand, the influx into the Upper Sixth comes, of course, from the Lower Sixth, a proportion of whom have been exposed to the pathogen before, and are thus immune. This highlights a crucial point, which we will discuss in detail in Chapter 6: early acquisition of immunity reduces overall time-integrated cases (i.e., the total number of cases at the end of the epidemic) significantly. This is the reason behind vaccinating as early as it is biologically sensible. Not only will that individual be protected but, as long as the vaccination provides enduring immunity, they will enter later age strata not as susceptibles but individuals with immunity. Since the driving dynamic of most outbreaks is the product of infected and susceptible individuals (the mass action term), they will not participate in the infectious dynamics in later age strata and will not "fuel" the susceptible pool the pathogen requires for its survival. Or, to put it in a somewhat more personifying way, the pathogen will have one less person to infect at its disposal. Thus effects compound over time, and vaccinating a single individual early enough can protect many others from disease over time.

### 3.2.4 Inference of mixing matrices

Whereas WAIFW matrices tell us about who acquires infections from whom, a mixing matrix tells us about who encounters whom. The reason why mixing matrices are considered separately, especially where it comes to age-stratified models, is that age mediates many of our associative behaviors as humans.

Mixing matrices can be obtained empirically, typically at a rather shocking investment of time, treasure, and manpower. The best known such epidemiological contact survey was POLYMOD, which sampled populations in eight European countries [101]. Since then, the methodology of POLYMOD has become a gold standard,
and it touched off a series of POLYMOD-like social contact surveys [102]. Gratifyingly, POLYMOD has proven to be quite amenable to extrapolative projection, as Prem, Cook, and Jit [103] have demonstrated by projecting it to most of the countries on the planet. This is, of course, much less expensive, but also somewhat less accurate, than performing the painstaking social contact research that gave us POLYMOD.

An alternative to empirical studies is the estimation of mixing matrices from synthetic populations. A synthetic population is essentially a population where individuals are drawn from distributions elicited from known data. This is greatly facilitated by the increasing availability of microdata, which gives us a household-level insight into populations. The approach adopted by Mistry et al. [104] is an excellent model of synthetic generation of high-resolution mixing matrices. Mistry et al.'s approach proceeded in three steps:

- Create mixing matrices for different contexts of mixing, e.g., work, school, etc.
- Create simulated assortativities, e.g., simulated households, schools, workplaces.
- Analyze these simulated assortativities to approximate the likelihood that an encounter by an individual of age $a_{i}$ will be with an individual of age $a_{j}$.

This methodology commends itself in two principal ways. First, though identifying distributions in a Bayesian approach then performing adaptive sampling for conditional probabilities is arguably the most elegant way, a good approximation of reality can be obtained by just sampling data as available. Second, such simulated assortativities are easy to build with adequate microdata.

Considering, for instance, family-based assortativities, the approach of Mistry et al. [104] proceeded by obtaining census data on households, and adaptive sampling. Thus we obtain the household size from the unconditional probability distribution of household sizes. The age of the head of household then follows from the conditional distribution given the household size. The age of the head of household's spouse and the number of children, follows from the head of household's age. The age of the children is then drawn from a distribution conditioned on the age of each of their parents. These figures can be obtained quite easily by filtering the data set to within a given tolerance band for ages, then drawing random samples. These amounts, in Bayesian terms, effectively to a uniform prior.

The advantage of more sophisticated Bayesian frameworks is the ability to calibrate the multivariate distributions, from which we draw the various conditional samples (e.g., age of head of household given family size) against empirical data, such as that obtained by POLYMOD. Nevertheless, as Computational Example 3.4 shows, it is possible to get a relatively good approximation of the mixing matrix at a good enough speed (thousands of simulated households per second of simulation time on commodity hardware) to be able to model nation-level processes. Such models can be arbitrarily expanded by introducing multiple different layers that together make up the mesoscale likelihood:

- Account differently for individuals in different settings. The US census microdata, for instance, identifies individuals living in group settings (institutionalization, incarceration). The example of COVID-19 has shown that the spatial-population dynamics and often overcrowded situations in settings of incarceration result in
higher incidence and mortality of infectious disease [105]. The age mixing dynamics of a prison, which by definition separates an individual from their family, perturb the ordinary, household/family-based age-assortativity model.
- The overall mixing matrix is typically a linearly weighted combination of the various matrices-representing work, school, home, and so on-by a weighting factor that represents partly the time spent in that setting, and partly the significance of that setting to pathogens. It also highlights the intensity of mixing: a 14-year-old index case may spend his school days among other students in the same range.
- Certain mixing processes are very stratal. We see these as relatively solid squares on the mixing matrix. To infectious disease modelers who have been dealing with age-stratified models, the diagonally successive $4 \times 4$ blocks that mark out the four-year segments in which much of the US divides school years (primary, middle, high) must be quite familiar. In England, the segregation is quite different: Sixth Formers (comparable to US 11th and 12th grade) typically live apart from the rest, but especially in boarding schools, lower grades constitute a single assortative mixture.


## Computational Note 3.4 Inference of mixing matrices

In this Computational Note, we will be estimating mixing matrices through a population simulation approach derived from Mistry et al. [104]. This approach is generally quite painstaking, and for this reason, only key elements of code will be reproduced here. The full code is, of course, reproduced in the book's companion Github repository (see link at the end of the Computational Note), including the parameters to obtain source data.

The general approach by which we create our synthetic contact matrices is to create synthetic households, schools, and workplaces. From this, we calculate a contact matrix by determining the absolute abundance of contacts. For a single instance of a household, school, or workplace $S$, which we represent as a vector of individual ages (with each element being one simulated individual), the absolute abundance of contacts is a (symmetric) matrix $\mathbf{C}$ defined as

$$
\begin{equation*}
\mathbf{C}_{i, j}=\frac{1}{|S|-1} \sum_{m=1}^{S}\left[S_{m}=i\right]\left(\sum_{n=1}^{S}\left[S_{n}=j\right]-\delta_{i, j}\right) \tag{3.9}
\end{equation*}
$$

where $\delta_{i, j}$ is the Kronecker delta function [104]. We obtain the total abundance of contacts for a given number of simulated instances of the setting by adding up their matrices. From this, we obtain the mixing probability matrix

$$
\begin{equation*}
\mathbf{M}_{i, j}=\sum \frac{\mathbf{C}_{i, j}}{N_{i}} \tag{3.10}
\end{equation*}
$$

where $N_{i}$ is the number of $i$-aged individuals in the sample. Thus a value of $\mathbf{M}_{i, j}$ is the per capita probability that an individual of age $j$ will encounter an individual of age $i$. This is, of course, asymmetrical, because it is per-capitalized by reference to the population for each $i$. The example of schools in Fig. 3.7 shows this quite well: the bright band on the bottom results from the fact that for most adults, the vast majority of contacts will be with those of school age (since students outnumber teachers in most cases). Given various simulated settings, we obtain a composite through linear weighting by a scaling vector $\eta$, so that

$$
\begin{equation*}
\mathbf{M}_{\text {composite }}=\sum_{p=1}^{\{\mathbf{M}\}} \eta_{p}\{\mathbf{M}\}_{p} \tag{3.11}
\end{equation*}
$$

where $\{\mathbf{M}\}$ is the set of the component matrices corresponding to a setting (e.g., households, schools, and workplaces) ordered correspondingly to their scaling coefficient in $\eta$.

$\eta$ can be ascertained by optimization with respect to a reference matrix $\mathbf{M}^{\mathrm{ref}}$ and a distance metric. The Canberra distance metric, as used by Mistry et al. [104], is a particularly attractive target of optimization. We intend to ascertain $\eta$ so as to minimize the Canberra distance,

$$
\begin{equation*}
\sum_{i=1}^{m} \sum_{j=1}^{n} \frac{\left|\mathbf{M}_{i, j}^{\eta}-\mathbf{M}_{i, j}^{\mathrm{ref}}\right|}{\left|\mathbf{M}_{i, j}^{\eta}\right|+\left|\mathbf{M}_{i, j}^{\mathrm{ref}}\right|} \tag{3.12}
\end{equation*}
$$

where $\mathbf{M}^{\eta}$ is a composite matrix, as described in Eq. (3.11) with the linear coefficient vector $\eta$.

To illustrate the methodology of what Mistry et al. [104] called "adaptive sampling," our method of creating synthetic families proceeds as follows:

1. We use census microdata, obtained from IPUMS [106], to calculate the distribution of household sizes. The American community survey (ACS) product of the United States census uses the ```FAMSIZE``` attribute for family size, which is a good approximation of the household size. We are interested in a single figure per household, and for this reason, we group by ```SERIAL```, the unique identifier assigned to each household, and take the first value (using ```groupby("SERIAL").first()```).
2. Next, we determine the age of the head of household given the family size by filtering the data set to families of the desired size, then sampling the ```AGE``` property.
3. Next, we determine the likelihood of a spouse, given the age of the head of household: we filter all heads of household of the age from the previous step, and join their spouse's age (a spouse would have a ```RELATE``` property of 2 and share the head of household's ```SERIAL```). This yields $\mathrm{NaN}$ if the individual has no spouse, and the spouse's age otherwise. Thus it acts as both a way of
determining whether the head of household would have a spouse, and what their age would be.
4. We determine the remaining number of individuals to be allocated by subtracting 1 (if there is no spouse) or 2 (if there is) from the household size.
5. We also determine, given the age of the head of household, the size of the household and the age of the spouse, the likelihood that any other person in the family is a child, rather than another relative (e.g., parents, siblings, more distant relatives). We do so by filtering the microdata sample to the age of the head of household, to the age of the spouse, and to families the size of the household from the first step. This gives us $p_{c}$, the probability that a person in the family is a child of the head of household.
6. For each remaining individual to be allocated, if any, we generate a random number between $[0,1]$. If $\operatorname{rand}()<p_{c}$, the new person will be a child. If not, it will be another relative.
7. If the new person is a child, we filter for the age of the head of household and the age of the spouse, and sample the ages of children (```RELATE``` is 3) who are in households with the corresponding head of household's and spouse's age. We do the same for other relatives, except that we sample the ages of other relatives (```RELATE``` is any value other than 1,2 , or 3 ).

In the same vein, we can sample from various other populations, e.g., to determine the faculty age distribution; we can use occupation-filtered census data and determine an age distribution we can sample. In most cases, for sufficiently large data sets, simple sampling of the empirical data, filtered for age conditionals with a tolerance ( $\pm 2$ years tend to give a fairly good approximation), is very fast and allows full population simulations of mid- to large US states and mid-size nations on commodity hardware.

An alternative to simple empirical sampling is to use the observed data to fit multivariate probability distributions, and sample these for the conditional probability. The key difference between these approaches is that whereas the latter is more computationally expensive, it gives "smoother" values towards the edges. If the source microdata does not contain at least one 100 -year-old individual, then there will be no data at all about them at all. The smaller the available microdata set, the stronger the case for fitting multivariate distributions, rather than simply sampling the empirical observations filtered by conditionals.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder /ch03/contact_matrix.

### 3.2.5 Age-dependent continuous heterogeneities

Anderson and May [110] describe a basic model for age-dependent modeling in a compartmental structure. Let $S(a, t), I(a, t)$, and $R(a, t)$ be the proportion of individ-

![](https://cdn.mathpix.com/cropped/2024_06_11_7acef27a50e7509ebe89g-25.jpg?height=1212&width=1008&top_left_y=224&top_left_x=260)

Figure 3.7 Inferred contact matrices for different settings for Virginia. The bottom left figure shows the matrix for the same area estimated by Mistry et al. [104] for comparison. The bottom right figure shows the Canberra distance between the composite from the model described in Computational Note 3.4.

Demographic data on households obtained from IPUMS [106]. Data on schools obtained from the Virginia Department of Education [107]. Data on businesses [108] and number of teachers [109] were obtained from the U.S. Census Bureau. The comparator matrix was obtained from Supplementary Information 1 to Mistry et al. [104].

uals of age $a$ at time $t$, who are susceptible, infectious, or recovered, respectively. We assume that $\beta$ is the same for all age groups, i.e., perfect assortative mixing with equal transmission odds, and that the force of infection $\lambda$ is a pure function of the infectious compartment's size at time $t$, so that

$$
\begin{equation*}
\lambda(t)=\beta \int_{0}^{\infty} I(a, t) d a \tag{3.13}
\end{equation*}
$$

Then, the individual compartments' rates of change will be

$$
\begin{align*}
& \frac{\partial S(a, t)}{\partial t}+\frac{\partial S(a, t)}{\partial a}=-\lambda(t) S(a, t) \\
& \frac{\partial I(a, t)}{\partial t}+\frac{\partial I(a, t)}{\partial a}=\lambda(t) S(a, t)-\gamma I(a, t)  \tag{3.14}\\
& \frac{\partial R(a, t)}{\partial t}+\frac{\partial R(a, t)}{\partial a}=\gamma I(a, t)
\end{align*}
$$

However, as we noted in Subsection 3.2.1, transmission is often age-dependent. This is not only due to the fact that social interactions are not, in fact, perfectly assortative, but rather highly structured with regard to age, but also because of intrinsic differences in both physiology and behavior. Toddlers, for instance, are generally less adept at the application of hygienic measures in their every-day lives than fully grown adults. We therefore generalize the WAIFW matrix concept (see Eq. (3.1)) to a continuous function $\beta\left(a^{\prime}, a\right)$, denoting the transmission coefficient for the interaction between susceptibles aged $a$ with infectious individuals aged $a^{\prime}$ (following the notation by Keeling and Rohani [39]). This allows us to rewrite Eq. (3.13) in an agedependent form, as

$$
\begin{equation*}
\lambda(a, t)=\int_{0}^{\infty} \beta\left(a^{\prime}, a\right) I\left(a^{\prime}, t\right) d a^{\prime} \tag{3.15}
\end{equation*}
$$

Inserting Eq. (3.15) into Eq. (3.14) yields

$$
\begin{align*}
& \frac{\partial S(a, t)}{\partial t}+\frac{\partial S(a, t)}{\partial a}=-S(a, t) \int_{0}^{\infty} \beta\left(a, a^{\prime}\right) I\left(a^{\prime}, t\right) d a \\
& \frac{\partial I(a, t)}{\partial t}+\frac{\partial I(a, t)}{\partial a}=S(a, t) \int_{0}^{\infty} \beta\left(a, a^{\prime}\right) I\left(a^{\prime}, t\right) d a-\gamma I(a, t)  \tag{3.16}\\
& \frac{\partial R(a, t)}{\partial t}+\frac{\partial R(a, t)}{\partial a}=\gamma I(a, t)
\end{align*}
$$

It follows from this that

$$
\begin{align*}
& \frac{\partial S(a)}{\partial t}=-S(a) \int_{0}^{\infty} \beta\left(a, a^{\prime}\right) I\left(a^{\prime}, t\right) d a^{\prime}-\frac{\partial S}{\partial a} \\
& \frac{\partial I(a)}{\partial t}=\int_{0}^{\infty} \beta\left(a, a^{\prime}\right) I\left(a^{\prime}, t\right) d a^{\prime}-\gamma I(a)-\frac{\partial I}{\partial a} \tag{3.17}
\end{align*}
$$

In practice, values for $\lambda(a, t)$ can be obtained from contact tracing data. $a^{\prime}$ and $a$ can be conceptualized as the list of value pairs of each infectious case's age and the age of the newly infected case to whom they have passed on the infection. $\beta\left(a^{\prime}, a\right)$ can then be estimated by fitting a probability distribution over the value pairs. $I\left(a^{\prime}, t\right)$ is equally ascertainable from contact tracing data, typically by estimating the number of cases whose date of initial symptoms has been fewer than $\frac{1}{\gamma}$ days ago. Thus $\lambda(a, t)$
is often quite easy to numerically estimate if a sufficient volume (and accuracy) of contact tracing data is available.

## Practice Note 3.5 To bin or not to bin?

Whereas the method laid out above as to $\lambda(a, t)$ (see Eq. (3.15)) generalizes the WAIFW matrix concept to a continuous function, it does contribute to a degree of additional complexity. In practice, $\beta\left(a^{\prime}, a\right)$ is rarely a smooth distribution. Rather, most values are along the diagonal axis, as noted in Subsection 3.2.1; we spend most of our existence with people relatively close to our own age, especially in the institutional educational context. This is true for interpersonal relationships, too: over a third of American couples in 2017 were less than a year apart in age, and only four in ten were more than three years apart.

This makes creating age compartments or "bins" often preferable to dealing with an irregular age-encounter function, whose approximations may be less accurate. Where there is a clear rationale for age grouping due to interactions, such as for primary, middle, high school, and college-aged individuals (most of whose contacts will come from the same age group), a discrete WAIFW matrix by age groups is likely to yield much better results than numerical approximation of $\lambda(a, t)$.

The best test to determine whether a particular binning by age makes sense is to look at the statistical distributions of values in the WAIFW matrix. A good age structure will result in "tight" estimates of each value within the WAIFW matrix, with a low standard deviation. This is reflective of a homogeneous encounter behavior between the two age groups. It is often useful to look at the $\sigma(\mathbf{b})$ matrix, comprising the standard deviation of each WAIFW matrix element, and delineate age groups in a way that minimizes the grand sum (the sum of every element in a matrix, i.e., $\left.\sum_{i, j} \sigma(\mathbf{b})_{i, j}\right)$.

