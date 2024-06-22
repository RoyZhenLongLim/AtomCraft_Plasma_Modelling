import freegs
from freegs.machine import Solenoid, Wall, Circuit, Coil


def sensitivity_training_poloidal_coils(r1, r2, z1, z2):
    PR1 = 0.50738376
    PZ1 = 0.39384023
    PR2 = 0.62576723
    PZ2 = 0.1996288
    solenoid_height = 0.94
    inner_radius = 51e-3
    outer_radius = 60e-3
    solenoid_turns = 104
    central_solenoid = [("SOL", Solenoid((inner_radius + outer_radius) / 2, -solenoid_height / 2, solenoid_height / 2,
                                         solenoid_turns, control=False))]
    poloidal_coils = [
        (
            "VERT", Circuit([
                ("VERT_U", Coil(PR1 + r1, PZ1 + z1), 1.0),
                ("VERT_L", Coil(PR1 + r1, -PZ1 - z1), 1.0)
            ])
        ),
        (
            "HORIZ", Circuit([
                ("HORIZ_U", Coil(PR2 + r1, PZ2 + z2), 1.0),
                ("HORIZ_L", Coil(PR2 + r1, -PZ2 - z2), 1.0)
            ])
        )
    ]
    walls = Wall(
        [0.160, 0.1761, 0.2200, 0.280, 0.3400, 0.3839, 0.40, 0.3839, 0.3400, 0.280, 0.2200, 0.1761],  # R
        [0.000, 0.0600, 0.1039, 0.120, 0.1039, 0.0600, 0.00, -0.0600, -0.1039, -0.120, -0.1039, -0.0600]  # Z
    )
    tokamak = freegs.machine.Machine(
        central_solenoid + poloidal_coils,
        walls,
    )
    tokamak["VERT"]["VERT_U"].area = tokamak["VERT"]["VERT_L"].area = tokamak["HORIZ"]["HORIZ_U"].area = \
    tokamak["HORIZ"][
        "HORIZ_L"].area = 0.000213825 * 4
    eq = freegs.Equilibrium(tokamak=tokamak,
                            Rmin=0.01, Rmax=0.6,  # Radial domain
                            Zmin=-0.5, Zmax=0.5,  # Height range
                            nx=65, ny=65  # Number of grid points
                            )
    plasma_major_radius = 0.28
    toroidal_magnetic_field_strength_at_plasma_centre = 0.875
    vacuum_toroidal_magnetic_field = plasma_major_radius * toroidal_magnetic_field_strength_at_plasma_centre
    profiles = freegs.jtor.ConstrainBetapIp(eq,
                                            0.05,  # Plasma poloidal beta
                                            3e3,  # Plasma current [Amps]
                                            vacuum_toroidal_magnetic_field)  # Vacuum f=R*Bt
    xpoints = [(0.3, -0.24)]  # (R,Z) locations of X-points
    isoflux = [(0.3, -0.24, 0.3, 0.24)]  # (R1,Z1, R2,Z2) pairs
    constrain = freegs.control.constrain(xpoints=xpoints, isoflux=isoflux)
    print('==========================')
    freegs.solve(eq,
                 profiles,
                 constrain,
                 show=False,
                 check_limited=True,
                 limit_it=0
                 )
    print(f'Adjustments: r1: {r1}, r2: {r2}, z1: {z1}, z2: {z2}')
    print(f"Plasma current: {eq.plasmaCurrent():.2E} Amps")
    print(f"Plasma pressure on axis: {(eq.pressure(0.0)):.2E} Pascals")
    print(f"Poloidal beta: {eq.poloidalBeta():.2E}")
    print("Current")
    for label, coil in tokamak.coils:
        print(f"{label}: {coil.current:.2F}A")

    print("Forces")
    for label, coil in tokamak.coils:
        forces = coil.getForces(eq)
        for key, value in forces.items():
            print(f'{key}: {value}')
    print('==========================')
    print('\n')
