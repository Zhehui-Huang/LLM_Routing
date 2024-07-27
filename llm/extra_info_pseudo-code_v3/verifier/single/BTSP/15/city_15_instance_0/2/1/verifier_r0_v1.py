import math

# City coordinates as provided
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 
    4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23), 
    8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40), 
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city2][0] - cities[city1][0]) ** 2 + (cities[city2][1] - cities[city1][1]) ** 2)

# Provided solution to evaluate
tour = [0, 8, 0, 10, 0, 0]
total_travel_cost = 98.91044083590607
max_distance = 29.732137494637012

# Tests corresponding to the requirements:
def test_solution():
    # Requirement 1: Visit each city at least once, starting and ending at 0
    unique_cities = set(tour) - {0}
    if not unique_cities.issubset(cities.keys()):  # check all cities are visited at least once
        return "FAIL"

    # Requirement 4: Output tour starting and ending at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculating distances and total cost
    calculated_cost = 0
    distances = []
    for i in range(len(tour) - 1):
        dist = euclidean_distance(tour[i], tour[i + 1])
        distances.append(dist)
        calculated_cost += dist

    # Requirement 2: Correct calculation of total distance
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Requirement 6: Correct calculation of maximum distance between consecutive cities
    if not math.isclose(max(distances), max_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Execute the test function
result = test_solution()
print(result)