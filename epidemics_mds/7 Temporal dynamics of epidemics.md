# Temporal dynamics of epidemics Epidemics in time 

It is only in appearance that time is a river. It is rather a vast landscape and it is the eye of the beholder that moves.

Wilder, The Eighth Day, 1967 [238]

### 7.1 Equilibrium states and stability analysis

Equilibria-specifically, stable equilibria-are long-term destinies of dynamic systems. A system in a stable equilibrium will not subject to any external force or dislodge itself therefrom. As epidemiologists, we are interested in equilibria, because stable equilibria tell us when a system has attained stability or where it will, eventually, attain stability. Epidemics are "extraordinary events." The term outbreak, beloved of the popular media when commenting on epidemics, emphasizes that we are dealing with a phenomenon that goes counter to "business as usual." Stable equilibria are nothing more than mathematical descriptions of states, in which the system can settle again and attain a measure of normalcy.

A compartmental model is at equilibrium when the derivative of each compartment with respect to time is zero. For instance, the equilibrium of a SIR model is

$$
\begin{equation*}
\frac{d S}{d t}=\frac{d I}{d t}=\frac{d R}{d t}=0 \tag{7.1}
\end{equation*}
$$

We denote this state by $\left(S^{\star}, I^{\star}, R^{\star}\right)$. There are, in general, two possible equilibria:

1. the trivial equilibrium, which is more commonly known as the disease-free equi-

librium, where $I^{\star}=0$, and

2. the nontrivial or endemic equilibrium, in which $I^{\star}>0$.

The stability of each of these, and their attraction, determines the long-term destiny of any infectious process. In much of this chapter, we will be concerned-directly or indirectly-with the way systems behave at, around, or towards these equilibria.

### 7.1.1 Case study: pandemics, epidemics, and endemics

The definition of a pandemic is relatively clear [239-241]. The distinction between epidemics and endemic processes, at least for us arriving at the matter from the perspective of quantitation, is much less so.

First, there is an unhelpful tendency to use the term "epidemic" to refer to any phenomenon that rapidly arises in time; from the more widely discussed obesity [242] and opioid epidemics to notions such as that of a selfie epidemic [243], which
might perhaps sound closer to social phenomena like the medieval Tanzwut (dancing plague) $[244,245]$ than actual epidemics. These share an important feature with actual epidemics: early near-exponential growth, but the resemblance ends there.

In mathematical and computational epidemiology, we are rather more careful with our words. Importantly, we distinguish between epidemics and endemics. The fundamental difference is that an endemic disease is at, or converging at, an equilibrium, whereas an epidemic is growing and moving away from an equilibrium state.

Definition 7.1 (Endemic vs. epidemic disease). A disease process is endemic if it is at an equilibrium $\left(\frac{d I}{d t}=\frac{d S}{d t}=0\right)$ and $I>0$. A disease process can only be stable and endemic if a stable equilibrium $\left(S^{\star}, I^{\star}, R^{\star}\right)$ exists so that $\frac{d S}{d t}=\frac{d I}{d t}=\frac{d R}{d t}=0$.

A disease process is an epidemic if $\frac{d I}{d t}>0$ and $I>0$. An epidemic is not an equilibrium state, and is therefore never stable.

The counterintuitive result of this is that a disease with a dozen cases might, in theory, be an epidemic, but a disease with hundreds of thousands cases a year might be "merely" endemic. The crucial point to recall is that endemicity versus epidemicity is not about absolute (or relative) numbers, but rather whether the state of the system occupies a stable endemic equilibrium point. It is perfectly possible, for instance, for a disease with relatively high $\Re_{0}$, to occupy an endemic equilibrium, where the infectious compartment houses thousands of individuals at a time, whereas for another disease, a hundred cases constitute no doubt an epidemic if the endemic equilibrium is at tens of cases. The popular understanding of epidemics as being primarily about numbers is misleading: more than anything, it is about rates and about the relationship to the equilibrium point.

### 7.1.2 Disease-free and endemic equilibria

A compartmental model may have two equilibria: the disease-free equilibrium and the endemic equilibrium.

Definition 7.2 (Disease-free equilibrium). The disease-free equilibrium (DFE) is an equilibrium state, where $I^{\star}=0$. This equilibrium is always stable if $\Re_{0}<1$.

Definition 7.3 (Endemic equilibrium). The endemic equilibrium is an equilibrium state with a nonzero value of $I^{\star}$. This equilibrium is always unstable if $\Re_{0}<1$. It may be stable at $\mathfrak{R}_{0}>1$.

The two equilibria are, essentially, the alternative long-term destinies of pathogens: they become endemic or they disappear altogether (along with immunity to them). For this reason, we are deeply interested not only in where these equilibria occur, but also whether they are stable (i.e., whether the system, once it achieves that equilibrium, will remain in that state indefinitely unless influenced from the outside).

### 7.1.3 Identifying equilibria

A system is at an equilibrium when, as we have stated mathematically in Eq. (7.1), the derivative of all compartments in respect of time is zero. We thus identify possible equilibria by setting each of the terms of the model to zero, and solve for the variables. For a SIR model with equal births and deaths $\mu$, we essentially obtain the following system of equations:

$$
\begin{array}{r}
\mu-\beta S I-\mu S=0 \\
\beta S I-\gamma I-\mu I=0  \tag{7.2}\\
\gamma I-\mu R=0
\end{array}
$$

This system has a trivial solution in $(1,0,0)$ : if $S=1$, then $\mu$ and $\mu S$ will be equal. All other terms, which contain either $I$ or $R$, will be zero. Consequently, we have an equilibrium at $(1,0,0)$, the disease-free equilibrium.

The endemic equilibrium can be found either symbolically or through some penand-paper mathematics. The second equation is a good place to start. Factoring out $I$ yields,

$$
I(\beta S-\gamma-\mu)=0
$$

This is satisfied if either side of the product is zero.

- $\quad I=0$ is the disease-free equilibrium that we have already worked out.
- $\beta S-\gamma-\mu=0$ can be rearranged so that $\beta S=\gamma+\mu$, and hence $S=\frac{\gamma+\mu}{\beta}$.

Notably, this is the inverse of $\mathfrak{R}_{0}$. Thus we have the value for $S^{\star}$ for the endemic equilibrium. Inserting this into the expression for $I$ simplifies to $\frac{\mu\left(\Re_{0}-1\right)}{\beta} \cdot R^{\star}$ is then obtained through $1-S^{\star}-I^{\star}$. This gives the endemic equilibrium of a SIR model as

$$
\begin{align*}
S^{\star} & =\Re_{0}^{-1} \\
I^{\star} & =\frac{\mu\left(\Re_{0}-1\right)}{\beta}  \tag{7.3}\\
R^{\star} & =1-\Re_{0}^{-1}-\frac{\mu\left(\Re_{0}-1\right)}{\beta}
\end{align*}
$$

## Computational Note 7.1 Symbolic identification of equilibria

SymPy is a very useful tool for the identification of equilibria, especially if we have a more complex system. The solve function solves a system of equations symbolically.

We initialize our symbols as

mu, beta, gamma, S, I, R = sympy.symbols("mu beta gamma S I R")

By definition, the solve function accepts either equations or zero-valued expressions. Since we are essentially setting each of the differentials to zero, this will be straightforward. The partition constraint $S+I+R=1$ can be expressed in the form $1-S-I-R$, or as an equality:

sympy.Equality(S $+\mathrm{I}+\mathrm{R}, 1)$

In an Equality object, the two arguments correspond to the left-hand side and the right-hand side of the equality, respectively. This gives us

```
sympy.solve((
    mu - beta * S * I - mu * S,
    beta * S * I - gamma * I - mu * I,
    gamma * I - mu * R,
    sympy.Equality(S + I + R, 1)
), [S, I, R])
```

This returns a list of tuples, which each represent a solution for the system of equations. Unfortunately, SymPy is not particularly strong at substituting subexpressions with variables, so the nontrivial endemic equilibrium will look somewhat different from what is documented in Eq. (7.3), although it is mathematically entirely equivalent of course.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch07/ sir_ stability.

### 7.1.4 Equilibrium stability analysis

We have now found equilibria, but we are interested in the stability of these equilibrium points. A system of ordinary differential equations at an equilibrium point may be unstable or asymptotically stable. To determine this, we ordinarily use the eigenvalues of the Jacobian matrix of the differential equation vis-a-vis each of its compartments.

Definition 7.4 (Jacobian matrix). For a system of $n$ ordinary differential equations with $n$ variables $x_{1}, x_{2}, \ldots, x_{n}$, let $f_{i}$ be $\frac{d x_{i}}{d t}$ for all $i$ in $n$. The Jacobian matrix, or Jacobian for short, is then defined as

$$
\mathbf{J}=\left(\begin{array}{ccc}
\frac{\partial f_{1}}{\partial x_{1}} & \cdots & \frac{\partial f_{1}}{\partial x_{n}}  \tag{7.4}\\
\vdots & \ddots & \vdots \\
\frac{\partial f_{n}}{\partial x_{1}} & \cdots & \frac{\partial f_{n}}{\partial x_{n}}
\end{array}\right)
$$

The eigenvalues of the Jacobian evaluated at an equilibrium point $x^{\star}=x_{1}^{\star}, x_{2}^{\star}, \ldots, x_{n}^{\star}$ define the system's stability:

1. If all eigenvalues have negative real parts $\left(\operatorname{Re}\left(\lambda_{i}\right)<0\right.$ for all $i$ in $\left.n\right)$, the equilibrium is asymptotically stable.
2. If at least one eigenvalue has a positive real part $\left(\operatorname{Re}\left(\lambda_{i}\right)>0\right.$ for at least one $i$ in $n$ ), the equilibrium is unstable.
3. If all eigenvalues have zero or negative real parts, with at least one eigenvalue being zero, the Jacobian method does not work, and typically, a Lyapunov function needs to be constructed for equilibrium analysis.

Consider a simple SIR model, as described in Subsection 2.1.4, with a constant birth and death rate $\mu$. The Jacobian of this system at the equilibrium point $\left(S^{\star}, I^{\star}, R^{\star}\right)$ is

$$
\mathbf{J}=\left(\begin{array}{ccc}
-\beta I^{\star}-\mu & -\beta S^{\star} & 0  \tag{7.5}\\
\beta I^{\star} & \beta S^{\star}-\mu-\gamma & 0 \\
0 & \gamma & -\mu
\end{array}\right)
$$

If we substitute the disease-free equilibrium $\left(S^{\star}, I^{\star}, R^{\star}\right)=(1,0,0)$, the Jacobian assumes the following shape:

