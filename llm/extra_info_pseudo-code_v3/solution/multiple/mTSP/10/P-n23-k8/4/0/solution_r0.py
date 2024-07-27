import math
import numpy as np
from scipy.spatial.distance import cdist

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
    21: (32, 39), 22: (56, 37)
}

# Number of robots and their starting city
num_robots = 8
depot = 0

# Distance function using Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Precompute the distances to speed up access
dist_matrix = cdist(list(cities.values()), list(cities.values()), 'euclidean')

# Assign cities to robots
def assign_cities_to_robots(cities, num_robots, depot):
    # Here we can use different strategies such as clustering, greedy algorithms etc.
    # For simplicity and demonstration, we are using a naive equally distributing method.
    all_cities = list(cities.keys())
    all_cities.remove(depot)
    np.random.shuffle(all_cities)
    assigned = np.array_split(all_cities, num_robots)
    return assigned

# Create tours for robots starting from depot
def create_tours(assigned_cities, depot):
    tours = []
    for cities in assigned_cities:
        tour = [depot] + list(cities) + [depot]
        tours.append(tour)
    return tours

# Calculate total travel cost for a tour
def calculate_tour_cost(tour, dist_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += dist_matrix[tour[i], tour[i+1]]
    return total_cost

assigned_cities = assign_cities_to_robots(cities, num_robots, depot)
tours = create_tours(assigned_cities, depot)
tour_costs = []
overall_total_cost = 0

for i, tour in enumerate(tours):
    cost = calculate_tour_cost(tour, dist_matrix)
    tour_costs.append(cost)
    overall_total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")