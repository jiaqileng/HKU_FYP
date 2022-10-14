#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:10:49 2019

@author: lengjiaqi
"""
# This is a realization of the finite difference scheme to solve the Thomas 1968 scalar MHD model.
# The system is assumed to defined on a periodic domain [0,1].

import numpy as np


def MHD_solver(v, lbd, T, N1, N2, f, g):
    
    dx = 1/N1
    dt = T/N2

    r = dt/np.power(dx,2)
    s = dt/(2*dx)
    print("The von Neumann coefficient is " + str(v*r/2))
    
    u = np.zeros((N2+1, N1))
    b = np.zeros((N2+1, N1))
    
    u[0] = f
    b[0] = g
    
    for i in range(N2):
    	print(100*i/N2)
    	for j in range(N1):
            mr = (j+1)%(N1)
           
            a1 = u[i,mr] - 2*u[i,j]+u[i, j-1]
            a2 = u[i,mr] - u[i,j-1]
            b1 = b[i,mr] - 2*b[i,j]+b[i, j-1]
            b2 = b[i,mr] - b[i,j-1]
    
            u[i+1, j] = v * r * a1 + u[i,j] * (1-s*a2) + b[i,j] * s * b2
            b[i+1, j] = lbd * r * b1 + b[i,j] * (s*a2 + 1) - u[i,j] * s * b2
    	
    return u, b


#_step solves MHD between 1 (x<0) and 0 (x>1)
def MHD_solver_step(v, lbd, T, N1, N2, f, g):
    
    dx = 1/N1
    dt = T/N2

    r = dt/np.power(dx,2)
    s = dt/(2*dx)
    print("The von Neumann coefficient is " + str(v*r/2))
    
    u = np.zeros((N2+1, N1+1))
    b = np.zeros((N2+1, N1+1))
    
    u[0] = f
    b[0] = g
    
    for i in range(N2):
        print(100*i/N2)
        for j in range(1, N1):
            a1 = u[i,j-1] - 2*u[i,j]+u[i, j+1]
            a2 = u[i,j-1] - u[i,j+1]
            b1 = b[i,j-1] - 2*b[i,j]+b[i, j+1]
            b2 = b[i,j-1] - b[i,j+1]
        
            u[i+1, j] = v * r * a1 + u[i,j] * (1-s*a2) + b[i,j] * s * b2
            b[i+1, j] = lbd * r * b1 + b[i,j] * (s*a2 + 1) - u[i,j] * s * b2
    	
        u[i+1,0] = 1
        u[i+1, N1] = 0
        b[i+1,0] = 0
        b[i+1, N1] = 1

    return u, b

def get_matrix(s):
        A = []
        with open(s,'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A