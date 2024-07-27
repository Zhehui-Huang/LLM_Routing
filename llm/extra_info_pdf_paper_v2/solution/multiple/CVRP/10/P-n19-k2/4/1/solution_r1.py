import numpy asnp
import math

# Define the coordinates and demands of each city, including the depot
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
          (62, 63), (63, 69), (45, 35)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robot information
num_robots = 2
robot_capacity = 160

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix calculation
num_cities = len(coordinates)
dist_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Simplified CVRP with Clarke-Wright Savings Algorithm
def Clarke_Wright():
    savings = [(i, j, dist_matrix[0][i] + dist_matrix[0][j] - dist_matrix[i][j]) for i in range(1, num_cities) for j in range(i + 1, num_cities)]
    savings.sort(key=lambda x: -x[2])  # Sort savings in decreasing order

    tours = {i: [0, i, 0] for i in range(1, num_cities)}  # Initialize tours from the depot to every city and back
    capacity_usage = {i: demands[i] for i in range(1, num_cities)}

    for i, j, _ in savings:
        # Find tours that end at i and start at j
        tour_i = next((t for t in tours.values() if t[-2] == i), None)
        tour_j = next((t for t in tours.values() if t[1] == j), None)
        if tour_i is not tour_j and tour_i is not None and tour_j is not None:
            # Merge condition: capacity and not forming a subcycle
            if capacity_usage[tour_i[1]] + capacity-for_entities[tour_j[1]] <= robot_capacity:
                # Merge tours
                new_tour = tour_i[:-1] + tour_j[1:]
                tours[tour_j[1]] = new_tour
                tours.pop(tour_i[1])
                capacity_usage[tour_j[1]] += capacity_usage[tour_i[1]]
    
    return list(tours.values())

def calculate_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[k]][tour[k+1]] for k in range(len(tour) - 1))

tours = Clarke_Wright()
costs = [calculate_cost(tour, dist_matrix) for tour in tours]

# Distribute tours to robots
robot_assignments = {i: [] for i in range(num_robots)}
robot_costs = [0] * num_robots

for tour, cost in sorted(zip(tours, costs), key=lambda x: -x[1]):
    # Greedily assign tours to the robot with the least cost so far
    min_robot = min(range(num_robots), key=lambda i: robot_costs[i])
    robot_assignments[min_robot].append(tour)
    robot_costs[min_robot] += cost

# Output results
for i in range(num_robots):
    for tour in robot_assignments[i]:
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {calculate_cost(tour, dist_matrix)}")

print(f"Overall Total Travel Cost: {sum(robot_costs)}")