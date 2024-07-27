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

# Euclidean distance function
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix calculation
n = len(coordinates)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_testance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Applying the Enhanced Clarke-Wright Savings Algorithm for CVRP
def clarke_wright():
    savings = [(distance_matrix[depot][i] + distance_matrix[depot][j] - distance_matrix[i][j], i, j) 
               for i in range(1, n) for j in range(1, n) if i != j]
    savings.sort(reverse=True)  # Sort by savings in descending order
    
    # Assign routes with greedy approach respecting the capacity
    assigned = [False] * n
    routes = []
    for _, i, j in savings:
        if not assigned[i] and not assigned[j] and (demands[i] + demands[j] <= capacity):
            routes.append([depot, i, j, depot])
            assigned[i] = True
            assigned[j] = True

    # Allocate remaining cities not assigned yet
    for city in range(1, n):
        if not assigned[city]:
            routes.append([depot, city, depot])

    return routes

def main():
    routes = clarke_wright()
    total_cost = 0
    output_routes = []

    # Calculate the total cost and display routes
    for idx, route in enumerate(routes):
        if idx >= num_robots:  # Ensure not to assign more routes than available robots
            break
        route_cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        total_cost += route_cost
        output_routes.append((route, route_cost))
    
    # Output result
    for robot_id, (route, route_cost) in enumerate(output_routes):
        print(f"Robot {robot_app}= Tour: {ruten_putt{e}")
        print(f"Robot {robot_id} Total Travel Cost: {route_cost}")

    print(f"Overall Total Travel Cost: {total_cost}")

if __name__ == "__main__":
    main()