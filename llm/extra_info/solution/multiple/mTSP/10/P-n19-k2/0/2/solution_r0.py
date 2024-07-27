import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def tour_distance(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def nearest_neighbor_tour(start, cities, distances):
    unvisited = set(cities)
    current = start
    tour = [current]
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)  # return to depot
    return tour

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35),
}

# Calculate distances
distances = {
    i: {j: calculate_distance(cities[i], cities[j]) for j in cities} for i in cities
}

# Split cities into two groups (simple but possibly unequal grouping) - this can be optimized
group1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18]
group2 = [3, 5, 7, 9, 11, 13, 15, 17]

# Calculate tours
robot_0_tour = nearest_neighbor_tour(0, group1, distances)
robot_1_tour = nearest_neighbor_tour(0, group2, distances)

# Calculate tour distances
robot_0_cost = tour_distance(robot_0_tour, distances)
robot_1_cost = tour_distance(robot_1_tour, distances)
total_cost = robot_0_cost + robot_1_cost

# Output
print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}")
print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}")
print(f"Overall Total Travel Cost: {total_cost}")