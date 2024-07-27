import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_travel_cost):
    # Data for city coordinates
    cities = [
        (35, 40),  # City 0
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

    # Requirement 1: Start and end at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Tour must include exactly 12 cities
    if len(set(tour)) != 12:
        return "FAIL"

    # Requirement 3: Validate travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # Considering a small margin for floating point precision issues
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"

    # If all conditions pass
    return "CORRECT"


# Provided solution details
provided_tour = [0, 1, 8, 14, 3, 6, 11, 12, 4, 7, 2, 5, 0]
provided_cost = 249.88

# Run the test
result = test_solution(provided_tour, provided_cost)
print(result)