import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        x1, y1 = coordinates[tour[i-1]]
        x2, y2 = coordinates[tour[i]]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    return total_cost

def check_solution():
    coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
        6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
        18: (62, 63), 19: (63, 69), 20: (45, 35)
    }

    tours = [
        [0, 20, 5, 14, 9, 2, 19, 4, 11, 1, 16, 0],
        [1, 10, 3, 18, 8, 13, 17, 7, 6, 0, 15, 12, 1]
    ]

    expected_costs = [161.1973946059796, 148.14160770216228]
    expected_total_cost = 309.33900230814186

    all_cities_visited = set(range(21))
    cities_visited = set()

    # Validate robots visit all cities exactly once
    for tour in tours:
        cities_visited.update(tour)

        # Include a check for tours starting at their initial depot and ending at a depot
        if not (tour[0] in [0, 1] and tour[-1] in [0, 1]):
            return "FAIL"

    # Check expected travel costs
    actual_costs = [calculate_total_travel_cost(tour, coordinates) for tour in tours]
    actual_total_cost = sum(actual_rossts)

    if cities_visited != all_cities_visited:
        return "FAIL"

    # Check if calculated and expected tour costs are within a tiny floating point tolerance
    if not all(abs(actual - expected) < 1e-6 for actual, expected in zip(actual_costs, expected_costs)):
        return "FAIL"
    
    # Check the total travel cost
    if not abs(actual_total_cost - expected_total_cost) < 1e-6:
        return "FAIL"

    return "CORRECT"

# Run the check function and print the result
print(check_solution())