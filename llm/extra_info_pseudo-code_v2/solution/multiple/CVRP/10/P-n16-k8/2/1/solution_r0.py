import numpy as np

# Cities coordinates and demands
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

demands = {
    1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 8, 10: 8,
    11: 7, 12: 14, 13: 6, 14: 19, 15: 11
}

num_cities = len(cities)
num_robots = 8
robot_capacity = 35

# Calculate the Euclidean distance between two cities
def euclidean_dist(c1, c2):
    return np.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate cost matrix
def generate_cost_matrix():
    cost_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            cost_matrix[i][j] = euclidean_dist(i, j) if i != j else float('inf')
    return cost_matrix

# Generate saving matrix
def generate_savings_matrix(cost_matrix):
    savings = {}
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            if i != j:
                s = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
                savings[(i, j)] = s
    sorted_savings = sorted(savings.items(), key=lambda item: item[1], reverse=True)
    return sorted_savings

# Clarke-Wright Algorithm
def clarke_wright_savings():
    cost_matrix = generate_cost_matrix()
    savings = generate_savings_matrix(cost_matrix)
    
    routes = {i: [0, i, 0] for i in range(1, num_cities)}
    load = {i: demands[i] for i in range(1, num_cities)}
    
    for ((i, j), _) in savings:
        if routes[i] != routes[j] and load[i] + load[j] <= robot_capacity:
            # Combine routes
            new_route = routes[i][:-1] + routes[j][1:]
            routes[i] = new_route
            del routes[j]
            load[i] += load[j]
            del load[j]
    
    return routes

# Calculate total travel cost for a route
def calculate_route_cost(route, cost_matrix):
    cost = 0
    for k in range(len(route) - 1):
        cost += cost_matrix[route[k]][route[k+1]]
    return cost

# Main function to execute Clarke-Wright and output results
def main():
    cost_matrix = generate_cost_matrix()
    routes = clarke_wright_savings()
    overall_cost = 0
    for idx, route in enumerate(routes.values()):
        route_cost = calculate_route_cost(route, cost_matrix)
        overall_cost += route_cost
        print(f'Robot {idx} Tour: {route}')
        print(f'Robot {idx} Total Travel Cost: {route[1]}: {route_cost:.2f}')
    print(f'Overall Total Travel Cost: {overall_cost:.2f}')

main()