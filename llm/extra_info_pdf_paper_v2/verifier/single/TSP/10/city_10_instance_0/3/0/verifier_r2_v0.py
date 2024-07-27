import math

# Given tour solution and expected total cost
tour = [0, 5, 9, 4, 8, 3, 2, 1, 6, 7, 0]
reported_cost = 271.4716218753353

# City coordinates
city_coordinates = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Validate the TSP requirements
def validate_tsp_solution(tour, reported_cost, city_coordinates):
    # Requirement 2: Start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 4: Tour format containing all cities exactly once except depot
    unique_cities = set(tour)
    if len(tour) - 1 != len(city_coordinates) or unique_cities != set(city_coordinates.keys()):
        return "FAIL"

    # Requirement 5: Correct calculation of total travel cost (Requirement 3 implicitly checked within)
    calculated_cost = sum(calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run the unit test
test_result = validate_tsp_solution(tour, reported_cost, city_coordinates)
print(test_result)