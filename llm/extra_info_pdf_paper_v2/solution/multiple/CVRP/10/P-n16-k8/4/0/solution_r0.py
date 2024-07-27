import math
import numpy as np

# Coordinates and demands
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Robot info
robot_count = 8
robot_capacity = 35

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generating initial saving list
num_cities = len(coordinates)
savings = []
for i in range(1, num_cities):
    for j in range(i + 1, num_cities):
        save = distance(0, i) + distance(0, j) - distance(i, j)
        savings.append((save, i, j))
savings.sort(reverse=True, key=lambda x: x[0])

# Initialize routes
routes = [[i] for i in range(1, num_cities)]

# Clustering phase using Clarke-Wright Savings
while savings:
    save, i, j = savings.pop(0)
    index_i = next((idx for idx, route in enumerate(routes) if i in route), None)
    index_j = next((idx for idx, route in enumerate(routes) if j in route), None)
    
    # Ensure two indexes are in different clusters and would not violate capacity
    if index_i != index_j:
        if np.sum([demands[k] for k in routes[index_i] + routes[index_j]]) <= robot_capacity:
            if routes[index_i][0] != i:
                routes[index_i].reverse()
            if routes[index_j][-1] != j:
                routes[index_j].reverse()
            routes[index_i].extend(routes[index_j])
            routes.pop(index_j)

# Route post-improvement procedures can be implemented here if needed

# Generate full tours starting and ending at the depot
full_tours = [[0]+route+[0] for route in routes]

# Calculate travel cost of each tour
def calculate_route_cost(route):
    return sum(distance(route[k], route[k+1]) for k in range(len(route) - 1))

# Output the tours and costs
total_cost = 0
for idx, tour in enumerate(full_tours):
    tour_cost = calculate_route_cost(tour)
    total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Drive: {total_cost}")