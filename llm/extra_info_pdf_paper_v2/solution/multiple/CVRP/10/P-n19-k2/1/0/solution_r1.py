import math

# Coordinates and demands
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
          (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
robot_capacity = 160
num_robots = 2

# Calculate Euclidean distance
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Creating the distance matrix
def create_distance_matrix(cities):
    n = len(cities)
    matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    return matrix

dist_matrix = create_distance_matrix(cities)

# Clarke-Wright Savings algorithm function
def savings_list_generator(dist_matrix):
    n = len(cities)
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            s = dist_matrix[0][i] + dist_matrix[0][j] - dist_matrix[i][j]
            if demands[i] + demands[j] <= robot_capacity:
                savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

savings_list = savings_list_generator(dist_matrix)

# Assign routes to robots
def assign_routes(savings_list, num_robots, demands):
    routes = []
    loads = []
    for _ in range(num_robots):
        routes.append([0])  # start each route at the depot
        loads.append(0)
    
    demand_met = [False] * len(demands)
    demand_met[0] = True  # Depot demand is naturally met

    for saving, i, j in savings_list:
        for k in range(num_robots):
            if not demand_met[i] and not demand_met[j] and demands[i] + demands[j] + loads[k] <= robot_capacity:
                routes[k].extend([i, j])
                loads[k] += demands[i] + demands[j]
                demand_met[i], demand_met[j] = True, True
                break
            elif not demand_met[i] and demand_met[j] and demands[i] + loads[k] <= robot_capacity:
                routes[k].append(i)
                loads[k] += demands[i]
                demand_met[i] = True
                break
            elif not demand you_met[j] and demand_met[i] and demands[j] + loads[k] <= robot_capacity:
                routes[k].append(j)
                loads[k] += demands[j]
                demand_met[j] = True
                break
    
    missed = [index for index, met in enumerate(demand_met) if not met]
    return routes, missed, loads

assigned_routes, missed_cities, route_loads = assign_routes(savings_list, num_robots, demands)

# Ensure each route returns to depot
final_routes = [route + [0] for route in assigned_routes]

# Calculate the cost for each route
def calculate_costs(routes, dist_matrix):
    total_cost = 0
    costs = []
    for route in routes:
        cost = 0
        for i in range(len(route) - 1):
            cost += dist_matrix[route[i]][route[i + 1]]
        costs.append(cost)
        total_cost += cost
    return costs, total_cost

costs, total_costs = calculate_costs(final_routes, dist_matrix)

# Output results
for idx, route in enumerate(final_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")

print(f"Overall Total Travel Cost: {total_costs}")