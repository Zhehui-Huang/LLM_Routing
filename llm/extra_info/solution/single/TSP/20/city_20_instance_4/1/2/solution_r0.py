from concorde.tsp import TSPSolver
import numpy as np

# Coordinates for the cities
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# Convert coordinates to a numpy array
coords = np.array(coordinates)

# Instantiate and solve the TSP
solver = TSPSolver.from_data(coords[:, 0], coords[:, 1], norm="EUC_2D")  # Euclidean distance in 2-D
solution = solver.solve()

# Extract the tour and calculate the total distance
tour = solution.tour
total_distance = solution.optimal_value

# Make sure the tour starts and ends at the depot city 0
if tour[0] != 0:
    # Find the index of 0 and rotate
    zero_idx = np.where(tour == 0)[0][0]
    tour = np.roll(tour, -zero_idx)

# Ensuring the tour starts and ends at 0
tour = np.append(tour, 0)

# Output results
print("Tour:", list(tour))
print("Total travel cost:", total_distance)