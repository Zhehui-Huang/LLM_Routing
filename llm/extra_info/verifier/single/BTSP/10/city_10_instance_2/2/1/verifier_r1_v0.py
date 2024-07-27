import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at the depot city 0."
    
    if len(set(tour)) != len(tour) or len(tour) != len(cities):
        return "FAIL: Tour does not include each city exactly once or includes duplicates."
    
    # Extract coordinates based on tour indices
    tour_coordinates = [cities[idx] for idx in tour]
    
    # Calculate total travel cost and max distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour_coordinates) - 1):
        distance = calculate_distance(tour_coordinates[i], tour_coordinates[i + 1])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Check if results match given maximum distance
    if not math.isclose(max_distance, 78.64, rel_tol=1e-2):
        return "FAIL: Provided maximum distance does not match with calculated value."
    
    # Check if results match total cost
    if not math.isclose(total_cost, 384.79, rel_tol=1e-2):
        return "FAIL: Provided total cost does not match with calculated value."
    
    return "CORRECT"

# Define the city locations based on environment information
cities = {
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

# Given solution
tour = [0, 8, 5, 4, 7, 2, 1, 9, 6, 3, 0]

# Running verification function
result = verify_solution(tour, cities)
print(result)