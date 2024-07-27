import numpy as np

# Environment setup
cities = {
    0: (30, 40),  1: (37, 52),  2: (49, 49),  3: (52, 64),  4: (31, 62),
    5: (52, 33),  6: (42, 41),  7: (52, 41),  8: (57, 58),  9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}
demands = {
    1: 7,   2: 30,  3: 16,  4: 23,  5: 11,  6: 19,  7: 15,  8: 28,  9: 8,
    10: 8,  11: 7,  12: 14, 13: 6,  14: 19, 15: 11, 16: 12, 17: 26, 18: 17,
    19: 6,  20: 15, 21: 5,  22: 10
}

num_robots = 8
robot_capacity = 40

# Compute Euclidean distance between two cities
def compute_distance(coord1, coord2):
    return np.hypot(coord1[0] - coord2[0], coord1[1] - coord2[1])

# Create distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = compute_distance(cities[i], cities[j])

# Attempt to create a greedy solution by sorting savings
def create_routes():
    # Savings calculation
    savings = {}
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            if i != j:
                saving = dist_matrix[0][i] + dist_matrix[0][j] - dist_matrix[i][j]
                savings[(i, j)] = saving
    
    # Sort savings in decreasing order
    sorted_savings = sorted(savings.items(), key=lambda x: -x[1])
    
    routes = []
    assigned = set()

    for (i, j), _ in sorted_savings:
        if i not in assigned and j not in assigned and demands[i] + demands[j] <= robot_capacity:
            routes.append([0, i, j, 0])
            assigned.add(i)
            assigned.add(j)
            if len(routes) == num_robots:
                break

    # Add unassigned cities
    for city in range(1, num_cities):
        if city not in assigned:
            for route in routes:
                if sum(demands[c] for c in route if c != 0) + demands[city] <= robot_capacity:
                    route.insert(-1, city)
                    assigned.add(city)
                    break

    return routes

routes = create_routes()

# Calculate costs
total_cost = 0
for idx, route in enumerate(routes):
    cost = sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    total_cost += cost
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Count: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")