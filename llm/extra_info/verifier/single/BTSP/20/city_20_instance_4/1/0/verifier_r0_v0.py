import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_travel_cost, max_distance):
    # Coordinates of each city
    cities = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
              (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
              (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]
    
    # Check Requirement 1
    assert tour[0] == 0 and tour[-1] == 0, "Tour must start and end at the depot city."
    
    # Check Requirement 2
    unique_cities = set(tour)
    assert len(unique_cities) == 20 and all(city in unique_cities for city in range(20)), \
        "Each city must be visited exactly once."
    
    # Calculate total travel cost and find maximum distance
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour)-1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Check calculated total travel distance
    assert math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-2), \
        "Total travel cost is incorrect."
    
    # Check maximum distance
    assert math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2), \
        "Maximum distance between consecutive cities is incorrect."

    print("CORRECT")

# Given solution for the problem
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
total_travel_cost = 410.04
max_distance_between_cities = 89.01

# Running the test
try:
    test_solution(tour, total_travel_cost, max_distance_between_cities)
except AssertionError as e:
    print("FAIL:", e)