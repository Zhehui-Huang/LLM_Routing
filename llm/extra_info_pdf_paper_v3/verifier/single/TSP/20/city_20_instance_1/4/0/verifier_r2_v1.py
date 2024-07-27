import math

# List of cities with coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85),
    11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23),
    16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Provided solution
given_tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
given_total_cost = 477.05

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_tour_requirements(tour, expected_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour doesn't start and end at depot city 0."
    
    visited_cities = tour[1:-1]  # exclude the start/end depot city
    if sorted(visited_cities) != list(range(1, 20)):
        return False, "Not all cities are visited exactly once."

    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(total_cost, expected_cost, abs_tol=1e-2):
        return False, f"Calculated total cost {total_cost:.2f} does not match given cost {expected_cost:.2f} within tolerance."

    return True, "Tour satisfies all requirements."

result, message = check_tour_requirements(given_tour, given_total_cost)
print("CORRECT" if result else "FAIL", message)