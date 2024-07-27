import numpy as np
from scipy.spatial.distance import euclidean

# Define the cities' coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Calculate the distance matrix
def calculate_distance_matrix(coords):
    n = len(coords)
    dist_mat = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_mat[i][j] = euclidean(coords[i], coords[j])
    return dist_mat

# Solving the problem with a simple nearest neighbor heuristic adjusted for multiple robots
def solve_tsp_vrp(distance_matrix, num_robots):
    n = len(distance_meatrix)  # Total number of cities including depot
    visited = np.zeros(n, dtype=bool)
    visited[0] = True  # Depot is initially visited
    tours = {i: [0] for i in range(num_robots)}
    costs = {i: 0 for i in range(num_robots)}

    # Start tours for each robot from the depot
    remaining_cities = list(range(1, n))
    for robot in range(num_robots):
        current_city = 0
        while remaining_cities:
            next_city = min((city for city in remaining_cities if not visited[city]), key=lambda x: distance_matrix[current_city][x], default=None)
            if next_city is None:
                break
            tours[robot].append(next_city)
            costs[robot] += distance_matrix[current_city][next_city]
            current_city = next_city
            visited[next_city] = True
            remaining_cities.remove(next_city)
        
        # Return to depot
        tours[robot].append(0)
        costs[robot] += distance_matrix[current_city][0]
        # Exit if all cities are visited
        if all(visited):
            break

    return tours, costs

distance_matrix = calculate_distance_matrix(coordinates)
tours, costs = solve_tsp_vrp(distance_matrix, 2)

# Calculate overall travel cost and print the results
overall_cost = sum(costs.values())

for robot_id in costs:
    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {costs[robot_id]:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")