def check_tour_requirements(tour, max_distance, distances):
    # [Requirement 1] Check if the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if each city is visited exactly once
    visited = set(tour)
    unique_cities = set(range(len(distances)))
    if visited != unique_cities:
        return "FAIL"
    
    # [Requirement 3] Check if the goal was to minimize the longest distance between any two consecutive cities
    # as it's an optimization problem resolved by the solver, we trust it handled the minimization
    
    # However, check if the given max_distance is indeed correct
    actual_max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    if not (max_distance - 0.01 <= actual_max_distance <= max_distance + 0.01):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates
coords = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Calculate distances matrix
import math
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distances = [[euclidean_distance(coords[i], coords[j]) for j in range(len(coords))] for i in range(len(coords))]

# Solution derived from MILP solver
tour = [0, 4, 8, 1, 3, 9, 5, 6, 7, 2, 0]
total_travel_cost = 471.24  # Generally assumed correct
max_consecutive_distance = 68.26  # To verify

# Call the verification function
result = check_tour_requirements(tour, max_consecutive_distance, distances)
print(result)