$$
\mathbf{J}_{\mathrm{DFE}}=\left(\begin{array}{ccc}
-\beta-\mu & 0 & 0  \tag{7.6}\\
\beta & -\mu-\gamma & 0 \\
0 & \gamma & -\mu
\end{array}\right)
$$

The eigenvalues of this Jacobian are $-\mu$ and $\beta-\mu-\gamma$. This equilibrium is stable

if $-\mu<0$ and $\beta-\mu-\gamma<0$. That holds true if $\beta<\mu+\gamma$, or $\frac{\beta}{\mu+\gamma}<1$. Since $\frac{\beta}{\mu+\gamma}$ is, of course, $\mathfrak{R}_{0}$, the disease-free equilibrium is obtained if and only if $\Re_{0}<1$, a result that should, in view of the previous, be no cause for any surprise.

If we evaluate the Jacobian at the endemic equilibrium, we get

$$
\mathbf{J}_{\mathrm{EE}}=\left(\begin{array}{ccc}
-\mu\left(\Re_{0}-1\right)-\mu & -\gamma-\mu & 0  \tag{7.7}\\
\mu\left(\Re_{0}-1\right) & 0 & 0 \\
0 & \gamma & -\mu
\end{array}\right)
$$

The eigenvalues associated with the endemic equilibrium are

$$
\begin{equation*}
\lambda_{2,3}=-\frac{\mu \Re_{0}}{2} \pm \frac{\sqrt{\left(\mu \Re_{0}\right)^{2}-4(\mu+\gamma) \mu\left(\Re_{0}-1\right)}}{2} \tag{7.8}
\end{equation*}
$$

Since $\frac{1}{\mu+\gamma}$ is the mean infectious period $\tau$, and $\frac{1}{\mu\left(\Re_{0}-1\right)}$ is the mean age at sustaining infection (see Eq. (2.55)), the above may be simplified to

$$
\begin{equation*}
\lambda_{2,3}=-\frac{\mu \Re_{0}}{2} \pm \frac{\sqrt{\left(\mu \Re_{0}\right)^{2}-\frac{4}{\tau A}}}{2} \tag{7.9}
\end{equation*}
$$

In line with Keeling and Rohani [39]'s approach, we can discount the $\left(\mu \Re_{0}\right)^{2}$ component, as this is typically a very small value; recall that the value of $\mu$ is the inverse

