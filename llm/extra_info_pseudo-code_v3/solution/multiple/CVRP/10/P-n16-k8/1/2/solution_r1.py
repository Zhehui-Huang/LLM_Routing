import math

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Network informations
num_robots = 8
robot_capacity = 35

# Function to calculate Euclidean distance
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Find initial feasible solution
def build_initial_solution():
    routes = [[] for _ in range(num_robots)]
    capacity_remaining = [robot_capacity for _ in range(num_robots)]
    city_visited = [False] * len(coordinates)
    city_visited[0] = True  # Depot is always considered visited

    for robot in range(num_robots):
        route = [0]  # start with depot
        current_city = 0
        while True:
            next_city = None
            min_distance = float('inf')
            for city in range(1, len(coordinates)):
                if not city_visited[city] and demands[city] <= capacity_remaining[robot]:
                    if distance_matrix[current_city][city] < min_distance:
                        min_distance = distance_matrix[current_city][city]
                        next_city = city
            if next_city is None:
                break
            route.append(next_city)
            city_visited[next_city] = True
            capacity_remaining[robot] -= demands[next_city]
            current_city = next_city
        route.append(0)  # end with depot
        routes[robot] = route
    return routes

# Calculate the travel cost for each route
def calculate_route_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += distance_matrix[route[i]][route[i+1]]
    return total_cost

# Main execution
routes = build_initial_solution()
total_cost = 0

# Output the result
print("Resulting Tours:")
for index, route in enumerate(routes):
    if len(route) > 2:  # More than just depot to depot
        route_cost = calculate_route_cost(route)
        total_cost += route_cost
        print(f"Robot {index} Tour: {route}")
        print(f"Robot {index} Total Travel Cost: {round(route_cost, 2)}")

print(f"\nOverall Total Travel Cost: {round(total_cost, 2)}")