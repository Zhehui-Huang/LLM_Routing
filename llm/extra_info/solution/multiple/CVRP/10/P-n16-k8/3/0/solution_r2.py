import numpy as np

# Coordinates and demands of the cities (incl. depot)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Robot parameters
num_robots = 8
robot_capacity = 35

# Euclidean distance calculator
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initialize robot tours
tours = {i: [0] for i in range(num_robots)}
current_loads = {i: 0 for i in range(num_robots)}
total_costs = {i: 0 for i in range(num_robots)}

# Assign delivery tasks
undelivered = set(range(1, len(coordinates)))

def assign_city_to_robot():
    for city in sorted(undelivered, key=lambda x: demands[x], reverse=True):
        for robot in range(num_robots):
            if current_loads[robot] + demands[city] <= robot_capacity:
                last_city = tours[robot][-1]
                tours[robot].append(city)
                current_loads[robot] += demands[city]
                total_costs[robot] += euclidean_distance(last_city, city)
                undelivered.remove(city)
                break

# Perform assignment
assign_city_to_robot()

# Close all tours back to the depot
for robot in range(num_robots):
    last_city = tours[robot][-1]
    tours[robot].append(0)  # return to depot
    total_costs[robot] += euclidean_distance(last_city, 0)

# Output
overall_cost = 0
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {total_costs[robot]}")
    overall_cost += total_costs[robot]

print(f"Overall Total Travel Cost: {overall_cost}")