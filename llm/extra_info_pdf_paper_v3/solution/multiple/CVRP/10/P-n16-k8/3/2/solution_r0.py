import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_distance_matrix(coords):
    size = len(coords)
    dist_matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            dist_matrix[i][j] = euclidean_distance(coords[i], coords[j])
    return dist_matrix

# Coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
robot_capacity = 35
num_robots = 8

# Compute distance matrix
distance_matrix = calculate_distance_matrix(coordinates)

# Assign cities to robots using a simple heuristic method
def simple_heuristic_assignment(coords, demands, robot_capacity, num_robots):
    assignments = [[] for _ in range(num_robots)]
    robot_loads = [0] * num_robots
    city_assigned = [False] * len(demands)
    city_assigned[0] = True  # Depot is not to be assigned

    for city in range(1, len(demands)):
        if city_assigned[city]:
            continue
        for robot in range(num_robots):
            if robot_loads[robot] + demands[city] <= robot_capacity:
                assignments[robot].append(city)
                robot_loads[robot] += demands[city]
                city_assigned[city] = True
                break

    return assignments

def calculate_tour_cost(tour, depot=0):
    total_cost = 0
    # start from depot
    current_city = depot
    for city in tour:
        total_cost += distance_matrix[current_city][city]
        current_city = city
    # return to depot
    total_cost += distance_matrix[current_city][depot]
    return total_cost
    
assignments = simple_heuristic_assignment(coordinates, demands, robot_capacity, num_robots)

# Calculate and output tour costs
overall_total_cost = 0
for i, tour in enumerate(assignments):
    tour_with_depot = [0] + tour + [0]
    cost = calculate_tour_cost(tour_with_depot)
    overall_total_cost += cost
    print(f"Robot {i} Tour: {tour_with_depot}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")