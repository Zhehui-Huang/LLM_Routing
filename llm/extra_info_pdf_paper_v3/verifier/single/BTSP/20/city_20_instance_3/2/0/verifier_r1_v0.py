from math import sqrt

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    cities = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
        (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95),
        (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
    reported_total_cost = 458.37
    reported_max_distance = 68.15

    # Check if the tour starts and ends at the depot city 0
    assert tour[0] == 0 and tour[-1] == 0, "Tour does not start and end at the depot city 0."
    
    # Check if all cities are visited exactly once, excluding the depot city which is visited twice (start and end)
    visited_cities = set(tour)
    assert len(visited_cities) == 20 and all(city in visited_cities for city in range(20)), "Not all cities are visited exactly once."

    # Compute total travel cost and maximum distance between consecutive cities
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += dist
        if dist > calculated_max_distance:
            calculated_max_idstance = dist
    
    # Check if calculated and reported costs are close enough (accounting for floating-point precision issues)
    assert abs(calculated_cost - reported_total_cost) < 0.1, "Total travel cost is incorrect."
    assert abs(calculated_max_distance - reported_max_distance) < 0.1, "Maximum distance between consecutive cities is incorrect."
    
    print("CORRECT")

try:
    test_solution()
except AssertionError as e:
    print(f"FAIL: {str(e)}")