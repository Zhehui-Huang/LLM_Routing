import math

# Coordinates of the cities including the depot (index 0)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Demand of each city including the depot (index 0)
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

# Number of robots and capacity
num_robots = 8
capacity_per_robot = 40

def euclidean_distance(c1, c2):
    """Compute Euclidean Distance between two coordinates."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Initialize tours and capacity tracker
tours = [[] for _ in range(num_robots)]
current_capacity = [0] * num_robots
current_location = [0] * num_robots  # starting at the depot for all robots
total_cost = [0] * num_robots
visited = set()

# Function to find the next city
def find_next_city(current_city, current_cap):
    min_dist = float('inf')
    next_city = None
    for i in range(1, len(coordinates)):  # skip the depot
        if i not in visited and demands[i] <= (capacity_per_robot - current_cap):
            dist = euclidean_distance(coordinates[current_city], coordinates[i])
            if dist < min_dist:
                min_dist = dist
                next_city = i
    return next_city, min_dist

# Assign cities to robots
for robot_id in range(num_robots):
    start_city = 0
    tours[robot_id].append(start_city)
    while True:
        next_city, dist = find_next_city(current_location[robot_id], current_capacity[robot_id])
        if next_city is None:
            break  # No next city found, or no capacity left, return to depot
        visited.add(next_city)
        tours[robot_id].append(next_city)
        current_location[robot_id] = next_city
        current_capacity[robot_id] += demands[next_city]
        total_cost[robot_id] += dist
    # Return to depot
    return_to_depot = euclidean_distance(coordinates[current_location[robot_id]], coordinates[0])
    total_cost[robot_id] += return_to_depot
    tours[robot_id].append(0)  # end tour by returning to the depot

# Output results
overall_total_cost = sum(total_cost)
for robot_id in range(num_robots):
    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {total_cost[robot_id]}")
print(f"Overall Total Travel Cost: {overall_total_cost}")