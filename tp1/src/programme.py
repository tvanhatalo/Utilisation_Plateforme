#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

import methodes
import equations

# Résolution approchée de y' = 2-y avec y(0) = 3 pour t dans [0,5]
equations.a = -1.
equations.b = 1. #originally 2
t0,y0 = 0.,5. #3
T = 1. #5
# Avec un pas de 0.1, il faut donc 50 iterations
N,h = 50,0.00625
[t,y1] = methodes.euler_explicite(t0,h,N,y0,equations.f_affine)
#[t,y1] = methodes.euler_explicite(t0,h,N,y0,equations.f_carree)
# Solution exacte aux mêmes instants
z1 = equations.sol_affine(t,y0)
#z1 = equations.sol_carree(t,y0)
# Calcul de l'erreur maximum relative
e1 = np.max(np.abs((z1-y1)/z1))
# Graphe des solutions exactes et approchées
plt.loglog(t,y1,'b-+',label='solution approchée h=0.00625')
plt.loglog(t,z1,'r-',label='solution exacte')
plt.xlabel('t')
plt.ylabel('y')
plt.title("Méthode d'Euler explicite")
#plt.title("Méthode de RK2")
plt.legend()
plt.savefig("Pas000625.png")
plt.show("Pas000625.png")  #il le faut en echelle log

# Écriture de l'erreur en fonction de h
print("{0} | {1}".format(h,e1))


#Résolution approchée de y' = 1-y^2 avec y(0) = 0 (y(0) = 2) avec t dans [0,1]
