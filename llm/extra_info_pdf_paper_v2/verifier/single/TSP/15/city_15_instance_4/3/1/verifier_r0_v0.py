import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_solution(tour, total_cost_computed):
    # Define the cities coordinates
    cities = [
        (35, 40),  # Depot city 0
        (39, 41),  # City 1
        (81, 30),  # City 2
        (5, 50),   # City 3
        (72, 90),  # City 4
        (54, 46),  # City 5
        (8, 70),   # City 6
        (97, 62),  # City 7
        (14, 41),  # City 8
        (70, 44),  # City 9
        (27, 47),  # City 10
        (41, 74),  # City 11
        (53, 80),  # City 12
        (21, 21),  # City 13
        (12, 39)   # City 14
    ]

    # Requirement 1: Start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit each city exactly once (except depot which is visited twice)
    if sorted(tour) != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]:
        return "FAIL"

    # Requirement 3 and 5: Correct calculation of the total travel distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(total_cost_computed, calculated_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour_solution = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
total_travel_cost_solution = 337.8447016788252

# Run the validator
result = validate_solution(tour_solution, total_travel_cost_solution)
print(result)