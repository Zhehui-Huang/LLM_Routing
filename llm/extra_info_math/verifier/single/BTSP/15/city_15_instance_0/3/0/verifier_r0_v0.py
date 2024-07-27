def verify_solution(tour, max_distance, cities):
    # Extract the list of visited cities
    visited = set(tour)
    
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once + must visit all and only the cities in the list
    if len(visited) != len(cities) or len(tour) != len(cities) + 1:
        return "FAIL"
    
    # Checking if all cities are visited exactly once and only those cities are visited
    expected_cities = set(range(len(cities)))
    if visited - {0} != expected_cities:
        return "FAIL"
    
    # Requirement 3: Traverse each pair and calculate distances, check max distance
    import math
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    observed_max_distance = 0
    for i in range(len(tour)-1):
        d = distance(cities[tour[i]], cities[tour[i+1]])
        if d > observed_max_distance:
            observed_max_distance = d
            
    if observed_max_distance > max_distance:
        return "FAIL"
    
    return "CORRECT"

# City coordinates (id corresponds to index position)
cities = {
    0: (9, 93), 
    1: (8, 51), 
    2: (74, 99), 
    3: (78, 50), 
    4: (21, 23), 
    5: (88, 59), 
    6: (79, 77), 
    7: (63, 23), 
    8: (19, 76), 
    9: (21, 38), 
    10: (19, 65), 
    11: (11, 40), 
    12: (3, 21), 
    13: (60, 55), 
    14: (4, 39)
}

# Tour results from solver
tour = [0, 8, 1, 11, 14, 12, 9, 4, 7, 3, 5, 2, 6, 13, 10, 0]
max_distance = 42.37924

# Testing the output
result = verify_solution(tour, max_distance, cities)
print("Result:", result)