import numpy as np

# Coordinates and demands
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
robot_capacity = 160
num_robots = 2

# Function to compute Euclidean distance
def euclidean_distance(i, j):
    return np.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)

# Initialize data structures
num_cities = len(coords)
dist_matrix = [[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Clarke-Wright Savings Algorithm Initialization
savings = {}
for i in range(1, num_cities):
    for j in range(i + 1, num_cities):
        savings[(i, j)] = dist_matrix[0][i] + dist_matrix[0][j] - dist_matrix[i][j]

sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)

# Vehicle tours initialization
tours = {k: [0] for k in range(num_robots)}
loads = {k: 0 for k in range(num_robots)}
remaining = set(range(1, num_cities))

# Assign routes to vehicles
for (i, j), s in sorted_savings:
    if i in remaining and j in remaining:
        for robot in range(num_robots):
            if loads[robot] + demands[i] + demands[j] <= robot_capacity:
                if tours[robot][-1] == 0:  # Only extend from the depot initially
                    tours[robot].insert(-1, i)
                    tours[robot].insert(-1, j)
                    loads[robot] += (demands[i] + demands[j])
                    remaining.remove(i)
                    remaining.remove(j)
                    break

# Ensuring all cities are visited (Greedy fill for remaining cities, not optimal but fills requirement)
for city in remaining:
    for robot in range(num_robots):
        if loads[robot] + demands[city] <= robot_capacity:
            if tours[robot][-1] == city - 1:  # Append after the last city if possible
                tours[robot].insert(-1, city)
            else:
                tours[robot].append(city)
                tours[robot].append(0)  # Return to depot
            loads[robot] += demands[city]
            break

# Calculate travel cost for each robot
total_cost = 0
for robot in range(num_robots):
    cost = sum(dist_matrix[tours[robot][i]][tours[robot][i + 1]] for i in range(len(tours[robot]) - 1))
    total_cost += cost
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")