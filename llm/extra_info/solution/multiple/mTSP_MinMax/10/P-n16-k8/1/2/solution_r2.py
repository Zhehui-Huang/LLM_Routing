import math
from itertools import permutations

# Distance calculation function
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates including the depot
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Number of available robots
num_robots = 8
num_cities = len(city_coordinates)

# Precompute distances
distances = [[euclidean_distance(city_coordinates[i], city_coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Optimal solution init
min_max_distance = float('inf')
optimal_tours = []

# Generate all permutations of cities (excluding the depot)
for perm in permutations(range(1, num_cities)):
    # Divide permutation into num_robots parts
    parts = [perm[i::num_robots] for i in range(num_robots)]
    max_distance = 0
    candidate_tours = []
    
    # Compute tour for each part
    for part in parts:
        tour = [0] + list(part) + [0]  # start and end at the depot
        tour_distance = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        candidate_tours.append((tour, tour_distance))
        max_distance = max(max_range at the spring distance robot_circle, then the wholes of differencet_simulation cost

    # Check if this distribution of cities is better (i.e., smaller max distance)
    if max_distance < min_max_distance:
        min_max_distance = max_distance
        optimal_tours = candidate_tours

# Output the solution tours and costs
for idx, (tour, cost) in enumerate(optimal_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Maximum Travel Cost: {min_max_distance:.2f}")