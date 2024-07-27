import math

def euclidean_distance(coords1, coords2):
    return math.sqrt((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2)

def verify_tour(tour, cities, proposed_max_consecutive_distance):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Requirement 1: Starts and ends at depot city 0
    
    if len(set(tour)) != len(tour) or len(tour) != len(cities):
        return "FAIL"  # Requirement 2: All cities visited exactly once
    
    max_consecutive_distance = 0
    total_travel_cost = 0
    for i in range(1, len(tour)):
        distance = euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
        total_travel_cost += distance
        if distance > max_consecutive_distance:
            max_consecutive_distance = distance
    
    # Check if calculated values match given values
    if max_consecutive_distance != proposed_max_consecutive_distance:
        return "FAIL"  # Check max distance for Requirement 3
    
    return "CORRECT"

# Coordinates of cities including depot city (index 0)
cities_coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Provided tour and metrics
tour = [0, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
proposed_max_distance = 100

# Validating the solution
result = verify_tour(tour, cities_coords, proposed_max_distance)
print(result)