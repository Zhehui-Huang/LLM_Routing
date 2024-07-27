import math

# Coordinates of each city including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Tours provided in the solution
robot_0_tour = [0, 2, 1, 18, 3, 13, 9, 5, 7, 15, 6, 0]
robot_1_tour = [0, 17, 4, 11, 14, 8, 10, 12, 16, 0]

# To calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.hypot(coordinates[city1][0] - coordinates[city2][0], coordinates[city1][1] - coordinates[city2][1])

# To compute the total travel cost for each tour
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Validation flags
validation_results = {
    "tour_exclusivity": set(),  # To check exclusivity of city visits between robots
    "correct_start_end": True,  # Each tour must start and end at the depot city
    "total_cities_visited": set()  # To ensure all cities are visited
}

# Calculate and check robot routes and costs
robot_0_cost = calculate_tour_cost(robot_0_tour)
robot_1_cost = calculate_tour_cost(robot_1_tour)
maximum_cost = max(robot_0_cost, robot_1_cost)

# Check correct start and end at the depot
validation_results["correct_start_end"] = (robot_0_tour[0] == 0 and robot_0_tour[-1] == 0 and
                                           robot_1_tour[0] == 0 and robot_1_tour[-1] == 0)

# Check that every city except the depot is visited exactly once
all_cities = set(range(1, 19))
validation_results["tour_exclusivity"].update(robot_0_tour[1:-1])
validation_results["tour_exclusivity"].update(robot_1_tour[1:-1])
validation_results["total_cities_visited"] = validation_results["tour_exclusivity"] == all_cities

# Conditional output based on validation results
if (validation_results["correct_start_end"] and
    validation_results["total_cities_visited"] and
    len(validation_results["tour_exclusivity"]) == 18):
    print("CORRECT")
else:
    print("FAIL")