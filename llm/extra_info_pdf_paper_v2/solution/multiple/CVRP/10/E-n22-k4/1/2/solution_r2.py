import numpy as np

# City Coordinates and Demand
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Number of robots, Capacity, and Depot
num_robots = 4
capacity = 6000
depot = 0

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix calculation
n = len(coordinates)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

def generate_routes():
    routes = [[] for _ in range(num_robots)]
    capacity_remaining = [capacity] * num_robots
    demand_fulfilled = [False] * n
    demand_fulfilled[0] = True  # Depot has no demand
    
    # Sort demands by largest demand met first (greedy for demand and closer proximity to depot)
    city_indices = sorted(range(1, n), key=lambda x: (-demands[x], distance_matrix[depot][x]))
    
    for city in city_indices:
        assigned = False
        for robot_id in range(num_robots):
            if capacity_remaining[robot_id] >= demands[city] and not assigned:
                if not routes[robot_id]:
                    routes[robot_id] = [depot, city, depot]
                else:
                    routes[robot_id].insert(-1, city)
                capacity_remaining[robot_id] -= demands[city]
                demand_fulfilled[city] = True
                assigned = True

    return routes

def calculate_cost(route):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

def main():
    routes = generate_routes()
    total_cost = 0
    
    print("Tour Details:")
    for robot_id in range(num_robots):
        if routes[robot_id]:
            route_cost = calculate_cost(routes[robot_id])
            total_cost += route_cost
            print(f"Robot {robot_id} Tour: {routes[robot_id]}")
            print(f"Robot {robot_id} Total Travel Cost: {route_cost}")
    
    print(f"Overall Total Travel Cost: {total_cost}")

if __name__ == "__main__":
    main()