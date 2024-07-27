import math

# Coordinates of the cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), 
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Provided solution
tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
total_travel_cost = 337.84
maximum_distance = 60.67

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution(tour, total_travel_cost, maximum_distance):
    # Test Requirement 1: Tour starts and ends at depot city 0
    assert tour[0] == 0 and tour[-1] == 0, "Tour must start and end at depot city 0."

    # Test Requirement 2: Each city is visited exactly once
    assert sorted(tour[:-1]) == list(range(15)), "Each city must be visited exactly once."

    # Calculate travel costs and validate them
    calculated_total_cost = 0
    calculated_max_distance = 0

    for i in range(len(tour) - 1):
        dist = calculate_distance(tour[i], tour[i+1])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    # Check if costs are as expected
    assert abs(calculated_total_cost - total_travel_covered) < 1e-2, "Total travel cost does not match."
    assert abs(calculated_max_distance - maximum_distance) < 1e-2, "Maximum distance between consecutive cities does not match."

    print("CORMAL")

try:
    test_solution(tour, total_traveled_cost, maximum_distance)
except AssertionError as e:
    print("FAIL:", str(e))