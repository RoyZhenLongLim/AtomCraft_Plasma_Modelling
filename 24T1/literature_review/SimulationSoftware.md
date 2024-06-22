# Simulation Software

This file is dedicated to provide a general overview into how tokamaks are simulated at different stages of operation
## Motivation
Modelling a tokamak means we need modelling for the following stages:
- Plasma Burn-through Simulation
  - Model plasma burn-through discharge via Ohmic Heating 
  - Aim of simulation:
    - Verify our prediction of threshold prefill gas pressure required 
    - Measure the effects of ECRH-assisted plasma burn-through 
    - Investigate the effect of impurities and eddy current in passive structures on simulation results
    - Investigate how PF coils can be used to increase connection length
- Fixed Boundary Plasma Simulation
  - Models plasma when the shape of the plasma is fixed/static during the simulation
  - Aim of simulation:
    - Assess the stability of plasma equilibrium
    - Determine how plasma stability can be improved 
- Free Boundary Plasma Simulation
  - Models plasma equilibrium with the shape of plasma as an output of simulation
  - Aim of simulation:
    - Determine the shape of the plasma giving various changing factors (e.g. change in plasma pressure) to optimise
      for stability
    - Helps explore how disruptions make affect the plasmas shape 
    - Determine what various sensors should detect given a specific equilibrium state
- Transport Code 
  - Transport code is a general term for any type of transfer that occurs in a tokamak. These include but are not
    limited to:
    - Particle Transport 
    - Energy Transport

In general, simulating a tokamak is necessary for:
- simulating evolution of plasma from plasma formation (heating and current drive), plasma current ramp up, plasma
  equilibrium and confining plasma (i.e. plasma stability)
- determine how current in coils interact with each other as tokamak starts up
- testing control system responses
- evaluate safety
  - max voltage induced within coils
  - heating of the vacuum vessel due to radio waves or plasma

## General Purpose
- [PROCESS](https://ccfe.ukaea.uk/wp-content/uploads/2019/11/A-User-Guide-to-the-PROCESS-systems-code.pdf)
  - Code from Culham Centre for Fusion Energy (CCFE) (UK's national laboratory for nuclear fusion Research)
  - Not publicly available
  - For modelling fusion power plants 
- [BOUT++](https://bout-dev.readthedocs.io/en/latest/)
  - General Purpose Plasma Simulations
  - **Source**: https://boutproject.github.io/
- [METIS](https://fusenet.eu/metis-plasma-simulator)
- Tokamak Plasma simulation based off of CRONOS Integrated Modelling Suite for transport simulations
- **Source**: Obtained by asking permission with authors(s) of METIS
- [CRONOS](https://iopscience.iop.org/article/10.1088/0029-5515/50/4/043001)
  - Suite of numerical codes for predictive/interpretive simulation of a full tokamak discharge
  - [CRONOS Modules](http://www-fusion-magnetique.cea.fr/cronos/gp/cronos_gb.pdf)
  - **Source**: Not 100% sure but seems like we can ask for it
  - 
- [OMFit](https://www.osti.gov/servlets/purl/1411210)
  - One Modelling Framework for Integrated Task
  - Contains a large variety of modelling tools for tokamak design and manufacturing
  - Seems very promising tho I am not sure whether we can customise it to our tokamak since it seems to only be used for
    modelling large, research tokamaks
  - **Source**: https://omfit.io/publications.html

## Tokamak Equilibrium
- [FreeGS](https://freegs.readthedocs.io/en/latest/)
  - Free Boundary Grad-Shafranov Solver
  - **Source**: https://github.com/freegs-plasma/freegs
- [Fiesta](https://arxiv.org/abs/1310.8450)
  - Free Boundary Grad-Shafranov Solver
  - **Source**: Not publicly available (can ask author for it)


## Tokamak Start-Up
- [Verificatation and validation of plasma burn-through simulations in preparation for ITER First Plasma](https://conferences.iaea.org/event/214/contributions/17228/attachments/9791/15307/poster_695.pdf)
  - [DYON](https://arxiv.org/pdf/1403.0380.pdf)
    - Plasma Burn-through Solver developed at Joint European Torus (JET)
    - JET acts as a test-bed for exploring plasma behaviour and testing technologies for ITER
    - **Source**: Could not find publicly available code
  - [SCENPLINT](https://iopscience.iop.org/article/10.1088/0029-5515/16/5/005)
    - Plasma Burn-through Solver
  - [BKDO](https://info.fusion.ciemat.es/OCS/EPS2018PAP/pdf/P4.1074.pdf)
    - Plasma Burn-through Solver

## Control Systems
- [SPARC](https://pubs.aip.org/aip/pop/article/30/9/090601/2909870/SPARC-as-a-platform-to-advance-tokamak-science)
    - The SPARC plasma control system will be based on an in-house control framework known as neutrino. Developed
      primarily in C++ and Python, this framework has emphasized simplicity and flexibility from the beginning, meaning
      that it can be readily upgraded to include additional functionality.
    - **Source**: Could not find publicly available code

## MISC
- [Report of the Workshop on Integrated Simulations for Magnetic Fusion Energy Sciences](https://science.osti.gov/-/media/fes/pdf/workshop-reports/2016/ISFusionWorkshopReport_11-12-2015.pdf?la=en&hash=1432311A0F2EAD8CCF2375C76A9366BE1A96019C)
  - Outline current landscape of simulations for Tokamak 
- [PlasmaPy](https://docs.plasmapy.org/en/latest/index.html)
  - Open Source package for plasma research and education
- [Virtual Tokamak](https://ippex.pppl.gov/#vt)
  - Interactive simulation of how a tokamak works
- [Emulation Techniques for Scenario and Classical Control Design of Tokamak Plasmas](https://arxiv.org/pdf/2403.18912.pdf)
    - Methodology behind training a neural network to learn how to control a tokamak to bypass the heavy computational
      cost of solving Grad-Shafranov Equation