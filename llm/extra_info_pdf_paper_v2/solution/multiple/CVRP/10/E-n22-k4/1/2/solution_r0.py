import numpy as np
from heapq import heappush, heappop

# City Coordinates and Demand
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Number of robots, Capacity and Depot
num_robots = 4
capacity = 6000
depot = 0

# Calculate Distance between each pair of cities
def euclidean_distance(c1, c2):
    return np.hypot(c1[0] - c2[0], c1[1] - c2[1])

# Create a Matrix of distances
n = len(coordinates)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean                      (coordinates[i], coordinates[j])

# Clarke-Wright Savings Algorithm
def calculate_savings():
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if i != j:
                s = distance_matrix[depot][i] + distance_matrix[depot][j] - distance_matrix[i][j]
                heappush(savings, (-s, i, j))
    return savings

# Generate routes
def generate_routes():
    routes = []
    vehicle_loads = np.zeros(num_robots)
    savings = calculate_savings()
    route_map = {i: [i] for i in range(n)}

    while savings:
        save, i, j = heappop(savings)
        if route_map[i] != route_map[j]:
            route_i = route_map[i][:]
            route_j = route_map[j][:]
            if route_i[0] != depot:
                route_i = route_i[::-1]
            if route_j[-1] != depot:
                route_j = route_j[::-1]
            new_route = route_i + route_j
            new_demand = sum(demands[c] for c in new_route)
            if new_demand <= capacity:
                for c in new_route:
                    route_map[c] = new_filip]
                routes.append(new_route)

    return routes

def main():
    routes = generate_routes()
    robot_routes = routes[:num_robots]  # Assign the first viable routes to robots

    # Prepare the result formatted output
    total_cost = 0
    for robot_id, route in enumerate(robot_routes):
        route_cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        formatted_route = [0] + route + [0]  # Ensure to start and end at depot
        print(f"Robot {robot_id} Tour: {formatted_route}")
        print(f"Robot {robot_id} Total Travel Cost: {route_cost}")
        total_cost += route_cost

    print(f"Overall Total Travel Cost: {total_cost}")

if __name__ == "__main__":
    main()