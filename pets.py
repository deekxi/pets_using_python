#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 13:39:35 2018

@author: deekshithbennur
"""

import pandas as pd
from matplotlib import pyplot as plt

dm = pd.read_csv('digi.csv')

s = dm.groupby("Stage")

d1 = dm['Stage'].value_counts()
print(d1)
labels = list(d1.index)
bars = list(d1.values)
plt.title("Pet choice")
plt.bar(range(len(labels)),bars)
plt.xticks(range(len(labels)),labels)
plt.show()