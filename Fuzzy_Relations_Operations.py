# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:01:07 2018
@author: Sanatt
"""
import numpy as np

def cartprod(x, y):
    x, y = np.asarray(x).ravel(), np.asarray(y).ravel()
    m, n = len(x), len(y)

    a = np.dot(np.atleast_2d(x).T, np.ones((1, n)))
    b = np.dot(np.ones((m, 1)), np.atleast_2d(y))

    return np.fmin(a, b)

def maxmin_composition(s, r):
    if s.ndim < 2:
        s = np.atleast_2d(s)
    if r.ndim < 2:
        r = np.atleast_2d(r).T
    m = s.shape[0]
    p = r.shape[1]
    t = np.zeros((m, p))

    for y in range(p):
        for x in range(m):
            t[x, y] = (np.fmin(s[x, :], r[:, y].T)).max()

    return t

def complement(r):
   m = r.shape[0]
   n = r.shape[1]
   t = np.zeros((m, n))
   
   for x in range(m):
       for y in range(n):
           t[x, y] = 1 - r[x, y]
   
   return t 

def maxprod_composition(s, r):
    m = s.shape[0]
    p = r.shape[1]
    t = np.zeros((m, p))
    
    for x in range(m):
        for y in range(p):
            t[x, y] = (s[x, :] * r[:, y].T).max()
    
    return t

def union(s, r):
    m = s.shape[0]
    p = r.shape[1]
    t = np.zeros((m, p))
    
    for x in range(m):
        for y in range(p):
            t[x, y] = max(s[x, y], r[x, y])
    
    return t

def intersection(s, r):
    m = s.shape[0]
    p = r.shape[1]
    t = np.zeros((m, p))
    
    for x in range(m):
        for y in range(p):
            t[x, y] = min(s[x, y], r[x, y])

    return t

X = [0.2, 0.5, 1]
Y = [0.7, 0.9]
Z = [0.3, 0.8, 0.6]
# R = X x Y
R = cartprod(X, Y)
print("Relation R :")
print(R)
print("R Complement :")
print(complement(R))
# S = Y x Z
S = cartprod(Y, Z)
print("Relation S :")
print(S)
print("MaxMin composition (R, S) :")
print(maxmin_composition(R, S))
print("MaxProd composition (R, S) :")
print(maxprod_composition(R, S))
print("R Union S-Transpose :")
print(union(R, S.T))
print("R Intersection S-Transpose :")
print(intersection(R, S.T))
