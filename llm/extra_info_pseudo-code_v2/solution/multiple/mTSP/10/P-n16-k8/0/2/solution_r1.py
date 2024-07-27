import numpy as np

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
    tours = [[] for _ in range(num_robots)]
    assigned_cities = len(non_depot_cities) // num_robots
    extras = len(non_depot_cities) % num_robots

    for i in range(num_robots):
        start = i * assigned_cities + min(i, extras)
        end = start + assigned_cities + (1 if i < extras else 0)
        tours[i] = [0] + non_depot_cities[start:end] + [0]

    return tours

# Conduct the 2-opt algorithm to optimize the tour
def two_opt(tour):
    minimal_change = 0.01
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                old_cost = get_distance(tour[i-1], tour[i]) + get_distance(tour[j-1], tour[j])
                new_cost = get_distance(tour[i-1], tour[j-1]) + get_distance(tour[i], tour[j])
                if new_cost < old_cost - minimal_change:
                    tour[i:j] = tour[i:j][::-1]
                    improvement = True
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