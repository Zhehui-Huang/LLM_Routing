import math
import numpy as as np

# Cities coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

demands = [  # Starting with Depot, which has demand 0
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 
    1800, 700
]

# Constants
number_of_robots = 4
capacity = 6000
depot = 0

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


# Calculate distance matrix
n = len(coordinates)
distance_matrix = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = euclidean_idxstance(coordinates[i], coordinates[j])

print("Calculated Distance Matrix:")

# Function to print matrix
def print_matrix(mat):
    print("\n".join(["\t".join([f"{value:.2f}" for value in row]) for row in mat]))

print_matrix(distance_matrix)