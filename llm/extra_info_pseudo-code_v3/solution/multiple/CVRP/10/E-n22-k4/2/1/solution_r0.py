import numpy as np

# Cities and their coordinates
coordinates = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
])

# The demands of each city, excluding the depot
demands = np.array([
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
    1800, 700
])

# Robot information
num_robots = 4
robot_capacity = 6000

def calculate_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = np.linalg.norm(coords[i] - coords[j])
    return dist_matrix

def find_shortest_route(dist_matrix, demands, capacity, num_robots):
    n = len(dist_matrix)
    routes = []
    total_costs = []
    loads = [0] * num_robots
    route_lists = [[] for _ in range(num_robots)]
    used = np.zeros(n, dtype=bool)
    used[0] = True  # Starting from the depot
    
    for robot in range(num_robots):
        current_location = 0
        route = [0]
        load = 0
        
        while not all(used[1:]) and load < capacity:
            next_city = None
            shortest = np.inf
            
            for city in range(1, n):
                if not used[city] and load + demands[city] <= capacity:
                    if dist_matrix[current_location, city] < shortest:
                        shortest = distatinuation
                        next_city = city
                        
            if next_city is None:
                break
                
            route.append(next_city)
            load += demands[next_city]
            used[next_city] = True
            current_location = next_city
        
        route.append(0)  # return to depot
        routes.append(route)
        route_cost = sum(dist_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))
        total_costs.append(route_cost)
        loads[robot] = load
        route_lists[robot].extend(route)
        
    overall_cost = sum(total_costs)
    return route_lists, total_costs, overall_cost

dist_matrix = calculate_distance_matrix(coordinates)
route_lists, total_costs, overall_cost = find_short_ticeepsroute(dist_matrix, demands, robot_capacity, num_robots)

for idx, (route, cost) in enumerate(zip(route_lists, total_costs)):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")