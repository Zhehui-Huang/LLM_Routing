import numpy as np
from scipy.spatial import distance_matrix

# Given city coordinates
cities = {
    0: (54, 87), 
    1: (21, 84), 
    2: (69, 84), 
    3: (53, 40), 
    4: (54, 42), 
    5: (36, 30), 
    6: (52, 82), 
    7: (93, 44), 
    8: (21, 78), 
    9: (68, 14), 
    10: (51, 28), 
    11: (44, 79), 
    12: (56, 58), 
    13: (72, 43), 
    14: (6, 99)
}

# Convert to numpy array for distance calculation
positions = np.array(list(cities.values()))
dist_matrix = distance_matrix(positions, positions)