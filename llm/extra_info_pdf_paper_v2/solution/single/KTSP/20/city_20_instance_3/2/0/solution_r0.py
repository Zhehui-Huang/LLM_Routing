import numpy as np

# Coordinates of cities
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Number of cities to visit (including depot)
k = 13

# Total number of cities
n = len(cities)

# Distance matrix using Euclidean distance
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i][j] = np.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Function to calculate the total cost of a given tour
def tour_cost(tour):
    cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    return cost