import math

# Function to calculate Euclidean distance
def calculate_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def verify_solution(tour, total_cost):
    # Cities and their coordinates
    cities = {
        0: (3, 26),
        1: (85, 72),
        2: (67, 0),
        3: (50, 99),
        4: (61, 89),
        5: (91, 56),
        6: (2, 65),
        7: (38, 68),
        8: (3, 92),
        9: (59, 8),
        10: (30, 88),
        11: (30, 53),
        12: (11, 14),
        13: (52, 49),
        14: (18, 49),
        15: (64, 41),
        16: (28, 49),
        17: (91, 94),
        18: (51, 58),
        19: (30, 48)
    }

    # Check Requirement 1: Initial and ending point must be depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Exactly 10 cities must be visited, including the depot
    if len(set(tour)) != 10 or tour.count(0) != 2:
        return "FAIL"

    # Requirement 3: Implicitly tested by verifying the travel cost
    # Requirement 4: Already checked by other conditions (first and last city)

    # Calculate the travel cost from the tour and compare with the provided cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # Requirement 5: Check provided total travel cost
    if not math.isclose(total_cost, calculated_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Provided tour and total travel cost
tour = [0, 14, 11, 7, 3, 4, 1, 18, 19, 12, 0]
total_travel_cost = 248.03

# Verify the provided solution
result = verify_solution(tour, total_travel_cost)
print(result)  # Output either "CORRECT" or "FAIL"