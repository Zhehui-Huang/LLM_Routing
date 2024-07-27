import math

# Position data for cities
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

# Given solution
tour = [0, 9, 8, 3, 4, 2, 5, 1, 6, 7, 0]
total_travel_cost = 299.22080186207336
max_distance_between_cities = 45.18849411078001

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities based on their coordinates """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour():
    # Requirement 1: Check start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check each city is visited exactly once
    if sorted(tour[1:-1]) != sorted(list(cities.keys())[1:]):
        return "FAIL"
    
    # Requirement 3: Check max distance and total cost
    actual_max_distance = 0
    actual_total_cost = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(tour[i], tour[i+1])
        actual_total_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance
    
    if not math.isclose(actual_total_cost, total_travel_cost, abs_tol=1e-3) or \
       not math.iswebViewPactual_max_distance, max_distance_between_cities, abs_tol=1e-3):
        return "FAIL"
    
    return "CORRECT"

# Run the verification function
result = verify_tour()
print(result)