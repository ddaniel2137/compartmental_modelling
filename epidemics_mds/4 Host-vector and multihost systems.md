# Host-vector and multihost systems Dynamics of host-vector transmission 


#### Abstract

The virus now known as Hendra wasn't the first of the scary new bugs. [...] It made its debut near Brisbane, Australia, in 1994. Initially there were two cases, only one of them fatal. No, wait, correction: there were two human cases, one human fatality. Other victims suffered and died too, more than a dozen-equine victims-and their story is part of this story. The subject of animal disease and the subject of human disease are [...] strands of one braided cord.


Quammen, Spillover: animal infections and the next human pandemic, 2012 [111]

Some pathogens live exciting double lives, with entirely separate life cycles and behaviors in different animals. We see this manifest in three different ways:

1. In pure vector-borne diseases, the hosts are incapable of transmitting the pathogen among themselves. Contact with the vector is necessary for infection. Malaria is an example of pure vector-borne diseases.
2. In human-transmissible zoonoses, the human hosts are also capable of transmitting the infection. Contact with the vector is not necessary for infection, as contact with another infected individual can also pass on the pathogen. Examples of human-transmissible zoonoses include most ebolaviruses, pneumonic plague (Yersinia pestis), and Lake Victoria marburgvirus.
3. Multispecies pathogens can infect both humans and nonhuman animals. Many, but not all, such pathogens allow for both zoonotic infection (animal to human) and zooanthroponotic infection (human to animal). Examples include Rift Valley fever, foot-and-mouth disease and a recently emerging health concern among domestic animals, the zooanthroponotic transmission of tuberculosis [112].

### 4.1 Pure vector-borne diseases

A pure vector-borne disease requires every host to come into contact with a vector; there is, in other words, no interhost transmission. Pure vector-borne diseases therefore rely on abundant vectors that have the appropriate mechanisms for transmissiontypically, transdermal penetration-to pass on the pathogen. Because of their abundance and presence in almost all biomes, haematophagous insects make up the overwhelming majority of vectors. Table 4.1 outlines some examples of pure vector-borne pathogens with their associated vectors.

Table 4.1 Representative examples of pure vector-borne diseases.

| Pathogen | $\overline{\text { Vector }}$ | Disease |
| :---: | :---: | :---: |
| Plasmodium spp. | Anopheles spp. | malaria |
| Trypanosoma brucei | Glossinidae (tsetse) | trypanosomiasis (sleeping <br> sickness) |
| Trypanosoma cruzi | Triatominae | Chagas disease |
| genus Leishmania | sand flies | leishmaniasis |
| Onchocerca volvulus | blackflies (Simuliidae) | onchocerciasis (river <br> blindness) |
| Dengue virus (DENV) | Aedes spp. | dengue fever |
| Chikungunya virus (CHIKV) | Aedes spp. | chikungunya |
| Zika virus (ZIKV) | Aedes spp. | Zika virus disease |
| Borrellia spp. | Ixodes spp. | Lyme disease |
| La Crosse virus (LACV) | Aedes triseriatus | La Crosse encephalitis |

### 4.1.1 Case study: malaria

In 1895 Sir Ronald Ross, then still unknighted and a mere surgeon in the Indian Medical Service, began an extraordinary journey. It would culminate in an 1897 article that would forever change the way we thought about one of humanity's oldest fellow travelers [113]. The paper, which would eventually earn Ross the Nobel Prize in physiology or medicine five years later, proved that malaria was a parasitic disease transmitted by mosquitoes.

Malaria is an infectious disease caused by eukaryotes of the genus Plasmodium spp. Plasmodium is an apicomplexan parasite, with specific cellular forms for effecting life cycle specific tasks. Fig. 4.1 illustrates this life cycle. Upon a mosquito bite, sporozoites (1) enter the human host, and lodge in the liver. This begins the hepatic phase of malaria, which lasts approximately 2-3 weeks. At the end of this stage, the infected hepatocytes burst and release merozoites into the bloodstream (2). This launches the erythrocytic phase of the disease, during which merozoites infect red blood cells and multiply (3). Infected red cells play host to a cycle of asexual reproduction (4). The synchronous waves of merozoite release (and the ensuing immune reaction) are responsible for the hallmark symptom of malaria, namely periodic recurrent fevers (tertian and quartan fever).

Some merozoites differentiate into gametocytes (5), which are ingested when a mosquito bites, or, in the rarefied language of malaria epidemiologists, "takes a blood meal" from an infected human. The gametocytes then multiply in the mosquito (6 and 7), eventually producing sporozoites (8), and as these are transmitted by the next blood meal, the cycle begins anew.

Few diseases have had an impact on human evolution, culture and society on par with malaria $[114,115]$. It is one of the oldest documented infectious diseases. Indeed, it has been hypothesized by Wellems, Hayton, and Fairhurst [116] that the protective effect bestowed by a heterozygous sickle cell allele explains its survival to the modern

