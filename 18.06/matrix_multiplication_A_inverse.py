# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12oLUCSKxNExx180FeXD7ct8rqOYyZYwX
"""

import numpy as np;

A = np.array([[4, 3],[(-5), 9]])
b = np.array([20, 26])
Ai = np.array([[(3/17), -(1/17)],[(5/51), (4/51)]])
Aii = np.linalg.inv(A)
i = np.dot(A, Aii)
print(i)
print(Aii)
print(Ai)