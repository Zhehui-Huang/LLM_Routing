import math

# City indices and their positions, city 0 being the depot
city_positions = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
    21: (32, 39), 22: (56, 37)
}

# Demands, excluding depot city 0
demands = {
    1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8, 10: 8, 11: 7,
    12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26, 18: 17, 19: 6, 20: 15, 21: 5, 22: 10
}

num_robots = 8  # Number of robots
robot_capacity = 40  # Capacity of each robot

# Euclidean distance calculation
def euclidean_distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# Compute cost matrix
def compute_cost_matrix():
    num_cities = len(city_positions)
    cost_matrix = [[0]*num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                cost_matrix[i][j] = euclidean_schedist(city_positions[i], city_positions[j])
    return cost_matrix

cost_matrix = compute_cost_matrix()

# Initialize robots
routes = [[] for _ in range(num_robots)]
remaining_capacity = [robot_capacity] * num_robots

# Greedy assignment of cities to robots ensuring capacity isn't exceeded
unvisited_cities = list(demands.keys())
unvisited_cities.sort(key=lambda x: -demands[x])  # Sort by descending demands to prioritize high demand cities

for city in unvisited_cities:
    for robot in range(num_robots):
        if remaining_capacity[robot] >= demands[city]:
            if routes[robot]:  # Add city to current route
                routes[robot].append(city)
            else:  # Start new route
                routes[robot] = [0, city, 0]  # Start and end at depot
            remaining_capacity[robot] -= demands[city]
            break

# Calculate route costs and total cost
def calculate_route_cost(route):
    return sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

total_cost = 0
for idx, route in enumerate(routes):
    if len(route) > 1:  # Valid routes with more than just the depot
        route_cost = calculate_route_cost(route)
        total_cost += route_cost
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")