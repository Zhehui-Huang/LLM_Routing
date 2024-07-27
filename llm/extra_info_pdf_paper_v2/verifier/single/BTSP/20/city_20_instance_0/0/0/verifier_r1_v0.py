import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    solution = {
        'Tour': [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0],
        'Total travel cost': 349.2,
        'Maximum distance between consecutive cities': 32.39
    }

    cities = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
        (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
        (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
    ]
    
    tour = solution['Tour']
    total_cost = solution['Total travel'.replace(' ', '_') + '_cost']
    max_dist = solution['Maximum_distance_between_consecutive_cities'.replace(' ', '_')]

    # Requirement 1: Check if all cities are visited exactly once and start/end at depot (city 0)
    if sorted(tour[:-1]) != list(range(20)):
        return "FAIL"

    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 3: Check output format indirectly by the keys and data types
    if 'Tour' not in solution or 'Total travel cost' not in solution or 'Maximum distance between consecutive cities' not in solution:
        return "FAIL"
    
    # Calculate actual total cost and maximum distance
    actual_total_cost = 0
    actual_max_dist = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        actual_total_cost += dist
        if dist > actual_max_dist:
            actual_max_dist = dist
    
    # Compare calculated total cost and maximum distance with provided solution
    if not (abs(actual_total_cost - total_cost) < 1e-1 and abs(actual_max_dist - max_dist) < 1e-1):
        return "FAIL"
    
    return "CORRECT"

# Execute the test
print(test_solution())