import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_travel_cost, city_coordinates):
    # [Requirement 3] Tour starts and ends at depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 1] Robot visits each city exactly once apart from the depot
    unique_cities = set(tour[1:-1])  # Exclude the repeating depot city 0
    if len(unique_cities) != len(city_coordinates) - 1 or len(tour) - 2 != len(unique_cities):
        return "FAIL"
    
    # Calculate the travel cost and verify with given
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    # [Requirement 5] Check if the calculated cost matches the provided total travel cost
    if not math.isclose(calculated_cost, total_travel što, rel_tol=1e-9):
        return "FAIL"
    
    # [Requirement 4] Already ensured format by returning the given tour and total_cost which is implied by parameter input
    
    return "CORRECT"

# Cities coordinates: Depot city 0 and other cities 1-9
city_coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Provided tour and cost
tour = [0, 3, 6, 4, 7, 2, 1, 9, 5, 8, 0]
total_travel_cost = 354.91010610434057

# Testing the solution
result = test_solution(tour, total_travel_cost, city_coordinates)
print(result)