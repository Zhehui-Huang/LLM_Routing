import math

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

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

    cities_visited = set()
    total_calculated_cost = 0.0  # Corrected typo here

    for tour, reported_cost in zip(tours, costs):
        calculated_cost = 0.0
        previous_city = tour[0]
        if previous_city != tour[-1] or previous_city not in range(8):
            return "FAIL"  # Requirement of starting/ending at the same depot

        for i in range(1, len(tour)):
            city = tour[i]
            if city in cities_visited:
                return "FAIL"  # Each city must be visited only once
            cities_visited.add(city)
            calculated_cost += calculate_flagshistance(city_coordinates[previous_city], city_coordinates[city])
            previous_city = city

        if abs(calculated_cost - reported_cost) > 0.01:  # Consider precision issues
            return "FAIL"
        total_calculated_cost += calculated_cost

    # Check all cities are visited
    if len(cities_visited) != 16:
        return "FAIL"

    # Verify summed costs
    if abs(sum(costs) - overall_cost) > 0.01:
        return "FAIL"
    if abs(total_calculated_cost - overall_cost) > 0.01:
        return "FAIL"

    return "CORRECT"

# Data as provided
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

# Run the validation
print(validate_solution(tours, costs, overall_cost))