import math
from itertools import permutations

# Define helper functions
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_tour_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

# Define cities and their coordinates
coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Initialize robot tours and related variables
num_robots = 2
city_list = list(coordinates.keys())[1:]  # Excluding the depot city
city_permutations = list(permutations(city_list))
best_max_cost = float('inf')
best_tours = []

# Evaluate all city permutations for a solution
for permutation in city_permutations:
    slice_size = len(permutation) // num_robots
    tours = []
    max_tour_cost = 0
    
    # Create tours for each robot
    for i in range(num_robots):
        tour_start_index = i * slice_size
        tour_end_index = tour_start_index + slice_size + (1 if i < len(permutation) % num_robots else 0)
        tour = [0] + list(permutation[tour_start_index:tour_end_index]) + [0]
        tour_cost = calculate_tour_cost(tour, coordinates)
        tours.append((tour, tour_cost))
        max_tour_cost = max(max_tour_cost, tour_cost)
        
    # Record the best solution found
    if max_tour_cost < best_max_cost:
        best_max_cost = max_tour_cost
        best_tours = tours

# Output the result
for i, (tour, cost) in enumerate(best_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {int(cost)}")

print(f"Maximum Travel Cost: {int(best_max_cost)}")