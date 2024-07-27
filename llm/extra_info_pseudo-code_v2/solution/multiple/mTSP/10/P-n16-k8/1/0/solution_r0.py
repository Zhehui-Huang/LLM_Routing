import numpy as np
import math
from itertools import permutations

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to calculate total travel cost of a tour
def total_cost(tour, distances):
    return sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Greedy algorithm to build an initial solution
def nearest_neighbor(cities, start_city, distances):
    unvisited = set(cities)
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city, city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(start_city)  # return to depot
    return tour

# 2-opt optimization
def optimize_tour(tour, distances):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if distances[tour[i - 1], tour[i]] + distances[tour[j], tour[j + 1]] > \
                   distances[tour[i - 1], tour[j]] + distances[tour[i], tour[j + 1]]:
                    tour[i:j + 1] = reversed(tour[i:j + 1])
                    improved = True
    return tour

# Assign cities to robots
def assign_cities_to_robots(num_robots, cities):
    return [cities[i::num_robots] for i in range(num_robots)]

# Define cities and their coordinates
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69)
}
num_robots = 8
depot = 0
cities = list(cities_coordinates.keys())
cities.remove(depot)

# Compute distances between all pairs of cities
distances = {}
for c1 in cities_coordinates:
    for c2 in cities_coordinates:
        distances[c1, c2] = euclidean_distance(cities_coordinates[c1], cities_coordinates[c2])

# Assign initial cities to robots
robot_cities = assign_cities_to_robots(num_robots, cities)

# Initialize tours for each robot
all_tours = []
total_dist = 0

for i, robot_city_list in enumerate(robot_cities):
    tour = [depot] + robot_city_list + [depot]
    tour = nearest_neighbor(tour, depot, distances)
    tour = optimize_tour(tour, distances)
    tour_cost = total_cost(tour, distances)
    total_dist += tour_cost
    all_tours.append((i, tour, tour_cost))

# Output results
for i, tour, cost in all_tours:
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_dist}")