import freegs
import numpy as np
import math

from scipy.special import iv
from scipy.special import modstruve

tokamak = freegs.machine.TestTokamak()

from freegs.machine import Coil
from freegs.machine import Circuit
from freegs.machine import Solenoid

I_cs = 0

coils = [("VERT", Circuit( [("VERT_U", Coil(0.50738376, 0.39384023), 1.0),
                           ("VERT_L", Coil(0.50738376, -0.39384023),1.0)] ))
         ,("HORIZ", Circuit( [("HORIZ_U", Coil(0.62576723, 0.1996288), 1.0),
                           ("HORIZ_L", Coil(0.62576723, -0.1996288), 1.0)] ))
         ,("SOL", Solenoid(0.051, -0.44, 0.44, 103, control=False, current=I_cs))
        ]

from freegs.machine import Wall

wall = Wall([0.160,0.1761,0.2200,0.280,0.3400,0.3839,0.40, 0.3839, 0.3400, 0.280, 0.2200, 0.1761 ],   # R
            [0.000,0.0600,0.1039,0.120,0.1039,0.0600,0.00,-0.0600,-0.1039,-0.120,-0.1039,-0.0600])   # Z

tokamak = freegs.machine.Machine(coils, wall)

tokamak["VERT"]["VERT_U"].area = tokamak["VERT"]["VERT_L"].area = tokamak["HORIZ"]["HORIZ_U"].area = tokamak["HORIZ"]["HORIZ_L"].area = 0.000213825*4

eq = freegs.Equilibrium(tokamak=tokamak,
                     Rmin=0.01, Rmax=0.6,    # Radial domain
                     Zmin=-0.5, Zmax=0.5,   # Height range
                     nx=65, ny=65)          # Number of grid points


# Investigate plasma properties / what params 
# Ask Marcus what params are required for the constraints + Matthew Hole
profiles = freegs.jtor.ConstrainBetapIp(eq,
                                        0.05, # Plasma poloidal beta
                                        3e3, # Plasma current [Amps]
                                        0.0245) # Vacuum f=R*Bt
# These point don't have any meaning, can be changed.
xpoints = [(0.3, -0.24)]  # (R,Z) locations of X-points

isoflux = [(0.3, -0.24, 0.3, 0.24)] # (R1,Z1, R2,Z2) pairs
           


constrain = freegs.control.constrain(xpoints=xpoints, isoflux=isoflux)

# check_limited params is related to limited vs diverted plasma
# need to investigate the param
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
print(eq.getForces())

#Toroidal coil forces
n=0
ntot = 100
r_1 = 0.1
r_2 = 0.59
r_0 = math.sqrt(r_1*r_2)
k = 0.5*math.log(r_2/r_1)
I_1 = iv(1, k)
L_neg1 = modstruve(-1,k)
h_straight = 2*math.pi*k*r_0*I_1
h_total = math.pi*k*r_0*(I_1+L_neg1)
I_t = 2544.844659

R = []
Z = []
Br = []
Bz = []
Ir = []
Iz = []
F = []
R.append("R")
Z.append("Z")
Br.append("Br")
Bz.append("Bz")
Ir.append("Ir")
Iz.append("Iz")
F.append("F")

#straight region
while n<=ntot:
    R_temp = r_1
    Z_temp = -h_straight/2+h_straight*n/ntot
    Br_temp = eq.Br(R_temp,Z_temp)
    Bz_temp = eq.Bz(R_temp,Z_temp)
    Ir_temp = 0  
    Iz_temp = I_t
    F_temp = Ir_temp*Bz_temp-Iz_temp*Br_temp
    R.append(R_temp)
    Z.append(Z_temp)
    Br.append(Br_temp)
    Bz.append(Bz_temp)
    Ir.append(Ir_temp)
    Iz.append(Iz_temp)
    F.append(F_temp)
    n += 1
#small ellipse top
n = 0
a = r_0 - r_1
b = (h_total-h_straight)/2
z_0 = h_straight/2

while n<=ntot:
    R_temp = r_1+ (r_0-r_1)*n/ntot
    Z_temp = z_0+b*math.sqrt(1-(R_temp-r_0)**2/a**2)
    Br_temp = eq.Br(R_temp,Z_temp)
    Bz_temp = eq.Bz(R_temp,Z_temp)
    if Z_temp == z_0:
        m = math.atan(float('inf'))
    else:
         m = -b**2/a**2*(R_temp-r_0)/(Z_temp-z_0)
    Ir_temp = I_t*math.cos(math.atan(m))  
    Iz_temp = I_t*math.sin(math.atan(m))  
    F_temp = Ir_temp*Bz_temp-Iz_temp*Br_temp
    R.append(R_temp)
    Z.append(Z_temp)
    Br.append(Br_temp)
    Bz.append(Bz_temp)
    Ir.append(Ir_temp)
    Iz.append(Iz_temp)
    F.append(F_temp)
    n += 1

