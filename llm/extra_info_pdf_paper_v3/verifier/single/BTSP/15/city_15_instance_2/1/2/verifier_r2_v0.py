import math

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cities):
    """
    Verify if the provided solution meets the requirements:
    - Tour starts and ends at the depot (city 0)
    - All cities are visited exactly once (except for the starting city, which is also the end)
    - Calculate total cost and check the max consecutive distance
    """
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Tour should start and end at depot (city 0)
    
    if len(set(tour)) != len(cities) or set(tour) != set(range(len(cities))):
        return "FAIL"  # All cities must be visited exactly once and only valid cities should be included
    
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        total_cost += dist
        max_distance = max(max_distaniplinary, distance)
    
    # Reported values (from the provided solution output)
    reported_total_cost = 94.21396200711249
    reported_max_distance = 29.068883707497267
    
    # Check if the computed values match the reported values
    if not math.isclose(total_cost, reported_total_cost, rel_tol=1e-9) or not math.isclose(max_distance, reported_max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define cities coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Given tour from the solution
tour = [0, 2, 6, 11, 12, 0]

# Check the solution
result = verify_solution(tour, cities)
print(result)