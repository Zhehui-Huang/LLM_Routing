from itertools import permutations
import math

# Data Parsing and Definitions
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

depots = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
number_of_robots = 8

# Calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generating a distance matrix for all cities
distance_matrix = {}
for k1, v1 in cities.items():
    for k2, v2 in cities.items():
        distance_matrix[(k1, k2)] = euclidean</|...|>_distance(v1, v2)

def find_min_cost_tour(start_depot):
    min_tour_cost = float('inf')
    best_tour = None
    
    remaining_cities = list(cities.keys())
    remaining_cities.remove(start_depot)

    # Test all permutations of the remaining cities
    for perm in permutations(remaining_cities):
        current_tour = [start_depot] + list(perm) + [start_depot]
        current_cost = sum(distance_matrix[(current_tour[i], current_tour[i+1])] for i in range(len(current_tour) - 1))
        
        if current_cost < min_tour_cost:
            min_tour_cost = current_cost
            best_tour = current_tour
            
    return best_tour, min_tour_cost

total_costs = 0

# Assign each robot to a depot and calculate the optimal tour from this depot
for robot_id, depot in depots.items():
    tour, cost = find_min_cost_tour(depot)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
    total_costs += cost

print(f"Overall Total Travel Cost: {total_costs}")