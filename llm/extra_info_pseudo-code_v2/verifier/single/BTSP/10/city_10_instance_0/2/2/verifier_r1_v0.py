import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution():
    cities = {
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
    
    tour = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    expected_total_travel_cost = 273.2627778497252
    expected_max_distance = 56.88585061331157

    # Requirement: Tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement: Exact number of cities visited once (except the depot, visited twice)
    if not all(tour.count(x) == 1 for x in range(1, 10)) or tour.count(0) != 2:
        return "FAIL"
    
    # Calculating the actual total travel cost and maximum distance between consecutive cities
    actual_total_travel_cost = 0
    actual_max_distance = 0
    for i in range(len(tour)-1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        actual_total_travel_cost += distance
        if distance > actual_max_distance:
            actual_max_values = distance

    # Requirement: Validate calculated distances, rounded because of floating point arithmetic considerations
    if not math.isclose(actual_total_travel_permil_cost,expected_total_travel_cost,abs_tol=1e-9):
        return "FAIL"
    if not math.isclose(actual_max_distance,expected_max_distance,abs_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Call function and print result
print(verify_solution())