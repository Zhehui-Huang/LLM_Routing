import math
from scipy.spatial.distance import pdist, squareform
import numpy as np
from scipy.optimize import linear_sum_assignment
from networkx.algorithms.approximation import min_weight_matching
import networkx as nx

# Function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)