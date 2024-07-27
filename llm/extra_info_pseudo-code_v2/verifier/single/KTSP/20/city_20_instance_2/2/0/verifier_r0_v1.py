import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_tour(cities, tour, reported_cost):
    # Requirement 1: Start and end at the depot city, city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly 10 cities, including the depot city.
    if len(tour) != 11:  # includes city 0 at start and end, so 11 total entries
        return "FAIL"
    
    # Requirement 3: Calculate the travel cost.
    total_calculated_cost = 0
    for i in range(len(tour)-1):
        total_calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Checking if the reported cost matches the calculated cost rounded to two decimal places.
    if not math.isclose(reported_cost, total_calculated_cost, abs_tol=1e-2):
        return "FAIL"
    
    # If all conditions are met
    return "CORRECT"

# Define city coordinates
cities_coordinates = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), 
                      (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
                      (28, 49), (91, 94), (51, 58), (30, 48)]

# Tour and Reported Total Cost
tour = [0, 12, 16, 19, 13, 15, 18, 7, 11, 14, 0]
reported_total_cost = 186.92

# Verify the provided tour against the requirements
result = verify_tour(cities_coordinates, tour, reported_total_cost)
print(result)