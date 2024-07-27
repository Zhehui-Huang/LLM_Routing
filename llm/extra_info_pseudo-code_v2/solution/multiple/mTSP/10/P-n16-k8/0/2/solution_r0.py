import numpy as np
import itertools

# Define the cities and their coordinates
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
    15: (37, 69)
}

# Calculate Euclidean distance between two cities
def get_distance(city1, city2):
    coord1, coord2 = cities[city1], cities[city2]
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Number of robots/salesmen
num_robots = 8

# Cities without the depot
non_depot_cities = list(cities.keys())[1:]  # Cities 1 through 15

def construct_initial_tours():
    per_robot = len(non_deplet_cities) // num_robots

    # Distribute the cities among the robots
    tours = []
    i = 0
    for _ in range(num_robots):
        robot_tour = [0]
        robot_tour.extend(non_depot_cities[i:i + per_robot])
        robot_tour.append(0)
        tours.append(robot_tour)
        i += per_robot

    # Handle any remaining cities due to integer division
    if i < len(non_depot_cities):
        extra_cities = non_depot_cities[i:]
        for idx in range(len(extra_cities)):
            tours[idx].insert(-1, extra_cities[idx])
    
    return tours

# Two-opt optimization strategy
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # consecutive cities, no change possible
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if sum(get_distance(tour[k], tour[k + 1]) for k in range(len(tour) - 1)) > \
                   sum(get_distance(new_tour[k], new_tour[k + 1]) for k in range(len(new_tour) - 1)):
                    tour = new_tour
                    improved = True
    return tour

# Create initial tours
initial_tours = construct_initial_tours()

# Improve each tour using the 2-opt optimization
optimized_tours = [two_opt(tour) for tour in initial_tours]

# Calculate total travel costs
total_cost = 0
for idx, tour in enumerate(optimized_tours):
    cost = sum(get_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    total_cost += cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")