#big ellipse top
n = 0
a = r_2 - r_0
b = (h_total)/2
z_0 = 0

while n<=ntot:
    R_temp = r_0+ (r_2-r_0)*n/ntot
    Z_temp = z_0+b*math.sqrt(1-(R_temp-r_0)**2/a**2)
    Br_temp = eq.Br(R_temp,Z_temp)
    Bz_temp = eq.Bz(R_temp,Z_temp)
    if Z_temp == z_0:
        m = math.atan(float('inf'))
    else:
        m = -b**2/a**2*(R_temp-r_0)/(Z_temp-z_0)
    Ir_temp = I_t*math.cos(math.atan(m))  
    Iz_temp = I_t*math.sin(math.atan(m))  
    F_temp = Ir_temp*Bz_temp-Iz_temp*Br_temp
    R.append(R_temp)
    Z.append(Z_temp)
    Br.append(Br_temp)
    Bz.append(Bz_temp)
    Ir.append(Ir_temp)
    Iz.append(Iz_temp)
    F.append(F_temp)
    n += 1

#big ellipse bottom
n = 0
a = r_2 - r_0
b = (h_total)/2
z_0 = 0

while n<=ntot:
    R_temp = r_2-(r_2-r_0)*n/ntot
    Z_temp = z_0-b*math.sqrt(1-(R_temp-r_0)**2/a**2)
    Br_temp = eq.Br(R_temp,Z_temp)
    Bz_temp = eq.Bz(R_temp,Z_temp)
    if Z_temp == z_0:
        m = math.atan(float('inf'))
    else:
        m = -b**2/a**2*(R_temp-r_0)/(Z_temp-z_0)
    Ir_temp = -I_t*math.cos(math.atan(m))  
    Iz_temp = -I_t*math.sin(math.atan(m))  
    F_temp = Ir_temp*Bz_temp-Iz_temp*Br_temp
    R.append(R_temp)
    Z.append(Z_temp)
    Br.append(Br_temp)
    Bz.append(Bz_temp)
    Ir.append(Ir_temp)
    Iz.append(Iz_temp)
    F.append(F_temp)
    n += 1

#small ellipse bottom
n = 0
a = r_0 - r_1
b = (h_total-h_straight)/2
z_0 = -h_straight/2

while n<ntot:
    R_temp = r_0- (r_0-r_1)*n/ntot
    Z_temp = z_0-b*math.sqrt(1-(R_temp-r_0)**2/a**2)
    Br_temp = eq.Br(R_temp,Z_temp)
    Bz_temp = eq.Bz(R_temp,Z_temp)
    if Z_temp == z_0:
        m = math.atan(float('inf'))
    else:
        m = -b**2/a**2*(R_temp-r_0)/(Z_temp-z_0)
    Ir_temp = -I_t*math.cos(math.atan(m))  
    Iz_temp = -I_t*math.sin(math.atan(m))  
    F_temp = Ir_temp*Bz_temp-Iz_temp*Br_temp
    R.append(R_temp)
    Z.append(Z_temp)
    Br.append(Br_temp)
    Bz.append(Bz_temp)
    Ir.append(Ir_temp)
    Iz.append(Iz_temp)
    F.append(F_temp)
    n += 1
rows = zip(R,Z,Br,Bz,Ir,Iz,F)

import csv

with open('TF.csv', "w",newline='') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)

#solenoid points
n=0
ntot = 104
R_cs = 0.051
A_cs = 0.000025
mu0 = 1.25664E-06

minor_radius = np.sqrt(A_cs / np.pi)
self_inductance = 0.5
self_fr = (mu0 * I_cs ** 2 / (4.0 * np.pi * R_cs)) * (
            np.log(8.0 * R_cs / minor_radius) - 1 + self_inductance / 2.0)
Ltor = 2 * np.pi * R_cs

R = []
Z = []
Br = []
Bz = []
I = []
Fr = []
Fz = []
R.append("R")
Z.append("Z")
Br.append("Br")
Bz.append("Bz")
I.append("I")
Fr.append("Fr")
Fz.append("Fz")

while n<ntot:
    R_temp = R_cs
    Z_temp = h_total - n*(h_total*2/ntot)
    Br_temp = eq.Br(R_temp,Z_temp)
    Bz_temp = eq.Bz(R_temp,Z_temp)
    I_temp = I_cs
    Fr_temp = (I_temp * Bz_temp + self_fr)*Ltor
    Fz_temp = -I_temp * Br_temp * Ltor
    R.append(R_temp)
    Z.append(Z_temp)
    Br.append(Br_temp)
    Bz.append(Bz_temp)
    I.append(I_temp)
    Fr.append(Fr_temp)
    Fz.append(Fz_temp)
    n += 1
rows = zip(R,Z,Br,Bz,I,Fr,Fz)

import csv

with open('CS.csv', "w",newline='') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)



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


#%%
