# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:56:02 2021

@author: leand
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

def staysFinite(fcnt, x0, a, N=1000, lim=1E100):
  XX = x0.copy()
  MASK = np.ones(np.shape(XX))
  for i in range(N):
    XX_NEW = fcnt(XX, a)
    MASK = MASK * np.where(np.abs(XX_NEW) < 1E100, 1, 0)
    XX = MASK * XX_NEW
  return MASK

def heat(XX, AA, SF):
    colmap = matplotlib.colors.ListedColormap(['black', 'white'])
    plt.figure(dpi=300)
    plt.imshow(SF, extent=[min(xx), max(xx), min(aa), max(aa)], origin='lower', cmap=colmap)
    plt.xlabel('x0')
    plt.ylabel('a')
    plt.title('black: blows up; white: stays below 1E100')
    plt.show()


fcnt = lambda x, a: a*x*(1 - x)

# MUCH DETAIL
xx = np.linspace(-5, 5, 3000)
aa = np.linspace(-5, 5, 3000)

XX, AA = np.meshgrid(xx, aa) 

SF = np.where(staysFinite(fcnt, XX, AA), 1, 0)

heat(XX, AA, SF)

# ZOOMED OUT
xx = np.linspace(-20, 20, 3000)
aa = np.linspace(-20, 20, 3000)

XX, AA = np.meshgrid(xx, aa) 

SF = np.where(staysFinite(fcnt, XX, AA), 1, 0)

heat(XX, AA, SF)


