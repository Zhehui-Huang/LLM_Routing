import numpy as np

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)

def calculate_total_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        city_from = int(tour[i])  # Ensure indices are integers
        city_to = int(tour[i+1])  # Ensure indices are integers
        total_cost += euclidean_distance(coordinates[city_from], coordinates[city_to])
    return total_cost

# Coordinates for each city (city index corresponds to positions in the list)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Provided solution tour and cost
solution_tour = [1, 2, 5, 7, 9, 6, 8, 10, 12, 15, 18, 20, 17, 21, 19, 16, 14, 0, 13, 11, 4, 3, 1]
claimed_cost = 278.4370769587606

# Validate that each city is visited exactly once and starts/ends at the designated depot
unique_cities_in_tour = len(set(solution_tour)) == len(coordinates)
is_valid_tour_start_end = solution_tour[0] == solution_tour[-1] == 1  # Assumed depot at 1 for both start and end

# Compute the actual cost from the solution
actual_cost = calculate_total_cost(solution_tour, coordinates)

# Compare the reported cost to the calculated cost
cost_matched = np.isclose(claimed_cost, actual_cost, atol=1e-5)

# Complete verification
if unique_cities_in_tour and is_valid_tour_start_end and cost_matched:
    print("CORRECT")
else:
    print("FAIL")