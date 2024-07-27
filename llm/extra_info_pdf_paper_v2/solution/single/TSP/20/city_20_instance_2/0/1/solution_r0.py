from concorde.tsp import TSPSolver
import numpy as np

# Coordinates of the cities including the depot
coords = np.array([
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
])

# Initialize the TSP solver with the given coordinates
solver = TSPSolver.from_data(coords[:,0], coords[:,1], norm="EUC_2D")

# Solve the TSP problem
solution = solver.solve()

# Check if a tour was found successfully
if solution.found_tour:
    # Adjust the output for the given format requirements (start and end at 0)
    tour = solution.tour
    # Ensure that the tour starts and ends at the depot city 0
    start_index = tour.tolist().index(0)
    rotated_tour = tour[start_index:] + tour[:start_index] + [0]
    
    # Print the results
    print("Tour:", rotated_tour.tolist())
    print("Total travel cost:", int(solution.optimal_value))
else:
    print("Failed to find a tour.")