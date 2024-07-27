import numpy as np

# Assign city coordinates and demands
coord = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
         (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Number of robots and their capacities
num_robots = 2
robot_capacity = 160

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Constructing the distance matrix
def calculate_cost_matrix(coords):
    n = len(coords)
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            cost_matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return cost_matrix

# Clarke-Wright Savings Algorithm
def clarke_wright_savings(num_cities, depot, demands, capacity, cost_matrix):
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            if i != j:
                s_ij = cost_matrix[depot][i] + cost_matrix[depot][j] - cost_matrix[i][j]
                savings.append((s_ij, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])

    routes = [[] for _ in range(num_robots)]
    load = [0] * num_robots
    used = [False] * num_cities
    
    # Assign routes to vehicles by savings
    for save, i, j in savings:
        if not used[i] and not used[j]:
            # Find first available robot with capacity
            for r in range(num_robots):
                if load[r] + demands[i] + demands[j] <= capacity:
                    routes[r].append(i)
                    routes[r].append(j)
                    load[r] += demands[i] + demands[j]
                    used[i] = used[j] = True
                    break
    
    # Assign remaining cities singly
    for city in range(1, num_cities):
        if not used[city]:
            for r in range(num_robots):
                if load[r] + demands[city] <= capacity:
                    routes[r].append(city)
                    load[r] += demands[city]
                    used[city] = True
                    break

    # Calculating total travel cost
    def compute_route_cost(route):
        total_cost = cost_matrix[depot][route[0]] + cost_matrix[route[-1]][depot]
        for k in range(len(route) - 1):
            total_cost += cost_matrix[route[k]][route[k+1]]
        return total_cost

    total_costs = [compute_route_cost([depot] + route + [depot]) for route in routes]
    return routes, total_costs, sum(total_costs)

# Main computation
cost_matrix = calculate_cost_matrix(coord)
routes, total_costs, overall_cost = clarke_wright_savings(len(coord), 0, demands, robot_capacity, cost_matrix)

# Output results
for i, (route, cost) in enumerate(zip(routes, total_costs)):
    print(f"Robot {i} Tour: {[0] + route + [0]}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")
print(f"Overall Total Travel Calc: {overall_cost:.2f}")