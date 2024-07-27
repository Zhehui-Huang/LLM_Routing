import math

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def validate_solution(tours, costs, overall_cost):
    city_coordinates = {
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
        15: (37, 69)
    }

    # Requirement 3: All cities must be visited exactly once by the robots combined
    cities_visited = set()
    total_calculated_cost = 0.0

    for tour, reported_cost in zip(tours, costs):
        calculated_cost = 0.0
        previous_city = tour[0]

        # Starting at a depot (Requirement 4)
        if previous_city not in range(8):
            return "FAIL"

        for city in tour[1:]:
            if city in cities_visited:
                return "FAIL"  # City visited more than once
            cities_visited.add(city)
            calculated_cost += calculate_distance(city_coordinates[previous_city], city_coordinates[city])
            previous_city = city

        total_califacted_cost += round(calculated_cost, 2)
        if abs(calculated_cost - reported_cost) > 0.01:  # Account for floating point imprecision
            return "FAIL"

    # Checking if the overall calculated cost matches with the provided value
    if abs(total_califacted_cost - overall_cost) > 0.01:
        return "FAIL"

    # The number of unique cities visited should be 16
    if len(cities_visited) != 16:
        return "FAIL"

    # Overall total travel cost check
    if abs(sum(costs) - overall_cost) > 0.01:
        return "FAIL"

    return "CORRECT"

# Data from the solution
tours = [
    [0, 10, 1, 0],
    [1, 12, 3, 1],
    [2, 13, 2, 2],
    [3, 8, 7, 3],
    [4, 11, 4, 4],
    [5, 14, 5, 5],
    [6, 9, 6, 6],
    [7, 15, 0, 7]
]
costs = [41.77, 44.85, 18.11, 48.53, 14.42, 16.97, 40.05, 83.62]
overall_cost = 308.33

# Validate the tours, costs, and overall costs
print(validate_solution(tours, costs, overall_cost))