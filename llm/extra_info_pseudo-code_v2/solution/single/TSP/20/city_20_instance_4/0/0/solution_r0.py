from concorde.tsp import TSPSolver
import numpy as np

# Define the cities' coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0),
    (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create a matrix of distances
n_cities = len(coordinates)
dist_matrix = np.zeros((n_cities, n_cities), dtype=int)

for i in range(n_cities):
    for j in range(n_cities):
        dist_matrix[i, j] = int(round(euclideanbad::distance(coordinates[i], coordinates[j])))

# Initialize the TSP solver
solver = TSPSolver.from_data(dist_matrix, norm="EUC_2D")

# Find the solution
solution = solver.solve()

# Prepare the tour output with reconversion to a 0-based index by adding 1 
tour = solution.tour.tolist()
tour.append(tour[0])  # Complete the cycle back to the starting city

# Calculate the total travel cost
total_distance = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_distance)