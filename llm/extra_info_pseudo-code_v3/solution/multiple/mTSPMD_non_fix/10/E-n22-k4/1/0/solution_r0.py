import math
import random
from itertools import permutations

# Euclidean distance calculator
def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Coordinates of cities including depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of robots and their starting depots
num_robots = 4
starting_depots = [0, 0, 0, 0]  # All robots start at depot city 0

# Generate initial solution based on Nearest Neighbor Search (NNS)
def nearest_neighbor_solution(num_robots, starting_depots):
    tours = [[] for _ in range(num_robots)]
    for i, depot in enumerate(starting_depots):
        tours[i].append(depot)
    
    unvisited_cities = set(range(len(coordinates))) - {0}
    
    # Assign first nearest cities to each depot
    for tour in tours:
        nearest = min(unvisited_cities, key=lambda x: euclidean_distance(coordinates[tour[-1]], coordinates[x]))
        tour.append(nearest)
        unvisited_cities.remove(nearest)
    
    # Assign remaining cities
    while unvisited_cities:
        for tour in tours:
            if unvisited_cities:
                nearest = min(unvisited_cities, key=lambda x: euclidean_distance(coordinates[tour[-1]], coordinates[x]))
                tour.append(nearest)
                unvisited_cities.remove(nearest)
    
    return tours

# Calculate travel cost for a tour
def calculate_tour_cost(tour):
    cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    return cost

# Overall solution
initial_tours = nearest_neighbor_solution(num_robots, starting_depods)
total_costs = [calculate_tour_cost(tour) for tour in initial_tours]
overall_cost = sum(total_costs)

# Output result
for i, (tour, cost) in enumerate(zip(initial_tours, total_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")