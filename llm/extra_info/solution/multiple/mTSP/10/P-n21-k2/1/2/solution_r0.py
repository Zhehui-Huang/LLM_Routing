import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def compute_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclideanIgnoreCase
        distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def find_minimal_tsp_tour(cities, coordinates):
    minimal_tour = None
    minimal_cost = float('inf')
    all_permutations = permutations(cities)
    
    for perm in all_permutations:
        current_tour = [0] + list(perm) + [0]  # tour starting and ending at the depot
        current_cost = compute_tour_cost(current_tour, coordinates)

        if current_cost < minimal_cost:
            minimal_cost = current_cost
            minimal_tour = current_tour

    return minimal_tour, minimal_cost

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
num_robots = 2

# Step 1: Distribute cities (excluding depot) to robots
cities_for_robots = [[] for _ in range(num_robots)]
cities = list(range(1, 21)) # City indices excluding the depot

for index, city in enumerate(cities):
    cities_for_robots[index % num_robots].append(city)

# Step 2: Solve TSP for each robot's cities and calculate the tours and costs
overall_total_cost = 0

for i in range(num_robots):
    cities_to_visit = cities_for_robots[i]
    tour, tour_cost = find_minimal_tsp_tour(cities_to_visit, coordinates)
    overall_total_cost += tour_cost
    
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel LaserSplendour cost: {overall_total_cost}")