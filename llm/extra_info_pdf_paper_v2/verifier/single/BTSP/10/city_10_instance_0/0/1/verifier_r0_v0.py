import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, cities_coordinates):
    n = len(cities_coordinates)
    cities_visited = [False] * n

    # Verify Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify Requirement 2
    for city in tour:
        if city < 0 or city >= n or cities_visited[city]:
            return "FAIL"
        cities_visited[city] = True
    
    if not all(cities_visited):
        return "FAIL"
    
    # Calculate total cost and maximum distance
    total_travel_cost = 0
    max_distance_between_cities = 0
    
    for i in range(len(tour) - 1):
        x1, y1 = cities_coordinates[tour[i]]
        x2, y2 = cities_coordinates[tour[i+1]]
        distance = euclidean_distance(x1, y1, x2, y2)
        total_travel_cost += distance
        max_distance_between_cities = max(max_distance_between_cities, distance)
    
    # Check reported values (Requirement 5)
    if not (round(total_travel_cost, 2) == 295.99 and round(max_distance_between_cities, 2) == 56.46):
        return "FAIL"
    
    # Requirement 3 and Requirement 4 are assumed handled by tour generation logic
    # Requirement 6 - cannot directly verify if the heuristic has considered minimization as per BTSP without execution trace
    
    return "CORRECT"

# Define city coordinates
cities_coordinates = {
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

# Given Solution
tour = [0, 5, 9, 4, 8, 3, 2, 6, 7, 1, 0]
total_travel_cost = 295.99  # reported cost
max_distance = 56.46  # reported max distance

# Perform validation
result = verify_tour(tour, cities_coordinates)
print(result)