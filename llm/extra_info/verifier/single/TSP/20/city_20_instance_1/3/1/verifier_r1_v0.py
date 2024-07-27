import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour_and_cost(tour, total_cost):
    # Coordinates of cities (index correlates to city number)
    cities = [
        (14, 77),  # Depot city 0
        (34, 20),  # City 1
        (19, 38),  # City 2
        (14, 91),  # City 3
        (68, 98),  # City 4
        (45, 84),  # City 5
        (4, 56),   # City 6
        (54, 82),  # City 7
        (37, 28),  # City 8
        (27, 45),  # City 9
        (90, 85),  # City 10
        (98, 76),  # City 11
        (6, 19),   # City 12
        (26, 29),  # City 13
        (21, 79),  # City 14
        (49, 23),  # City 15
        (78, 76),  # City 16
        (68, 45),  # City 17
        (50, 28),  # City 18
        (69, 9)    # City 19
    ]

    # Requirement 1: Check if tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Check if tour visits all cities exactly once (excluding depot)
    if len(tour) != 21 or len(set(tour)) != 21:
        return "FAIL"

    # Requirement 4: Ensure tour is formatted correctly
    if not all(isinstance(city, int) and 0 <= city < len(cities) for city in tour):
        return "FAIL"

    # Calculate the journey cost to validate Requirement 3 and 5
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # Requirement 5: Check if total cost matches the computed cost
    if not math.isclose(total_cost, calculated_cost, abs_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Given solution's tour and total cost
result = verify_tour_and_cost(
    tour=[0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0],
    total_cost=477
)

print(result)