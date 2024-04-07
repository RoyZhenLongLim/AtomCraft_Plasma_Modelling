# Simulation Software

This document details relevant simulation software

## Tokamak Operation

Tokamaks are pulsed machine and its operation can be broken down to a few key stages.

Generally it goes:
1. Breakdown (ionizing the gas to get plasma)
2. Ramp-up (get the plasma current and other parameters to increases in a stable manner)
3. Flat-top (plasma has reached desired parameters and needs to be kept constant for power generation)
4. Ramp-down (The plasma is extinguished)

The first 2 steps involves the tokamak starting up.
To be more specific:
1. Vacuum Vessel (VV) is filled with gas
2. Plasma break-down (ions and electrons are separated using central solenoid)
3. Plasma burn-through (plasma is full ionised)
4. Plasma current ramp-up (heating the plasma to desired temperature and density)

## Relevant Simulation

### Plasma Transport Code
Verdict: Mostly likely Bout++ if we can't get METIS Code
- More research need to done to evaluate the suitability of each option before we dedicate time to either option.

- [METIS](https://www.google.com/search?channel=fs&client=ubuntu-sn&q=fusenet+metis)
  - Pro: More sophisticated and complete modelling based off CRONOS
  - Con: Requires us to ask for permission from author to get access
- [CRONOS](https://iopscience.iop.org/article/10.1088/0029-5515/50/4/043001)
    - Pro: Well established code base with alot of features
    - Con: CRONOS is a suite of code written in Fortran, Matlab and C++. Very scattered.
    - [CRONOS Code Outline](https://www.google.com/search?channel=fs&client=ubuntu-sn&q=fusion-magnetique+cronos+cronos_gb)
- [Bout++](https://bout-dev.readthedocs.io/en/latest/user_docs/introduction.html)
    - C++ Framework for plasma fluid simulations in 3D curvilinear coordinates
    - Pro: Open Source Code
    - Con: Difficult to use as code is in C++. Is not specific to plasma transport / more general.
    - [Modelling of magnetic null points using BOUT++](https://etheses.whiterose.ac.uk/15359/1/BShanahan_thesis_final_definitely.pdf)
    - [Simulation of plasma transport in MPS-LD linear plasma device by using BOUT++](https://iopscience.iop.org/article/10.1088/1361-6587/ac8c6a/meta)

### Plasma Equilibrium
Use to compute current necessary at equilibrium

- [FreeGS](https://github.com/freegs-plasma/freegs)
  - For modelling plasma equilibrium and optimising coil position
  - Free-Boundary Grad-Shafranov Solver


## Relevant Literature
Literature that I think are important

- [Designing a tokamak fusion reactor—How does plasma physics fit in?](https://dspace.mit.edu/bitstream/handle/1721.1/111207/Designing%20a%20tokamak.pdf?sequence=1)
    - Good introduction to plasma physics and how they influence design decisions in tokamak

### Plasma Burn-Through
- [The physics of tokamak start-up](https://nstx.pppl.gov/nstxhome/DragNDrop/Publications_Presentations/Publications/2013%20Papers/Mueller_PoP.pdf)
    - Good overview of the physics of the different phases in start up
- [Plasma burn-through simulations using the DYON code and predictions for ITER](https://arxiv.org/pdf/1403.0380.pdf)
    - Discuss how simulations for full ionization process required to generate higher T plasma
- [Criterion for Plasma Burn-Through in Tokamaks](http://golem.fjfi.cvut.cz/wiki/Experiments/BreakDownStudies/library/EFDP12016.pdf)
    - Explore how DYON code is used to model plasma burn-through
- [Experimental results with an optimized magnetic field configuration for JET breakdown](https://iopscience.iop.org/article/10.1088/0029-5515/52/12/123010)
    - Explores modelling connection length during Plasma Break-down
    - Compares theoretical simulation to experimental values
    - [Electromagnetic Models of Plasma Breakdown in the JET Tokamak](https://www.researchgate.net/publication/260525826_Electromagnetic_Models_of_Plasma_Breakdown_in_the_JET_Tokamak)
        - Goes through how the code was written in order to model null configurations (no code provided)
        - Goes ionization length and connection length / what is required in order
    - [Enhancement of plasma burn-through simulation and validation in JET](https://iopscience.iop.org/article/10.1088/0029-5515/52/10/103016/meta)
- [Runaway electron generation during tokamak start-up](https://arxiv.org/pdf/2203.09900.pdf)
    - Modelling Plasma Burn-through in ITER, specifically on the effects of runaway electrons

### Plasma
- [Plasma Magnetic Control](https://github.com/AdrianoMele/PlasmaMagneticControl)
    - Include Matlab Code for plasma control based off of CREATE-L/NL
    - [Create-L Plasma response model](https://iopscience.iop.org/article/10.1088/0029-5515/38/5/307/pdf)
        - Paper for understanding the underlying assumptions made in modelling
- [Chapter 8: Plasma operation and control](https://people.physics.anu.edu.au/~bdb112/ITER_Physics_2007/nf7_6_S08.pdf)
    - How ITER plasma control works
- [Magnetic Control of Tokamak](https://link.springer.com/book/10.1007/978-3-319-29890-0)
    - Goes through how control and diagnostics for multiple different stages of tokamak operations

### Tokamaks to reference
Small Tokamaks
- [ST25](https://www.fusionenergybase.com/project/st25)

Large Tokamak
- [JET](https://www.google.com/search?channel=fs&client=ubuntu-sn&q=JET+tokamak)
- [ITER](https://www.iter.org/mach/Tokamak)

### Other Literature
Literature that I don't think is important by might be useful down the track
- [Development of a free boundary Tokamak Equilibrium Solver (TES) for Advanced Study of Tokamak Equilibria](https://arxiv.org/pdf/1503.03135.pdf)
    - [KSTAR_tokamak_simulator](https://github.com/jaem-seo/KSTAR_tokamak_simulator/tree/main)