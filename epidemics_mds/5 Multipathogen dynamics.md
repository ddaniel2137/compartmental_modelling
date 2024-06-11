# Multipathogen dynamics Competition, cross-immunity, and cosusceptibility 

![](https://cdn.mathpix.com/cropped/2024_06_11_ae648d58b489163f3247g-01.jpg?height=150&width=110&top_left_y=226&top_left_x=1248)


#### Abstract

When a new influenza virus emerges, it is highly competitive, even cannibalistic. It usually drives older types into extinction. This happens because infection stimulates the body's immune system to generate all its defenses against all influenza viruses to which the body has ever been exposed. When older viruses attempt to infect someone, they cannot gain a foothold. They cease replicating. They die out. So, unlike practically every other known virus, only one type-one swarm or quasi species-of influenza virus dominates at any given time. This itself helps prepare the way for a new pandemic, since the more time passes, the fewer people's immune systems will recognize other antigens.


Barry, The Great Influenza: the epic story of the deadliest plague in history, 2005 [144]

In our previous pursuits, we have largely focused on a single pathogen, much to the exclusion of all others. This is a sensible choice when the likelihood of interaction between our pathogen of concern and other pathogens is not particularly significant. Keeling and Rohani [39] note that there is almost always some effect between multiple pathogens that can infect the same organism, a phenomenon they refer to as "interference." This may take place either on a physiological/biochemical level, such as by way of cytokine activation by one pathogen that makes the individual less susceptible to subsequent infection by another in the short term [145]. Alternatively, behavioral factors may be at play: symptomatic illness may reduce an individual's encounter rate, thus reducing the likelihood of infection with another pathogen.

In this chapter, we are concerned with multiple pathogens. Multipathogen modeling is crucial where the interaction is nontrivial. This may be because there is a meaningful biological connection between the pathogens, for instance, the similarity in at-risk groups and the inherent increase in the likelihood of seroconversion due to immunosuppression means Hepatitis C often presents as a coinfection with HIV [146]. Alternatively, there might be an evolutionary concern, such as the development of antibiotic-resistant strains (which is explored in more detail in Subsection 5.1.5). Finally, there are often interactions that are behaviorally defined. Pertussis and measles, which is discussed in more detail in Subsection 5.2.1, is perhaps one of the most prominent examples, where there is a behavioral element to the interaction between two pathogens.

Multipathogen models are challenging, because they comprise, essentially, multiple compartmental models stacked upon each other. The complexity increases rather rapidly with the number of pathogens.

### 5.1 Multipathogen systems with cross-immunity

This section deals with scenarios where there is partial or total cross-immunity. Crossimmunity has been at the heart of Jenner's vaccination for smallpox: Jenner's vaccination worked, because infection with cowpox generated cross-immunity with smallpox (see Section 6.1). Models of complete cross-immunity are the simplest multipathogen models, and thus we shall begin with this simple scenario.

Because immunity is at the heart of this matter, we will consider two pathogens to be distinct if they are immunologically distinct.

Definition 5.1 (Immunological distinctiveness). Two organisms are immunologically distinct if there is a meaningful difference between the immune response. Thus if the pathogens $a$ and $b$ are immunologically distinct, the immune response evoked by $a$ is less effective in respect of $b$ than it is in respect of $a$.

Thus we take a principally immunological view of genetic variance: pathogens are "distinct" (i.e., in terms of serovariants) as long as antibodies against one type are less efficient against another. With that in mind, let us explore the effects of serovariance and serological diversity on infectious dynamics.

### 5.1.1 Case study: too much of a good thing?

Dengue fever is an unpleasant, but rarely life-threatening, illness caused by the dengue virus (DENV), an RNA flavivirus, and hence a distant relative of yellow fever. The majority of patients experience an approximately week-long illness, comprising fever, arthralgia, and a rather peculiar rash. A small minority, however, go on to develop dengue haemorrhagic fever, which may be life-threatening. Similarly to other haemorrhagic fevers, it manifests as thrombocytopaenia, haemorrhage, and hypovolaemic shock.

In 2016 a vaccine became available for dengue fever. CYD-TDV is a chimeric vaccine that uses an attenuated yellow fever strain altered to express the envelope (E) and premembrane (PrM) proteins from selected dengue serotypes [147]. Following a vaccination campaign across the Philippines, it emerged in a 2018 analysis that seronegative individuals who were vaccinated had a paradoxically elevated risk of severe illness [148]. Though those who have had dengue before have benefited greatly from the vaccine, for dengue seronegative vaccine recipients aged 9 to 16 , the hazard ratio of virologically confirmed dengue infection requiring hospitalization was $1.57 \%$, as opposed to only $1.09 \%$ among unvaccinated controls, a hazard ratio of 1.41.

An explanatory hypothesis was presented by Halstead in 2017, arguing that the vaccine created antibodies that contributed to the development of antibody-dependent enhancement (ADE) [149]. ADE occurs when a vaccine elicits antibodies that either do not bind at a neutralizing epitope (i.e., their binding does not preclude the virion's ingress into a host cell) or have low binding affinity, and thus, paradoxically, antibodies end up facilitating viral entry. The detailed mechanics of ADE are discussed in Subsection 5.1.4, and its handling in the vaccine context in Practice Note 5.2.

In the case of the dengue vaccine, the indiscriminate administration regardless of serostatus has resulted in exposing individuals to a higher risk of severe disease from dengue infection than they would have experienced in the absence of immunization. Too much of a good thing, alas, can thus have detrimental outcomes. Revelations about the potential for ADE arising from the dengue vaccine have led to a widespread crisis of confidence in vaccinations in the Philippines, which compounds the damage [150]. When considering immunizations for macrophagotrophic or respiratory pathogens, the low but nonzero risk of ADE must not be discounted.

### 5.1.2 Simple multipathogen models with perfect cross-immunity

The simplest multipathogen models ordinarily pertain to two strains or pathogenic species, which we shall denote using numbers. Simple models follow the principle known as Gause's law of competitive exclusion: competition between two organisms occupying the same ecological niche is always "absolute," in that the stable equilibrium of such competition is the absolute dominance of one organism [151].

Definition 5.2 (Gause's law of competitive exclusion). If two or more organisms inhabit the same ecological niche, the stable equilibrium will be the complete dominance of the more advantaged species and the complete extinction of the disadvantaged species.

Our simple models reflect this by allowing for one and only one course of infection, after which individuals return to a recovered compartment. This is the case when there is perfect cross-immunity, i.e., recovery from pathogen $1\left(R_{1}\right)$ immunizes against pathogen 2 as well, and vice versa. The model can thus be described as

$$
\begin{align*}
& \overbrace{\text { from strain } 1 \quad \text { from strain } 2}^{\text {mass action }} \\
& \frac{d S}{d t}=-\overbrace{\beta_{1} S I_{1}}-\overbrace{\beta_{2} S I_{2}} \\
& \frac{d I_{1}}{d t}=\beta_{1} S I_{1}-\gamma_{1} I_{1} \\
& \frac{d I_{2}}{d t}=\beta_{2} s I_{2}-\gamma_{2} I_{2}  \tag{5.1}\\
& \frac{d R}{d t}=\underbrace{\underbrace{\gamma_{1} I_{1}}_{\text {from strain } 1}+\underbrace{\gamma_{2} I_{2}}_{\text {from strain } 2}}_{\text {recoveries }} .
\end{align*}
$$

This model generalizes for $n$ pathogens as

$$
\frac{d S}{d t}=-\overbrace{\sum_{i=1}^{n} \overbrace{\beta_{i} S I_{i}}^{\text {mass action for } i}}^{\text {total mass action }}
$$

$$
\begin{align*}
& \overbrace{\text { mass action }}^{\text {for } i} \\
& \frac{d I_{i}}{d t}=\overbrace{\beta_{i} S I_{i}}-\overbrace{\gamma_{i} I_{i}}, \tag{5.2}
\end{align*}
$$

![](https://cdn.mathpix.com/cropped/2024_06_11_ae648d58b489163f3247g-04.jpg?height=178&width=340&top_left_y=403&top_left_x=221)

and in line with the equation in Subsection 2.1.5, the pathogen-wise basic reproduction number $\mathfrak{R}_{0}^{i}$ would be $\frac{\beta_{i}}{\gamma_{i}}$ for all $i$ in $n$.

The dynamics of multiple pathogens with different values of $\mathfrak{R}_{0}$ and providing complete cross-immunity are somewhat nontrivial. In the long run, competitive exclusion means that the pathogen with the larger value of $\mathfrak{R}_{0}$ will become absolutely dominant (i.e., the pathogen with the smaller value of $\mathfrak{R}_{0}$ will become extinct). A pathogen $i$ is at an equilibrium if $S=\mathfrak{R}_{0}^{i}$ (i.e., if $S \mathfrak{R}_{0}^{i}=1$ ). This results in $n$ equilibrium points for $n$ pathogens. For the simple case of two pathogens, the equilibrium points will be $S=\frac{1}{\mathfrak{R}_{0}^{1}}$ and $S=\frac{1}{\mathfrak{R}_{0}^{2}}$. If $\mathfrak{R}_{0}^{2}>\mathfrak{R}_{0}^{1}$, then the equilibrium point at $S=\frac{1}{\mathfrak{R}_{0}^{1}}$ will not be stable for pathogen 2 , because the growth rate of pathogen 2 at that point is still positive. On the other hand, at $S=\frac{1}{\mathfrak{\Re}_{0}^{2}}$, the growth rate of pathogen 1 is negative. Thus pathogen 2 can reach an equilibrium that eventually stabilizes into the extinction of pathogen 1 , which is the long-term evolutionary destiny of multipathogen systems with complete cross-immunity and different values of $\mathfrak{R}_{0}$.

## Practice Note 5.1 The long and short (term) of it

Gause's law tells us what happens in the long run. However, short-term processes might be quite different.

Fig. 5.1 describes just such a scenario. With pathogen $b$ having a higher $\mathfrak{R}_{0}$ than $a$, its eventual dominance is all but assured. On the other hand, in the short term, the more rapid lifecycle of $a$ makes it temporarily dominant in the short term. In short: the long-term evolutionary destiny is determined by $\mathfrak{R}_{0}$, whereas short-term dynamics are determined by the values that make up $\mathfrak{R}_{0}$ (i.e., $\beta$ and $\gamma$ ).

The consequence of that in practice is that when two pathogens emerge that induce cross-immunity, $\mathfrak{R}_{0}$ alone might not account for short term processes. Rather, its constituent elements must be taken into account. Epidemiological modeling, such as has been discussed in Computational Note 4.4, can assist in preparing a response that allocates resources accordingly. This is particularly important where the two pathogens produce sufficiently different presentations that might require different treatments or are associated with different severity.

![](https://cdn.mathpix.com/cropped/2024_06_11_ae648d58b489163f3247g-05.jpg?height=633&width=1075&top_left_y=224&top_left_x=227)

Figure 5.1 Short and long-term dynamics of a two-pathogen system with complete crossimmunity, with $\beta_{1}=1.5, \gamma_{1}=1.0, \beta_{2}=0.4$, and $\gamma_{2}=0.2$ and $I_{1}(0)=I_{2}(0)=10^{-6}$. It follows from the above that whereas pathogen 2 is dominant in terms of $\mathfrak{R}_{0}$, pathogen 1 follows a much faster dynamics with a shorter lifecycle. The result of this is that whereas pathogen 1 eventually becomes extinct, pathogen 2 is briefly dominant in the short term.

### 5.1.3 Incomplete cross-immunity

In incomplete cross-immunity, exposure to a pathogen produces a nonzero level of cross-immunity against another pathogen. Fig. 5.2 demonstrates such a scenario with two pathogens. Recovery from either pathogen provides perfect immunity, i.e., there is no "loopback" from $R_{1}$ to $I_{1}$ and $R_{2}$ to $I_{2}$, respectively. We denote the compartment of previously recovered individuals who sustain an infection from the other pathogen as the heterotypic infectious compartment $(H)$. The flows are strictly "crosswise," i.e., they go from $R_{1}$ to $H_{2}$, and vice versa. Recovery from heterotypic infection results in dual immunity, denoted as $R_{1,2}$. Because heterotypic infections are part of the infectious subsystem, they must be considered part of the mass action term of the infectious compartment (since a susceptible individual may be infected by an initial or a heterotypic infection). Therefore the susceptible subsystem is

$$
\begin{equation*}
\frac{d S}{d t}=-S\left(\beta_{1}\left(I_{1}+H_{1}\right)+\beta_{2}\left(I_{2}+H_{2}\right)\right) \tag{5.3}
\end{equation*}
$$

We denote the heterotypic penalty of each strain as $\psi_{1}$ and $\psi_{2}$ for strains 1 and 2 , respectively. $\psi_{1}$ would represent the reduction to $\beta_{2}$ vis-a-vis an individual who has recovered from strain 1 , and vice versa. The infectious subsystem $(I$ and $H$ ) is then

$$
\frac{d I_{1}}{d t}=\beta_{1} S \underbrace{\left(I_{1}+H_{1}\right)}_{\text {all infections with strain } 1}-\gamma_{1} I_{1}
$$

![](https://cdn.mathpix.com/cropped/2024_06_11_ae648d58b489163f3247g-06.jpg?height=622&width=1132&top_left_y=225&top_left_x=159)

Figure 5.2 Interaction between two pathogens with incomplete cross-immunity. Individuals who recover from one pathogen are still susceptible to heterotypic infection with the other, albeit subject to a penalty $\psi$.

$$
\begin{align*}
\frac{d I_{2}}{d t} & =\beta_{2} S \underbrace{\left(I_{2}+H_{2}\right)}_{\text {all infections with strain } 2}-\gamma_{2} I_{2} \\
\frac{d H_{1}}{d t} & =\underbrace{\psi_{2} \beta_{1} R_{2}\left(I_{1}+H_{1}\right)}_{\text {heterotypic infections with strain 1 }}-\gamma_{1} H_{1}  \tag{5.4}\\
\frac{d H_{2}}{d t} & =\underbrace{\psi_{1} \beta_{2} R_{1}\left(I_{2}+H_{2}\right)}_{\text {heterotypic infections with strain 2 }}-\gamma_{2} H_{2}
\end{align*}
$$

This model for two competing pathogens with some cross-immunity can be expanded to arbitrary numbers of pathogens, although model complexity does increase significantly.

### 5.1.4 Antibody-dependent enhancement

Antibody-dependent enhancement (ADE) is a phenomenon observed in a small number of pathogens (most significantly perhaps in dengue virus, see, e.g., Subsection 5.1.1) that have multiple circulating subtypes or serotypes. Normally, antibodies bind to virions, then to the fragment crystallizable region gamma IIa receptors (Fc $\gamma$ RIIa) on cells that express it (commonly known as CD32+ cells), such as macrophages, dendritic cells, and B-cells. If the antibodies do not neutralize the pathogen, but facilitate its phagocytosis by binding to the Fc $\gamma$ RIIa receptor, infectioncompetent virions can enter these cells with relative ease. Thus, paradoxically, the presence of antibodies work in favor of the pathogen, rather than against it.

There has been relatively little quantitative modeling of ADE in general. Ferguson, Anderson, and Gupta [152] examined a model of ADE in the context of dengue, concluding that ADE can result in temporary oscillatory dynamics, in which the heterotypic serotype that benefits from ADE outpaces its competitors until it burns through the available susceptible population and once again recedes. In the context of COVID-19, Adil Mahmoud Yousif et al. [153] proposed a compartmental approach, in which a certain percentage of the vaccinated cohort (between 1 to $2 \%$ ) develop a predisposition for ADE. A more effective compartmental approach for the modeling of ADE is to separate serotypes and exposures. For $n$ serotypes, the cross-ADE matrix A is the $n \times n$ hollow matrix

$$
\mathbf{A}=\left(\begin{array}{cccc}
0 & \alpha_{1,2} & \cdots & \alpha_{1, n}  \tag{5.5}\\
\alpha_{2,1} & 0 & \cdots & \alpha_{2, n} \\
\vdots & \vdots & \ddots & \vdots \\
\alpha_{n, 1} & \alpha_{n, 2} & \cdots & 0
\end{array}\right)
$$

where $\alpha_{p, q}$ is the likelihood of developing ADE when exposed to serotype $q$, given a past exposure to serotype $p$.

The values of this matrix may be ascertained empirically from in vivo studies or from in vitro research, since $\alpha_{p, q}$ is likely to relate inversely to the ability of anti- $p$ antibodies to neutralize $q$ (in other words, $\alpha_{p, q}$ is a metric of the deficiency of anti- $p$ antibodies in neutralizing $q$, i.e., the specificity of anti- $p$ vis-a-vis $q$ ). The matrix $\mathbf{A}$ is hollow, because only heterotypic exposures can result in ADE. This is an assumption that is, of course, subject to perfect serological categorization (i.e., it assumes that all of the serotypes are perfect partitions, i.e., every infected individual is infected with one serotype, and the sum of each serotype's infectious subcompartment equates to the entire population, and binding is a binary property of serotypal identity). As such, it is a somewhat idealized picture of reality, where antibodies to a particular serotype may nonetheless bind less than perfectly to their target epitopes. Nonetheless, it is analytically helpful for the purpose of modeling ADE. For the compartment $C_{p}$, comprising all individuals who were exposed to, and recovered from, serotype $p$, ADE on exposure to $q$ accounts for $C_{p} I_{q} \mathbf{A}_{p, q}$, so that

$$
\begin{equation*}
\frac{d I_{q}}{d t}=\beta S\left(1+\mathbf{A}_{p, q} C_{p} \epsilon\right) I_{q}-\gamma I_{q} \tag{5.6}
\end{equation*}
$$

where $\epsilon$ is a measure of the impact of ADE, expressed as the increase in $\beta$, where ADE occurs (i.e., A gives the likelihood, $\epsilon$ gives the impact). This generalizes for all $n$ serotypes as

$$
\begin{equation*}
\frac{d I_{q}}{d t}=\beta S\left(1+\sum_{i=1}^{n} A_{i, q} C_{i} \epsilon\right) I_{q}-\gamma I_{q} \tag{5.7}
\end{equation*}
$$

## Practice Note 5.2 ADE and vaccination

It bears repeating that $\mathrm{ADE}$ is a marginal phenomenon, and must be represented in context. The study by Adil Mahmoud Yousif et al. [153], cited above, found that at most $2 \%$ of COVID-19 vaccinations would result in ADE (and in all likelihood, real figures are much lower). ADE figures must be presented in the context of the risk averted by vaccination, which in the overwhelming majority of cases is going to be much higher. During the COVID-19 pandemic, ADE was identified as a significant driver behind vaccine hesitancy [154-156], when in reality the least effective vaccines were quite significantly beneficial, even when accounting for ADE.

It is important not to obscure the reality of ADE, and where appropriate, encourage understanding of the phenomenon to assist physicians in appreciating the sometimes surprisingly severe presentation of infectious diseases in individuals who ought to have acquired or induced immunity [157-160]. At the same time, in the vast majority of circumstances, the benefits from vaccination and the protective effect of recent prior infection are going to be vastly more beneficial than the detriment incurred by ADE. In addition, the effect of ADE depends on changes or diversity in the serotype that renders the previous immunity, acquired or induced, to be no longer effective in neutralizing. Therefore communicating the effects of ADE must take into account the counterfactual risk averted by reducing the risk of contracting the illness in the first place.

### 5.1.5 Antimicrobial resistance as a multipathogen problem

We may conceptualize antimicrobial resistance as the competition of pathogens $s$ (susceptible or "wild type") and $r$ (resistant). If $r$ and $s$ exhibit complete cross-immunity, then, as we have discerned in Subsection 5.1.2, only one can survive, and the evolutionary dominance will be determined by the relative values of $\mathfrak{R}_{0}^{r}$ and $\mathfrak{R}_{0}^{s}$.

Because antimicrobial treatment shortens the course of disease, $\gamma_{s}$ will be greater than $\gamma_{b}$ by a variable we shall call treatment effect or $\epsilon_{T}$ for short, and by the fraction of the population of people who have a susceptible infection and receive antibiotic treatment. The latter is the treatment fraction $\theta$. Thus the infectious subsystem of this model is

$$
\begin{align*}
& \frac{d I_{s}}{d t}=\beta_{s} S I_{s}-(\gamma-\overbrace{\theta \epsilon_{T}}^{\text {penalized recovery for susceptible strain }}) I_{s}  \tag{5.8}\\
& \frac{d I_{r}}{d t}=\beta_{r} S I_{r}-\underbrace{\gamma I_{r}}_{\text {unpenalized recovery for }} \cdot
\end{align*}
$$

It follows from this that $s$ is dominant if $\mathfrak{R}_{0_{s}}$ is greater than $\mathfrak{R}_{0_{r}}$, otherwise $r$ becomes the dominant strain, which means that most infections will be caused by the
type less susceptible to antimicrobials. The inflection point depends, of course, on the parameters, but most crucially, on $\theta$. Setting the $\mathfrak{R}_{0}$ s equal, we can define the critical value of $\theta$, so that treating a larger proportion of the population would lead towards dominance by the resistant pathogen. This is the critical value ${ }^{\Delta} \theta$, which is defined as

$$
\begin{equation*}
\Delta_{\theta}=\frac{\gamma}{\epsilon_{T}}\left(1-\frac{\beta_{s}}{\beta_{r}}\right) \tag{5.9}
\end{equation*}
$$

Subject to the caveat in Practice Note 5.3, we can conceive of ${ }^{\Delta} \theta$ as the maximum safe proportion of the infected population that can be treated with antimicrobials of efficacy $\epsilon_{T}$ without enabling the dominance of the resistant strain. This model can, of course, be expanded to multiple antimicrobials, where the pathogenic model would comprise the $2^{n}$ permutations of $n$ potential susceptibilities. This is particularly useful where there are multiple dimensions of drug resistance, i.e., multiple drug groups against which a pathogen can develop immunity.

Practice Note 5.3 Compensatory mutations and a caveat about critical values

A corollary of Eq. (5.9) is that what percentage of the population can be treated without handing over dominance to the drug-resistant strain depends on the fitness cost, in terms of relative $\Re_{0} \mathrm{~s}$, of drug resistance (along with the effectiveness of treatment, $\epsilon_{T}$ ). In general, resistance has a fitness cost, so that drug resistant mutants have a typically lower $\beta$ (and thus, lower $\mathfrak{R}_{0}$ ) [161]. The difference between the respective values of $\Re_{0}$ is the mathematical expression of this fitness cost. However, evolution is a continuous process. Compensatory mutation refers to the process of subsequent mutations "offsetting" the fitness cost of the drug resistance mutation [162].

The critical value ${ }^{\Delta} \theta$ is a theoretical estimate of what percentage of the population can be treated without benefiting the drug-resistant strain; the critical value of $\Delta^{\Delta}$ in this case may drop over time due to compensatory mutations [163,164]. It is therefore important to treat ${ }^{\Delta} \theta$ as an indicative upper bound and approach it with considerable caution. Pathogenic evolution does not stop, and if a pathogen were to overcome its innate deficiencies through compensatory mutations, reasonable treatment rates well below ${ }^{\Delta} \theta$ could prove excessive. Vigilant tracking of pathogenic dynamics is crucial for data-driven antibiotic stewardship.

### 5.1.6 Microscale models of antimicrobial treatment and immunity

The compartmental models we have encountered are mean-field models that represent population flows by mapping the overall rate of processes. We may not be able to account for every individual, but at sufficiently large populations, even relatively simple

Table 5.1 Phenotype-specific parameters of the phenotypes for the model described in Subsection 5.1.6.

| Phenotype | Population | Growth rate | Killing rate by antimicrobials |
| :--- | :---: | :---: | :---: |
| Susceptible | $B_{r}$ | $r_{r}$ | $\kappa_{r}$ |
| Partially resistant | $B_{s}$ | $r_{s}$ | $\kappa_{s}$ |

systems of ODEs result in a good enough approximation of reality. The same principle can be applied on the microscale to quantities of bacteria and immune cells to model the effect (and the lack thereof, in some cases) of antibiotic resistance.

Such models, which Hellriegel [165] aptly described as "immuno-epidemiological" models, are microscale in relation to population models, but macroscale models with respect to populations of pathogens and immune cells, which make up the equivalent of the population. Typically, an immuno-epidemiological model would be somewhat similar to the models that deal with different planes of transmission in the context of zoonotic and vector-borne disease (see Chapter 4):

- There is a population of pathogens, potentially of multiple strains, which is being killed at a certain rate by some (but not all) immune cells, and potentially by external influences (such as the administration of an antimicrobial).
- There is a separate population of immune cells, which go through a cycle of maturation, typically from some form of precursor cell to effector cells and eventually, some fraction matures into memory cells. The immune systems of higher organisms are fairly complex, and it is often a matter for the judgment of an infectious disease modeler to determine what detail is required to adequately represent the host population's immune topology. Studying the peculiarities of the host population's immune system tends to pay abundant dividends.

The model of antimicrobial therapy developed by Gjini and Brito [161] is a good example of such a model. It represents two concurrent planes:

1. In the pathogenic plane, a susceptible and a partially resistant strain compete.
2. In the immune plane, immune cells differentiate, mature, and divide from naive immune cells to effector cells to memory cells.

Both of these processes take place in the presence of antimicrobial treatment. Fig. 5.3 describes the structure of such a model, describing a typical CD8+ mediated immune response in the pathogenic and the immune plane. The pathogenic plane contains two phenotypes: $B_{s}$, susceptible to the antibiotic, and $B_{r}$, which is partially resistant. The properties of the phenotypes are described in Table 5.1.

We may characterize the dynamics of each plane, following Gjini and Brito [161], by a system of two sets of differential equations: one pair of ODEs corresponding to $B_{r}$ and $B_{s}$, and three ODEs corresponding to naive precursor cells $(N)$, effector cells $(E)$, and memory cells $(M)$. Antimicrobial treatment is reflected by the pathogen-specific antibiotic kill rate $\kappa$, the treatment indicator function $\eta(t)$ determining whether the person is receiving treatment at time $t$, and the mean serum antibiotic concentration, $\overline{c_{a}}$. In addition, both pathogens have a pathogen-nonspecific kill rate $\kappa_{\ell}$, attributable
to the leukocytes.

$$
\begin{align*}
& \frac{d B_{s}}{d t}=\overbrace{r_{s} B_{s}}^{\text {growth }}-\overbrace{\kappa_{\ell} B_{s}(M+E+N)}^{\text {killing by leukocytes }}-\overbrace{\kappa_{s} B_{s} \eta(t) \overline{c_{a}}}^{\text {killing by antibiotics }}, \\
& \frac{d B_{r}}{d t}=\underbrace{r_{r} B_{r}}_{\text {growth }}-\underbrace{\kappa_{\ell} B_{r}(M+E+N)}_{\text {killing by leukocytes }}-\underbrace{\kappa_{r} B_{r} \eta(t) \overline{c_{a}}}_{\text {killing by antibiotics }} . \tag{5.10}
\end{align*}
$$

We note that the rate of pathogens killed by the antibiotic is the product of the treatment function $\eta(t)$, which determines whether the patient is receiving treatment at $t$, the susceptibility of the strain to the antibiotic (expressed as the kill rate $\kappa$ ), and the amount of the antibiotic administered (which we describe by reference to the mean serum antibiotic concentration, $\overline{c_{a}}$ ).

The second half of this system represents the immune cell populations. Key to this are three factors: the rate of recruitment of naive immune cells $\mu_{\max }$, the rate at which effector cells die or become memory cells $\left(\frac{1}{\tau_{E}}\right)$, and a third factor, which links the immune system's dynamics to that of the pathogenic population's, that is, the pathogen load dependent immune growth rate $\sigma_{B}$. We model the growth of the immune system as a Monod equation (a special case of the Langmuir-Hill equation for $n=1$ ) [166], so that the growth rate at a given level of total pathogen load $B=B_{s}+B_{r}$ is

$$
\begin{equation*}
\mu(B)=\mu_{\max } \frac{B}{K_{B}+B} \tag{5.11}
\end{equation*}
$$

where $K_{B}$ is the half-velocity coefficient, that is, the value of $B$ so that $\frac{\mu(B)}{\mu_{\max }}=\frac{1}{2}$.

We also account for the fact that effector cells may either die off or become memory cells. We assume that after $\tau_{E}$ time, an effector cell either dies, becomes a memory cell with $p_{M}$ probability. Thus

$$
\begin{align*}
& \frac{d N}{d t}=-N \underbrace{\mu_{\max } \frac{B}{K_{B}+B}}_{\begin{array}{c}
\text { recruitment of } \\
\text { naive T cell precursors }
\end{array}} \\
& \frac{d E}{d t}=\underbrace{2 N \mu_{\max } \frac{B}{K_{B}+B}}_{\begin{array}{c}
\text { division and differentiation of } \\
\text { naive T cell precursors }
\end{array}}+\underbrace{E \mu_{\max } \frac{B}{K_{B}+B}}_{\begin{array}{c}
\text { proliferation of } \\
\text { effector cells }
\end{array}}-\underbrace{\frac{1}{\tau_{E}} E\left(1-\frac{B}{K_{B}+B}\right.}_{\begin{array}{c}
\text { apoptosis and differentiation } \\
\text { into memory cells }
\end{array}})
\end{align*}
$$

$$
\frac{d M}{d t}=\underbrace{p_{M} \frac{1}{\tau_{E}} E\left(1-\frac{B}{K_{B}+B}\right)}_{\begin{array}{c}
\text { differentiation into } \\
\text { memory cells }
\end{array}}
$$

The benefit of microscale immunoepidemiological models is that they allow us to reason quantitatively about antimicrobial treatment. Gjini and Brito [161], for instance, utilized this model to evaluate different treatment strategies by different for-

![](https://cdn.mathpix.com/cropped/2024_06_11_ae648d58b489163f3247g-12.jpg?height=1444&width=1187&top_left_y=227&top_left_x=136)

Figure 5.3 Outline of an immunoepidemiological model with two pathogens, $B_{S}$ (susceptible to the antimicrobial) and $B_{r}$ (partially resistant). Dotted red lines describe the influence of pathogens on differentiation and proliferation of immune cells. Solid lines describe the effect of immune cells on the pathogen. The dashed lines represent the partial efficiency of antimicrobials against $B_{r}$.

mulations of the treatment indicator function $\eta(t)$, contrasting a fixed-time treatment regimen with a critical pathogen density-dependent treatment strategy.

It is worth reflecting on a particular feature of immunity that this model illuminates. The rate at which long-term immunity is incurred (through memory cells) depends on
the rate at which the immune system is activated. We have seen in Eq. (5.11) that this is a function of pathogenic load. For an $n$-day illness, the total pathogenic load for the entire illness is

$$
\begin{align*}
B_{\text {total }}=\int_{0}^{n} & \left(r_{s} B_{s}(t)+r_{r} B_{r}(t)\right. \\
& -\kappa_{\ell}\left(B_{s}(t)+B_{r}(t)\right)(M(t)+E(t)+N(t))  \tag{5.13}\\
& \left.-\left(\kappa_{s} B_{s}(t)+\kappa_{r} B_{r}(t)\right) \eta(t) \overline{c_{a}}\right) d t
\end{align*}
$$

This is, of course, a strictly monotonically decreasing function of the total antimicrobial burden

$$
\mathrm{TAB}=\int_{0}^{n} \eta(t) \overline{c_{a}} d t
$$

On the other hand, it follows from Eq. (5.12) that the overall memory T cell gain $M^{+}$by the end of infection,

$$
\begin{equation*}
M^{+}=\int_{0}^{n} p_{m} \frac{1}{\tau_{E}} E(t)\left(1-\frac{B_{r}(t)+B_{s}(t)}{K_{B}+B_{r}(t)+B_{s}(t)}\right) d t \tag{5.14}
\end{equation*}
$$

is a strictly monotonically increasing function of $B_{\text {total }}$. The consequence of this is that higher antimicrobial loads will result in a lower total pathogenic load, but also a lower involvement of the immune system, and therefore less immunity in the long run (as indeed has been empirically demonstrated in a number of experiments summarized in a sweeping review by Benoun, Labuda, and McSorley [167]). Thus though rapid and aggressive antimicrobial treatment is sometimes appropriate, the long-term absence of ensuing CD4+ immunity is its cost. The overall effectiveness of the same $\mathrm{TAB}$ decreases as the fitness benefit of resistance $\frac{\kappa_{r}}{\kappa_{s}}$ increases. The consequence is that antibiotic treatment exerts a selection pressure in favor of resistant strains, while resulting in a reduction of developing long term $\mathrm{T}$ cell immunity that would not be affected by the pathogen's antimicrobial resistance, that is, trading long term protection for immediate elimination and the reduction of early infectious potential. Microscale models resting on empirical data are useful in quantifying the cost-benefit ratio of early and aggressive antimicrobial interventions in view of the risks posed by the pathogen and the prevalence of resistant strains.

### 5.2 Multipathogen systems without cross-immunity

In this section, we turn to the study of multipathogen systems without cross-immunity. Pathogens are no exception to the fundamental imperatives of biology: all life exists in competition for finite resources. For pathogens, the crucial resource is, of course, the availability of suitable hosts.

An inherent bias of epidemiology is that we observe all things from the perspective of the host. In reality, looked at it from the perspective of the "pathogen," much (but not all) of the pathogenic effect is quite epiphenomenal to the pathogen's "interests." A hypothesis commonly known as the "trade-off theory" or "avirulence theory" argues that pathogenic evolution moves inevitably towards higher infectiousness but lower lethality [168-170]. Even if a strict trade-off theory, whereby evolution implies monotonously decreasing virulence over time, does not necessarily hold in that simple formulation [171-173], our mathematical models clearly show that altogether too high a mortality leads to rapid epidemic burnout, whereas successful pathogens converge to be less virulent but more infectious.

The risk of this inherent bias is that we might not realize the pressure under which any pathogen finds itself, that is, not from the host's defenses but from other pathogens. When multiple pathogens affect the same host, they may act synergistically or they may act adversarially. This section examines cases where no cross-immunity is elicited, i.e., where immunity to one pathogen does not confer immunity to the other.

### 5.2.1 Case study: pertussis and measles

Pertussis, more commonly known as whooping cough, is a bacterial disease caused by the bacterium Bordetella pertussis. Although quite rare in the developed world due to near-universal vaccination (typically as part of the TDaP combination vaccine), pertussis was once a major cause of death among children in particular. Even today, the death toll from pertussis is not insignificant: Koenig and Guiso [174] note that in 2014, pertussis claimed the lives of 160,000 children under 5 .

Measles is a viral disease caused by the measles morbillivirus (MeV), the single most infectious naturally occurring agent known to man [175]. Fortunately, measles, too, is rarely seen in the developed world, thanks to vaccination programmes, although there has been a worrying increase in cases following the surge in vaccine hesitancy in the aftermath of widely spread misinformation of a link between the MMR vaccine and autism $[176,177]$.

On the surface, the two seem to have little to do with each other. However, in a 2015 article, Coleman [178] noted an interaction between the temporal dynamics of measles and pertussis. Examining state-level data on incidence for both conditions in the United States between 1938 and 1954, Coleman found that states with a higher incidence of measles would also go on to have a higher incidence of pertussis. More poignantly, he also noted that the dynamics of pertussis lagged behind measles by about 3-4 weeks. Coleman hypothesizes that measles infection might result in recovery into an immunosuppressed state, which increases the likelihood of contracting pertussis. Recent studies on the immunological effect of measles have identified a postinfectious state of "immune amnesia," which included not merely immunosuppression through the destruction of $\mathrm{T}$ and $\mathrm{B}$ lymphocytes, but also the destruction of memory $\mathrm{B}$ cells that serve as the mainstay of immunological memory in humans [179,180]. A 2020 study by MacIntyre, Costantino, and Heslop [181] following the 2019 Samoa measles outbreak seems to support this hypothesis.

![](https://cdn.mathpix.com/cropped/2024_06_11_ae648d58b489163f3247g-15.jpg?height=892&width=1062&top_left_y=226&top_left_x=238)

Figure 5.4 Interaction between two pathogens with no cross-immunity. Red boxes denote the infectious subsystem of pathogen 1 and blue boxes that of the pathogen 2 , respectively. Arrows that transition into infectious states are colored based on which infectious subsystem governs the mass action term.

Fortunately, for much of the world's population, pertussis is a thing of the past, and though measles has regained an odd stature as a "reemerging" pathogen, it remains quite rare. Nevertheless, the dynamics observed by Coleman [178] show the complex way in which pathogens exist in a complex microbiome, competing but also, from time to time, facilitating each other.

### 5.2.2 Simple multipathogen systems without cross-immunity and without coinfection

The absence of cross-immunity makes models rather more complex, since we have to account for each person's status in respect of two pathogens. Simple models assume the absence of coinfection, i.e., one individual can be in no more than one infectious system at any given time. As Keeling and Rohani [39] note, this is epidemiologically plausible, since infection tends to reduce encounters sufficiently to make infectious interactions less frequent and may, through mortality, permanently render individuals unavailable to the competitor infection.

Fig. 5.4 describes the structure of a model without cross-immunity and without coinfection. We may, given the infectious subsystems $I_{1}=N_{I, S}+N_{I, R}$ and
$I_{2}=N_{S, I}+N_{R, I}$, express this model as the following system:

$$
\begin{align*}
& \frac{d N_{S, S}}{d t}=-\left(\beta_{1} N_{S, S} I_{1}+\beta_{2} N_{S, S} I_{2}\right) \\
& \frac{d N_{I, S}}{d t}=\beta_{1} N_{S, S} I_{1}-\gamma_{1} N_{I, S} \\
& \frac{d N_{S, I}}{d t}=\beta_{2} N_{S, S} I_{2}-\gamma_{2} N_{S, I} \\
& \frac{d N_{R, S}}{d t}=\gamma_{1} N_{I, S}-\beta_{2} N_{R, I} I_{2} \\
& \frac{d N_{S, R}}{d t}=\gamma_{2} N_{S, I}-\beta_{1} N_{I, R} I_{1}  \tag{5.15}\\
& \frac{d N_{R, I}}{d t}=\beta_{2} N_{R, I} I_{2}-\gamma_{2} N_{R, I} \\
& \frac{d N_{I, R}}{d t}=\beta_{1} N_{I, R} I_{1}-\gamma_{1} N_{I, R} \\
& \frac{d N_{R, R}}{d t}=\gamma_{2} N_{R, I}+\gamma_{1} N_{I, R}
\end{align*}
$$

From a computational perspective, it may often be useful in such situations to make use of the techniques discussed in Computational Note 5.1 to handle vector-valued calculations.

## Computational Note 5.1 Modeling the no-coinfection no-cross immunity interaction

One might be tempted to transpose the system described in Eq. (5.15) directly into a derivative function:

def deriv(t, y, beta_1, beta_2, gamma_1, gamma_2, mu, nu):

SS, IS, RS, SI, RI, SR, IR, RR $=y$

I_1 = IS + IR

I_2 = SI + RI

```
dNSSdt = nu - beta_1 * SS * I_a + beta_2 * SS * I_2 - mu * SS
dNISdt = beta_1 * SS * I_a - gamma_1 * IS - mu * IS
dNRSdt = gamma_1 * IS - beta_2 * RS * I_2 - mu * RS
dNSIdt = beta_2 * SS * I_2 - gamma_2 * SI - mu * SI
dNRIdt = beta_2 * RS * I_2 - gamma_2 * RI - mu * RI
dNSRdt = gamma_1 * IS - beta_1 * SR * I_1 - mu * SR
dNIRdt = beta_1 * SR * I_1 - gamma_1 * IR - mu * IR
```

```
dNRRdt = gamma_1 * IR + gamma_2 * RI - mu * RR
return dNSSdt, dNISdt, dNRSdt, dNSIdt, dNRIdt, dNSRdt, dNIRdt,
    dNRRdt
```

There is, strictly speaking, nothing wrong with this, but we can turn this into better, more elegant and more performant code. First, note that there are four terms that describe recovery: those that describe recovery from the pathogen 1 subsystem (gamma_1 * I[S/R]) and those that describe recovery from the pathogen 2 subsystem (gamma_2 * $[S / R] \mathrm{I}$ ). We can turn this into a matrix quite easily, by constructing a matrix in which each column corresponds to a subsystem, then multiplying it by a vector of both values of $\gamma$ :

$$
\left(\begin{array}{ll}
I S & S I  \tag{5.16}\\
I R & R I
\end{array}\right) \vec{\gamma}=\left(\begin{array}{ll}
\gamma_{1} I S & \gamma_{2} S I \\
\gamma_{1} I R & \gamma_{2} R I
\end{array}\right)
$$

We do so by constructing a matrix on the fly with np.array and multiplying it:

gmat $=$ gamma * np.array([[IS, SI], [IR, RI]])

Next, we note that the first equation involves subtracting $\beta_{1} N_{S, S} I_{1}$ and $\beta_{2} N_{S, S} I_{2}$. If we create a vector $\vec{I}$ for the infectious subsystems, where $\vec{I}=\binom{I_{1}}{I_{1}}$, we can simplify this as $\vec{\beta} N_{S, \dot{S} I}$. We solve this by first defining the infectious subsystem vector:

$I=$ np.array([[IS + IR], [SI + RI]])

Next, we substitute the dot product form into the derivative functon's calculation of $\frac{d N_{S, S}}{d t}$ :

$d N S S d t=n u-(b e t a * S S) . d o t(I)-m u * S S$

Finally, we note that the force of infection in the mass action terms can be vectorized out as $\vec{\beta} \vec{I}$. The element of the vector that corresponds to subsystem $a$ is multiplied by $N_{S, S}$ and $N_{S, R}$, whereas the element of the vector that corresponds to $b$ is multiplied by $N_{S, R}$ and $N_{R, S}$. This gives us

bmat $=$ beta $* \mathrm{I}$ * np.array([[SS, SS], [SR, RS] ])
which is of course a matrix representation of

$$
\left(\begin{array}{cc}
\beta_{a} I_{a} S S & \beta_{b} I_{b} S S  \tag{5.17}\\
\beta_{a} I_{a} S R & \beta_{b} I_{b} R S
\end{array}\right) .
$$

Thus our derivative function in its final glory, will look something rather like this:

```
def deriv(t, y, beta, gamma, mu, nu):
    SS, IS, RS, SI, RI, SR, IR, RR = y
    I = np.array([[IS + IR], [SI + RI]])
    gmat = gamma * np.array([[IS, SI], [IR, RI]])
    bmat = beta * I * np.array([[SS, SS], [SR, RS]])
    dNSSdt = nu - (beta * SS).dot(I) - mu * SS
    dNISdt = bmat[0,0] - gmat[0,0] - mu * IS
    dNRSdt = gmat[0,0] - bmat[1,1] - mu * RS
    dNSIdt = bmat[0,1] - gmat[0,1] - mu * SI
    dNRIdt = bmat[1,1] - gmat[1,1] - mu * RI
    dNSRdt = gmat[0,0] - bmat[1,0] - mu * SR
    dNIRdt = bmat[1,0] - gmat[1,0] - mu * IR
    dNRRdt = gmat[1:,].sum() - mu * RR
```

return dNSSdt, dNISdt, dNRSdt, dNSIdt, dNRIdt, dNSRdt, dNIRdt,

dNRRdt

The output of integrating this ODE is presented as Fig. 5.5.

Concise code is almost always better code, and the use of matrices and vectorization can greatly assist with improving code quality and speed of execution. A caveat is that since there are design choices involved in the use of matrices (e.g., what to represent in rows and what in columns), such code should be assiduously documented (as is indeed good practice in all cases).

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch05/transition_ matrix.

### 5.2.3 Multipathogen systems without cross-immunity and with coinfection

In the previous subsection, we primarily examined systems that excluded coinfection; every individual was at most in a single infectious compartment. In this section, we

![](https://cdn.mathpix.com/cropped/2024_06_11_ae648d58b489163f3247g-19.jpg?height=954&width=1046&top_left_y=226&top_left_x=242)

Figure 5.5 Short and long-term dynamics of a two-pathogen system with no cross-immunity and no coinfection, with $\beta_{1}=1.5, \gamma_{1}=1.0, \beta_{2}=0.4$, and $\gamma_{2}=0.2$ and $I_{1}(0)=I_{2}(0)=$ $10^{-6}$. The calculations leading up to this figure are discussed in Computational Note 5.1.

turn to situations in which the infectious compartment of one pathogen is also susceptible to infection by the other. It differs little from the model without coinfection discussed in Subsection 5.2.2, except that it also permits for a coinfected compartment $I, I$ :

$$
\begin{aligned}
& \frac{d N_{S, S}}{d t}=-(\overbrace{\beta_{1} N_{S, S} I_{1}}^{\text {infections with } 1}+\overbrace{\beta_{2} N_{S, S} I_{2}}^{\text {infections with 2 }}), \\
& \frac{d N_{I, S}}{d t}=\underbrace{\beta_{1} N_{S, S} I_{1}}_{\text {new infections }}-\underbrace{\gamma_{1} N_{I, S}}_{\text {recoveries }}-\underbrace{\beta_{2} N_{I, S} I_{2}}_{\text {superinfection with 2 }}, \\
& \frac{d N_{S, I}}{d t}=\underbrace{\beta_{2} N_{S, S} I_{2}}_{\text {new infections }}-\underbrace{\gamma_{2} N_{S, I}}_{\text {recoveries }}-\underbrace{\beta_{1} N_{S, I} I_{1}}_{\text {superinfection with 1 }}, \\
& \frac{d N_{I, I}}{d t}=\underbrace{\beta_{1} N_{S, I} I_{1}}_{\text {superinfections with 1 }}+\underbrace{\beta_{2} N_{I, S} I_{2}}_{\text {superinfections with 2 }}-\underbrace{\gamma_{c} N_{I, I}}_{\text {superinfection recoveries }},
\end{aligned}
$$

$$
\begin{align*}
& \frac{d N_{R, S}}{d t}=\underbrace{\gamma_{1} N_{I, S}}_{\text {recoveries }}-\underbrace{\beta_{2} N_{R, I} I_{2}}_{\text {infections with } 2},  \tag{5.18}\\
& \frac{d N_{S, R}}{d t}=\underbrace{\gamma_{2} N_{S, I}}_{\text {recoveries }}-\underbrace{\beta_{1} N_{I, R} I_{1}}_{\text {infections with } 1}, \\
& \frac{d N_{R, I}}{d t}=\underbrace{\beta_{2} N_{R, I} I_{2}}_{\text {infections with } 2}-\underbrace{\gamma_{2} N_{R, I}}_{\text {complete recoveries }}, \\
& \frac{d N_{I, R}}{d t}=\underbrace{\beta_{1} N_{I, R} I_{1}}_{\text {infections with } 1 \text { from } S, R}-\underbrace{\gamma_{1} N_{I, R}}_{\text {recoveries }}, \\
& \frac{d N_{R, R}}{d t}=\underbrace{\gamma_{2} N_{R, I}}_{\text {recoveries from } R, I}+\gamma_{1} \underbrace{N_{I, R}}_{\text {recoveries from } I, R}+\underbrace{\gamma_{c} N_{I, I}}_{\text {recoveries from coinfections }} .
\end{align*}
$$

The underlying assumption here is that $\beta_{1}$ and $\beta_{2}$ are the probabilities of infection with pathogens 1 and 2 , respectively, regardless of status with respect to the other pathogen. This is appropriate where there is neither significant superinfection exclusion or a significant multipathogen facilitation, i.e., where the coinfection coefficient is around zero.

### 5.2.4 The coinfection matrix

When dealing with multipathogen systems, we are sometimes interested in a simplified picture of relative transmission risk as a function of infection status. The state transition matrix is a useful tool that tells us about the quantities in the compartments, but not all that much about relative risk. The coinfection matrix $\mathbf{C}$ is analogous to a WAIFW matrix (see Subsection 3.1.2), except that it describes the transmission between groups with respect to their pathogenic status over the number of pathogens. The coinfection matrix for two pathogens, $\mathbf{C}^{2}$, for instance, is

$$
\mathbf{C}^{2}=\left(\begin{array}{cccc}
0 & \beta_{S, S \rightarrow S, I} & \beta_{S, S \rightarrow I, S} & 0  \tag{5.19}\\
0 & 0 & 0 & \beta_{S, I \rightarrow I, I} \\
0 & 0 & 0 & \beta_{I, S \rightarrow I, I} \\
0 & 0 & 0 & 0
\end{array}\right)
$$

Coinfection matrices are strictly upper triangular, because the number of pathogens for which the individual is infectious increases monotonically along the axis, and only infectious individuals can transmit the pathogen. The relevance of the coinfection matrix lies in its usefulness to understand how infectious status with respect to one pathogen modulates sustaining infection by another. From this, we can calculate the coinfection coefficient $\zeta_{p, q}$, which represents the relative effect that infection with the $p$-th pathogen has on infection with the $q$-th pathogen. For two pathogens, infection by the first pathogen changes the relative transmission coefficient with respect to the
second by

$$
\begin{equation*}
\frac{\beta_{S, S \rightarrow S, I}}{\beta_{I, S \rightarrow I, I}} \tag{5.20}
\end{equation*}
$$

We may express this more generally.

Definition 5.3 (Coinfection coefficient). Let there be a system of $n$ pathogens, in which we distinguish a set $\mathbb{P}$ of $2^{n}$ distinct combinations of states with respect to each pathogen. Any two elements in $\mathbb{P}$ are associated with a transmission coefficient $\beta_{i, j}$ for $i, j \in \mathbb{P}$. The coinfection coefficient with respect to the $p$-th and the $q$-th pathogen is defined as

$$
\begin{equation*}
\zeta_{p, q}=\log \left(\frac{1}{|\mathbb{P}|} \frac{\sum_{i \in \mathbb{P}[p=S, q=S]} \sum_{j \in \mathbb{P}[p=S, q=I]} \beta_{i \rightarrow j}}{\sum_{k \in \mathbb{P}[p=I, q=S]} \sum_{m \in \mathbb{P}[p=I, q=I]} \beta_{k \rightarrow m}}\right) \tag{5.21}
\end{equation*}
$$

The coinfection coefficient of two pathogens determines the impact of $p$ on subsequent infections with $q$ :

- If $\zeta_{p, q}$ is negative, infection with $p$ makes infection with $q$ less likely. This is seen in certain cases of superinfection exclusion (SIE) (see Subsection 5.1.2).
- If $\zeta_{p, q}$ is zero, infection with $p$ does not make infection with $q$ more or less likely.
- If $\zeta_{p, q}$ is positive, infection with $p$ increases the likelihood of sustaining infection with $q$ upon an encounter. We say that $p$ facilitates $q$.


### 5.2.5 Multipathogen facilitation

In facilitation, infection with one pathogen results in a greater susceptibility for infection by another. This facilitation may be one-sided or two-sided. For instance, HIV facilitates the virulence of Candida albicans, a normally rather commensal opportunistic fungus, but the extent of $C$. albicans infection does not affect HIV itself, thus resulting in a one-sided facilitation [182]. On the other hand, not only is infection with Mycobacterium tuberculosis facilitated with the immune suppression that accompanies HIV infection, but through a mechanism that at this time remains poorly understood, M. tuberculosis infection facilitates the replication of HIV in turn [183]. This makes HIV and M. tuberculosis an example of two-sided facilitation.

The coinfection matrix and the coinfection coefficient (see Subsection 5.2.4) are our primary tools to explore multipathogen facilitation quantitatively. We speak of pathogen $p$ facilitating $q$ if $\zeta_{p, q}$ is positive. In such cases, an encounter between an individual susceptible to both $p$ and $q$ with a $q$-infectious individual is less likely to produce infection than it would if the individual were susceptible to $q$ but infectious with respect to $p$. In general, the coinfection coefficient is not commutative, i.e., $\zeta_{p, q}$ does not necessarily equal $\zeta_{q, p}$. This reflects situations such as the above-mentioned example of HIV and C. albicans.

One-sided facilitation is adequately modeled using a differential- $\beta$ approach, similarly to the way we have tackled risk in host heterogeneities (see Subsection 3.1.2),
with the difference that in this case, the transmission coefficient will change as a function of infectious compartment status.

It is worth noting that in general, only symptomatic disease is capable of facilitating infections. This is a fortiori the case for HIV, where pathogenic facilitation does not emerge until CD4+ counts are sufficiently depleted, signaling full-blown AIDS. Similarly, symptomatic infection may often be forestalled by early initiation of aggressive treatment. For this reason, where multipathogen facilitation is modeled, the phase of infection needs to be accounted for. This is often best accomplished by creating two subcompartments of the infectious compartment: nonfacilitating disease (e.g., HIV infection without significant depression of CD4+ counts) and facilitating disease (HIV infection with immune compromise).

