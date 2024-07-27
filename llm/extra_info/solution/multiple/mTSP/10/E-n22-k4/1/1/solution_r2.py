import math

# Coordinates for the cities
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to compute total distance for a tour
def total_distance(tour):
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Function to generate initial naive partitioning solution
def generate_initial_solution():
    cities_list = list(cities.keys())[1:]  # exclude the depot city
    num_robots = 4
    part_len = len(cities_list) // num_robots
    robot_tours = []
    
    for i in range(num_robots):
        part = cities_list[i * part_len: (i + 1) * part_len if (i + 1) * part_len < len(cities_list) else None]
        robot_tours.append([0] + part + [0])  # start and end at the depot

    return robot_tours

robot_tours = generate_initial_solution()
overall_total_cost = 0

# Report and calculate
for idx, tour in enumerate(robot_tours):
    tour_cost = total_distance(tour)
    overall_total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")