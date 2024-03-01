import freegs

tokamak = freegs.machine.TestTokamak()

from freegs.machine import Coil
from freegs.machine import Circuit

coils = [("P1", Circuit( [("P1U", Coil(0.38, 0.18), 1.0),
                           ("P1L", Coil(0.38, -0.18),1.0)] ))
         ,("23", Circuit( [("P2U", Coil(0.42, 0.08), 1.0),
                           ("P2L", Coil(0.42, -0.08), 1.0)] ))
        ]



#Coil current control - uncomment if you want to fix a coils current
#Coil(1.0, -1.1, control=False, current=1000.)


from freegs.machine import Solenoid

solenoid = Solenoid(0.08, -0.11, 0.11, 20)

from freegs.machine import Wall

wall = Wall([ 0.125, 0.13514955,  0.17097779,  0.21650635,   0.28169304,   0.33439407, 0.36571204, 0.375, 0.36571204, 0.33439407, 0.28169304, 0.21650635,  0.17097779, 0.13514955, 0.125],   # R
            [0.10653632, 0.14379866, 0.17319257, 0.18184212, 0.16667951, 0.1254265, 0.06627928, 0, -0.06627928, -0.1254265, -0.16667951, -0.18184212,  -0.17319257, -0.14379866, -0.10653632])   # Z

tokamak = freegs.machine.Machine(coils, wall)

eq = freegs.Equilibrium(tokamak=tokamak,
                     Rmin=0.05, Rmax=0.39,    # Radial domain
                     Zmin=-0.18, Zmax=0.18,   # Height range
                     nx=65, ny=65)          # Number of grid points


profiles = freegs.jtor.ConstrainPaxisIp(eq,
										1e4, # Pressure on axis [Pa]
                                        1e6, # Plasma current [Amps]
                                        1.0) # Vacuum f=R*Bt

xpoints = [(0.21650635, -0.10653632)]  # (R,Z) locations of X-points

isoflux = [(0.21650635, -0.10653632, 0.21650635, 0.10653632)] # (R1,Z1, R2,Z2) pairs
           
#xpoints = [(0.13, 0),   # (R,Z) locations of X-points
           #(0.35,0)]

constrain = freegs.control.constrain(xpoints=xpoints, isoflux=isoflux)


freegs.solve(eq,
            profiles, 
            constrain,
            show=True,
            check_limited = True,
            limit_it = 0)


# eq now contains the solution

print("Done!")

print("Plasma current: %e Amps" % (eq.plasmaCurrent()))
print("Plasma pressure on axis: %e Pascals" % (eq.pressure(0.0)))
print("Poloidal beta: %e" % (eq.poloidalBeta()))

# Currents in the coils
tokamak.printCurrents()

# Forces on the coils
eq.printForces()

print("\nSafety factor:\n\tpsi \t q")
for psi in [0.01, 0.9, 0.95]:
    print("\t{:.2f}\t{:.2f}".format(psi, eq.q(psi)))

##############################################
# Save to G-EQDSK file

from freegs import geqdsk

with open("lsn.geqdsk", "w") as f:
    geqdsk.write(eq, f)

##############################################
# Final plot of equilibrium

axis = eq.plot(show=False)
eq.tokamak.plot(axis=axis, show=False)
constrain.plot(axis=axis, show=True)

# Safety factor

import matplotlib.pyplot as plt
plt.plot(*eq.q())
plt.xlabel(r"Normalised $\psi$")
plt.ylabel("Safety factor")
plt.show()