import math

# ----------------------------------------------------------
# City Coordinates and Demands
# ----------------------------------------------------------
cities = {
    0: (30, 40, 0),
    1: (37, 52, 7),
    2: (49, 49, 30),
    3: (52, 64, 16),
    4: (31, 62, 23),
    5: (52, 33, 11),
    6: (42, 41, 19),
    7: (52, 41, 15),
    8: (57, 58, 28),
    9: (62, 42, 8),
    10: (42, 57, 8),
    11: (27, 68, 7),
    12: (43, 67, 14),
    13: (58, 48, 6),
    14: (58, 27, 19),
    15: (37, 69, 11),
    16: (38, 46, 12),
    17: (61, 33, 26),
    18: (62, 63, 17),
    19: (63, 69, 6),
    20: (45, 35, 15)
}

# Number of robots and robot capacity
num_robots = 2
robot_capacity = 160

# ----------------------------------------------------------
# Function to calculate Euclidean distance between two cities
# ----------------------------------------------------------
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Compute distance matrix
n = len(cities)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# ----------------------------------------------------------
# Greedy Solution Construction
# ----------------------------------------------------------
def greedy_solution():
    robots_routes = [[] for _ in range(num_robots)]
    demands_remaining = [cities[i][2] for i in range(n)]
    current_locations = [0] * num_robots
    loads = [0] * num_robots
    
    remaining_cities = set(range(1, n))
    
    while remaining_cities:
        for robot in range(num_robots):
            if not remaining_cities:
                break
            
            next_city = None
            min_dist = float('inf')
            
            for city in remaining_cities:
                if loads[robot] + demands_remaining[city] <= robot_capacity:
                    dist = distance_matrix[current_locations[robot]][city]
                    if dist < min_dist:
                        min_dist = dist
                        next_city = city
                        
            if next_city is not None:
                robots_routes[robot].append(next_city)
                loads[robot] += demands_remaining[next_city]
                demands_remaining[next_city] = 0
                current_locations[robot] = next_city
                remaining_cities.remove(next_city)
    
    # Closing the routes to the depot
    for robot in range(num_robots):
        robots_routes[robot].insert(0, 0) # Start from depot
        robots_routes[robot].append(0) # Return to depot

    return robots_routes, loads

# ----------------------------------------------------------
# Calculate route costs and output the solution
# ----------------------------------------------------------
def calculate_route_cost(route):
    cost = 0
    for i in range(1, len(route)):
        cost += distance_matrix[route[i-1]][route[i]]
    return cost

routes, loads = greedy_solution()
total_cost = 0

for i, route in enumerate(routes):
    cost = calculate_route_cost(route)
    total_cost += cost
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel budongbiost: {total_cost}")