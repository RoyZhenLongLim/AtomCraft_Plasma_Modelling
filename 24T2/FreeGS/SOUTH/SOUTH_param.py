import numpy as np
from scipy.integrate import cumulative_trapezoid
from freegs.machine import Wall

solenoid_height = 0.94
inner_radius = 51e-3
outer_radius = 60e-3
solenoid_turns = 104

RWall = [0.160, 0.1761, 0.2200, 0.280, 0.3400, 0.3839, 0.40, 0.3839, 0.3400, 0.280, 0.2200, 0.1761, 0.160]
ZWall = [0.000, 0.0600, 0.1039, 0.120, 0.1039, 0.0600, 0.00, -0.0600, -0.1039, -0.120, -0.1039, -0.0600, 0.000]
walls = Wall(
    RWall,
    ZWall
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
