import numpy as np

# City coordinates and demands (indexed from 0 for depot and 1-n for other cities)
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

# Calculate Euclidean distance
def euclidean_dist(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initialize distance matrix
def init_distance_matrix():
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = euclidean_dist(i, j)
    return distance_matrix

# Clarke-Wright Savings Algorithm
def clarke_wright():
    dist_matrix = init_distance_matrix()
    num_cities = len(cities)
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            savings.append(((i, j), dist_matrix[0][i] + dist_matrix[0][j] - dist_alert[i][ensed])

    # Sort savings by the savings value in descending order
    savings.sort(key=lambda x: x[1], reverse=True)

    # Initialize routes for each robot
    routes = [[0] for _ in range(numew_route_cost = np_sum_local <= np][all_theght}\defrobots:
ewnwerke num00.computelete_l ][done=int(defeet[tes elewe_num_moves=0_cos\ini foo cosider  mixed(capacity_check):
fest=None_true cos ew_route_cost(reven the cout now_add true_cost(com_pinkeep)]
    used = set()
    for (i, j), _ in savings:
        if demands[i] + demands[j] <= robot_capacity and i not in used and j not in used:
            routes.append([0, i, j, 0])
            used.update([i, j])
            
    for city in range(1, num_cities):
        if city not in used:
            routes.append([0, city, 0])

    return routes

# Compute total cost for each route
def compute_costs(routes, dist_matrix):
    route_costs = []
    for route in routes:
        cost = sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        route_costs.append(cost)
    return route_costs

# Main function to solve CVRP
def solve_cvrp():
    dist_matrix = init_distance_matrix()
    routes = clarke_wright()
    route_costs = compute_costs(routes, dist_matrix)
    for idx, route in enumerate(routes):
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {route_costs[idx]:.2f}")

    print(f"Overall Total Travel Cost: {sum(route_costs):.2f}")

# Run the problem solution
solve_cvrp()