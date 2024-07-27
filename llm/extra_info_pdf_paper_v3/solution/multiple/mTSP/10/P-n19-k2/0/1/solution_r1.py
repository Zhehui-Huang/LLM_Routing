import math

# Define cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Total number of robots
num_robots = 2

# Simple initial greedy splitting method
def initial_solution():
    city_ids = list(cities.keys())[1:]  # Exclude the depot initially
    tours = [[0] for _ in range(num_robots)]
    total_distances = [0] * num_robots

    # Iteratively assign cities to each robot
    for i in range(len(city_ids)):
        robot_ind = i % num_robots
        last_city = tours[robot_ind][-1]
        # Find nearest city not yet in any tour
        next_city = min((city for city in city_ids if city not in [c for t in tours for c in t]),
                        key=lambda x: calculate_distance(last_city, x))
        tours[robot_ind].append(next_city)

    # Complete each tour by returning to the depot
    for i in range(num_robots):
        tours[i].append(0)
        total_distances[i] = sum(calculate_distance(tours[i][j], tours[i][j + 1]) for j in range(len(tours[i]) - 1))

    return tours, total_distances

tours, total_distances = initial_solution()
overall_total_cost = sum(total_distances)

# Print the results
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {total_distances[robot]}")
print(f"Overall Total Travel Cost: {overall_total_cost}")