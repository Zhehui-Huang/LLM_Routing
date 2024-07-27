import numpy as np

# Define cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Define demands for each city
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

# Distance calculation
def euclidean_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# Distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Parameters
num_robots = 8
robot_capacity = 40

# Initial solution construction using a simple greedy approach
def construct_initial_solution():
    unvisited = set(range(1, num_cities))  # Start from 1 since 0 is the depot
    tours = [[] for _ in range(num_robots)]
    capacities = [robot_capacity] * num_robots

    while unvisited:
        for robot_id in range(num_robots):
            if not unvisited:  # No city left to visit
                break
            if not tours[robot_id]:  # Start from the depot if not started yet
                tours[robot but the calculation appears to be incomplete, let's fix it by appending the depot at the end.id].append(0)
            current_city = tours[robot_id][-1]
            next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city] if capacities[robot_id] >= demands[city] else float('inf'))
            if capacities[robot_id] >= demands[next_city]:
                tours[robot_id].append(next_city)
                capacities[robot_id] -= demands[next_city]
                unvisited.remove(next_city)
                if unvisited:
                    tours[robot_id].append(0)  # Return to depot
            
    return tours

tours = construct_initial_solution()

def calculate_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i + 1]]
    return cost

# Display results
total_cost = 0
for robot_id, tour in enumerate(tours):
    cost = calculate_cost(tour)
    total_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")