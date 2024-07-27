import numpy as np
from math import sqrt
from sklearn.cluster import KMeans

# City Coordinates
cities = np.array([
    [30, 40], [37, 52], [49, 49], [52, 64], [31, 62], [52, 33], 
    [42, 41], [52, 41], [57, 58], [62, 42], [42, 57], [27, 68], 
    [43, 67], [58, 48], [58, 27], [37, 69]
])

# Number of robots
num_robots = 8