import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Provided city coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Robot tours as given
robot_tours = [
    [0, 16, 21, 17, 15, 7, 0],
    [0, 19, 14, 10, 2, 11, 0],
    [0, 20, 9, 8, 3, 4, 0],
    [0, 12, 18, 13, 6, 1, 0]
]

# Reported costs
reported_costs = [104.34, 154.26, 126.50, 132.21]
overall_reported_cost = 517.31

def verify_solution():
    # Check unique city visit requirement
    all_visited = set()
    for tour in robot_tours:
        if not all_visited.isdisjoint(tour):
            return "FAIL - Cities visited more than once."
        all_visited.update(tour[1:-1])  # Exclude the depot starts/ends which repeat
    
    if len(all_visited) != 21:  # There are 21 cities minus 1 depot
        return "FAIL - Not all cities were visited."

    # Check the cost calculations
    computed_total_cost = 0
    for index, tour in enumerate(robot_tours):
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
        computed_total_cost += tour_cost
        if not math.isclose(tour_cost, reported_costs[index], abs_tol=0.01):
            return "FAIL - Tour cost discrepancy for Robot {}: Expected {}, Got {}".format(index, reported_costs[index], round(tour_cost, 2))

    # Overall cost check
    if not math.isclose(computed_total_cost, overall_reported_cost, abs_tol=0.01):
        return "FAIL - Overall cost discrepancy: Expected {}, Got {}".format(overall_reported_cost, round(computed_total_cost, 2))

    return "CORRECT"

# Execute verification
print(verify_solution())