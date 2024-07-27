import numpy as np
import itertools

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function to calculate the total distance of a tour
def calculate_total_distance(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Improved nearest neighbor algorithm
def nearest_neighbor(start_city, unvisited_cities, cities):
    path = [start_city]
    current_city = start_city
    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        path.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city
    return path

# Two-Opt optimization technique
def two_opt(route, cities):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue
                new_route = route[:i] + route[i:j+1][::-1] + route[j+1:]
                if calculate_total_distance(new_route, cities) < calculate_total_distance(route, cities):
                    route = new_route
                    improved = True
        break
    return route

cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Split cities between robots based on some heuristic or pre-defined rule
robot_tours = {0: [0], 1: [1]}
remaining_cities = set(range(2, len(cities)))

# Divide remaining cities
robot_tours[0] += nearest_neighbor(0, remaining_cities.copy(), cities)
robot_tours[1] += nearest_neighbor(1, remaining_cities.difference(set(robot_tours[0])), cities)

# Optimize each tour using 2-opt
robot_tours[0] = two_opt(robot_tours[0], cities)
robot_tours[1] = two_opt(robot_tours[1], cities)

# Calculate travel costs
cost_0 = calculate_total_distance(robot_tours[0], cities)
cost_1 = calculate_total_distance(robot_tours[1], cities)

overall_total_cost = cost_0 + cost_1

# Output results
print(f"Robot 0 Tour: {robot_tours[0]}")
print(f"Robot 0 Total Travel Cost: {cost_0:.2f}")

print(f"Robot 1 Tour: {robot_tours[1]}")
print(f"Robot 1 Total Travel Cost: {cost_1:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")