import math

# City data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8,
    8, 7, 14, 6, 19, 11, 12, 26, 17, 6,
    15, 5, 10
]

# Robot data
num_robots = 8
robot_capacity = 40
depot = 0

# Helper function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Assign robots to cities using a simple greedy approach (initial feasible solution)
routes = [[] for _ in range(num_robots)]
loads = [0] * num_robots
city_assignment = [False] * len(coordinates)

for robot_id in range(num_robots):
    current_city = depot
    route = [current_city]
    while True:
        nearest_city = None
        min_distance = float('inf')
        for city in range(1, len(coordinates)):  # Start from 1 to skip depot
            if not city_assignment[city] and loads[robot_id] + demands[city] <= robot_capacity:
                if distance_matrix[current_city][city] < min_distance:
                    nearest_city = city
                    min_distance = distance_matrix[current_city][city]

        if nearest_city is None:
            break

        route.append(nearest_city)
        city_assignment[nearest_city] = True
        loads[robot_id] += demands[nearest_city]
        current_city = nearest_city

    route.append(depot)
    routes[robot_id] = route

    if all(city_assignment[1:]):  # Check if all cities are covered
        break

# Calculate total and individual travel costs
def calculate_cost(route):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

individual_costs = [calculate_cost(route) for route in routes]
total_cost = sum(individual_costs)

# Output the results
for idx, (route, cost) in enumerate(zip(routes, individual_costs)):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")