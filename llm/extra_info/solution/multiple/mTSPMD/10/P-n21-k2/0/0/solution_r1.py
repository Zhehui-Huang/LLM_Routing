from math import sqrt
from itertools import permutations

def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Hardcoded city coordinates
cities = {
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

depot0 = 0
depot1 = 1

# Assume a simple division of cities based on even and odd indices
# Optimization of this division can be treated by more specialized algorithms such as clustering
robot_0_cities = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
robot_1_cies = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def calculate_total_travel_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

def find_minimal_tsp_tour(cities_list, depot):
    best_cost = float('inf')
    best_tour = None
    for perm in permutations(cities_list[1:]):
        # Adding depot at start and end of tour
        tour = [depot] + list(perm) + [depot]
        cost = calculate_total_travel_cost(tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
    return best_tour, best_cost

# Find tours and costs for both robots
tour_robot_0, cost_robot_0 = find_minimal_tsp_tour(robot_0_cities, depot0)
tour_robot_1, cost_robot_1 = find_minimal_tsp_tour(robot_1_cies, depot1)
overall_cost = cost_robot_0 + cost_robot_1

print(f"Robot 0 Tour: {tour_robot_0}")
print(f"Robot 0 Total Travel Cost: {cost_robot_0}")
print(f"Robot 1 Tour: {tour_robot_1}")
print(f"Assuming that no 2 cities in a robot's tour are not sequential")
print(f"Robot 1 Total Travel Cost: {cost_robot_1}")
print(f"Overall Total Travel Cost: {overall_cost}")