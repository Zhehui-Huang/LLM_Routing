import math

# Define the cities coordinates
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

# Function to calculate the Euclidean distance between two cities
def calculate_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Function to compute total travel cost for a tour
def total_distance(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Initial simple partitioning to generate starting solution
def generate_initial_solution():
    cities_list = list(cities.keys())[1:]  # exclude the depot
    num_robots = 4
    part_length = len(cities_list) // num_robots
    robot_tours = []

    for i in range(num_robots):
        if i == num_robots - 1:
            part = cities_list[i * part_length:]
        else:
            part = cities_list[i * part_length:(i + 1) * part_length]
        robot_tours.append([0] + part + [0])  # start and end at the depot
    
    return robot_tours

# Generate initial tours
robot_tours = generate_initial_solution()

# Report tours and calculate costs
overall_cost = 0
for idx, tour in enumerate(robot_tours):
    tour_cost = total_distance(tour)
    overall_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_constants:.2f} ")