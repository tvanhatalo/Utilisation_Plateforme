#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# Fonction f(t,y), second membre d'équations différentielles d'ordre 1
# écrite sous la forme d'un problème de Cauchy, y'(t) = f(t,y(t)) avec
# y(0)=y0

a = -1.
b = 1.

#dans la fonction f_affine, il faut prendre t comme argument car il est utilisé dans methodes.py

def f_affine(t,y):
    """Fonction affine pour y' = ay+b. Les coefficients a et b sont des
    variables globales du module.

    """
    return a*y+b
def sol_affine(t,y0):
    """Pour une fonction affine, on connait la solution exacte. C'est y(t) =
    y0*exp(a*t) - b*(1-exp(a*t))/a.

    """
    return y0*np.exp(a*t) - b * (1.-np.exp(a*t))/a
def f_carree(t,y):
    """Fonction pour y' = ay^2+b
    
    """
    return a*(y**2)+b
def sol_carree(t,y0):
    """Solution exacte selon le signe de (1-y) et (1+y)
    
    """
    if (1-y < 0) and (1+y < 0):
        c = np.log(1) - y0
        sol = (np.exp(2*t+c)-1) / (np.exp(2*t+c)+1)
    if (1-y < 0) and (1+y > 0):
        print("Error: l'équation n'a pas de solution.")
    if (1-y > 0) and (1+y > 0):
        c = np.log(1) + y0
        sol = (np.exp(2*t+c)-1) / (np.exp(2*t+c)+1)
    if (1-y > 0) and (1+y < 0):
        print("Error: l'équation n'a pas de solution.")
    return sol
