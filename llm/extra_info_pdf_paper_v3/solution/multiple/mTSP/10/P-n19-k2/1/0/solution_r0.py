import numpy as np
import itertools

# Define the cities' coordinates
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
          (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Compute Euclidean distance between each pair of cities
def calc_distance(city1, city2):
    return np.hypot(city1[0] - city2[0], city1[1] - city2[1])

# Compute the distance matrix
n = len(cities)
distances = np.empty((n, n))
for i in range(n):
    for j in range(n):
        distances[i, j] = calc_distance(cities[i], cities[j])

# Initial naive partition of cities to each robot (Simple split method)
def naive_partition():
    return list(range(1, n // 2 + 1)), list(range(n // 2 + 1, n))

# Apply the 2-opt algorithm to optimize each robot's tour
def two_opt(route, distance_matrix):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]
                if sum(distance_matrix[new_route[k - 1], new_route[k]] for k in range(1, len(new_route))) < sum(distance_matrix[best[k - 1], best[k]] for k in range(1, len(best))):
                    best = new_route
                    improved = True
        route = best
    return best

# Generate the routes for each robot
def generate_routes(partitions):
    reorganized_routes = []
    for part in partitions:
        part = [0] + part + [0] # add depot to the beginning and end
        optimized_tour = two_opt(part, distances)
        reorganized_routes.append(optimized_tour)
    return reorganized_routes

# Calculate total travel cost for each route
def calculate_travel_cost(routes):
    costs = []
    for route in routes:
        cost = sum(distances[route[i - 1], route[i]] for i in range(1, len(route)))
        costs.append(cost)
    return costs

partitions = naive_partition()
routes = generate_routes(partitions)
total_costs = calculate_travel_cost(routes)
overall_total_cost = sum(total_costs)

# Output the tours and costs
for i, route in enumerate(routes):
    print(f'Robot {i} Tour: {route}')
    print(f'Robot {i} Total Travel Attend Cost: {total_costs[i]:.2f}')

print(f'Overall Total Travel Cost: {overall_total_cost:.2f}')