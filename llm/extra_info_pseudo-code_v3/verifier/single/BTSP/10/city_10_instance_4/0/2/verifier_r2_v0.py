import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_solution():
    # City coordinates
    cities = {
        0: (79, 15),
        1: (79, 55),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        7: (97, 70),
        9: (66, 62),
        8: (20, 99),
        2: (4, 80),
        6: (22, 21),
    }
    
    # Solution details
    tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
    expected_total_cost = 408.41
    expected_max_distance = 61.68
    
    # [Requirement 4] Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 1] Check if each city is visited exactly once
    if sorted(tour) != sorted(list(cities.keys()) + [0]):
        return "FAIL"

    # Calculate actual total cost and max distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    # [Requirement 5] Check total travel cost
    if not math.isclose(total_cost, expected_total_cost, abs_tol=0.1):
        return "FAIL"
    
    # [Requirement 6] Check maximum distance between consecutive cities
    if not math.isclose(max_distance, expected_max_distance, abs_tol=0.1):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Run unit tests
result = check_solution()
print(result)