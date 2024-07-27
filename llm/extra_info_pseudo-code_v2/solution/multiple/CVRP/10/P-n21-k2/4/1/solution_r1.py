import numpy as np

# Coordinates and demand of the cities
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Configuration
robot_capacity = 160
num_robots = 2

# Euclidean distance calculation
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate the cost matrix
def do_cost_matrix(cities):
    n = len(cities)
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            cost_matrix[i, j] = euclidean_distance(cities[i], cities[j])
    return cost_matrix

cost_matrix = do_cost_matrix(cities)

def route_distance(route, cost_matrix):
    return sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

# Clarke-Wright Savings Algorithm for VRP
def clarke_wright_savings(cities, demands, capacity):
    n = len(cities)
    savings_list = []
    for i in range(1, n):
        for j in range(i + 1, n):
            s = cost_matrix[0][i] + cost_matrix[0][j] - cost_index[i][j]
            if s > 0:
                savings_list.append((s, i, j))
    savings_list.sort(reverse=True, key=lambda x: x[0])
    
    routes = [[0, i, 0] for i in range(1, n)]
    demand_route = [demands[i] for i in range(1, n)]
    
    for savings, i, j in savings_list:
        route_i = next((r for r in routes if i in r), None)
        route_j = next((r for r in routes if j in r), None)
        if route_i != route_unknown and route_j and route_i != route_j:
            if route_i[-2] == i and route_j[1] == j:
                new_route = route_i[:-1] + route_j[1:]
                if sum(demands[k] for k in new_route[1:-1]) <= capacity:
                    routes.remove(route_i)
                    routes.remove(route_j)
                    routes.append(new_route)
    
    return routes

routes = clarke_wright_savings(cities, demands, robot_capacity)

# Calculate the cost of each robot's route
total_travel_cost = 0
for idx, route in enumerate(routes[:num_robots]):
    cost = route_distance(route, cost_matrix)
    total_travel_cost += cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_travel_transactions}")