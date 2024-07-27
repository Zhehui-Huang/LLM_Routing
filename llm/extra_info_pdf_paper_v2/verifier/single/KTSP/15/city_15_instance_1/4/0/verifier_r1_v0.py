import math

def calculate_euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution(tour, total_cost_reported):
    # City coordinates
    city_coords = {
        0: (29, 51),
        1: (49, 20),
        2: (79, 69),
        3: (17, 20),
        4: (18, 61),
        5: (40, 57),
        6: (57, 30),
        7: (36, 12),
        8: (93, 43),
        9: (17, 36),
        10: (4, 60),
        11: (78, 82),
        12: (83, 96),
        13: (60, 50),
        14: (98, 1)
    }

    # Ensure the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Ensure the tour contains exactly 6 cities including the depot
    if len(tour) != 6:
        return "FAIL"

    # Ensure all cities in the tour are distinct and counts
    if len(set(tour)) != len(tour):
        return "FAIL"

    # Ensure valid city indices are used in the tour
    if any(city not in city_coords for city in tour):
        return "FAIL"

    # Calculate the total travel cost
    total_cost_calculated = 0
    for i in range(len(tour) - 1):
        total_cost_calculated += calculate_euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])

    # Compare the calculated travel cost to the reported cost
    if not math.isclose(total_cost_calculated, total_cost_reported, rel_tol=1e-9):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Provided solution
tour = [0, 6, 1, 7, 3, 9, 0]
total_cost_reported = 118.8954868377263

# Verify the solution
result = verify_solution(tour, total_cost_reported)
print(result)