# Calculate the torsional stiffness of a shaft
# First import math Library
import math
"""
Do = Outer Diameter of the shaft - user input
Di = Inner Diameter of the shaft - user input
L = Length of the shaft - user input
G = Modulus of Rigidity - user input
J = Polar moment of area
T = Twisting Torque
theta = Angle of twist
"""

def calculate(Do,Di,L,G):
    J = (math.pi*(float(Do)**4 - float(Di)**4))/32
    calc = ((float(G)*1E9)*J)/float(L)
    return J, calc

Shaft_Outer_Diameter = input("Outer Diameter of the Shaft [meter] \n example : 0.022 m \n")
Shaft_Inner_Diameter = input("Inner Diameter of the Shaft [meter] \n example : 0 for solid bar \n")
Shaft_Length = input("Length of the Shaft [meter] \n example : 1.3 \n")
Modulus_of_Rigidity = input("Modulus of Rigidity of Shaft [GPa] \n example : steel = 77 \n" )

"""Shaft_Outer_Diameter = 22/1000
Shaft_Inner_Diameter = 16/1000
Shaft_Length = 1300/1000
Modulus_of_Rigidity = 95"""


Do = Shaft_Outer_Diameter
Di = Shaft_Inner_Diameter
L = Shaft_Length
G = Modulus_of_Rigidity
X = calculate(Do,Di,L,G)


calc_Nmprad = X[1]
calc_Nmpdeg = round((calc_Nmprad*math.pi/180),2)
print("The Torsional Stiffness of the Shaft = " + str(calc_Nmpdeg) + " Nm/deg")
