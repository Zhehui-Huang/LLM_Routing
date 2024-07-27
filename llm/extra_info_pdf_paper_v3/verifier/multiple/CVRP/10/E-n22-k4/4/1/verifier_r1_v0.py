import math

# Given Coordinates and Demands Data
cities_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
            600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
            1800, 700]

# Solution provided
tours = [
    [0, 14, 16, 17, 20, 21, 8, 0],
    [0, 12, 15, 18, 19, 6, 0],
    [0, 13, 11, 10, 9, 7, 2, 3, 0],
    [0, 5, 1, 4, 0]
]
tour_costs = [135.63, 163.95, 165.66, 124.18]
robot_capacity = 6000

# Calculating Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities_coordinates[city1][0] - cities_coordinates[city2][0]) ** 2 +
                     (cities_coordinates[city1][1] - cities_coordinates[city2][1]) ** 2)

# Function to verify each robot tour
def verify_solution(tours, tour_costs, demands, robot_capacity):
    total_calculated_cost = 0
    demands_fulfilled = [0] * len(demands)

    for robot, tour in enumerate(tours):
        cost_acc = 0
        current_load = 0

        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # robot must start and end at depot 0

        for i in range(len(tour) - 1):
            from_city = tour[i]
            to_city = tour[i + 1]
            cost_acc += euclidean_distance(from_city, to_city)
            if i > 0:  # skip the depot for load counting
                current_load += demands[tour[i]]

        if current_load > robot_capacity:
            return "FAIL"  # load exceeds capacity

        for city in tour:
            if city != 0:
                demands_fulfilled[city] += demands[city]

        # Compare calculated route costs to provided ones
        if not math.isclose(cost_acc, tour_costs[robot], rel_tol=0.05):  # allowing small precision tolerance
            return "FAIL"

        total_calculated_cost += cost_acc

    # Check if all demands are exactly met
    if any(demand != fulfilled for demand, fulfilled in zip(demands, demands_fulfilled)):
        return "FAIL"

    # Compare overall costs
    if not math.isclose(total_calculated_cost, sum(tour_costs), rel_tol=0.05):
        return "FAIL"

    return "CORRECT"

# Validate the solution and print the result
result = verify_solution(tours, tour_costs, demands, robot_capacity)
print(result)