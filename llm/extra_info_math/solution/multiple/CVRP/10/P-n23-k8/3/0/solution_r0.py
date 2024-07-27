import math
from itertools import combinations

# Coordinates and demands for each city including the depot
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
          (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
          (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
capacity = 40  # Capacity of each robot

# Function to calculate the euclidean distance between two cities
def euclidean_distance(i, j):
    return math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)

# Generate savings list using the Clarke and Wright method
def savings_list():
    savings = []
    for i in range(1, len(coords)):
        for j in range(i + 1, len(coords)):
            save = euclidean_distance(0, i) + euclidean_distance(0, j) - euclidean_distance(i, j)
            savings.append((save, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

# Create initial routes (each city as a separate route)
routes = [[0, i, 0] for i in range(1, len(coords))]

# Merge routes according to savings, respecting capacity constraints
def merge_routes():
    savings = savings_list()
    for save, i, j in savings:
        route_i = next((r for r in routes if i in r), None)
        route_j = next((r for r in routes if j in r), None)
        if route_i != route_j and route_i is not None and route_j is not None:
            if route_i.index(i) == 1 and route_j.index(j) == len(route_j) - 2:
                # Check capacity before merging
                if sum(demands[k] for k in route_i[1:-1]) + sum(demands[k] for k in route_j[1:-1]) <= capacity:
                    routes.remove(route_i)
                    routes.remove(route_j)
                    merged_route = [0] + route_i[1:-1] + route_j[1:-1] + [0]
                    routes.append(merged_route)
merge_routes()

# Calculate travel cost of each route and the overall total cost
def calculate_costs(routes):
    total_cost = 0
    for r, route in enumerate(routes):
        cost = sum(euclidean_distance(route[i], route[i + 1]) for i in range(len(route) - 1))
        total_cost += cost
        print(f"Robot {r} Tour: {route}")
        print(f"Robot {r} Total Travel Cost: {cost:.2f}")
    print(f"\nOverall Total Travel Cost: {total_cost:.2f}")

calculate_costs(routes)