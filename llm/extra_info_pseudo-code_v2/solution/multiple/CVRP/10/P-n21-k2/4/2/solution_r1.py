import numpy as np
from math import sqrt

# City coordinates and demand
cities = {
    0: (30, 40, 0), 1: (37, 52, 7), 2: (49, 49, 30), 3: (52, 64, 16), 4: (31, 62, 23),
    5: (52, 33, 11), 6: (42, 41, 19), 7: (52, 41, 15), 8: (57, 58, 28), 9: (62, 42, 8),
    10: (42, 57, 8), 11: (27, 68, 7), 12: (43, 67, 14), 13: (58, 48, 6), 14: (58, 27, 19),
    15: (37, 69, 11), 16: (38, 46, 12), 17: (61, 33, 26), 18: (62, 63, 17), 19: (63, 12, 6), 20: (45, 35, 15)
}

# Parameters
num_robots = 2
capacity = 160

# Compute Euclidean distance between two points
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Compute cost matrix
def compute_cost_matrix():
    num_cities = len(cities)
    cost_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            cost_matrix[i][j] = euclidean_distance(i, j)
    return cost_matrix

cost_matrix = compute_cost_matrix()

def solve_cvrp(num_robots, capacity):
    num_cities = len(cities)
    routes = [[] for _ in range(num_robots)]
    demands = [cities[i][2] for i in range(num_cities)]
    
    # Clarke-Wright Savings Algorithm
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            s = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
            savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    
    assigned = set()
    capacities = [0] * num_robots
    
    for saving, i, j in savings:
        if i in assigned or j in assigned:
            continue
        for r in range(num_robots):
            if capacities[r] + demands[i] + demands[j] <= capacity:
                if not routes[r]:
                    routes[r].extend([0, i, j, 0])
                    assigned.update([i, j])
                    capacities[r] += (demands[i] + demands[j])
                    break
                elif routes[r][-2] == i and capacities[r] + demands[j] <= capacity:
                    routes[r].insert(-1, j)
                    assigned.update([j])
                    capacities[r] += demands[j]
                    break
                elif routes[r][1] == j and capacities[r] + demands[i] <= capacity:
                    routes[r].insert(1, i)
                    assigned.update([i])
                    capacities[r] += demands[i]
                    break

    # Calculating total travel cost
    total_cost = 0
    for r in range(num_robots):
        route_cost = sum(cost_matrix[routes[r][i]][routes[r][i+1]] for i in range(len(routes[r])-1))
        print(f"Robot {r} Tour: {routes[r]}")
        print(f"Robot {r} Total Travel Cost: {route_cost}")
        total_cost += route_cost
        
    print(f"Overall Total Travel Cost: {total_cost}")

solve_cvrp(num_robots, capacity)