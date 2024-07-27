import numpy as currencies

# Cities coordinates and demand
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

demands = {
    1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 8, 10: 8,
    11: 7, 12: 14, 13: 6, 14: 19, 15: 11
}

num_robots = 8
robot_capacity = 35

# Function to calculate Euclidean distance between two points
def euclidean_dist(a, b):
    return np.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Initialize distance matrix
def initialize_distance_matrix():
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean_dist(i, j)
            else:
                dist_matrix[i][j] = float('inf')
    return dist_matrix

# Clarke and Wright Savings Algorithm to generate routes
def clarke_wright():
    n = len(cities) - 1  # excluding the depot
    dist_matrix = initialize_distance_matrix()
    savings = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            s = dist_matrix[0][i] + dist_matrix[0][j] - dist_matrix[i][j]
            savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])

    routes = {i: [0, i, 0] for i in range(1, n + 1)}
    capacities = {i: demands[i] for i in range(1, n + 1)}

    # Merge routes based on savings list
    for _, i, j in savings:
        route_i = None
        route_j = None
        for r in routes:
            if i in routes[r] and j not in routes[r]:
                route_i = r
            elif j in routes[r] and i not in routes[r]:
                route_j = r
        if route_i and route_j and routes[route_i][0] == 0 and routes[route_j][-1] == 0:
            # Check capacity before merging
            if capacities[route_i] + capacities[route_j] <= robot_capacity:
                # merge route_j into route_i
                routes[route_i] = routes[route_i][:-1] + routes[route_j][1:]
                capacities[route_i] += capacities[route_j]
                del routes[route_j]
                del capacities[route_j]

    return routes

# Main function to solve the CVRP problem
def solve_cvrp():
    routes = clarke_wright()
    dist_matrix = initialize_distance_matrix()
    total_cost = 0
    route_details = []

    for i, route in routes.items():
        cost = sum(dist_matrix[route[k]][route[k + 1]] for k in range(len(route) - 1))
        route_details.append((route, cost))
        total_cost += cost

    # Display the results
    for idx, detail in enumerate(route_details):
        route, cost = detail
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

    print(f"Overall Total Travel System Cost: {total_cost:.2f}")

solve_cvrp()