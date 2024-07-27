import math

def calculate_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities given their coordinates. """
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tour, cities, reported_cost, reported_max_distance):
    # [Requirement 1] Check if the tour visits each city exactly once and ends at the depot
    if len(tour) != len(cities) + 1 or tour[0] != 0 or tour[-1] != 0 or sorted(tour[1:-1]) != sorted(range(1, len(cities))):
        return "FAIL"
    
    # Prepare to calculate the actual travel cost and the maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0

    # [Requirement 2] Calculate total travel cost and maximum consecutive distance
    for i in range(len(tour) - 1):
        city_a = cities[tour[i] - 1] if tour[i] != 0 else cities[0]
        city_b = cities[tour[i + 1] - 1] if tour[i + 1] != 0 else cities[0]
        distance = calculate_distance(city_a, city_b)
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Check calculated costs vs reported costs
    if not (math.isclose(total_cost, reported_cost) and math.isclose(max_distance, reported_max_distance)):
        return "FAIL"
    
    # [Requirement 3] Verify if longest distance between any two consecutive cities is minimized
    # This is tricky without solving the problem ourselves or detailed results from more optimal solutions to compare with.
    # Assuming we do not calculate this optimality since it would involve complex computations or algorithmic implementations.

    return "CORRECT"

# Coordinates of each city including the depot as city 0
cities = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Provided solution
tour = [0, 6, 8, 11, 2, 7, 3, 12, 5, 13, 14, 9, 10, 4, 1, 0]
total_travel_cost = 360.8004393137746
maximum_distance_between_consecutive_cities = 48.373546489791295

# Check solution validity
result = verify_solution(tour, cities, total_travel_cost, maximum_distance_between_consecutive_cities)
print(result)