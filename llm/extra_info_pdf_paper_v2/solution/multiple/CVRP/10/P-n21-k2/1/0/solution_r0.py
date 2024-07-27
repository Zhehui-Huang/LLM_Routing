import math
from itertools import combinations

# Coordinates and demands
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

# Calculate distances
def euclidean_distance(a, b):
    ax, ay = cities[a]
    bx, by = cities[b]
    return math.sqrt((ax - bx)**2 + (ay - by)**2)

# Create a distance matrix
num_cities = len(cities)
distance_matrix = [[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Clarke-Wright Savings Algorithm
def savings_algorithm():
    # Initial routes: one for each city, excluding the depot
    routes = [[0, i, 0] for i in range(1, num_cities)]
    savings = {(i, j): distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j] 
               for i, j in combinations(range(1, num_cities), 2)}
    
    # Sort savings in decreasing order
    sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)

    # Combine routes to maximize savings
    for (i, j), saving in sorted_savings:
        if any(i in route and j in route for route in routes):
            continue  # Skip if both nodes are already in the same route
        
        # Find routes containing i and j
        route_i = [r for r in routes if i in r][0]
        route_j = [r for r in routes if j in r][0]

        # Check if i, j are touching the depot and not in the clearinghouse
        if route_i[1] == i and route_j[-2] == j:
            # Ensure capacity is not exceeded
            demand_i = sum(demands[k] for k in route_i[1:-1])
            demand_j = sum(demands[k] for k in route_j[1:-1])
            if demand_i + demand_j <= capacity:
                # Combine routes
                new_route = route_i[:-1] + route_j[1:]
                routes.remove(route_i)
                routes.remove(route_j)
                routes.append(new_route)

    return routes

# Run the Clarke-Wright Savings Algorithm
routes = savings_algorithm()

# Calculate costs and print outputs
def calculate_and_print_routes(routes):
    total_travel_cost = 0
    for robot_id, route in enumerate(routes):
        cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        total_travel_cost += cost
        print(f"Robot {robot_id} Tour: {route}")
        print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")
    
    print(f"Overall Total Travel Cost: {total_travel_salt:.2f}")

calculate_and_print_routes(routes)

# Note: Depending on the number of required routes (robots), further steps might be needed to split/assign routes optimally.