![](https://cdn.mathpix.com/cropped/2024_06_11_9842913b8cdb0b8f0b50g-06.jpg?height=898&width=1013&top_left_y=232&top_left_x=223)

Figure 7.1 Size of the infectious compartment at the stable endemic equilibrium for a SIR model with $\mu=0.02$ per annum as a function of $\tau$ and $\mathfrak{R}_{0}$. The white area denotes the space below $\Re_{0}=1$, where no stable endemic equilibrium can exist.

of the mean life expectancy of the population. This simplifies the equation to

$$
\begin{equation*}
\lambda_{2,3} \approx \frac{\mu \Re_{0}}{2} \pm \frac{i}{\sqrt{\tau A}} \tag{7.10}
\end{equation*}
$$

This expression is negative for all values of $\mathfrak{R}_{0}$ greater than one. Consequently, the endemic equilibria of SIR models are asymptotically stable if $\mathfrak{R}_{0}>1$. (See Fig. 7.1.)

## Computational Note 7.2 Numerical equilibrium analysis

In practice, we are more often interested in the equilibria of a particular system with known parameters, rather than an abstract symbolic solution. For this reason, as long as we have a relatively good idea of the parameters of the system, we can obtain a solution and numerically evaluate it.

Consider the simple SIR system in Computational Note 7.1. We can obtain the values of the endemic equilibrium, given values of $\beta, \gamma$, and $\mu$, by taking the nontrivial solution and substituting our known values.

```
def get_endemic_equi1ibrium(g, m, r0):
    return [solution.subs({"gamma": g,
        "mu": m,
        "beta": R0 * (g + m)})
        for solution in solutions[1]]
```

With this function, we can calculate the endemic equilibrium for any arbitrary value of $\gamma, \mu$, and $\mathfrak{R}_{0}$ (since $\mathfrak{R}_{0}=\frac{\beta}{\gamma+\mu}$. However, we are also interested in whether the endemic equilibrium is going to be stable. For this, we once again construct the Jacobian:

```
jac = sympy.Matrix([
    mu - beta * S * I - mu * S,
    beta * S * I - gamma * I - mu * I,
    gamma * I - mu * R,
]).jacobian([S, I, R])
```

Recall that an equilibrium is asymptotically stable if and only if the real part of all of its eigenvalues are negative. We must, therefore, proceed in a few wellconsidered steps:

1. Substitute the equilibrium solution and the parameters for $\beta, \gamma$, and $\mu$, into the Jacobian.
2. Obtain the eigenvalue. Since this is a purely numerical problem at this point, there are no benefits to using SymPy. SciPy's 1 inalg subpackage provides the eigvals function to obtain the eigenvalues. To be able to do so, however, we will have to convert the substituted Jacobian into a NumPy array using np.array(jac).astype(np.f1oat64). The type casting into float64 is necessary, because the eigvals function does not operate on object arrays.
3. We then take the real parts of each eigenvalue, using . rea 1 on the result. Since we are interested in whether all of the results are less than zero, we use np.a11 (eigenvalues.real < 0 ) to obtain a single truth value.

This would produce a tidy function that determines the endemic equilibrium, returns it, and returns a Boolean indicator of its stability:

```
def get_endemic_equilibrium(g: float,
    m: float,
    r0: float,
    jac: sympy.Matrix) -> tuple:
solutions = sympy.solve([
    mu - beta * S * I - mu * S,
    beta * S * I - gamma * I - mu * I,
    gamma * I - mu * R,
```

```
sympy.Equality(S + I + R, 1)
], [S, I, R])
endemic_sol = [solution.subs({"gamma": g,
    "mu": m,
    "beta": R0 * (g + m)})
                    for solution in solutions[1]]
substituted_jacobian = jac.subs({"S": endemic_sol[0],
                    "I": endemic_sol[1],
                    "R": endemic_sol[2],
                    "gamma" : g,
                    "mu": m,
                    "beta": R0 * (g + m)})
eigenvalues
    = eigvals(np.array(substituted_jacobian).astype(np.float64))
return *endemic_sol, np.al1(eigenvalues.real < 0)
```

It makes sense to precalculate the Jacobian, and supply it to the function in case we wish to evaluate the function iteratively. Symbolic calculation of the Jacobian is relatively expensive, and since the symbolic result does not change by changing the parameters that govern it, we may calculate it once, then call it an arbitrary number of times.

The method discussed above can be applied to any model of any specification, although more complex models will be computationally more expensive. The iterative evaluation of equilibria, and their stability, at various points and for various parameters is a helpful tool in understanding how the parameters of an infectious disease govern its long-term destiny.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch07/s sir_ stability.

### 7.1.5 Bifurcations and equilibria

As we have seen, the existence of equilibria and their stability depends on $\mathfrak{R}_{0}$. Bifurcation diagrams, such as that exhibited in Fig. 7.2 for a simple SIR model, show the critical point at $\mathfrak{R}_{0}=1$ in determining the equilibrium number of infecteds $\left(I^{\star}\right)$ :

- For $\Re_{0}<1$, the disease-free equilibrium (DFE) is stable at $I^{\star}=0$.
- At $\mathfrak{R}_{0} \geq 1$, the model experiences a transcritical bifurcation, and a new equilibrium emerges (the endemic equilibrium, EE). At this point, the DFE becomes unstable and the $\mathrm{EE}$ becomes stable. As $\mathfrak{R}_{0}$ increases, the equilibrium value of $I^{\star}$ increases.

![](https://cdn.mathpix.com/cropped/2024_06_11_9842913b8cdb0b8f0b50g-09.jpg?height=435&width=899&top_left_y=226&top_left_x=315)

Figure 7.2 A compartmental model has a stable disease-free equilibrium (DFE) if $\mathfrak{R}_{0}<1$. Above $\mathfrak{R}_{0}=1$, the DFE is not stable, and the endemic equilibrium (EE) exists and is stable. This is an example of forward bifurcation.

![](https://cdn.mathpix.com/cropped/2024_06_11_9842913b8cdb0b8f0b50g-09.jpg?height=429&width=895&top_left_y=814&top_left_x=315)

Figure 7.3 Backward bifurcation at $\mathfrak{R}^{\prime}$. Between $\mathfrak{R}^{\prime}$ and 1, a stable DFE (solid red line), a stable (upper) EE (solid blue line) and an unstable EE (dashed blue line) coexist. Consequently, only the necessary condition for the pathogen's elimination is met at $\mathfrak{R}_{0}=1$; the sufficient condition is only met at $\Re_{0}=\Re^{\prime}$.

This does not, however, hold universally. There exists an alternative pattern of bifurcation, known as backward (or subcritical) bifurcation, which is epidemiologically interesting for us, because, in such cases, reduction of a pathogen's $\Re_{0}$ might not be sufficient for the control of the disease. In backward bifurcation, the situation is the same for $\mathfrak{R}_{0}>1$, but quite significantly different below 1 : for a part $\left[\mathfrak{R}^{\prime}, 1\right]$, three equilibria coexist: a stable DFE and two endemic equilibria, of which the upper equilibrium is stable and the lower equilibrium is unstable. This is illustrated by Fig. 7.3.

The most robust mathematical formulation of determining if backward bifurcation occurs is the center manifold theory proposed by Castillo-Chavez and Song [246], which allows the quantitative determination of whether a system would exhibit backward bifurcation. Qualitatively speaking, backward bifurcation occurs in cases where a pathogen has some way to persist in the population, such as

- waning immunity, whether vaccine-induced or post-infectious [247],
- imperfectly protective vaccines [247],
- reimportation of pathogenic populations [246], and
- vector populations [248].

The importance of backward bifurcation is particularly significant for diseases that can persist in a latent infectious state, such as tuberculosis [246]. It is worth noting, as Greenhalgh and Griffiths [249] has done, that more complex bifurcations can exist, with more than two subcritical endemic equilibria.

### 7.1.6 Equilibria of SEIR models

The disease-free equilibrium of a SEIR model as laid out in Eq. (2.43) is, of course $(1,0,0,0)$. We are rather more interested in the endemic equilibrium, which is given, for an equal birth and death rate $\mu$, as

$$
\begin{align*}
S^{\star} & =\frac{(\mu+\gamma)(\mu+\sigma)}{\sigma \beta}=\Re_{0}^{-1} \\
E^{\star} & =\frac{\left(\Re_{0}-1\right) \mu(\mu+\gamma)}{\sigma \beta}  \tag{7.11}\\
I^{\star} & =\frac{\left(\Re_{0}-1\right) \mu}{\beta} \\
R^{\star} & =1-\Re_{0}^{-1}-\frac{\left(\Re_{0}-1\right) \mu(\mu+\gamma)}{\sigma \beta}-\frac{\left(\Re_{0}-1\right) \mu}{\beta}
\end{align*}
$$

The eigenvalues of the Jacobian for the SEIR model are somewhat challenging to identify. However, subject to some simplifications [250], it can be evaluated at the equilibrium point. The eigenvalues are negative if $\Re_{0}>1$. Thus similarly to SIR models (the equilibria of which we have discussed in Subsection 7.1.4), the endemic equilibrium of a SEIR model is stable at $\mathfrak{R}_{0}>1$. The inclusion of the exposed period means that perturbations to a SEIR model will however have a longer period of the decaying oscillations as the system converges on the endemic equilibrium.

## Computational Note 7.3 Symbolic equilibrium analysis of SEIR models

The eigenvalues of complex models make it often quite difficult to discern information about stability. Thankfully, symbolic manipulation can help us quite considerably.

Given the SEIR model

$$
\begin{align*}
& \frac{d S}{d t}=\mu+(\beta I+\mu) S \\
& \frac{d E}{d t}=\beta S I-(\sigma+\mu) E  \tag{7.12}\\
& \frac{d I}{d t}=\sigma E-(\gamma+\mu) I
\end{align*}
$$

$$
\frac{d R}{d t}=\gamma I-\mu R
$$

First, we obtain the equilibrium solutions of the system:

```
solutions = sympy.solve([
    mu - (beta * I + mu) * S,
    beta * S * I - (sigma + mu) * E,
    sigma * E - (gamma + mu) * I,
    gamma * I - mu * R,
    sympy.Equality(S + E + I + R, 1)
```

]$,[S, E, I, R])$

This yields the rather unsurprising DFE solution of $(1,0,0,0)$, which is stable. It also yields the solutions described in Eq. (7.11), in a somewhat unwieldier form. Thankfully, we will not have to directly engage with it. Next, we obtain the Jacobian of the system:

```
jac = sympy.Matrix([
    mu - (beta * I + mu) * S,
    beta * S * I - (sigma + mu) * E,
    sigma * E - (gamma + mu) * I,
    gamma * I - mu * R,
]).jacobian([S, E, I, R])
```

The Jacobian of the above is

$$
\mathbf{J}=\left(\begin{array}{cccc}
-I \beta-\mu & 0 & -S \beta & 0  \tag{7.13}\\
I \beta & -\mu-\sigma & S \beta & 0 \\
0 & \sigma & -\gamma-\mu & 0 \\
0 & 0 & \gamma & -\mu
\end{array}\right)
$$

We replace $S$ and $I$ with their equilibrium solutions from the endemic equilibrium (the second solution in the solutions object):

substituted_jacobian = jac.subs(\{"I": solutions[1][2],

This gives us the Jacobian

$$
\mathbf{J}=\left(\begin{array}{cccc}
-\mu-\frac{\mu\left(\beta \sigma-\gamma \mu-\gamma \sigma-\mu^{2}-\mu \sigma\right)}{(\gamma+\mu)(\mu+\sigma)} & 0 & \frac{-(\gamma+\mu)(\mu+\sigma)}{\sigma} & 0  \tag{7.14}\\
\frac{\mu\left(\beta \sigma-\gamma \mu-\gamma \sigma-\mu^{2}-\mu \sigma\right)}{(\gamma+\mu)(\mu+\sigma)} & -\mu-\sigma & \frac{(\gamma+\mu)(\mu+\sigma)}{\sigma} & 0 \\
0 & \sigma & -\gamma-\mu & 0 \\
0 & 0 & \gamma & -\mu
\end{array}\right) .
$$

This has four eigenvalues, all of which are fairly complex. Fortunately, we do not need to evaluate or even see them. We are not interested in them, but rather only in whether, and how, they fulfill the Jacobian equilibrium criteria. We obtain a list of the real parts of the eigenvalues as

```
real_parts
    = [sympy.re(i) for i in substituted_jacobian.eigenva1ues()]
```

The system is asymptotically stable if the real parts of all eigenvalues are negative. Of the four eigenvalues, the fourth eigenvalue has the real part $-\mu$, which means it is negative by default. At this point, we could theoretically solve for a neat analytical result, by setting each of the first three eigenvalues to zero, then solving for values of $\Re_{0}, \beta, \sigma$, and $\mu$ so that all eigenvalues have zero-valued real parts, and $\Re_{0}>1$. In practice, a symbolic analytical solution for this is not obtainable (as Keeling and Rohani [39] note, albeit arriving to the issue from a different angle). Symbolic computation is powerful, but often, highly complex dynamical systems are not amenable to analytical solutions. This is, then, a highly instructive failure: it shows that in many cases, a neat symbolic solution is not necessarily obtainable through computer algebra, and numerical stability analysis often proves much more suitable if values or approximations are known for some of the parameters.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch07/seir_ stability.

### 7.1.7 Equilibria of SIS models

Models that do not engender immunity (or for which immunity upon recovery is shortlived) are best approximated by a SIS model (see Subsubsection 2.3.2.2). We obtain the endemic equilibrium of a SIS model by first expressing $\frac{d S}{d t}$ in Equation 2.39 in terms of $I$. Since there are only two compartments, the partition property (see Definition 2.4) implies that anyone not in $I$ is in $S$, hence $S=1-I$. Consequently,

$$
\begin{equation*}
\frac{d I}{d t}=\beta I(1-I)-\gamma I \tag{7.15}
\end{equation*}
$$

Factoring out $\beta$ and replacing $\frac{\gamma}{\beta}=\mathfrak{R}_{0}^{-1}$, we get

$$
\begin{equation*}
\frac{d I}{d t}=\beta I\left(1-\mathfrak{R}_{0}^{-1}-1\right) \tag{7.16}
\end{equation*}
$$

Setting Eq. (7.16) to zero and solving for $I$ gives $I^{\star}=1-\frac{1}{\Re_{0}}$ and $S^{\star}=\frac{1}{\Re_{0}}$. The complementarity of these two results is, of course, the necessary corollary of $S^{\star}+I^{\star}=1$. This equilibrium value is stable for $\mathfrak{R}_{0}>1$.

### 7.1.8 Equilibria of SIRS models

SIRS models differ from the traditional SIR model in that immunity wanes, but it is also distinct from the SIS model in that immunity exists in the first place. It is thus an intermediate of the two. Solving the SIRS model specified as

$$
\begin{align*}
& \frac{d S}{d t}=\mu-(\beta I+\mu) S+\omega R \\
& \frac{d I}{d t}=\beta S I-(\gamma+\mu) I  \tag{7.17}\\
& \frac{d R}{d t}=\gamma I-(\omega+\mu) R
\end{align*}
$$

gives us the trivial solution of the $\operatorname{DFE}(1,0,0)$, and the endemic equilibrium at

$$
\begin{align*}
S^{\star} & =\Re_{0}^{-1} \\
I^{\star} & =\frac{(\mu+\omega)(\beta-\gamma-\mu)}{\beta(\gamma+\mu+\omega)}  \tag{7.18}\\
R^{\star} & =\frac{\gamma(\beta-\gamma-\mu)}{\beta(\gamma+\beta+\omega)}
\end{align*}
$$

This gives us the Jacobian at the endemic equilibrium as

$$
\mathbf{J}_{\mathrm{EE}}=\left(\begin{array}{ccc}
-\mu-\frac{(\mu+\omega)(\beta-\gamma-\mu)}{(+\mu+\omega)} & -\gamma-\mu & \omega  \tag{7.19}\\
\frac{(\mu+\omega)(\beta-\gamma-\mu)}{\gamma+\mu+\omega} & 0 & 0 \\
0 & \gamma & -\mu-\omega
\end{array}\right)
$$

We may reason about the stability of this system using the Routh-Hurwitz criteria. Recall that the eigenvalues of $\mathbf{J}_{\mathrm{EE}}$ would be the set of all values $\lambda$ so that

$$
\begin{equation*}
\left(\mathbf{J}_{\mathrm{EE}}-\lambda \mathbf{I}\right) v=0 \tag{7.20}
\end{equation*}
$$

where $\mathbf{I}$ is the identity matrix, and $v$ is the eigenvector scaled by $\lambda$ so that $\mathbf{J}_{\mathrm{EE}} v=\lambda v$.

We begin by taking the characteristic polynomial for $\mathbf{J}_{\mathrm{EE}}$. For a $3 \times 3$ matrix, the characteristic polynomial is

$$
\begin{equation*}
-\lambda^{3}+\operatorname{Tr}\left(\mathbf{J}_{\mathrm{EE}}\right) \lambda^{2}-\frac{1}{2}\left(\operatorname{Tr}\left(\mathbf{J}_{\mathrm{EE}}\right)^{2}-\operatorname{Tr}\left(\mathbf{J}_{\mathrm{EE}}^{2}\right)\right) \lambda+\operatorname{det}\left(\mathbf{J}_{\mathrm{EE}}\right) \tag{7.21}
\end{equation*}
$$

The trace of $\mathbf{J}_{\mathrm{EE}}$ is

$$
\begin{equation*}
\operatorname{Tr}\left(\mathbf{J}_{\mathrm{EE}}\right)=-2 \mu-\omega-\frac{(\mu+\omega)(\beta-\gamma-\mu)}{\gamma+\mu+\omega} \tag{7.22}
\end{equation*}
$$

This gives us the coefficients of the characteristic polynomial:

$$
\begin{align*}
& a_{1}=\frac{\beta \mu+\beta \omega+\gamma \mu+\mu^{2}+2 \mu \omega+\omega^{2}}{\gamma+\mu+\omega}, \\
& a_{2}=\frac{\beta \gamma \mu+\beta \gamma \omega+2 \beta \mu^{2}+3 \beta \mu \omega+\beta \omega^{2}-\gamma^{2} \mu-\gamma^{2} \omega-2 \gamma \mu^{2}-3 \gamma \mu \omega-\gamma \omega^{2}-\mu^{3}-\mu^{2} \omega}{\gamma+\mu+\omega}, \\
& a_{3}=\beta \mu^{2}-\beta \mu \omega-\gamma \mu^{2}-\gamma \mu \omega-\mu^{3}-\mu^{2} \omega . \tag{7.23}
\end{align*}
$$

A system with a third-order characteristic polynomial is Hurwitz stable if

1. $a_{1}, a_{2}$, and $a_{3}$ are all positive, and
2. $a_{1} a_{2}>a_{3}$.

Though this looks rather daunting symbolically, it can be numerically ascertained with ease if the parameters are known. The benefit of a Routh-Hurwitz stability analysis is that unlike the method of equilibria from eigenvalues, it can be applied to problems that otherwise would not be solvable. Moreover, Routh-Hurwitz stability theory generalizes conveniently to arbitrary higher degrees, i.e., more complex models.

It is worth noting that the reversion to susceptibility results in small perturbations around the equilibrium. As Keeling and Rohani [39] note, this dynamic has been used to explain the longer-term periodicities of infectious disease, most famously by Grassly, Fraser, and Garnett [70]'s model of the decadal cycle of syphilis incidence. The oscillatory period is given by

$$
\begin{equation*}
P=\frac{4 \pi}{4\left(\Re_{0}-1\right)(\gamma+\mu)(\omega+\mu)-\left(\omega+\mu-A^{-1}\right)^{2}} \tag{7.24}
\end{equation*}
$$

A number of terms in this equation relate to biologically significant quantities. $A$, of course, is the mean age at sustaining infection, which is calculated by

$$
\frac{\mu+\gamma+\omega}{(\mu+\omega)(\beta-\gamma-\mu)}
$$

Significantly, $I^{\star}=\frac{1}{\beta A}$-infections are at an endemic equilibrium point at a level given by the inverse of the transmission rate and the mean age of sustaining infection. The biological significance is not only that infections with a higher coefficient of transmission will result in a higher proportion of infectious individuals at the endemic equilibrium, but also that all things being equal, sustaining an infection at a younger age results in a higher disease burden. This, indeed, is the principal idea behind childhood vaccination: since $I^{\star} \propto \frac{1}{A}$, raising $A$ will lower $I^{\star}$, and thus reduce the overall disease burden.

### 7.2 Seasonality and periodicity in infectious diseases

Epidemics take place in time. The dynamics that we have examined in previous chapters inherently assumed a temporal element. The fact that we use differential equations means we are more concerned, in general, with change over time, rather than particular values at particular points in time. However, this should not keep us from realizing the time-dependent dynamics of epidemics. For this reason, we often represent various epidemic parameters, such as the incidence of a particular disease, as a time series.

Definition 7.5 (Time series). A time series is an array of one or more variables indexed by a discrete unit of time. We refer to the time series $X=\left(X_{t}: t \in T\right)$, and to each $X_{t}$ as an element or a data point in the time series. $T$ is called the time domain of the time series. Typically, we treat $t$ as zero-indexed, i.e., $t_{0}$ is the first value in a time series.

It is common to visualize time series of epidemic processes, particularly where a single outbreak is concerned, in a curve of the number of cases by the time of onset or time of confirmed diagnosis. This is frequently referred to as an epidemic curve.

Definition 7.6 (Epidemic curves). An epidemic curve (often called the epidemiological curve or epi curve for short) is a visual representation of incidence over time. It is a representation of an epidemic process in the time-amplitude space. Commonly, incidence is credited either with respect to the date of onset, i.e., each date shows the number of patients with onsets on a particular date, or the date of diagnosis/recognition.

An early finding of temporal analysis of epidemic dynamics relates to the symmetric nature of epidemic curves for outbreaks, known as Farr's law. The developments that have led to this finding-and with that, the first systematic study of the temporal dynamics of epidemics-are described in Subsection 7.2.1.

### 7.2.1 Case study: Farr's Law and smallpox in Britain

Dr. William Farr (1807-1883) was undoubtedly one of the heroic forerunners of the field that, over the centuries, grew to become modern epidemiology. His remarkable findings are the product not only of an agile mind, but also good fortune. When Britain embarked upon the first modern census, the United Kingdom Census of 1841, Farr obtained a position with the General Register Office, the organization newly established in 1837 to manage the registration of births, deaths, and marriages.

A physician who opened a (not very successful) practice in the 1830s, Farr's main interest was in statistics. This fit very well with the agenda of his supporters, the social reformer Edwin Chadwick and the Registrar General (the head of the General Register Office), Thomas Henry Lister, who saw the census as a way to illuminate health disparities in Britain, and thus bolster a socially progressive agenda. Farr used this support to create the first comprehensive tabulation of causes of death. As a side effect, he stumbled upon what became known as Farr's law. In an 1840 contribution to
the Second Annual Report of the Registrar General of Births, Deaths, and Marriages in England, he comments on a smallpox epidemic, asserting that "the small-pox increases at an accelerated and then a retarded rate; that it declines first at a slightly accelerated, and at a rapidly accelerated, and lastly at a retarded rate, until the disease attains the minimum intensity, and remains stationary" [251].

Epidemics are processes in space and time. Their temporal course often takes a characteristic shape, which we can mathematically exploit. Farr's law suggests that case counts are typically normally distributed around a peak value, with epidemics disappearing as fast as they appear. Indeed, this is often a perplexing phenomenon to behold: a raging outbreak can disappear with a rapidity that belies its seriousness, as if a switch had been flipped. Modern computational approaches [252] and clinical experience both confirm this phenomenon. The 2013-2016 West African Ebola outbreak is a good example: the epidemic struck Liberia in mid-May 2014, peaked in October of the same year, and by June 2015, it was nearly completely gone, just as suddenly as it appeared.

This section deals with the use of time series methods to understand epidemic processes.

### 7.2.2 Seasonality and decomposition

A time series may exhibit various patterns that we can usefully analyze. We are, more than anything, interested in two types of patterns:

1. recurrent relationships, which includes cycles, periodicities, and other patterns in which peaks or troughs occur at relatively constant intervals, and
2. trends, which are typically aperiodic changes over a long time.

We may thus express a time series as the sum of a seasonal (recurrent) process $S_{t}$, a nonseasonal (trend) process $T_{t}$ and a residual $R_{t}$ :

$$
\begin{equation*}
X_{t}=S_{t}+T_{t}+R_{t} \tag{7.25}
\end{equation*}
$$

This is known as an additive composition. Alternatively, the composition may be multiplicative, i.e.,

$$
\begin{equation*}
X_{t}=S_{t} \times T_{t} \times R_{t} \tag{7.26}
\end{equation*}
$$

Time series decomposition is essentially the challenge of identifying $S_{t}$ and $T_{t}$ for

all $t \in\left[t_{\min } ; t_{\max }\right]$ so as to minimize $\sum_{i=t_{\min }}^{t_{\max }} R_{i}$. When decomposing time series, additive decomposition is appropriate, where we may safely assume that the seasonal component is equal every year. In all other cases, multiplicative decomposition is the better choice. For instance, the number of hospital admissions for frostbite and hypothermia is higher in the winter than in the summer, but how much higher it varies from year to year.

There are numerous mathematical methods to accomplish time series decomposition, with the most frequently used methods being X11 decomposition [253], the LOESS-based STL algorithm [254] and seasonal adjustment methods [255]. We shall

![](https://cdn.mathpix.com/cropped/2024_06_11_9842913b8cdb0b8f0b50g-17.jpg?height=1404&width=1024&top_left_y=225&top_left_x=246)

Figure 7.4 Time series decomposition of influenza cases between 1920 and 1952 into a seasonal and trend component using an additive model, with residuals displayed at the bottom. Based on data from the U.S. Nationally Notifiable Diseases Surveillance System (NNDSS), maintained by the CDC. Data accessed from the University of Pittsburgh's Project Tycho.

however be primarily concerned with the results, rather than the ways to arrive at it (since the latter is helpfully catered for by a large number of Python packages).

Fig. 7.4 shows a time series decomposition of influenza incidence in the United States between 1920 and 1952. Analyzing a decomposition plot is a mainstay of understanding a composite periodical process. The breakdown in Fig. 7.4 is the standard format of presenting the results of time series decompositions:

1. Seasonality: as the name suggests, this is the periodic component of decomposition. The period of the process can be inferred from the distance between peaks of the periodic process, which in this case is approximately a year. The absolute value of the decomposition suggests the influence of the component in question. In this example, seasonality typically contributes to only about 15,000 cases a year, when total cases (shown in the top segment) are often quite a bit larger. This leads us to the second component, trend, which explains interyear variability.
2. Trend: this component explains longer-term interyear variability. For instance, there is a clear peak in the years between 1928 and 1930 and smaller peaks in the 1940s. The Great Depression, malnutrition, and the congregation of large numbers of people in makeshift "Hoovervilles" with scant, if any, medical care explains the former, whereas the latter is almost certainly a result of prolific influenzal spread among large numbers of servicemen confined in barracks and transport vessels that served as fertile breeding grounds for respiratory infections.
3. Residual: it is common to plot the residual differently from the trend and seasonal components to make explicit the nature of the residual as the "error term." The residual comprises values that are not explained by the seasonal or the term variables. In general, a low residual (no more than $25 \%$ of the total value) indicates a relatively good fit for the seasonal and trend decompositions. It is not uncommmon to see some periodicity in the residual, indicating a periodic process that is absent or excessively present in some years. In that case, it may be worthwhile to look at time segments where the residual appears to be periodic (e.g., in the case of Fig. 7.4, the years between 1920-1928) in a separate decomposition.

A time series decomposition is equal parts quantitative and qualitative. It uses quantitative methods to arrive at a decomposition that however is often interpreted in a qualitative context.

## Computational Note 7.4 Time series decomposition

There are multiple solutions to choose from for time series decomposition. The solution offered by statsmode1s is perhaps the most efficient, returning each of the time series as a separate object.

statsmode1s assumes that the input is a Pandas object with a DateTimeIndex or a similar time-index. If this is not the case, data points must be equally spaced, and the period between them must be supplied to the function using the period keyword.

First, we import statsmode1s:

import statsmodels.api as sm

Next, we obtain our data from Project Tycho and import it our time series into a data frame, which, for convenience's sake, we shall call df. Project Tycho is a
standardized interface to a wide range of disease surveillance data, including all of the National Notifiable Disease Surveillance System (NNDSS) in the United States. It can be accessed using an API key, which is how we will be obtaining the data. The project's website, tycho.pitt.edu, provides more information.

We begin by encoding our query parameters into a URL. It is a common practice to save API ketys as an environment variable, and obtain it using the os.getenv() function. This ensures we do not disclose or accidentally commit our API key to a repository. Because query items may contain strings that have spaces in them (e.g., to specify the United States as the geography of the query, we write CountryName=UNITED STATES OF AMERICA), we need to replace these with their "percent encoded" value to form a well-formed URL. The percent encoded value of a whitespace character is $\% 20$, so we replace all spaces in our initial query with $\% 20$ :

```
f1u_ur1 = "https://www.tycho.pitt.edu/api/query?apikey="
    + os.getenv("TYCHO_APIKEY") + " &ConditionName
    =Influenza&CountryName=UNITED STATES OF AMERICA
    &PeriodStartDate>=1930-01-01
    &PeriodEndDate<=1950-01-01".rep1ace(" ", "%20")
```

We now pass this URL on to Pandas, and perform some aggregations. In particular, we group by period end date and sum up values, and rename the columns to fit our specifications:

```
df=pd.read_csv(f1u_ur 1,
    1ow_memory=Fa1se)[["PeriodEndDate","CountVa1ue"]].\
                                groupby(["PeriodEndDate"]).\
                                sum().\
                                reset_index().\
                                rename(columns={
                                "PeriodEndDate":"Date",
                                "CountVa1ue":"Cases"})
```

In general, the best input for statsmode1s is a datetime-indexed Pandas dataframe. In most cases, incidence data is of a common columnar format:

|  | Date | Cases |
| :--- | :--- | :--- |
| 0 | $1919-11-01$ | 344 |
| 1 | $1919-11-08$ | 326 |
| 2 | $1919-11-15$ | 312 |
| 3 | $1919-11-29$ | 278 |
| 4 | $1919-12-06$ | 293 |
| $\ldots$ |  |  |

To convert the Date column into a datetime index, we may do so using pd.to_datetime(df.Date), then assign it as an index using pd.set_index(df.Date).

We can confirm that we have a datetime-indexed data frame by calling the index object:

```
DatetimeIndex(['1919-11-08', '1919-11-29',
...
'1941-02-01', '1941-02-01'],
dtype='datetime64[ns]',name='Date',1ength=221574,freq=None)
```

We now go on to decompose this time series:

decomposition = sm.tsa.seasonal_decompose(df)

By default, seasona 1_decompose( ) assumes an additive decomposition. The model parameter can be set to multiplicative for a multiplicative decomposition, e.g.,

```
decomposition = sm.tsa.seasonal_decompose(df,model="multiplicative")
```

The result is a DecomposeResult object. This comprises a number of attributes, each containing a component of the time series:

- observed contains the source time series,
- seasona 1 contains the seasonality component,
- trend contains the trend component, and
- resid contains the residuals.

We will discuss ways to represent the decomposition in a manner similar to Fig. 7.4 in Computational Note 7.5.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch07/ ts_ decomposition/.

### 7.2.3 Perennial processes

A perennial plant is one which blooms every year (as opposed to an annual plant, which completes its entire life cycle in a single year). The revolution of the Earth around the Sun mediates a broad range of infectious disease parameters. For instance, cold weather in winter causes vasoconstriction, and thus a less efficient immune response, and therefore a greater liability to contract respiratory illnesses. Less obviously, the greater degree of social contacts during winter, occasioned by our very human aversion to being out in the cold, means that certain pathogens, typically respiratory viruses, can take hold of larger populations. Perenniality is the most typical
form of periodic recurrence of human pathogens, and it therefore merits our special attention.

Fig. 7.4 shows the incidence of influenza in the United States between 1920 and 1952, decomposed into additive seasonal and trend components. This is an example of perennial phenomena with a trend. As the seasonal element shows, there is a strong perennial periodicity to influenza incidence.

Definition 7.7 (Perennial incidence). A perennially incident infectious disease is an infectious disease with a periodic incidence that exhibits a roughly 12-month periodicity.

## Computational Note 7.5 Plotting time series decompositions

In Computational Note 7.4, we discussed the decomposition of a time series into trend, seasonal, and residual components. It is often helpful to plot these along a shared axis. Given a decomposition result object decomposition, we would use GridSpec to create a structured plot like Fig. 7.4:

```
fig = plt.figure(figsize=(20, 16))
gs = gridspec.GridSpec(4, 1, height_ratios=[3,1,1,1])
gs.update(hspace=0.2)
ax1 = plt.subplot(gs[0])
ax1.p1ot(decomposition.observed)
ax1.set_yscale("log")
ax1.set_y7abel("Cases")
ax2 = plt.subplot(gs[1], sharex=ax1)
ax2.plot(decomposition.seasonal)
ax2.set_y7abe7("Seasona7")
ax3 = plt.subplot(gs[2], sharex=ax1)
ax3.p1ot(decomposition.trend)
ax3.set_y1abel("Trend")
ax4 = plt.subplot(gs[3], sharex=ax1)
ax4.scatter(decomposition.resid.index, decomposition.resid, s=0.05")
ax4.set_y7abel("Residual")
fig.align_1abels()
```

The results of such a plot, for the time series decomposition in Computational Note 7.4, is displayed as Fig. 7.4.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch07/ ts_ decomposition.

Of course, not all periodic peaks in disease are perennial. For instance, Grassly, Fraser, and Garnett [70] observed that the incidence of syphilis had an approximately 10 -year periodicity, which is consonant with the time it takes for post-infectious immunity to wane to levels that once again permit an outbreak. While this finding is far from uncontroversial (see, e.g., Breban et al. [256] for a skeptical view on the alleged periodicity of syphilis infections), it is clear that annual cycles and longer multiyear processes, are crucial to our understanding of infectious disease dynamics.

### 7.2.4 Continuous wavelet transform (CWT)

One of the greatest ideas of mathematics is that all time series one is likely to encounter in nature can be described as a superposition of periodic functions. This means that given a signal in the time domain (i.e., the $\mathrm{x}$-axis constituting time, the $\mathrm{y}$-axis constituting the value of the signal), such as a time series, we can obtain its representation in the frequency domain, giving rise to Fourier analysis. In other words, we can transform a time-denominated series into information on the frequencies that make up the series. To us as epidemiologists, this matters primarily, because the frequencies we are discussing here constitute the periodicities of the infectious process. Thus by transforming a time series into its frequency domain representation, we can gain significant insights about the recurrent properties. The result we obtain is called the spectrum.

Definition 7.8 (Spectrum). The spectrum of a time series $X_{t}$ is the representation of the time series in the frequency domain. The spectral value or spectral power of a frequency is the contribution of the periodic processes with that frequency to the overall time series.

The Fourier transform, a popular way of putting a time series into the frequency domain, analyzes time series using a complex exponential. Wavelet analysis is a significantly more powerful technique for the same purpose, using a wavelet as the analyzing function. This is relevant, because wavelets can be "scaled," allowing us some valuable insights into the rate at which values change.

Given a signal $X(t)$, such as a time series, the CWT at $t_{0}$ for the scale parameter $s$ is given by

$$
\begin{equation*}
\operatorname{CWT}\left(s, t_{0}, f(t), \psi(t)\right)=\int_{-\infty}^{\infty} f(t) \frac{1}{s}\left(\psi\left(\frac{t-t_{0}}{s}\right)\right) d t \tag{7.27}
\end{equation*}
$$

CWT can be used to obtain a visual representation called a scalogram, which shows the power of each of a continuous range of frequencies at all points in time of a time
series. This is commonly referred to as the signal in time-frequency space (as opposed to time-amplitude space, which is the epicurve we know and love). From an epidemiological perspective, scalograms are tools that help us identify the periodicity of an epidemic process and longer, multiyear dynamics.

The most frequently used approach to CWT analysis of time series originates with Torrence and Compo's 1998 paper, which applied CWT to elicit longer-term periodic dynamics of climate measurements [257]. The mathematics of wavelet transforms is complex, and I do not seek to repeat the work by Torrence and Compo [257] here. However, a brief overview is certainly appropriate.

A wavelet is, at its simplest, a short oscillating signal that begins at, and reverts to, zero, and is a function of a nondimensional time parameter, which we shall call $\eta$. We will, in particular, use a class of wavelets called Morlet wavelets, which are defined as

$$
\begin{equation*}
\psi_{0}(\eta)=\pi^{-\frac{1}{4}} e^{i \omega_{0} \eta} e^{-\frac{\eta^{2}}{2}} \tag{7.28}
\end{equation*}
$$

In this equation, $\omega_{0}$ is the nondimensional frequency. Then, given a time series $X_{t}: x_{1}, x_{2} \ldots x_{N}$, where each measurement is $\delta_{t}$ apart, the continuous wavelet transform of $X_{t}$ is the convolution of $X_{t}$ with the wavelet $\psi_{0}(\eta)$ scaled by the scale factor $s$ and translated along the time index, $t$. Specifically,

$$
\begin{equation*}
W_{t}(s)=\sum_{i=0}^{N-1} x_{i} \psi_{0} \overline{\left(\frac{(i-t) \delta_{t}}{s}\right)} \tag{7.29}
\end{equation*}
$$

where the bar denotes the complex conjugate. $W_{t}(s)$ is a complex variable with a real part $\operatorname{Re}\left(W_{t}(s)\right)$ and an imaginary part $\operatorname{Im}\left(W_{t}(s)\right)$. The amplitude is the modulus of $W_{t}(s)$, i.e., $\sqrt{\operatorname{Re}\left(W_{t}(s)\right)^{2}+\operatorname{Im}\left(W_{t}(s)\right)^{2}}$. The wavelet power spectrum is then $\left|W_{t}(s)\right|^{2}$.

We may conceive of this process as taking a signal (in this case, the weekly incidence data), and constructing a wavelet that is "dragged" across the signal. At each position, a similarity coefficient (similar, but not identical, to a correlation coefficient) is calculated. The process is then performed with the wavelet being scaled (stretched). At a sufficient granularity of scales, this eventually results in information about the magnitude (power) of periodicities over time, providing us with a view of what scale contributed to what degree to the overall signal. Since scale is inversely related to frequency, this grants us insight into the dominant periodicities of infectious processes.

To assist us in comparing the wavelet power spectra of different processes, it is helpful to perform some normalization. The expectation value of $\left|W_{t}(s)\right|^{2}$ for a white noise time series is the variance of the time series. Consequently, we divide the power by the variance $\sigma^{2}$ to normalize it. For the Morlet wavelet, the equivalent Fourier period is approximately equal to the inverse of the scale factor, whereas for other wavelets, it can be derived using the method described in the appendix of Meyers, Kelly, and O'Brien [258].

We can now plot the normalized power $\frac{\left|W_{t}(s)\right|^{2}}{\sigma^{2}}$ for each point of $t$ and $\frac{1}{s}$, i.e., time and period. This is how we arrive at the scalograms (middle figures) in Fig. 7.5.

![](https://cdn.mathpix.com/cropped/2024_06_11_9842913b8cdb0b8f0b50g-24.jpg?height=1332&width=1200&top_left_y=226&top_left_x=123)

Figure 7.5 Continuous wavelet transform of the weekly incidence of measles (left) and pertussis (right): source data (top), scalogram (middle) and 3-36 month scale-averaged power (bottom). The scalogram is a visual representation of the intensity to which a signal of a particular frequency contributes to the overall value of a variable over time. In this case, it shows that while the incidence of measles has a strong dominant and statistically significant annual component, pertussis does not exhibit the same regularity and is largely influenced by $2-4$ year trends.

Based on data from the U.S. Nationally Notifiable Diseases Surveillance System (NNDSS), maintained by the CDC. Data accessed from the University of Pittsburgh's Project Tycho.

Reading a scalogram is something of a learned skill, but may provide insights beyond simple Fourier plots due to its ability to represent changes over time. The scalogram is a plot of the relative power of different frequencies over time. Looking at
it as a series of year-width columns, the scalogram shows the periodicities of the dominant periodic processes in that year. Typically, brighter colors indicate higher powers at the given frequency. It is common for a scalogram to show statistical significance as a black outline. In addition, there is typically a "cone of interest" marking on scalograms, which is often presented as a hatched or faded area. This is because towards the end or beginning of the timeframe, periodicities above a certain length are no longer reliably calculated.

Fig. 7.5's left-side scalogram shows a prominent band at the period of one year. This is not overly surprising; a brief perusal of the time series, plotted above, would conclude equally well that measles has an annual periodicity. However, less obvious are the high-intensity areas between 1935 and 1950 at 3-4 years, indicating that during these years, an additional longer-term dynamic, with a period of 3 to 4 years, was at play.

Scalograms are even more useful when the time series does not exhibit any obvious "first glance" periodicity. The time series of pertussis, shown on the right of Fig. 7.5, does not seem to have any clear periodicities. The scalogram, however, suggests that there is, in fact, a two-year and a four-year dynamic involved, albeit this does not rise to the level of statistical significance.

CWT and scalograms are powerful qualitative-quantitative tools to detect longerterm and time-varying periodicities that would escape most other methods of time series analysis. Though CWT is one of the more intricate and challenging techniques in this book, it rewards analysts with often quite exceptional insights.

## Computational Note 7.6 Continuous wavelet transform

There are multiple packages for Python that offer continuous wavelet transform functionality, but of these, PyCWT is the most convenient and the most powerful at the same time. In this Computational Note, we will compare the continuous wavelet transforms of measles and pertussis between 1923 and 1956, obtained from Project Tycho.

First and foremost, we need to convert the DateTime Index to fractional years. It is a common notational convention in meteorology, where the CWT method was developed to analyze climate change, to describe dates as fractional years. To facilitate this conversion, we create a function for this:

```
def index_to_fractional_years(df: Union[pd.DataFrame, pd.Series])
    -> np.array:
    " " "
    Converts a datetime-indexed df's index to a numpy array of
    fractional years.
    " " "
    assert is instance(df.index, pd.DatetimeIndex)
```

```
return df.index.map(1ambda x: \
    (float(x.strftime("%j"))-1) / 366
    + float(x.strftime("%Y"))).to_numpy()
```

Next, we need to normalize our data by detrending. We do so by fitting a least squares first degree polynomial fit using the np.polyfit() function. This function returns the coefficients of the polynomial, which we then return to the np.polyval() function to evaluate the polynomial over the data. Finally, we normalize the data by dividing it by its standard deviation.

```
def normalize(data: pd.Series) -> (np.array, float):
    t = index_to_fractional_years(data)
    p = np.polyfit(t - t[0], data.values, 1)
    detrended_data = data - np.polyval(p, data)
    return detrended_data/detrended_data.std(), detrended_data.std()
```

The PyCWT package provides the .cwt() function to perform CWT analysis. For this to work, we will need to specify the "mother wavelet" and its possible scales. All wavelet filters are composed by varying the mother wavelet by way of two parameters: the number of "octaves" and the number of "suboctaves," sometimes referred to as "voices per octave." An octave increases the scale of the wavelet by doubling it (much as playing the same tone an octave higher corresponds to doubling its frequency). The number of suboctaves or "voices" refers to the number of equally-spaced parts that we subdivide each octave. Despite its name, the continuous wavelet transform is discontinuous in the sense that we need to evaluate it at particular values of the scaling factor $s$ to obtain a computational answer. The granularity of this evaluation is determined by the number of suboctaves.

We need to provide, other than the data, a few starting parameters:

- dt, the frequency of measurements. Our measurements are monthly, but since months are of slightly different lengths, their fractional year equivalent is going to be different. We compensate for this by taking the mean of the differences of the fractional year index

(np.diff(index_to_fractional_years(data)).mean()).

- s0, the starting scale. This is our assumption of the lowest possible value of whatever periodicity we expect to find. There is no harm in setting this at an unrealistically low level other than slightly increasing computational cost. For this reason, even though it is rare to find infectious diseases with a period under twelve months, we will set this to half a month.
- The number of octaves, $J$, is the upper limit on the largest resolvable scale. There is no real harm in setting this quite high, even beyond what we might
anticipate to be an epidemiologically realistic period. It is not entirely uncommon for epidemics, especially those that are closely connected to lowfrequency climatic changes, to have oscillatory components with a period that numbers in the decades. We specify, in addition, the number of suboctaves per octave, $\mathrm{dj}$.
- Finally, we need to specify the "mother wavelet," a wavelet that is then manipulated and shifted. Different wavelets are better at detecting different dynamic phenomena. The Morlet wavelet, discussed above, is specifically suitable to the analysis of signals, where the expected periodicity's frequency is likely to be mostly constant.

```
def cwt(data: pd.Series):
    mother = wavelet.Mor1et(6)
    idx = index_to_fractional_years(data)
    dt = np.diff(idx).mean()
    s0 = 2 *dt
    dj = 1/52
    J = 8/dj
    alpha, _, _ = wavelet.ar1(data.values)
    normalized_data, stdev = normalize(data)
    wave, scales, freqs, coi, fft, fftfreqs
        = wavelet.cwt(normalized_data.to_numpy(),
            dt,
            dj ,
            s0,
                    J,
                    mother)
```

. .

The .cwt() function returns the wavelet transform, including the Fourier spectra. One thing we are interested in particular is which scales and frequencies are statistically significant. For this, we will first need to obtain the power at each point, and also prepare our index for the values.

```
...
power = (np.abs(wave)) ** 2
period = 1/freqs
t = index_to_fractional_years(data)
. . 
```

We calculate the boundary of significance at $p<0.05$ at each point of evaluation (i.e., each time unit and each scale and subscale):

```
- . 
signif, fft_theor
    = wavelet.significance(1.0, dt, scales, 0, alpha,
        significance_1evel=0.95,
        wavelet=mother)
sig95 = np.ones([1, len(normalized_data)]) * signif[:, None]
sig95 = power/sig95
```

Owing to the last line, sig95 will be an array of the same size as the array of powers, with a value over unity for significant points. This is a practically quite sensible trick, as it allows us to plot the borders of the significant areas quite simply by drawing a contour where sig95 takes a value of 1 .

Finally, we calculate the average scale in the period between 0.25 and 3 years, and normalize the data against it:

```
sel = find((period >= 0.25) & (period < 3))
Cdelta = mother.cdelta
scale_avg
    = (scales * np.ones((1en(normalized_data), 1))).transpose()
scale_avg
    = power / scale_avg 非 As in Torrence and Compo (1998) eq. 24
scale_avg
    = stdev ** 2 * dj * dt / Cdelta * scale_avg[se1, : ].sum(axis=0)
scale_avg_signif, tmp
    = wavelet.significance(stdev ** 2, dt, scales, 2, alpha,
                                significance_1eve1=0.95,
                                dof=[sca1es[se1[0]],
                                scales[se1[-1]]],
                        wavelet=mother)
return t, dt, period, power, coi, sig95, scale_avg,
scale_avg_signif
```

The notebook on the book's companion repository details the plotting algorithm to obtain the scalogram. The coi output from the cwt function provides the "cone of influence," the cross-hatched area on the scalogram, within which edge effects become manifest. In short, as we move towards the start or the end of the time series, the data needs to be "extended" by padding it with zero-valued cells
to be able to fit wavelets above a certain scale. This reduces amplitudes below their correct values, and CWT is not reliable in these edge areas. The cwt function therefore provides this zone, in which information becomes less reliable due to edge phenomena, and we represent this by cross-hatching.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch07/ cwt/.

### 7.3 Temporal forcing

Sometimes, there is a significant time-dependent exogenous process that affects a pathogen's spread. For instance, most pediatricians are quite familiar with the sudden upsurge of infectious illnesses and crowded waiting rooms around September, when the school term starts. Temporal forcing (or temporal modulation of the force of infection) describes the manner in which the temporal dynamics of infectious diseases are modulated by an exogenous variable.

### 7.3.1 Case study: summer, school, and poliomyelitis

Poliomyelitis is a disease caused by an enterovirus, which typically colonizes the gastrointestinal tract and causes mild disease resembling a rather typical gastrointestinal infection. In a small fraction of cases, estimated to be around one case in a hundred, the poliovirus affects the central nervous system, causing a serious syndrome characterized by meningitis, and in a very small number of cases, acute flaccid paralysis [259]. Though poliomyelitis was eradicated in the United States in the late 1970s [260], the global eradication of polio remains a major public health priority [261,262].

Many of the seasonal dynamics that drive the ebbs and flows of infectious disease relate to natural features. For instance, Martinez [263] categorized a wide range of infectious diseases by their prime drivers: vector seasonality, climatic features, non-climatic abiotic features (e.g., water salinity), and seasonal exposure differences. A specific subset of the last category, in the context of paediatric infectious disease, is the effect of school terms on disease transmission.

In countries with near-universal public primary and secondary education, few factors affect the school-age population's encounter rate with other individuals as much as the scheduling of the school term. Fig. 7.6 shows the incidence, per week, of poliomyelitis in the United States between 1945 and 1953, highlighting the 245th day of each year, around which school terms tend to start. It is not by accident that those weeks are the high water mark of incidence, preceded by a few weeks that are accounted for by earlier starts of school years and late summer activities (e.g., late summer camps).

The impact of seasonal dynamics is not limited to poliomyelitis, of course. Equally, it is important to keep in mind that these seasonal dynamics often mediate other fac-

![](https://cdn.mathpix.com/cropped/2024_06_11_9842913b8cdb0b8f0b50g-30.jpg?height=791&width=1202&top_left_y=224&top_left_x=124)

Figure 7.6 Temporal forcing of poliomyelitis. Poliomyelitis cases between 1945 and 1953 tend to peak around the start of the school year. Day 245 (corresponding to September $1 /$ September 2) is marked with a black vertical line.

Based on data from the U.S. Nationally Notifiable Diseases Surveillance System (NNDSS), maintained by the CDC. Data accessed from the University of Pittsburgh's Project Tycho.

tors. As Dowell [264] notes, the summer-autumnal seasonality of many diseases in the Northern hemisphere is typically reversed in the Southern hemisphere, suggesting that the seasonality or time of the year in fact mediates the effect of temperature both on disease transmission and on human behavior. Sultan et al. [265], meanwhile, described how outbreaks of meningococcal meningitis in the Sahel correlate to periods of dry weather and intense winds that compromise the upper respiratory mucosa, thereby allowing pathogenic entry. These examples illustrate an important fact about seasonal dynamics that mediate seasonal climatic variabilities: the interaction between climate and individuals depends on the place and the population.

### 7.3.2 Sinusoidal forcing

The general model of temporal forcing is to replace the constant $\beta$ with a timedependent variable $\beta(t)$. This time-dependent variable is composed of a baseline transmission rate $\beta_{0}$ and a time-varying forcing component consisting of the amplitude of forcing, $\beta_{1}$, and the angular frequency of forcing, $\omega$ [39].

$$
\beta(t)=\beta_{0}(\overbrace{1}^{\text {base } \beta}+\overbrace{\beta_{1} \cos (\omega t)}^{\text {time-varying } \beta}) .
$$

For oscillations with an annual period-as the vast majority of oscillations are- $\omega=2 \pi$, and thus Eq. (7.30) becomes

$$
\begin{equation*}
\beta(t)=\beta_{0}(\overbrace{1}^{\text {base } \beta}+\overbrace{\beta_{1} \cos (2 \pi t)}^{\text {time-varying } \beta}) . \tag{7.31}
\end{equation*}
$$

At annual periodicity, in the winter, i.e. $2 \pi t$ is close to either zero or one. This may be suitable to model the classical winter infections (e.g., influenza) on the northern hemisphere, but would need to be adapted for the southern hemisphere or for pathogens that are more abundant in the summer. For these instances, the cos function may be inverted by reversing the sign of the forcing term, i.e.,

$$
\begin{equation*}
\beta(t)=\beta_{0}(\overbrace{1}^{\text {base } \beta}-\overbrace{\beta_{1} \cos (2 \pi t)}^{\text {time-varying } \beta} . \tag{7.32}
\end{equation*}
$$

For finer adjustments, it is possible to add a phase term $\psi$ :

$$
\begin{equation*}
\beta(t)=\beta_{0}(\overbrace{1}^{\text {base } \beta}+\overbrace{\beta_{1} \cos (\omega t+\underbrace{\psi}_{\text {phase }})}^{\text {time-varying } \beta}) . \tag{7.33}
\end{equation*}
$$

This is particularly useful for pathogens that occupy the spring $(\psi=-\pi)$ and autumn $(\psi=\pi)$ parts of the epidemic calendar, such as varicella and polio, respectively [263].

### 7.3.3 Term-time forcing

The sinusoidal model of forcing is a good approximation for processes that have a periodicity that largely depends on the season. For human populations, however, a significant factor is whether schools are in session at a particular time (which is also a relatively good proxy for when occupancy at workplaces is lower or higher). This is often accomplished using the Term function.

Definition 7.9 (Term function). The term function $\operatorname{Term}(t)$ takes the value 1 if $t$ falls within a school term and -1 if it does not.

School terms vary, but a summary of approximate dates for England is given in Table 7.1. This is a good starting point, although models should preferably use a termtime calendar from the population being considered.

The time-dependent transmission rate with the term-time function would be formulated as

$$
\begin{equation*}
\beta(t)=\beta_{0}\left(1+\beta_{1}\right)^{\operatorname{Term}(t)} \tag{7.34}
\end{equation*}
$$

where $\operatorname{Term}(t)$ is the term-time function

$$
\operatorname{Term}(t)= \begin{cases}1 & \text { if } t \text { is in term time }  \tag{7.35}\\ 0 & \text { otherwise }\end{cases}
$$

Table 7.1 Major school holidays in England, after Keeling, Rohani, and Grenfell [266].

| Holiday | Days | Dates |
| :--- | :---: | :--- |
| Winter | $356-6$ | 21 December-06 January |
| Easter | $100-115$ | 10 April-25 April |
| Summer | $200-251$ | 19 July-08 September |
| Autumn half-term | $300-307$ | 27 October-03 November |

Table 7.2 $\beta_{0}$ and $\beta_{1}$ parameters of three common infectious diseases in England and Wales, after Keeling, Rohani, and Grenfell [266].

| Pathogen | $\boldsymbol{\beta}_{\mathbf{0}}$ | $\boldsymbol{\beta}_{\mathbf{1}}$ |
| :--- | :--- | :--- |
| Measles | 1.175 | 0.25 |
| Pertussis | 0.664 | 0.25 |
| Rubella | 0.311 | 0.60 |

Fig. 7.6 is an example of both sinusoidal forcing and term-time forcing, which can coexist. The plot shows the incidence of poliomyelitis in the United States between 1945 and 1953. The peaks are centered around, and sometimes slightly to the right of, the start of September, when schools return from summer holidays. The combination of relatively warm late summer weather and the congregation of young susceptible individuals in close proximity creates a fertile breeding ground for illnesses, including transmission from still-infectious asymptomatic cases to susceptible individuals.

The basic reproduction number $\Re_{0}$ for a term-time forced model is essentially a weighted average of $\beta_{0}$ and $\beta_{1}$ divided by $\gamma$ :

$$
\begin{equation*}
\mathfrak{R}_{0}=\frac{1}{\gamma+\mu} \int_{t_{\min }}^{t_{\max }} \frac{\beta_{0}\left(1+\beta_{1}\right)^{\operatorname{Term}(u)}}{t_{\max }-t_{\min }} d u \tag{7.36}
\end{equation*}
$$

The term-time model can be adapted to other seasonal phenomena, e.g., for tourist seasons or work holidays. The variable $\beta_{0}$ and $\beta_{1}$ coefficients for some common pathogens is laid out in Table 7.2.

## Practice Note 7.1 School terms: not just for kids

It comes quite naturally to an infectious disease modeler to consider the impact of term times on a school-age population, but in fact, term times are quite applicable to other populations as well. Term-time mediates workplace attendance behaviors, so that most people take their holidays out of term-time. Factory shutdowns often coincide with major school holidays in the region.

In specific populations and specific settings, however, the inverse is true. There are certain encounters that take place more often outside of term-time. Long distance travel, for instance, increases outside term-time [267,268]. This vastly enhances the speed by which a novel pathogen can spread all over the world.

In addition, certain specific settings, such as long-term care facilities and nursing homes, experience a higher volume of visitors during the holidays, which may expose their patients to pathogens from the outside world. Halvorsrud and Örstavik [269] describe a particularly unpleasant instance of rotavirusassociated gastroenteritis that made its way to a care facility for elderly patients during the holiday season. It is therefore always important to keep in mind that all are not created equal when it comes to the effects of seasonal fluctuations; what may increase the encounter rate in one population might, in another, drive it down.

### 7.3.4 Non- $\beta$ forcing

$\beta$ forcing assumes that the time-varying parameter is the transmission coefficient. However, a number of other factors may change, most importantly, as it relates to the population. In particular where domestic animals bred at quantity are concerned (e.g., poultry, rabbits), births tend to occur in pulses. Fig. 7.7 exemplifies this tendency. In this case, the fluctuations in the birth rate create complex long-term dynamics. Davis et al. [270] observed, for instance, that cases of bubonic plague fluctuate in accordance with fluctuations of its intermediate host in the region, the great gerbil (Rhombomys opimus). Periodic oscillations in the number of hosts and vectors, which in turn is related, by way of the Lotka-Volterra model, to seasonal fluctuations in the number of their natural predators, create "downstream" oscillations in the number of infections on the host plane.

![](https://cdn.mathpix.com/cropped/2024_06_11_9842913b8cdb0b8f0b50g-33.jpg?height=486&width=1182&top_left_y=1528&top_left_x=174)

Figure 7.7 A birth-pulsed SIR system with a base birth rate of $\mu=0.001$ and a cosine birth pulsing model with a multiplier of $\mu_{1}=0.3$.

A special case of non- $\beta$ forcing is where there is a seasonal intervention, such as pulse vaccination (see Subsubsection 6.1.2.3). This effectively varies the pool of susceptibles in a pulsed manner. A concern with such approaches is that at and above certain values, a system may develop long-term nonlinearities, so that relatively small differences in the intervention (e.g., the time-varying aspect of the vaccination rate) might result in large differences with respect to long-term outcomes. For this reason, a detailed sensitivity analysis for such interventions, assisted by modeling of the effects of differences in phase, will often prove helpful. The method described in Computational Note 7.7 is a useful tool for the quantification of chaotic behavior.

### 7.3.5 Bifurcations and chaos

It is our ordinary expectation, gained from every-day life, that small changes to the parameters of a system will result in comparably small differences. A steak cooked to 140 degrees Fahrenheit might meet with a food inspector's disapproval, but it is not fundamentally different from a steak cooked to a safe 145 degrees Fahrenheit. Forced dynamical systems follow this rule, too; up to a point. As forcing increases, it becomes increasingly difficult to predict where the system will settle. The consequence is that above a certain critical point, extremely small differences in the forcing parameter will result in very different long-term outcomes [271]. The emergence of chaotic phenomena means that in the sufficiently long run, above a certain level of forcing, the relationship between the forcing parameter and the long-term equilibrium (as measured by the number of infected individuals measured at one-year intervals after running the model for several years) becomes quite discontinuous [272,273].

The analytical expansion of most epidemic models is often quite complex, and though an interesting problem from the mathematical standpoint, it is arguably of lower practical utility. Practically, however, understanding the nonlinear dynamics of small perturbations to an epidemic system at a sufficiently long time range helps us in reasoning about the accuracy of our predictions and identify when those might be affected by a strong nonlinear dependence on a parameter or initial condition. Computation affords us the ability to simulate outcomes (such as the proportion in the infectious compartment) at an arbitrary range of values for our initial parameter of choice, and thus numerically analyze a system's likelihood of nonlinear response.

## Computational Note 7.7 Discrete Lyapunov exponents to estimate chaos

Discrete Lyapunov exponents are a quantitative way to identify when the evolution of a deterministic system takes on chaotic features. Recall that we understand chaotic behavior as the point where, past a critical point, minor changes in a parameter result in major fluctuations in an outcome variable, and these fluctuations are largely quite discontinuous. The Lyapunov exponent allows us to quantify this transition.

Since we expect to solve our problems computationally, a discrete time model is perfectly adequate for our purposes. Let us consider $f_{t, p}$ a function over discrete time with the discrete parameter $p$. If we evaluate this function at a fairly long time scale, we would expect the difference between $f_{t, p}$ and $f_{t, p+\epsilon}$, where $\epsilon \rightarrow 0$, to be quite small. Chaotic systems, however, are characterized by a strong dependence on the value of the discrete parameter, so that even the minute change to $p$ that is represented by $\epsilon$ causes a very significant difference. We can thus analyze whether any value of $p$ will result in chaotic behavior by looking at the differences between $f_{t, p}$ and $f_{t, p+\epsilon}$ at sufficiently large values of $t$. The maximal discrete Lyapunov characteristic exponent (MDLCE) accomplishes this by essentially taking the limit of the mean of the logarithm of the absolute value of the difference between each value of $p$ and the next.

$$
\begin{equation*}
\lambda\left(f_{p}\right)=\lim _{t \rightarrow \infty} \lim _{\epsilon \rightarrow 0} \frac{1}{t} \ln \frac{\left|f_{t, p+\epsilon}-f_{t, p}\right|}{|\epsilon|} \tag{7.37}
\end{equation*}
$$

The idea is that as systems descend into chaotic behavior, the difference between the long term limits $\lim _{t \rightarrow \infty} f_{t, p}$ and $\lim _{t \rightarrow \infty} f_{t, p+\epsilon}$ increases for sufficiently large values of $t$, and the Lyapunov exponent allows us to express this in a single figure for each $p$, where values of $\lambda\left(f_{p}\right)>1$ suggest chaotic long-term behavior.

In practice, computational approaches do not favor infinities, so we will often have to make do with bounded but long periods of time. A conventional way to calculate a bifurcation map and the corresponding Lyapunov exponents (see, e.g., Keeling and Rohani [39]) is to integrate the system of ODEs for a long time for different values, then sample the compartment of interest (typically, $I$ ) at regular intervals, e.g., every year for the last ten years, as our approximation for $t \rightarrow \infty$. We will do so for a fairly large number of values, which is performanceintensive. For this reason, we will have to use a more performant ODE solver

JiTCODE is a highly performant ODE solver that has two remarkable features [204]. First, it precompiles code into C, which speeds up execution. Second, it comes with an automated functionality for determining the Lyapunov exponent.

We begin by importing jitcode, as well as the symbols for sin and pi from symengine, the symbolic computation tool that backs jitcode.

```
from jitcode import jitcode_lyap, jitcode, y, t
import symengine
from symengine import sin, pi
```

The $y$ symbol we imported is JiTCODE's abstraction for a vector of the lefthand side quantities in the differential equation. Since we prefer to call these by their name, we redefine $y(0)$ and $y(1)$ to the variables $S$ and $\mathrm{I}$ :

S, I $=[y(i)$ for i in range(2)]

Next, we define our constants:

```
beta_0 = 1.3
gamma = 1/13
mu = 1/(70 * 365)
I_0 = 1e-3
S_0 = 1 - I_0
```

These are the constants we do not envisage to change. $\beta_{1}$, on the other hand, will. For this reason, we need to represent it symbolically, by declaring a symengine symbol:

beta_1 = symengine.Symbol("beta_1")

We may now finally define our model. Unlike odeint and solve_ivp, JiTCODE does not require the differential equation to be defined as a function. Among others, it can be defined as a simple Python dictionary:

```
time_dependent_sir = {
    S: mu - beta_0 * (1 + beta_1 * sin(2 * pi * t / 365)) * S * I
        - mu * S,
    I: beta_0 * (1 + beta_1 * sin(2 * pi * t / 365)) * S * I
        - mu * I - gamma * I
}
```

Next, we define the ODE object with the jitcode_1yap function, supplying it with the model. Since we are only interested in the maximum Lyapunov coefficient, we set the n_lyap parameter to 1 . We define beta_1 as a control parameter, which means that the ODE will be capable of parameterization with various values of $\beta_{1}$ :

```
ODE = jitcode_1yap(time_dependent_sir, control_pars=[beta_1],
    n_1yap=1)
```

Next, we set the initial state of the ODE and set the integrator:

ODE.set_initial_value(initial_state, time=0.0)

ODE.set_integrator("dopri5")

JiTCODE supports a large number of integrators, including the explicit Runge-Kutta method of order 5(4) that is used by default by the solve_ivp
function call of previous examples. dopri 5 is a fast Dormand-Prince integrator of order 5 . Once the integrator is set, $\mathrm{C}$ code is generated for the function.

Finally, we need to define the space over which we shall evaluate $\beta_{1}$ :

beta_1_range = np.1inspace(0, 0.5, resolution)

The resolution variable is the number of different, linearly spaced, values of $\beta_{1}$ in the range of 0 to 0.5 with which the differential equation will be parameterized. A finer resolution (higher resolution variable) does result in a more granular picture of long-term behavior, but may be computationally vastly more expensive.

We also create two objects to hold our results:

- bifurcation_map, which holds our ten years' worth of samples (10 samples) for each point in the $\beta_{1}$ space, and
- Tyapunov_map, which holds the estimated Lyapunov exponent for each value of the $\beta_{1}$ space.

We can initialize these as zero-valued arrays:

```
bifurcation_map = np.zeros(shape=(10, resolution))
lyapunov_map = np.zeros(shape=(resolution))
```

We are finally ready to write the main loop that will iterate over the entire $\beta_{1}$ space, and sample ten years after day 5000 on the same day of the year. We specify a burn-in period of 1000 days: typically, systems do not attain their stable long-term periodicities for quite some time, and this period reduces unnecessarily storing values we are not going to sample. We take the Lyapunov exponent for a $\beta_{1}$ value to be the mean Lyapunov exponent after day 1730, once again to reduce susceptibility to initial oscillations.

```
for blidx, i in enumerate(beta_1_range):
    ODE.set_initial_value([S_0, I_0], time=0.0)
    ODE.set_parameters(i)
    ys, lyaps = [], []
    for T in np.arange(0, 7500, 1):
        y, lyap, _ = ODE.integrate(T)
        if T > 1000:
            ys.append(y[1])
            lyaps.append(1yap)
    for idx, val in enumerate(ys[4000::365]):
        bifurcation_map[idx, b1idx] = val
```

lyapunov_map[b1idx] = np.mean(1yaps[730:])

Note lines 2 and 3, in which we set the ODE solver to its initial value. In JiTCODE, ODE objects are stateful, that is, they retain a memory of their past execution. Consequently, if the ODE object has been run once, it will be on day 7500 , with the respective quantities as its current state with respect to $S$ and $I$. The .set_initial_value() method call resets these values to the initial conditions.

Our results are, at the end of iterative integration, stored in the two objects we initialized above. These can, with some patience, be plotted to reveal the bifurcation behavior and the Lyapunov exponent's corresponding values, as we indeed do in Fig. 7.8.

A notebook implementing the contents of this Computational Note is available on the book's companion Github repository in the folder / ch07/discrete_ 7 yapunov/.

The practical meaning of our computational exploration of a simple seasonally forced SIR system's chaotic dynamics is that such systems are capable of exhibiting highly nonlinear dependence on initial parameters after a certain point. As Fig. 7.8
![](https://cdn.mathpix.com/cropped/2024_06_11_9842913b8cdb0b8f0b50g-38.jpg?height=790&width=1024&top_left_y=1172&top_left_x=211)

Figure 7.8 Bifurcation map of the temporally forced SIR model described in Computational Note 7.7 and its Lyapunov exponents. The model was initialized with $\beta_{0}=1.3, \gamma=\frac{1}{13}$, $\mu=\frac{1}{40}$ per annum and a starting infectious population fraction of $10^{-3}$.
shows, our initially perfectly well-behaved system of linear equations experiences a bifurcation at around $\beta_{1} \approx 0.04$, and becomes entirely chaotic by $\beta_{1} \approx 0.21$. By $\beta_{1} \approx 0.3$, minuscule variations of $\beta_{1}$ can result in a range of outcomes six orders of magnitude apart, the difference between approximately 3.3 million cases per annum in the United States and fewer than four cases in the same period.

## Practice Note 7.2 Chaos in practice

There is, after a certain point, an inherent instability in dynamical systems, after which an incremental change might result in large differences. The consequence is that it is quite difficult to reason about these problems after a certain level. Assuming that $\beta_{1}$ is estimated to be 0.25 , with a $95 \%$ confidence interval of 0.24-0.26, the model explored in Computational Note 7.7 admits to values six orders of magnitude apart, a significant difference. The long-term destiny of dynamical systems can be immensely complex to predict, estimate, and influence once strong nonlinear dependence on an initial parameter enters the scene.

The consequence is that just as the weather forecast for tomorrow is more likely to be accurate than for next week, forecasting the long-term evolution of epidemic processes might be fraught with difficulty [274]. The analogy is not accidental: much of modern chaos theory, which is aimed at a mathematical exploration of what happens once a system slips into complex nonlinearity, is intrinsically connected to modern efforts to understand weather phenomena [275].

Another nonnegligible aspect is where the strong nonlinear dependence on a parameter is in respect to the parameters of a human intervention, such as seasonal pulse vaccination (see Subsection 6.1.2.3) [276]. In these cases, more is not necessarily better, and minuscule changes in the pulse rate or the phase of the pulse vaccination with respect to the natural ebbs and flows of the disease can result in hard-to-predict long-term nonlinearities. Simulation can help by identifying ranges and patterns of stability ("safe spots"), in which the effect of such phenomena is likely to be lower.

A Lyapunov exponent analysis of a long-term epidemic model or interventional approach can be seen as a sort of sensitivity analysis: given the uncertainty of each parameter, what is the range in which, at the time horizon at which we intend to operate, we expect to find a given fraction of our values? Simulation of a system's evolution with values from our parameter's confidence interval is a useful, and regrettably underused, tool in evaluating, interpreting, and communicating long-term models of complex dynamics.

