import numpy as np
from scipy.integrate import cumulative_trapezoid
from freegs.machine import Wall

solenoid_height = 0.94
inner_radius = 51e-3
outer_radius = 60e-3
solenoid_turns = 104

R0 = 0.3048     # Middle of the circle
rwall = 0.16195 # Radius of the circular wall

npoints = 50 # Number of points on the wall

# Poloidal angles
thetas = np.linspace(0, 2*np.pi, npoints, endpoint=False)
Rwalls = R0 + rwall * np.cos(thetas)
Zwalls = rwall * np.sin(thetas)

walls = Wall(
    Rwalls,
    Zwalls
)

plasma_major_radius = 0.28


def PrincetonDee(R1, R2):
    R0 = np.sqrt(R1 * R2)

    r = np.linspace(R2 * 0.9999, R1 * 1.0001, 500)
    integrand = np.log(r / R0) / np.sqrt(np.log(r / R1) * np.log(R2 / r))
    z = cumulative_trapezoid(integrand, x=r, initial=0)

    r = np.concatenate([r, r[::-1]])
    z = np.concatenate([-z, z[::-1]])

    return r, z