![](https://cdn.mathpix.com/cropped/2024_06_11_c8f56f588f7e82d7a0e9g-03.jpg?height=967&width=1180&top_left_y=226&top_left_x=175)

Figure 4.1 Lifecycle of Plasmodium falciparum.

day. As such, malaria has left its footprint on human evolution in a profound way few other diseases have.

Yet its true origins were the matter of considerable controversy. The clue is in the name; the prevailing theory until Ross's discovery was that malaria resulted from mala aria, that is, "bad air." It took the advent of modern evidence-based medical science to challenge this "miasma theory." Ross's elucidation of the role of mosquitoes in the lifecycle of malaria has opened up a new subject for epidemiological consideration: the vector-borne disease. This chapter deals with the modeling of such diseases.

### 4.1.2 The basic dynamics of a vector-borne disease

The hallmark feature of vector-borne diseases is the existence, as the name suggests, of at least one species that acts as a vector. Thus we are no longer preoccupied by a single population, but rather by two populations (planes of transmission), each of which is experiencing a disease process of its own. The epidemic among humans mirrors the epizootic, i.e., the disease process among the vectors.

Definition 4.1 (Planes of transmission). A plane of transmission refers to a set of unique compartments of individuals that play the same role, such as ultimate hosts,
vectors, intermediate vectors, and so on. These individuals may belong to the same species, but do not necessarily have to.

Transmission between individuals that belong to the same plane is referred to as intraplane transmission, whereas transmission between individuals that belong to different planes is referred to as interplane transmission.

There is some debate as to the definition of a vector [117]. For our purposes, however, and for the sake of simplicity, we shall define vectors and hosts in relation to their role within human disease.

Definition 4.2 (Vector). A vector is any living organism that is not itself directly a pathogen, but transmits a pathogen to another organism. We consider that target organism to be the host, noting that this is largely a matter of definitional convenience; vectors themselves play host to the pathogen.

A common misunderstanding is that in a vector-borne disease, the vector is "unaffected" by the pathogen's presence. This may be the case for some pathogens. It appears, for instance, that certain bat species may harbor ebolaviruses without themselves falling ill due to peculiarities of their immune systems that allow for effective (but infectious) immune control of the pathogen $[118,119]$. However, this is by no means a requirement. Indeed, many vectors suffer some loss of fitness due to infestation.

Definition 4.3 (Enzootic and epizootic processes). Most models of host-vector systems have a human host. For this reason, the terms "epidemic" and "endemic" are reserved for the human plane of transmission.

An epizootic is an epidemic process on the vector plane. An enzootic is the equivalent of an endemic disease in the vector plane.

By convention, we will refer to host plane processes as epidemics and endemics, even if they occur in nonhuman animals.

In a pure vector-borne disease, only vectors can transmit the disease to humans. Malaria is an example of a pure vector-borne disease, since it is not generally transmitted between humans. On the other hand, filoviral haemorrhagic fevers, such as Lake Victoria marburgvirus or the Zaire and Sudan ebolaviruses can be passed to humans through zoonotic transfer, but can also pass between humans.

Definition 4.4 (Pure vector-borne disease). In a pure vector-borne disease, there is only interplane transmission.

The key differentiation between pure vector-borne disease and host transmissible zoonoses is, of course, in the mass action term:

- For pure vector-borne diseases, the mass action is driven by the number of susceptible individuals and the infected vector population.
- For human-transmissible zoonoses, the mass action is driven by the number of susceptible individuals and both the infected vector population and the population of infected humans.

![](https://cdn.mathpix.com/cropped/2024_06_11_c8f56f588f7e82d7a0e9g-05.jpg?height=1331&width=1185&top_left_y=231&top_left_x=172)

Figure 4.2 Planes of transmission for a pure vector-borne disease.

It is often helpful to map these planes against each other, as in Fig. 4.2. In a pure vector-borne disease, there is no transmission between either vectors or hosts. Vectors can only acquire infection from a host, and hosts can only acquire infection from a vector. Mathematically formulated, the WAIFW matrix $\mathbf{b}$ of a pure vector-borne pathogen is

$$
\left(\begin{array}{cc}
0 & m  \tag{4.1}\\
n & 0
\end{array}\right)
$$

![](https://cdn.mathpix.com/cropped/2024_06_11_c8f56f588f7e82d7a0e9g-06.jpg?height=668&width=901&top_left_y=233&top_left_x=277)

Figure 4.3 Ross's malaria model. The subscripts $m$ and $h$ denote the mosquito and human compartments, respectively. $\mu_{M}$ is the mortality of mosquitoes. $a$ is the bite rate, $b$ and $c$ are the proportion of bites that transmit infection from mosquitoes to humans and humans to mosquitoes, respectively. $m$ is the number of female mosquitoes per human.

### 4.1.3 The Ross malaria model

There are no limits to the degree of complexity one may, with sufficient time and unfailing enthusiasm, refine any compartmental model. Malaria models attest to this fact: it is far from unusual to find models with dozens of compartments to account for a wide range of processes and states. A gentler introduction into malaria (and more generally, vectored transmission) models is provided by the Ross model, depicted in Fig. 4.3.

The Ross model makes some salient assumptions, one being that mosquitoes, once infected, remain infected for life. This is warranted given the relatively short lifespan of mosquitoes. The dynamics of the infection relies on the interaction between the infectious and susceptible compartments, and is focused around three variables: the bite rate $a$ (the number of bites per unit time), the likelihood that a bite passes an infection from a mosquito to a human $b$, and the likelihood that a bite passes an infection from a human to a mosquito $c$.

We may conceive of the infectious process as follows: For unit time, there are $a$ interactions per mosquito. From the perspective of the mosquito, the likelihood of contracting malaria from a human, per interaction, is governed by two factors: the likelihood of biting someone with malaria and the likelihood that the bite will result in transmission. The former is, of course, $I_{h}$, the number of humans who are infected, and thus capable of infecting the mosquito. The latter is the rate $c$. Together, acI ${ }_{h}$ represent the total volume of infections per unit time. $1-I_{m}$ represents the number of susceptible mosquitoes. As such, we see in $\operatorname{ac} I_{h}\left(1-I_{m}\right)$ the mass action term $\beta S I$ (in the order of $\beta I S$ ).

From the human perspective, the equation is largely the same, except in this case, we must also consider that mosquitoes are rather more abundant. Because $S_{m}, I_{m}$, $S_{h}, I_{h}$, and $R_{h}$ are all proportions, rather than actual numbers, we must account for this difference through a factor. $m$ thus denotes the number of female mosquitoes per human (since only female mosquitoes bite). Then, the mass action term for humans will be $\operatorname{abm} I_{m}\left(1-I_{h}\right)$, where $I_{m}$ corresponds to $I$ and $1-I_{h}$ corresponds to $S$ from previous formulations.

Based on this, we can write the WAIFW matrix of Ross's malaria model as

$$
\left(\begin{array}{cc}
0 & \overbrace{a c I_{h}\left(1-I_{m}\right)}^{\text {human-to-mosquito }}  \tag{4.2}\\
\underbrace{a b m I_{m}\left(1-I_{h}\right)}_{\text {mosquito-to-human }} & 0
\end{array}\right) .
$$

As is expected, this is a hollow matrix, since there is no intraplane transmission. Thus the whole system of differential equations works out to

$$
\begin{align*}
\frac{d S_{m}}{d t} & =\mu_{m}-a c I_{h}\left(1-I_{m}\right)-\mu_{m} S_{m} \\
\frac{d S_{h}}{d t} & =\mu_{h}-a b m I_{m}\left(1-I_{h}\right)-\mu_{h} S_{h} \\
\frac{d I_{m}}{d t} & =a c I_{h}\left(1-I_{m}\right)-\mu_{m} I_{m}  \tag{4.3}\\
\frac{d I_{h}}{d t} & =a b m I_{m}\left(1-I_{h}-R_{h}\right)-\gamma I_{h}-\mu_{h} I_{h} \\
\frac{d R_{h}}{d t} & =\gamma I_{h}-\mu_{h} R_{h}
\end{align*}
$$

## Computational Note 4.1 Implementing the Ross-MacDonald model

By now, we have sufficient practice in solving ODEs numerically to be able to omit a few moving parts. In particular, we can reduce the model and track only the infectious compartments:

```
def deriv(t, y):
    I_m, I_h = y
    dImdt = a * c * I_h * (1 - I_m) - mu * I_m
    dIhdt = a * b * m * I_m * (1 - I_h) - gamma * I_h
    return dImdt, dIndt
```

We will be using some of the sensible defaults from Table 4.2 for this model:

$$
\begin{aligned}
& \text { I_m_0 }=0.2 \\
& \text { I_h_0 }=0.005 \\
& a=0.1 \\
& b=0.2 \\
& c=0.5 \\
& m=10 \\
& \text { gamma }=0.05 \\
& m u=0.05 \\
& \text { y_0 }=\text { (I_m_0, I_h_0) }
\end{aligned}
$$

As we can see from solving this system of differential equations, a stable equilibrium emerges in the absence of human mortality and births both human and mosquito. This is convenient and somewhat accurate in the short term, but including a birth term might be important to accommodate population growth.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch04/ross_ macdona 7d.

Fig. 4.4 shows the convergent dynamics of the model. Streamplots are useful tools for understanding the convergent behavior of a system of differential equations, and are for this reason widely used in engineering and mathematics. They do, however, take some practice to read.

The best way of approaching streamplots is to consider their relationship to phase portraits, which we have discussed in Subsection 2.3.3. Recall that a phase portrait shows a single solution of a differential equation by plotting two values against each other. One may consider a streamplot to be a "generalized" version of a phase portrait,

Table 4.2 Some sensible default values for malaria models, based on Mandal, Sarkar, and Sinha [120].

| Symbol | Parameter | Value |
| :--- | :--- | :--- |
| $a$ | bite rate | $0.1-0.05 d^{-1}$ |
| $b$ | $m \rightarrow h$ transmission | $0.2-0.5$ |
| $c$ | $h \rightarrow m$ transmission | 0.5 |
| $\gamma$ | recovery rate, human | $0.05 d^{-1}$ |
| $m$ | female mosquitoes per human | $0.5-40$ |
| $\mu_{h}$ | death rate, human | $0.017 y^{-1}$ |
| $\mu_{m}$ | death rate, mosquito | $0.05-0.5 d^{-1}$ |
| $\tau_{m}$ | latent period, mosquito | $5-15 \mathrm{~d}$ |
| $\tau_{h}$ | latent period, human | $10-100 \mathrm{~d}$ |

![](https://cdn.mathpix.com/cropped/2024_06_11_c8f56f588f7e82d7a0e9g-09.jpg?height=985&width=1037&top_left_y=226&top_left_x=246)

Figure 4.4 Streamplot of the Ross-MacDonald model for the default values in Table 4.2.

in which the starting values are varied. Thus the plot in Fig. 4.4 shows a number of different starting values of $I_{m}$ and $I_{h}$. This gives a visual representation to the more abstract vector field that governs the two interacting quantities. Given a value of $I_{m}$ and $I_{h}$, you can estimate the trajectory of the phase portrait for those values by tracing the nearest line in its direction (noted by the arrows).

## Computational Note 4.2 Creating streamplots

Streamplots are a beautiful and convenient way to show more than a single phase profile of a system, and generalize it to show all potential phase profiles, given certain starting values.

Drawing streamplots is not difficult, but it requires some tricks. First and foremost, we need to select two differential equations out of the whole system. We will be able to vary their starting quantities, but not much else. Thus all of that is deemed constant.

In this case, we only have two differential equations. We begin by setting up a grid, which will give us the points at which we will "sample" the values of the vector field. Since this is a numerical solution, we are essentially calculating the values for $\frac{d I_{m}}{d t}$ and $\frac{d I_{h}}{d t}$ at every point.

The function np.mgrid creates a mesh grid at equally spaced distances; it is essentially a convenience method to give us the product space of two np. 1 inspaces.

i_h, i_m = np.mgrid[0:1:0.01, $0: 1: 0.01]$

Next, we define the two differential equations, in terms of the two axes created in the previous step:

```
u = a * c * i_h * (1 - i_m) - mu * i_m
v=a* b*m* i_m*(1 - i_h) - gamma * i_h
```

Finally, we can move on to plotting:

```
fig = plt.figure(facecolor="w", figsize=(6, 6))
ax = fig.add_subplot(111, axisbelow=True)
ax.streamplot(i_m, i_h, u, v, density=1, color=u + v)
ax.set_xlabel("$ I_m $")
ax.set_ylabel("$ I_h $")
```

A notebook implementing the contents of this Computational Note is available on
the book's companion Github repository in the folder / ch04/ross_ macdonald.

### 4.1.4 Basic reproductive number of the Ross malaria model

We may be interested in calculating $\Re_{0}$ for the Ross malaria model. If a human is infected, they will be infectious for $\tau=\gamma^{-1}$, so the total number of bites suffered during the infectious period will be $\frac{a}{\gamma}$. For each of these bites, we assume the mosquito has its full lifespan, $\mu_{m}^{-1}$ left. Thus each of those mosquitoes will go on to bite $\frac{a}{\mu_{m}}$ times.

The likelihood that biting an infectious human will transfer the infection is, of course, $c$, so the total number of bites by infectious mosquitoes attributable to the initial human case is $\frac{a c}{\gamma}$. Of these, only a fraction, namely, $b$, will be transmitted to another human. Consequently, the

$$
\begin{equation*}
\mathfrak{R}_{0}=\frac{a^{2} b c m}{\gamma \mu_{m}} \tag{4.4}
\end{equation*}
$$

### 4.1.5 Stability of the Ross malaria model

From examining the infectious subsystem

$$
\begin{align*}
& \frac{d I_{m}}{d t}=a c I_{h}\left(1-I_{m}\right)-\mu_{m} I_{m} \\
& \frac{d I_{h}}{d t}=a b m I_{m}\left(1-I_{h}-R_{h}\right)-\gamma I_{h}-\mu_{h} I_{h}
\end{align*}
$$

we can obtain the Jacobian of this system as

$$
\mathbf{J}_{I_{m}, I_{h}}=\left(\begin{array}{cc}
-a c I_{h}-\mu_{m} & a c\left(1-I_{m}\right)  \tag{4.6}\\
\operatorname{abm}\left(1-I_{h}-R_{h}\right) & -\gamma-a b m I_{m}-\mu_{h}
\end{array}\right)
$$

Since $a, b$, and $c$ are by biological necessity positive, and $1-I_{m}$ and $1-I_{h}-R_{h}$ are also positive due to the population partition property, whereby $I_{m}+S_{m}=1$ and $I_{h}+R_{h}+S_{h}=1$, both off-diagonal elements of the Jacobian are positive. We denote such a matrix, where all off-diagonal elements are positive, as a Metzler matrix. Where the Jacobian of a system is a Metzler matrix, the system is described as monotone, and if the matrix is irreducible, the system is strongly monotone. If a matrix is monotone, then, subject to some conditions,

1. the disease-free equilibrium will be globally asymptotically stable for $\mathfrak{R}_{0} \leq 1$, and
2. the endemic equilibrium will be globally asymptotically stable for $\Re_{0}>1$.

### 4.1.6 Temporal dynamics between planes

An important feature of some pure vector-borne diseases is that relative to the host, the vectors may have very short lifespans with pronounced seasonalities. An example is Aedes aegypti, an important vector of a number of pathogens, including Zika virus (ZIKV), Chikungunya virus (CHIKV), yellow fever, and the virus responsible for Eastern equine encephalitis. The mean lifespan of Aedes aegypti is, according to Meena [121], 19.94 days. Che-Mendoza et al. [122] describe the seasonality of Aedes aegypti populations as sinusoidal, peaking during the early rainy season, beginning to decline towards its end, and reaching lowest levels during the dry season. The reason why these temporal dynamics are important in modeling vector-borne infectious diseases is twofold:

1. Differences in the population of vectors affect the mass action term. The mass action term describes the likelihood of contact, and thus transmission of the pathogen. If there are fewer vectors, the number of host-vector interactions will decrease significantly.
2. We generally assume that vectors are born susceptible. The number of infectious vectors can be quite rapidly depleted due to natural mortality.

![](https://cdn.mathpix.com/cropped/2024_06_11_c8f56f588f7e82d7a0e9g-12.jpg?height=463&width=1197&top_left_y=221&top_left_x=122)

Figure 4.5 The Ross malaria model with time-dependent birth rates of the vector for $\phi_{0}=$ 0.01 and $\phi_{1}=0.05$. The period of forcing is annual and the phase $\psi$ is -90 days. All other parameters are as described in Computational Note 4.1.

Consider the Ross model, ignoring human births and deaths, in which mosquitoes are born according to a time-dependent forcing function:

$$
\begin{align*}
\frac{d I_{m}}{d t} & =\overbrace{\phi(t)}^{\text {time-dependent birth term }} \operatorname{ac} I_{h}\left(1-I_{m}\right)-\mu I_{m} \\
\frac{d I_{h}}{d t} & =a b m I_{m}\left(1-I_{h}\right)-\gamma I_{h},  \tag{4.7}\\
\phi(t) & =\overbrace{\phi_{0}}^{\text {base birth rate }}(1+\overbrace{\phi_{1}}^{\text {amplitude }} \sin (\frac{2 \pi}{365}(t-\underbrace{\psi}_{\text {phase }}))) .
\end{align*}
$$

The seasonality induced by the time dependent birth rate-via $\phi(t)$-does not only induce fluctuations in the vector, but also in the infected host population. This can create complex resonance and interference phenomena when the birth rate of the host population, too, is temporally dependent. (See Fig. 4.5.)

### 4.1.7 Parameter inference in vector-borne diseases

Vector-borne diseases confront us with the problem that a large number of crucial parameters are quite difficult to ascertain. Humans, for instance, are generally known to their governments and when unwell, seek care. Neither of those could be said for, say, mosquitoes. A task such as estimating the number of mosquitoes in a given area is daunting. Some factors of the Ross-McDonald model can be approximated with reasonable accuracy, such as the lifespan of a mosquito or the length of the viraemic period in humans.

Inferential methods help us where we run out of useful empirical data. Bayesian parametric inference is the currently dominant technique in this field. The Bayesian approach encompasses a diversity of solutions, but they all share a basic reasoning:
given a time series of observations $Y$, what is the posterior distribution of the parameter $\theta$ of the vector-valued function $\hat{f}(\theta)$ so as to minimize $\sum_{i=1}^{|Y|} \delta\left(Y_{i}, \hat{f}(\theta)_{i}\right)$, where $\delta\left(v, v^{\prime}\right)$ is a distance metric?

## Computational Note 4.3 Inferring parameters for a vector-borne disease

Dengue fever is a disease caused by the dengue virus (DENV), endemic throughout the tropics. Like malaria, dengue is a mosquito-borne disease, specifically transmitted by Aedes spp.. Similarly to malaria, it is not horizontally transmitted among either humans or mosquitoes, but rather require interplane transmission, making it a pure vector-borne disease. In most cases, it is an unpleasant albeit survivable illness that manifests as a 3-4 day long viraemia. In rare cases, it may present as dengue haemorrhagic fever (DHF), which is a rather more severe.

A good approximation of the dynamics of dengue fever is the system

$$
\begin{align*}
\frac{d S_{H}}{d t} & =\mu_{H} N_{H}-b \beta_{V, H} S_{H} \frac{I_{V}}{m N_{H}}-\mu_{H} S_{H} \\
\frac{d I_{H}}{d t} & =b \beta_{V, H} S_{H} \frac{I_{V}}{N_{H}}-\gamma I_{H}-\mu_{H} I_{H} \\
\frac{d S_{V}}{d t} & =\mu_{V} m N_{H}-\beta_{H, V} S_{V} \frac{I_{H}}{N_{H}}-\mu_{V} S_{V}  \tag{4.8}\\
\frac{d I_{V}}{d t} & =b \beta_{H, V} S_{V} \frac{I_{H}}{N_{H}}-\mu_{V} I_{V}
\end{align*}
$$

where $b$ is the bite rate, $m$ is the number of female mosquitoes per human, and $\beta_{V, H}$ and $\beta_{H, V}$ are the respective transmission rates upon contact from vector to host and host to vector.

There are many ways of multiparameter inference, but Markov chain Monte Carlo (MCMC) methods are among the most popular. The idea of MCMC to estimate parameters is quite simple: given some priors (i.e., our educated guesses as to the values of model parameters) and evidence (the actual number of cases), what is the most likely vector $\theta$ that comprises the model's parameters? In other words, what values of $\theta$ maximize the posterior probability density function?

Emcee [123] is a Python package that implements the affine invariant MCMC ensemble sampler described in Goodman and Weare [124]. In its syntax and its approach, it is rather different from other MCMC samplers. First, it defines priors not as probability distributions but as binary ranges. Considering the model above, we are interested in inferring $\beta_{V, H}, \beta_{H, V}, m$ (the number of female mosquitoes per human), $b$ (the bite rate), and $\frac{I_{V}(0)}{N_{V}}$, the fraction of infected mosquitoes at the start (denoted as pV0 in the model). These together make up our parameter vector $\theta$. Whereas in other tools (such as PyMC), we would ordinarily need to have a good guess as to the distribution from which each element
of $\theta$ is drawn, Emcee operates on a much simpler principle: the $\log$ prior of $\theta$ is defined as a binary function, being zero-valued if the value is within the range of acceptable priors, and $-\infty$ otherwise:

```
def log_prior(theta):
    beta_VH, beta_HV, m, b, pVO = theta
    if 0 < beta_VH < 0.66 and \
        0 < beta_HV < 0.66 and \
        1e2 < m < 1e4 and \
        0<b < 30 and \
        0 pV0 < 0.01:
        return 0.0
    else:
        return -np.inf
```

Next, we need to define the log likelihood function. Given a $\theta$ and a number of points in time ( $\mathrm{t}$ ), we define this function as

$$
\begin{equation*}
\ln \ell(\theta, t, y)=-\frac{1}{2 t} \sum_{i=1}^{t} \sum_{j=1}^{|y|}\left(y_{j}-\hat{y}_{j}(\theta)\right)^{2} \tag{4.9}
\end{equation*}
$$

where $y$ is the vector of actual infectious cases in humans, and $\hat{y}_{j}(\theta)$ is the number of infectious cases in humans at time $t$ given $\theta$. In Bayesian terms, this function gives us $p(\theta \mid y)$.

Finally, we need to build the function for the log probability. Recall that our function for the prior returned a finite value if (and only if) each element of $\theta$ was within the range of permissible values. This allows us to express log probability as the result of the log_1ikelihood() function if the log prior is within the permissible range, and $-\infty$ otherwise:

```
def log_probability(theta, t, data):
    1p = log_prior(theta)
    if not np.isfinite(1p):
        return -np.inf
    e1se:
        return log_likelihood(theta, t, data)
```

We now need to create the initial position matrix. This is an $m \times n$ matrix, where $m$ is the number of "walkers" and $n$ the number of parameters, i.e., $|\theta|$. An efficient way to get our model to work relatively fast is to provide some initial guesses for $\theta$, and perturb them by adding a small random number:

```
pos = np.array([0.3, 0.3, 200, 1/3, 0.001]) \
    + 1e-4 * np.random.randn(32, 5)
```

Because of broadcasting (see Subsubsection A.11.1.3), this will give us a matrix of 32 independent "guesses" for each of the five variables we are estimating.

We are now ready to initialize the sampler:

```
samp1er = emcee.Ensemb1eSamp1er(nwa1kers=pos.shape[0],
                                ndim=pos.shape[1],
    log_prob_fn=1og_probabi1ity,
    args=(np.arange(1, 1en(data)),
        data.to_numpy()))
sampler.run_mcmc(pos,
    nsteps=25_000,
    progress=True)
```

samp1er.get_b1obs(discard=1_000)

The method sampler.get_chain(flat\$=\$True) provides a convenient way to access the results, and taking the 50th percentile of the values gives a good estimate of what the median estimate is for each of the values:

```
beta_VH_hat, beta_HV_hat, m_hat, b_hat, pV0_hat = np.percentile(
    samp1er.get_chain(f1at=True),
    50,
    axis=0)
```

Fig. 4.6 shows a corner plot fitted for cases of dengue in the Ilocos Region of the Philippines between June 2016 and July 2017. Though the values are somewhat different from what we would expect (in particular, the number of female mosquitoes per human has a fat-tailed posterior distribution, suggesting that the model did not converge with particularly high confidence to a singular value), the example above shows the usefulness of MCMC parameter estimation techniques. Where real-world data is available, parameter estimation can provide fairly good estimates of parameters that are often costly and/or difficult to empirically determine.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder I ch04/ host_ vector_ pe.
![](https://cdn.mathpix.com/cropped/2024_06_11_c8f56f588f7e82d7a0e9g-16.jpg?height=1192&width=1080&top_left_y=230&top_left_x=186)

$\beta_{V, H}$

$\beta_{H, V}$

$m$

$\frac{I_{V}(0)}{N_{V}}$

Figure 4.6 Corner plot of parameter estimates for dengue fever in the 2016-17 dengue season in the Ilocos Region, Republic of the Philippines. Case data obtained from the Epidemiology Bureau of the Department of Health, Republic of the Philippines, obtained via the Humanitarian Data Exchange of the United Nations Office for the Coordination of Humanitarian Affairs.

### 4.2 Zoonotic disease

In the context of malaria, the human and the enzootic planes had no within-plane infectivity. For instance, in the malaria model we examined in Section 4.1, mosquitoes (the epizootic or vector plane) and humans (the epidemic or host plane) each could only "communicate" the pathogen between each other through host-vector interactions. In this section, we will deal with infectious diseases where a pathogen, once it passes through zoonotic transfer (sometimes called a spillover event) into the human (or other host) population, can be transmitted within that population directly. For this
reason, a single zoonotic event can touch off a wildfire of infection within the human population. Such events do not necessarily have to be frequent or even probable; these spillover events may in fact be quite rare, but a single spillover event can spark an epidemic that spreads like a wildfire with a death toll in the thousands. The case study of the West African ZEBOV outbreak, in Subsection 4.2.1, is a sad illustration of this effect.

## Practice Note 4.1 One Health

In 2005 the British Medical Journal and the Veterinary Record published an influential joint issue, titled Human and animal health: strengthening the link (or vice versa, for readers of the Veterinary Record). The decades preceding this joint publication saw a number of zoonotic outbreaks that highlighted the interdependence of animal and human populations. As Gibbs's 2014 historical retrospective noted, the outbreaks of bovine spongiform encephalitis (BSE), highly pathogenic avian influenza (HPAI) H5N1, and SARS shone a light on the interdependence of the health of human and animal populations [125]. In 2004 the Manhattan Principles laid the groundwork for what it called One Health: an interdisciplinary framework for public health that considers human and animal populations alike. In the wake of the COVID-19 pandemic, the Berlin Principles updated the Manhattan Principles, calling on world leaders to "recognize and take action to retain the essential health links between humans, wildlife, domesticated animals and plants, and all nature; and ensure the conservation and protection of biodiversity which, interwoven with intact and functional ecosystems, provides the critical foundational infrastructure of life, health, and well-being on our planet" [126].

Climate change, deforestation, and habitat loss (on the consequences of which see also Subsection 4.2.1) have increased the frequency of human-animal encounter events, including with species that are immunologically highly suitable to act as reservoir hosts for a wide range of pathogens [127]. The global commerce in animals and animal products has also greatly increased the potential reach of pathogens. Finally, health disparities and global differences in public health funding have resulted in an uneven ability to respond to a newly emergent pathogen. The One Health perspective has been a significant shift in integrating the domains of human and animal health, along with concerns of conservation ecology and biodiversity. This interdisciplinary approach may well hold the promise of bringing both human and veterinary epidemiological tools to bear on zoonotic disease.

### 4.2.1 Case study: Zaire ebolavirus and the 2013-16 West African outbreak

Zaire ebolavirus (ZEBOV) is a filovirus that causes a severe and often lethal viral haemorrhagic fever in primates and humans. Since the first documented outbreak in

Yambuku [128], there have been at least eight major outbreaks across Western Africa. The reservoir host of ZEBOV has not yet been definitively identified, but is widely presumed to be a bat species [129].

Emile Ouamouno, a young boy aged two, lived in the village of Meliandou, in Guinea's Nzerekore district. On 2 December 2013, he came down with a high fever, vomiting, and tarry stools suggestive of intestinal haemorrhaging. On Friday, his life was tragically cut short by what was not much later identified as an ebolavirus and presumed to be ZEBOV. It started a rapid chain of propagation, affecting first his close relatives, then spiralling out of control. By mid-May, it was in Sierra Leone, Liberia, and the Ivory Coast. In the waning days of July 2014, it entered Nigeria. Not long after, it spread across the globe, along the economic and commercial arteries that keep the global economy functioning: air routes, shipping, and freight.

By the time the epidemic burned out, over 11,300 were dead, but it all began with a single bite. Research into the zoonotic origins of the 2013-16 West African ZEBOV outbreak has traced the infection back to the index case playing under a hollow tree, where Angolan free-tailed bats (Mops condylurus) were roosting [130]. It is assumed that he was bitten or otherwise infected by the bats sometime around December 2013, and succumbed to Ebola virus disease not much later. His family were among the first secondary cases. Traditional funeral practices, which involve close contact with the decedent's body, and thus ample opportunity for secondary transmission, have also played a significant role in the epidemic (see Practice Note 2.6).

The West African ZEBOV outbreak highlights the incredible human cost that circulating zoonoses can exact. For that reason alone, we should turn our attention to zoonotic diseases that are also human-transmissible. Unlike exclusively vector-borne diseases, which only affect persons who have come into direct contact with the vector or reservoir host, human-transmissible zoonoses operate on "parallel planes," capable both of transmission from an animal to a human and from human to human. Indeed, most human-transmissible zoonoses are primarily transmitted by humans. (See Fig. 4.7.)

A spillover event is defined as an event where a pathogen jumps from an affected population, typically but not necessarily a reservoir host, to a different species that until then is largely naive to the pathogen. After the spillover event, such as the unfortunate encounter of the index case with the Angolan free-tailed bats, much of the transmission happens between humans. In this section, we will discuss ways to separately model the reservoir host and the human "planes" of transmission, and quantify interactions between them.

### 4.2.2 Modeling host-transmissible zoonoses

Our models of pure vector-borne diseases have so far focused on pathogens where transmission was exclusively interplane, i.e., every transmission event occurred between individuals that belonged to different populations. In this subsection, we turn our attention to pathogens that have at least one intraplane mode of transmission (Fig. 4.8).

![](https://cdn.mathpix.com/cropped/2024_06_11_c8f56f588f7e82d7a0e9g-19.jpg?height=617&width=931&top_left_y=219&top_left_x=299)

Figure 4.7 Human-transmissible zoonotic cycles: the example of Zaire ebolavirus (ZEBOV). ZEBOV is enzootic in the reservoir host, a bat species, who transmit the pathogen vertically and horizontally, without exhibiting symptoms. Interactions between the enzootically affected population and the human population can lead to spillover events, which can touch off chains of transmission to other humans, including healthcare workers, who are at a particularly high risk of contracting ZEBOV from infected cases.

The rate of new infections in each plane is governed by the interactions between that plane's susceptible population with all infectious populations, multiplied by a given value of $\beta$. This is, of course, quite similar to the way we dealt with host heterogeneities (see Subsection 3.1.2). For two planes $H$ and $V$, with closed populations,

![](https://cdn.mathpix.com/cropped/2024_06_11_c8f56f588f7e82d7a0e9g-19.jpg?height=344&width=597&top_left_y=1381&top_left_x=255)

Or, more generally, we may say that given $n$ classes and the $n \times n$ WAIFW matrix $\mathbf{b}$, the mass action term for $I_{m}$ (for $m \in n$ ) will be

$$
\begin{equation*}
\sum_{i=0}^{n} \mathbf{b}_{m, i} S_{m} I_{i} \tag{4.11}
\end{equation*}
$$

Depending on the structure of the infection, we may model human-transmissible zoonoses either as SI+S(E)IR or SIR+S(E)IR models.

![](https://cdn.mathpix.com/cropped/2024_06_11_c8f56f588f7e82d7a0e9g-20.jpg?height=1283&width=1145&top_left_y=224&top_left_x=157)

Figure 4.8 Planes of transmission for a zoonotic disease with limited or no transmission from the endemic to the enzootic plane but active transmission both within planes and from the enzootic to the endemic plane.

- In the SI+S(E)IR approach, we assume that infection is lifelong for the vector. This is warranted, in general, in two cases: vectors with relatively short lifespans and infections that significantly reduce the vector's lifespan.
- In the SIR+S(E)IR approach, our assumption is that vectors, too, can recover.


### 4.2.3 Reservoir hosts and reinfection

A zoonotic infection that has intraclass transmission on the vector plane has a "reservoir host," a host in which it can persist for a long time. Typically, a reservoir host

![](https://cdn.mathpix.com/cropped/2024_06_11_c8f56f588f7e82d7a0e9g-21.jpg?height=482&width=1200&top_left_y=216&top_left_x=169)

Figure 4.9 Size of the infectious compartments on the host and vector planes for a SIR+SI zoonosis model. The parameters of the model are those given in Computational Note 4.5.

suffers no significant reduction in evolutionary fitness from the infection's presence. Bats, for instance, act as reservoir hosts for certain filoviruses without exhibiting symptoms due to effective immune regulation [118].

The consequence of a reservoir host is that interactions with it can always spark off new chains of human transmission. Consider Lake Victoria marburgvirus (MARV): it is endemic (often maternally transmitted) in the vector population, and may be spread to the human (host) population through bites or the consumption of diseased animals. Among humans, it may be transmitted through bodily fluids. It only takes a single interaction between the human host and the vector to touch off a chain of transmission. In some cases, this will result in a single human case [131], whereas in other instances a longer chain of transmission can establish itself on the host plane. The consequence is that such infections can disappear in the host population altogether, then reappear after a short while.

From an evolutionary standpoint, zoonotic transmission allows a pathogen to afflict a population in which it could not otherwise persist. Consider a SI+SIR model, in which vectors do not recover from their infectious state:

$$
\begin{align*}
\frac{d S_{H}}{d t} & =\mu_{H}-\beta_{H, H} S_{H} I_{H}-\varrho \beta_{V, H} S_{H} I_{V}-\mu_{H} S_{H} \\
\frac{d S_{V}}{d t} & =\mu_{V}\left(1-m_{v}\right)-\beta_{V, V} S_{V} I_{V}-\varrho \beta_{H, V} S_{V} I_{H}-\mu_{V} S_{V} \\
\frac{d I_{H}}{d t} & =\varrho \beta_{V, H} S_{H} I_{V}+\beta_{H, H} S_{H} I_{H}-\gamma I_{H}-\mu_{H} I_{H}  \tag{4.12}\\
\frac{d I_{V}}{d t} & =\mu_{V} m_{V}+\beta_{V, V} S_{V} I_{V}+\varrho \beta_{H, V} S_{V} I_{H}-\mu_{V} I_{V}
\end{align*}
$$

where $\varrho$ is the encounter rate between hosts and vectors.

It follows that in such a model, $\Re_{0}$ will be composed of two factors: host-to-host transmission and host-to-vector transmission. The first component is, of course,

$$
\begin{equation*}
\mathfrak{R}_{0, H H}=\frac{\beta_{H, H}}{\gamma+\mu_{H}} \tag{4.13}
\end{equation*}
$$

To this, we add secondary cases in humans that are attributable to each case by way of indirect transmission. We account for three modes of indirect transmission via the enzootic plane:

1. Vectors who obtain infection from humans and pass it on to other humans directly (HVH transmission),
2. Vectors who obtain infection from humans, then have $\varrho_{V}$ interactions with other vectors, who then pass it on to humans (HVVH transmission),
3. Vectors who are female and obtain infection, then pass it on vertically to their offspring (vertical transmission).

These correspond to each of the terms in

$$
\begin{align*}
\Re_{0, H V}=\frac{1}{\gamma+\mu_{V}} & (\underbrace{\varrho^{2} \beta_{H, V} \beta_{V, H}}_{\text {HVH transmission }} \\
& +\underbrace{\varrho^{2} \varrho_{V} \beta_{H, V} \beta_{V, V} \beta_{V, H}}_{\text {HVVH transmission }}  \tag{4.14}\\
& +\underbrace{\frac{1}{2} \varrho^{2} \beta_{H, V} \beta_{V, H} \mu_{V} m_{v}}_{\text {vertical transmission }})
\end{align*}
$$

$m$ is the likelihood of vertical infection, and $\varrho_{V}$ is the vector-to-vector encounter rate, which primarily depends on the vector group size, whereas the absolute host-vector encounter rate is generally related to $\frac{N_{V}}{N_{H}}$, that is, the relative number of vectors per host within reach of each other. Together, this gives us the basic reproductive number of a zoonotic disease with horizontal and vertical transmission as

$$
\begin{equation*}
\mathfrak{R}_{0}=\frac{\beta_{H, H}}{\gamma+\mu_{H}}+\frac{\varrho^{2} \beta_{H, V} \beta_{V, H}}{\gamma+\mu_{V}}\left(1+\frac{\varrho_{V} \beta_{V, V}}{\mu_{V}}+\frac{\mu_{V} m_{V}}{2}\right) \tag{4.15}
\end{equation*}
$$

## Computational Note 4.4 Managing complex models with structures

Compartmental models of zoonotic disease are somewhat notorious for their complexity. Each plane of transmission is a model in its own right, with all its panoply of parameters. It can get quite difficult to keep track of these. Consider the model that yielded Fig. 4.9. Its starting conditions were

```
beta_HH = 0.01
beta_HV = 0.01
beta_VV = 1.225
beta_VH = 0.01
S_H_O = 1
```

```
S_V_0 = 0.9
I_H_O = 0
I_V_0 = 0.1
mu_I_V = 0.45
mu_I_H = 0.01
gamma_H, gamma_V = 1/30, 0
mu_V, mu_H = 5/365, 0.05/365
```

Note that this is in fact a simplified version of the model, since we do not track the recovered compartment. The value of gamma_V $=0$ reflects the fact that vectors do not recover. If the lifespan of vectors is sufficiently short, almost always the case for arboviruses and, often enough, the case for most other vectors by a fair degree of approximation, one may consider vectors to be infectious for life.

To manage this array of parameters, it helps to write the derivative function as accepting three tuples:

- beta, which comprises each of the values for $\beta$,
- gamma, which comprises each of the values for $\gamma$, and
- mu, for the birth and mortality rates in the model.

We thus specify the model as follows:

```
def deriv(t, y, beta, gamma, mu):
    S_H, S_V, I_H, I_V = y
    gamma_H, gamma_V = gamma
    beta_HH, beta_HV, beta_VV, beta_VH = beta
    mu_H, mu_V = mu
    dShdt = mu_H - (beta_HH * S_H * I_H + beta_HV * S_H * I_V) \
            - mu_H * S_H
    dSvdt = mu_V - (beta_VV * S_V * I_V + beta_VH * S_V * I_H)\
        - mu_V * S_V
    dIhdt = (beta_HH * S_H * I_H + beta_HV * S_H * I_V) - \
            gamma_H * I_H - mu_H * I_H - mu_I_H * I_H
    dIVdt = (beta_VV * S_V * I_V + beta_VH * S_V * I_H) - \
            gamma_V * I_V - mu_V * I_V - mu_I_V * I_V
```

return dShdt, dSvdt, dIhdt, dIvdt

The necessary corollary of this is that when we invoke our solver (in this case, solve_ivp, but the point applies equally well for odeint), we must provide the tuples we deconstruct in the beginning of our derivative function as such:

```
res = solve_ivp(fun=deriv,
    t_span = (0, 1000),
    y0=y_0,
    max_step=1,
    method="BDF",
    args=(
    (beta_HH, beta_HV, beta_VV, beta_VH),
    (gamma_H, gamma_V),
    (mu_H, mu_V)
        )
    )
```

A function that takes too many arguments can get clunky and hard to maintain. It is also considered by some to be generally unsightly code. Specifying tuple inputs can clarify the process and ensure more maintainable and legible code.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch04/ ross_ macdona 7 d.

In most cases, $I_{v}$ outnumbers $I_{h}$ quite significantly. Therefore even where human transmission is quite modest, the disease can persist if there is a significant transmission among reservoir hosts. By way of example, ignoring incidents of laboratory accidents, there have been, between 1975 (the first natural case) and 2021, 11 instances of MARV outbreaks in human populations. These correspond to 11 spillover events over the span of forty-six years, over a population at risk of approximately $800 \mathrm{~m}$ (with one instance where both MARV and Ravn virus (RAVV), a related marburgvirus, experienced quasi-simultaneous spillover events over the same population at roughly the same time [132]). This translates to a spillover rate of $3.26 \times 10^{-10}$ per person per year. Few of these spillover events have caused more than a handful of human cases (with the 2004-2005 Angolan outbreak and the 1998-2000 DRC outbreak, each of which had cases in the hundreds, being more exceptions than the rule). Human-to-human chains of transmission are very short, largely due to the severe course of the disease and rather unambiguous signs of illness. Yet MARV is alive and well, emerging from its reservoir host every few years to infect humans (and, presumably, more often infecting nonhuman animals as well, which however generally goes unrecorded). A serosurvey by Paweska et al. [133] of Egyptian rousettes (Rousettus aegyptiacus, the putative reservoir host of MARV [134]) in South Africa showed $71.6 \%$ of adult rousettes to be seropositive for MARV. MARV serves as a poignant example of the way a pathogen that is highly prevalent in its reservoir host population can hide safely without human notice, until in some unfortunate accident, hosts and vectors cross paths.

## Practice Note 4.2 Looking beyond the host

The wider availability of data-and the tools to process it—has recently reawakened interests in early warning systems of zoonotic diseases. The perspective of One Health (see Practice Note 4.1) is that especially where humans and animals coexist, their disease dynamics are often coupled. Wolking et al. [135] showed, for instance, that from a sample of pastoral communities in Tanzania, almost two-thirds of households with at least one human patient with diarrhoea also had at least one calf with diarrhoea in their herds. Cryptosporidium spp. and Giardia duodenalis affect bovine populations similarly to humans, and are easily transferred through every-day contact. Focusing not only on the host species but also on vectors or alternate hosts can serve as an early warning system for an emergence of the disease in human populations. Bisson, Ssebide, and Marra [136], for instance, propose the reporting of animal morbidity as sentinels to pathogenic emergence in human populations.

The historical experience in monitoring vectors to anticipate the human impact has not been extensive. Amato et al. [137] describe such an early warning project, noting that it is far from typical. Many disease vectors are particularly difficult to capture and test (bats take pride of place in this respect). Sampling networks are time- and resource-intensive to implement and analyze, and as Herten et al. [138] point out, using animals as bellwethers of human health might raise complex ethical (and economic) questions. As Hussain-Alkhateeb et al. [139]'s scoping review shows, such early warning systems have so far fallen short of the expectations of their promises. With the philosophical underpinnings provided by One Health and the technological solutions that have emerged over the last decades, the hope is that the promise of early warning systems of disease in host populations by examining the vector population or reservoir hosts might come nearer fulfillment.

### 4.2.4 Seasonal variance of zoonotic transmission

Humans have different needs at different times: most of us want some balance of solitude and privacy on one hand and communality and sharing on the other. We are, like much of the animal world, facultative cooperators.

- Cooperative behavior often has a protective effect for prey and the ability to hunt more effectively for predators. The Allee effect suggests that increasing group size increases individual fitness. Especially in resource-poor times or where there is no benefit in self-interested territoriality (e.g., during winter, where common survival is more important than mating), individuals might opt to cooperate [140].
- On the other hand, the cost of whatever benefits the Allee effect provides is that it has to be shared with a potentially quite large population of others. Thus when the pressures that justify cooperation-the need to hunt cooperatively due to food scarcity or the need to bunch together for defence-are less intense, individuals
might fare better focusing, essentially, on their own good. Wilson, Goodson, and Kingsbury [141], for instance, found evidence of neurobiochemical correlates of this process in sparrows, showing a seasonal shift between territoriality during mating season (summer) and flocking during resource scarcity (winter).

Just as most humans prefer a situation-appropriate mixture of solitude and engagement, the rate at which hosts and vectors interact with each other might vary with time:

- $\beta_{h \rightarrow h}$ may generally higher whenever hosts congregate on a seasonal basis. Weather modulates social behavior in humans and nonhuman animals alike. In the animal world, resource scarcity, cold weather, and migration can drive individuals together. Humans tend to congregate during the winter (a phenomenon discussed in more detail in Chapter 7) and, in agricultural societies, during seasons of increased cooperation (sowing and harvest season).
- $\beta_{h \rightarrow v}$ and $\beta_{v \rightarrow h}$ often change when interaction between the host and vector species changes. In some parts of the world, agriculture brings vectors and human host populations closer (a situation described also in Subsection 4.2.1), and the annual periodicity of agricultural activity often influences transmission rates.
- $\beta_{v \rightarrow v}$ is similarly governed by increased density of vectors, as it happens often during breeding periods. Vectors, too, may engage in seasonal flocking periods.

The effect of seasonal variance on a dynamic process in time is referred to as temporal forcing, and is explored in detail in Subsection 7.3. In a temporal forcing model of transmission, we represent one or more values of $\beta$ not as constants but as timevarying quantities, quite typically as a sinusoidal function that recapitulates rather conveniently how such processes evolve in nature.

Thus we could model a process like the annual seasonality of increased vector-tohost transmission due to

$$
\begin{equation*}
\beta(t)=\beta_{0}(\overbrace{1}^{\text {base } \beta}+\overbrace{\underbrace{\beta_{1}}_{\text {forcing parameter }} \sin (\underbrace{\omega}_{\text {period }} t+\underbrace{\psi}_{\text {phase }}}^{\text {time-varying } \beta}) . \tag{4.16}
\end{equation*}
$$

This should, of course, be quite familiar from high school physics, as it is essentially the sine wave equation. The amplitude of forcing $\beta_{1}$ is bounded by $[0,1]$, as negative values of $\beta$ are biologically nonsensical. $\omega$ describes the angular frequency, which relates to the ordinary frequency $f$ as $\omega=2 \pi f$. Thus for a process that repeats once a year, $\omega$ is $2 \pi$. Where $\omega$ is supplied as radians per year, care must be taken to supply $t$ and $\psi$ as fractions of the year by dividing them by 365. Compartmental models can easily be expanded to accommodate time-varying rates. For instance, the SI+SIR model from Eq. (4.12) can be parameterized with a time-varying value for $\beta_{v \rightarrow h}$ by replacing the term with its time-varying form, then defining it as a function
of $t$ :

$$
\begin{align*}
& \frac{d S_{h}}{d t}=\mu_{h}-(\overbrace{\beta_{h \rightarrow h} S_{h} I_{h}}^{h \rightarrow h}+\overbrace{\beta_{v \rightarrow h} S_{h} I_{v}}^{v \rightarrow h})-\overbrace{\mu_{h} S_{h}}^{\text {mortality }}, \\
& \frac{d I_{h}}{d t}=\overbrace{\beta_{h \rightarrow h} S_{h} I_{h}}^{h \rightarrow h}+\overbrace{\beta_{v \rightarrow h}(t) S_{h} I_{v}}^{v \rightarrow h}-\overbrace{\gamma I_{h}}^{\text {recovery }}-\overbrace{\mu_{h} I_{h}-\mu_{h}^{I} I_{h}}^{\text {mortality }},  \tag{4.17}\\
& \beta_{v \rightarrow h}(t)=\underbrace{\beta_{v \rightarrow h_{0}}}_{\text {base } \beta_{v \rightarrow h}}(1+\underbrace{\beta_{v \rightarrow h_{1}}}_{\text {forcing parameter }} \sin (\underbrace{\omega}_{\text {frequency }} \frac{2 \pi}{365}(\underbrace{t}_{\text {days }}+\underbrace{\psi}_{\text {phase }})) .
\end{align*}
$$

For an annually repeating process, $\omega=1$, and thus can altogether be omitted. The conversion factor $\frac{2 \pi}{365}$ converts days into radians, thus allowing us to specify $t$ and $\psi$ as days.

## Computational Note 4.5 Time dependence in ODE solvers

Until now, we have primarily worked with autonomous ODEs, that is, ODEs that describe the right-hand side without reference to $t$. Temporal forcing requires us to accommodate nonautonomous models, but as we shall find, this is not greatly different from previous cases. All major ODE solvers expose the time of evaluation as a variable to the derivative function. The odeint and solve_ivp APIs both make this available using the time parameter of the derivative function. Recall that we have defined the derivative as

```
def deriv(t, y,...):
    . . .
    return ...
```

for solve_ivp (and much the same way for odeint, except that in that case, the order of $t$ and $y$ is reversed). The consequence is that deriv() has access to $t$ at any time. Thus a time-dependent term is simply an expression over $t$. It sometimes pays to calculate the value of $\beta(t)$ at $t$ and store it as a separate variable within the deriv() function's scope (prefixing the current value with eff_ is a good enough starting point). This reduces ambiguity and prevents accidentally overwriting other variables.

Eq. (4.17) would then be formulated-omitting unchanged lines from Computational Note 4.4 -as

```
def deriv(t, y, beta, gamma, beta_1, psi):
    ...
    eff_beta_VH = beta_VH * \
        (1 + (beta_1 * np.sin(2 * np.pi/365 * (t - psi))))
```

```
dSvdt = mu_V - (beta_VV * S_V * I_V +\
                                eff_beta_VH * S_V * I_H) - mu_V * S_V
dIvdt = (beta_VV * S_V * I_V + eff_beta_VH * S_V * I_H) - \
    gamma_V * I_V - mu_V * I_V - mu_I_V * I_V
return dShdt, dSvdt, dIhdt, dIvdt
```

Note that time-dependent functions in the derivative function can be quite arbitrary, but adding conditional statements and branching processes tends to slow down the integrator considerably.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch04/ zoonos is.

### 4.2.5 Zoonoses and birth dynamics

We typically conceive of hosts and vectors as being fundamentally different; one longlived and relatively rare, the other short-lived yet abundant and reproducing rapidly. This is one of the very rare examples of inherent prejudice born of the human experience that is not entirely incorrect. Species with low birth rates and long lifespans generally make very bad vectors. Not only might they live long enough to clear (or, in the case of humans, treat) the pathogen, they might also succumb to the effects of the pathogen all too early. For what they can do for the pathogen in terms of disease transmission, they are much too rare. Ideal vectors have high birth rates, even if it is the result of short lives. For this reason, vectors that have seasonal dynamics of birth are worthy of our special attention.

In 2015, Hayman [142] remarked on the way the bi-annual periodicity of birth in R. aegyptiacus allowed a pathogen-in that case, MARV—-to persist. In mammals, pregnancy modulates the maternal immune system [143], to prevent rejection of the allogeneous offspring during pregnancy. Thus a vector population, and sometimes, a host population, may be increasingly susceptible to sustaining infection during pregnancy. Where births are seasonal in either the host or the vector population, related effects might emerge on transmission to the relevant compartment.

The consequence of multiple forcings with different periodicities is the evolution of complex time-dependent phenomena, much of which depend not only on the difference of the value between seasons but also on their temporal relationships (phase). Fig. 4.10 shows the effect of phase on a model with seasonally varying births and a seasonally varying transmission term (in that case, $\beta_{v \rightarrow v}$ ). For a relatively stable host population, a birth pulse in the vector population means a quick rise in susceptibles, who will in due course be recruited into the infectious vector compartment, and thus a rise in the relative number of infectious vectors per susceptible host. On the other hand, temporal dynamics of host-vector interactions can change the likelihood of a

![](https://cdn.mathpix.com/cropped/2024_06_11_c8f56f588f7e82d7a0e9g-29.jpg?height=1344&width=1055&top_left_y=229&top_left_x=246)

Figure 4.10 A dual temporally forced host-vector system at different phases. In this system, both the birth rate of vectors and intraplane transmission among vectors is temporally forced; the former with a period of 6 months, resembling the biannual births discussed by Hayman [142], the latter at an annual period. The effect of phase considerably changes the number of infections in the host compartment.

host acquiring the infection at times when the transmission coefficient rises. If these two processes are perfectly in phase, resonant phenomena can emerge, resulting in sharp spikes of infection in the host population.

