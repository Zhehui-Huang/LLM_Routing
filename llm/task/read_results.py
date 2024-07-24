#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 16:46:29 2024

@author: shiguangyao
"""

import gurobipy as gp
from gurobipy import GRB
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import math
import os
import pickle


filename = 'mtsp_md_free_result.dic'
with open(filename, 'rb') as f:
    result = pickle.load(f)

print(result)