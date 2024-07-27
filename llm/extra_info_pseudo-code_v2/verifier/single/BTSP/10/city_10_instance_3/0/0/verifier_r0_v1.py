import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def test_tour_solution():
    # Provided cities
    cities = [
        (84, 67),  # City 0
        (74, 40),  # City 1
        (71, 13),  # City 2
        (74, 82),  # City 3
        (97, 28),  # City 4
        (0, 31),   # City 5
        (8, 62),   # City 6
        (74, 56),  # City 7
        (85, 71),  # City 8
        (6, 76)    # City 9
    ]

    # Provided solution
    tour = [0, 1, 2, 4, 3, 9, 5, 6, 7, 8, 0]
    total_travel_cost = 379.34
    max_distance_between_cities = 68.26

    # Validate Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL - Requirement 1"

    # Validate Requirement 2: Each city visited exactly once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities) - 1 or sorted(unique_cities) != list(range(1, len(cities))):
        return "FAIL - Requirement 2"

    # Validate Requirement 5: Output tour as a list of city indices (implicitly checked by Python list format)
    
    # Validate Requirement 3, 6, 7: Correct cost and distances
    computed_total_cost = 0
    computed_max_distance = float('-inf')
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        computed_total_cost += distance
        if distance > computed_max_distance:
            computed_max_distance = distance

    if abs(computed_total_cost - total_travel_cost) > 1e-2:
        return f"FAIL - Requirement 6 (computed: {computed_total_cost})"
    
    if abs(computed_max_distance - max_distance_between_cities) > 1e-2:
        return f"FAIL - Requirement 7 (computed: {computed_max_distance})"

    return "CORRECT"

# Run the test
result = test_tour_solution()
print(result)