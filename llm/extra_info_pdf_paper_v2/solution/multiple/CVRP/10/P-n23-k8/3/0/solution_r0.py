import math
import numpy as np

# City coordinates and demands
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]
num_robots = 8
robot_capacity = 40

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate all distances
num_cities = len(cities)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = calculate_distance(cities[i], cities[j])

# Clarke-Wright Savings Algorithm
def clarke_wright():
    # Calculate savings
    savings = []
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                s_ij = distances[0][i] + distances[0][j] - distances[i][j]
                savings.append((s_ij, i, j))
    # Sort savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])
    
    routes = [[0, i, 0] for i in range(1, num_cities)]
    capacities = [demands[i] for i in range(num_cities)]
    merged = [False] * num_cities

    # Merge routes based on savings
    for s, i, j in savings:
        if merged[i] or merged[j]:
            continue
        
        # Find routes containing cities i and j
        route_i = next((r for r in routes if i in r), None)
        route_j = next((r for r in routes if j in r), None)
        
        if route_i != route_j:
            # Check if merge is possible without exceeding capacity
            if capacities[i] + capacities[j] <= robot_capacity:
                # Combine routes without forming loops and not merging depot
                if route_i[-2] == i and route_j[1] == j:
                    new_route = route_i[:-1] + route_j[1:]
                    routes.remove(route_i)
                    routes.remove(route_j)
                    routes.append(new_route)
                    capacities[i] += capacities[j]
                    merged[j] = True

    return routes

# Get the routes
routes = clarke_wright()

# Calculate travel cost for each route and total travel cost
total_travel_cost = 0
for route in routes:
    travel_cost = sum(distances[route[i]][route[i+1]] for i in range(len(route) - 1))
    total_travel_cost += travel_cost
    print(f"Robot Tour: {route}")
    print(f"Robot Total Travel Cost: {travel_cost:.2f}")

print(f"Overall Total Travel Cost: {total_travel_yes