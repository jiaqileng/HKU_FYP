#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 21:08:51 2018

@author: lengjiaqi
"""

#this program aims to compare the sup-norm of the two distinct numerical solutions

import numpy as np

def get_matrix1():
        A = []
        with open("vis_split.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A
    
def get_matrix2():
        A = []
        with open("hopf_cole.txt",'r') as r:
            cc = 0
            for row in r:
                A.append([])
                cols = row.split("\n")[0].split(" ")[:-1]
                for col in cols:
                    A[cc].append(float(col))
                cc += 1
        return A
    
#initialize the data & check shapes
u1 = get_matrix1()
u2 = get_matrix2()

print(len(u1))
print(len(u1[0]))
print(len(u2))
print(len(u2[0]))
#the test result should be all 501.

#compare without the initial data
A = np.zeros((501, 501))
for i in range(1, 501):
    for j in range(501):
        A[i,j] = np.abs(u1[i][j] - u2[i][j])

max1 = np.amax(A)

#compare with the initial data
for j in range(501):
    A[0,j] = np.abs(u1[0][j] - u2[0][j])

max2 = np.amax(A)

print('with the initial data')
print(max2)

print('without the initial data')
print(max1)