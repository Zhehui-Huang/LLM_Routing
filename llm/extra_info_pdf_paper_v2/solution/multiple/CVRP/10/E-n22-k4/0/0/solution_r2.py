import numpy as np

# Constants and setup information
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200,
           1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
num_robots = 4
robot_capacity = 6000

def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Varibles to hold routes and distance mappings
routes = [[] for _ in range(num_robots)]
current_loads = [0] * num_robots
overall_distance = 0

# Implement greedy solution part (Clarke-Wright enhancements could be simulated with better data handling)
# Start each robot tour from the depot and initially assign as per least distances and not exceeding capacities
distances = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]
assigned = [False] * len(coordinates)
assigned[0] = True  # Depot is always assigned (and visited by all)

for robot in range(num_robots):
    current_location = 0
    while True:
        next_city = None
        min_distance = float('inf')
        for i in range(1, len(coordinates)):
            if not assigned[i] and current_loads[robot] + demands[i] <= robot_capacity:
                if distances[current_location][i] < min_distance:
                    min_distance = distances[current_location][i]
                    next_city = i
        if next_city is None:
            break
        # "Visit" this city
        routes[robot].append(next_city)
        current_loads[robot] += demands[next_city]
        assigned[next_city] = True
        overall_distance += min_distance
        current_location = next_city
        
    # Close the tour returning to the depot
    if routes[robot]:
        overall_distance += distances[current_location][0]
        routes[robot].insert(0, 0)
        routes[robot].append(0)

# Output the results
for idx, route in enumerate(routes):
    if route:
        route_distance = sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {route_distance:.2f}")

print(f"Overall Total Travel Cost: {overall_distance:.2f}")