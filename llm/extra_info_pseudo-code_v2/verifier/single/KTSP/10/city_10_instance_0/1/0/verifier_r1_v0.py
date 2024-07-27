import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, reported_cost, cities_coordinates):
    # [Requirement 1] The tour must start and end at city 0.
    assert tour[0] == 0 and tour[-1] == 0, "Tour should start and end at depot city 0."
    
    # [Requirement 2] The tour must contain exactly 4 cities, including the depot city.
    assert len(tour) == 5, "Tour must have exactly 4 cities including the depot."
    
    # [Requirement 3] Travel cost calculated as the Euclidean distance
    total_distance = 0
    for i in range(len(tour) - 1):
        city_a = cities_coordinates[tour[i]]
        city_b = cities_coordinates[tour[i + 1]]
        total_distance += calculate_distance(city_a, city_b)
    
    # Check accuracy of the reported travel cost
    assert round(total_distance, 2) == reported_cost, f"Reported total travel cost is inaccurate. Expected: {round(total_distance, 2)}, Got: {reported_cost}"
    
    # [Requirement 5] Check if tour output format is correct (implicitly checked by the other assertions and inputs)

    # Not testing [Requirement 6] directly, as its application is not verifiable simply through outputs without information about the internal working steps

# Given solution to test
tour_given = [0, 7, 3, 9, 0]
total_cost_given = 168.21

# Coordinates of the cities
cities_coords = [
    (50, 42),  # City 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Run test
try:
    test_solution(tour_given, total_cost_given, cities_coords)
    print("CORRECT")
except AssertionError as e:
    print("FAIL:", e)