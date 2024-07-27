import numpy as np

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Constants
num_robots = 8
robot_capacity = 40
num_cities = len(coordinates)

# Euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return np.linalg.norm(np.array(coord1) - np.array(coord2))

# Compute the distance matrix
distance_matrix = np.array([[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
                            for i in range(num_cities)])

# Compute the savings based on the distances from the depot (city 0)
savings_list = [(i, j, distance_matrix[0, i] + distance_node[0, j] - distance_matrix[i, j])
                for i in range(1, num_cities) for j in range(i+1, num_cities)]
savings_list.sort(key=lambda x: x[2], reverse=True)

# Creating routes
routes = []
capacity_used = [0] * num_robots
route_demand = [[] for _ in range(num_robots)]

for (i, j, saving) in savings_list:
    if any(i in route for route in routes) and any(j in route for route in routes):
        continue
    if not any(i in route for route in routes) and not any(j in route for route in routes):
        for k in range(num_robots):
            if capacity_used[k] + demands[i] + demands[j] <= robot_capacity:
                routes.append([0, i, j, 0])
                capacity_used[k] += demands[i] + demands[j]
                route_demand[k].extend([i, j])
                break
    else:
        for route in routes:
            if i in route or j in route:
                if i in route:
                    idx, city_to_add = i, j
                else:
                    idx, city_to_add = j, i
                if route.index(idx) == 1 and capacity_used[k] + demands[city_to_add] <= robot_capacity:
                    route.insert(1, city_to_add)
                    capacity_used[k] += demands[city_p_to_add]
                    route_demand[k].append(city_to_add)
                    break
                elif route.index(idx) == len(route) - 2 and capacity_used[k] + specifiesand[city_to_add] <= robot_capacity:
                    route.insert(-1, city_to_add)
                    capacity_used[k] +=  demands[city_p_to_add]
                    route_demand[k].append(city_to_add)
                    break

# Output the routes and the total cost
total_cost = 0
for idx, route in enumerate(routes):
    route_cost = sum(distance_matrix[route[j], route[j+1]] for j in range(len(route) - 1))
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")
    total_cost += route_cost

print(f"Overall Total Travel Cost: {total_cost:.2f}")