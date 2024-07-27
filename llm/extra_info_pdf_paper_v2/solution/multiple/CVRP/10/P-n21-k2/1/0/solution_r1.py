import math
import heapq

# Coordinates and demands initialization
cities = {
    0: (30, 40), 1: (37, 52),  2: (49, 49),  3: (52, 64),  4: (31, 62),
    5: (52, 33), 6: (42, 41),  7: (52, 41),  8: (57, 58),  9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Robot parameters
num_robots = 2
capacity = 160

# Calculate Euclidean distances
def euclidean_distance(a, b):
    ax, ay = cities[a]
    bx, by = cities[b]
    return math.sqrt((ax - bx)**2 + (ay - by)**2)

# Generate distance matrix
num_cities = len(cities)
distance_matrix = [[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Define the savings calculator
def calculate_savings():
    return { (i, j): distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
            for i in range(1, num_cities) for j in range(i + 1, num_cities) }

# Clarke-Wright savings algorithm for CVRP
def clarke_wright():
    savings = calculate_savings()
    priority_list = sorted(savings.items(), key=lambda x: x[1], reverse=True)
    
    routes = {}
    for i in range(1, num_cities):
        routes[i] = [0, i, 0]  # Each city starts with its own route from and to the depot

    route_demand = {i: demands[i] for i in range(1, num_cities)}

    for (i, j), _ in priority_list:
        route_i = next((r for r in routes.values() if i in r), None)
        route_j = next((r for r in routes.values() if j in r), None)
        if route_i is not route_j and route_i[1] == i and route_j[-2] == j:
            # Check combined demand
            demand_i = sum(demands[k] for k in route_i[1:-1])
            demand_j = sum(demands[k] for k in route_j[1:-1])
            if demand_i + demand_j <= capacity:
                # Combine routes
                new_route = route_i[:-1] + route_j[1:]
                routes.pop(route_i[1])
                routes.pop(route_j[-2])
                routes[new_route[1]] = new_route  # Use starting city as key

    return list(routes.values())  # Return only the routes

def calculate_costs(routes):
    total_cost = 0
    for route in routes:
        cost = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
        total_cost += cost
        print(f"Tour: {route}")
        print(f"Total Travel Cost for this tour: {cost:.2f}")
    return total_cost

# Obtain routes using the Clarke-Wright algorithm
routes = clarke_wright()

# Print detailed information about routes
print("Generated Routes:")
total_cost = calculate_costs(routes)
print(f"Overall Total Travel Cost: {total_cost:.2f}")