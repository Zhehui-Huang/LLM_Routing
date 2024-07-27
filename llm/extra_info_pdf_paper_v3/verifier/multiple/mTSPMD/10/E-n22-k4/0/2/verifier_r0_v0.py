import math

# Define the cities' coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Given solution tours and costs for verification
given_tours = {
    0: ([0, 21, 19, 13, 11, 0], 111.12),
    1: ([1, 6, 8, 10, 9, 5, 7, 12, 15, 18, 20, 17, 16, 14, 1], 219.69),
    2: ([2, 2], 0.00),
    3: ([3, 4, 3], 5.66)
}

overall_cost_given = 336.47

# Unit tests
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def test_tours_and_costs():
    all_visited = set()
    total_calculated_cost = 0.0

    for robot, (tour, cost_given) in given_tours.items():
        previous_city = tour[0]
        total_robot_cost = 0.0
        for city in tour[1:]:
            distance = calculate_distance(previous_city, city)
            total_robot_cost += distance
            previous_city = city
            if city != tour[0]:
                all_visited.add(city)

        # Check if round-off errors within a reasonable range +/- 0.01
        if not (abs(total_robot_cost - cost_given) <= 0.01):
            return "FAIL"

        total_calculated_cost += total_robot_cost

    # Requirements 2 and 3: All cities visited exactly once and total cost checking
    if all_visited != set(range(4, 22)) or abs(total_calculated_cost - overall_cost_given) > 0.01:
        return "FAIL"

    # Check if the format of output could be validated: Requirement 4 is more about format.
    
    # Requirement 1 - whether depot starting/ending is validated within tours input:
    for robot, (tour, _) in given_tours.items():
        if tour[0] != tour[-1] or tour[0] != robot:
            return "FAIL"

    # Requirement 5 is about genetic algorithm strategy, which isn't directly verifiable by output.
    
    return "CORRECT"

# Running and checking the tests
print(test_tours_and_costs())