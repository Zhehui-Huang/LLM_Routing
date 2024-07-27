import math

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
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
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Given tours and costs
robot0_tour = [0, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 0]
robot0_cost = 109.8362166450987
robot1_tour = [1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 1]
robot1_cost = 117.2226527159768
total_cost_reported = 227.0588693610755

# Define functions to calculate distance and validate tours
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclideanDistance(cities[tour[i]], cities[tour[i+1]])
    return cost

def validate_solution():
    # Check if robots start and end at their respective depots
    if robot0_tour[0] != 0 or robot0_tour[-1] != 0:
        return "FAIL"

    if robot1_tour[0] != 1 or robot1_tour[-1] != 1:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    all_visited_cities = set(robot0_tour[1:-1] + robot1_tour[1:-1])  # Excude depots from outer set
    if len(all_visited_cities) != 20 or any(city not in all_visited_cities for city in range(2, 21)):
        return "FAIL"
    
    # Check if the total cost is minimized (cumulative cost calculation and verification)
    calculated_cost0 = calculate_tour_cost(robot0_tour)
    calculated_cost1 = calculate_tour_cost(robot1_tour)
    calculated_total_cost = calculated_cost0 + calculated_cost1

    if not math.isclose(calculated_cost0, robot0_cost, abs_tol=1e-7) or not math.isclose(calculated_cost1, robot1_cost, abs_tol=1e-7):
        return "FAIL"
    
    # Check the total cost side
    if not math.isclose(calculated_total_cost, total_cost_reported, abs_tol=1e-7):
        return "FAIL"
    
    return "CORRECT"

# Unit test execution
print(validate_solution())