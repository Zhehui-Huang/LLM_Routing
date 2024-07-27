import math

# Define the city coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Creating the distance matrix
distance_matrix = [[calculate_distance(i, j) for j in range(len(cities))] for i in range(len(cities))]

# Helper function to perform a greedy TSP solving approach
def solve_tsp_greedy(distance_matrix):
    n = len(distance_matrix)
    unvisited = set(range(1, n))
    tour = [0]
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: distance_matrix[last][x])
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(0)
    return tour

# Solve the TSP
tour = solve_tsp_greedy(distance_matrix)

# Assign tours to robots
num_robots = 4
split_tours = [[] for _ in range(num_robots)]
tour_length = len(tour)
part_length = (tour_length - 2) // num_robots

# Divide tours by assigning parts to each robot, ensuring start and end at the depot
start_index = 1
for i in range(num_robots):
    split_tours[i] = [0] + tour[start_index:start_index + part_length] + [0]
    start_index += part_length

# Adding residue cities to the last robot if any
split_tours[-1] += tour[start_index:-1]

# Calculate travel costs
def calculate_travel_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

costs = [calculate_travel_cost(robot_tour, distance_matrix) for robot_tour in split_tours]
max_travel_cost = max(costs)

# Print the results
for i, robot_tour in enumerate(split_tours):
    print(f"Robot {i} Tour: {robot_tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]:.2f}")

print(f"Maximum Travel Cost: {max_travel_cost:.2f}")