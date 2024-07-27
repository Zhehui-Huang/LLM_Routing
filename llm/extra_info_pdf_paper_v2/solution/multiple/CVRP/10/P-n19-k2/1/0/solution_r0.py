import math
from itertools import combinations

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_distance(cities[i], cities[j])
            dist_matrix[i][j] = dist
            dist_matrix[j][i] = dist
    return dist_matrix

def compute_savings(cities, depot):
    n = len(cities)
    saving_list = []
    for i in range(1, n):
        for j in range(i+1, n):
            s = dist_matrix[depot][i] + dist_matrix[depot][j] - dist_matrix[i][j]
            saving_list.append((s, i, j))
    # Sort by savings in descending order
    saving_list.sort(reverse=True, key=lambda x: x[0])
    return saving_list

def initial_solution(savings, demands, capacity):
    routes = []
    load = {}
    for _, i, j in savings:
        if demands[i] + demands[j] > capacity:
            continue
        merged = False
        for r in routes:
            if i in r and j not in r:
                if load[r]+demands[j] <= capacity:
                    r.append(j)
                    load[r] += demands[j]
                    merged = True
                    break
            elif j in r and i not in r:
                if load[r]+demands[i] <= capacity:
                    r.append(i)
                    load[r] += demands[i]
                    merged = True
                    break
        if not merged:
            routes.append([i,j])
            load[tuple(routes[-1])] = demands[i] + demands[j]
    return routes

def calculate_route_cost(route, dist_matrix):
    cost = 0
    prev_city = 0
    for city in route:
        cost += dist_matrix[prev_city][city]
        prev_city = city
    cost += dist_matrix[prev_city][0]  # return to depot
    return cost

cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
          (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

dist_matrix = create_distance_matrix(cities)
savings = compute_savings(cities, 0)

routes = initial_solution(savings, demands[1:], 160)  # demands[1:] to exclude the depot from consideration

# Insert depot to routes and calculate costs
final_routes = []
all_costs = []
total_cost = 0

for route in routes:
    full_route = [0] + route + [0]
    cost = calculate_route_cost(full_route, dist_matrix)
    total_cost += cost
    final_routes.append(full_route)
    all_costs.append(cost)

# Print results
for idx, route in enumerate(final_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {all_costs[idx]}")

print(f"Overall Total Travel Cost: {total_cost}")