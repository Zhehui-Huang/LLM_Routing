import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, cities):
    # Requirement 1: Visit each city exactly once, starting and ending at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Calculate travel cost and maximum distance between consecutive cities
    total_travel_cost = 0
    maximum_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_travel_cost += dist
        if dist > maximum_distance:
            maximum_distance = dist
    
    # Requirement 2: Travel cost calculated as the Euclidean distance between cities
    # Requirement 3: Minimize the longest distance between two consecutive cities
    # Checking the reported values for test conditions
    total_travel_cost_reported = 477.05
    max_distance_reported = 87.46

    if round(total_travel_context, 2) != round(total_travel_cost_reported, 2):
        return "FAIL"
    if round(maximum_distance, 2) != round(max_distance_reported, 2):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), 
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Tour solution from user
tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]

# Verify the tour
result = verify_tour(tour, cities)
print(result)