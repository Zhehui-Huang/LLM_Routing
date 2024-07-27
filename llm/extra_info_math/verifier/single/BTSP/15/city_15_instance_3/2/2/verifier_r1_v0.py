def calculate_distance(city1, city2):
    from math import sqrt
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_requirements(tour, distances, max_consecutive_distance):
    # Check Requirement 1: Tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Each city must be visited exactly once (except depot city)
    visited = set(tour)
    if len(visited) != 16 or any(city not in tour for city in range(15)):
        return "FAIL"
    
    # Calculate travelled distances between consecutive cities and total cost
    total_travel_cost = 0
    max_travelled_distance = 0
    for i in range(len(tour)-1):
        distance = calculate_distance(distances[tour[i]], distances[tour[i+1]])
        total_travel_cost += distance
        if distance > max_travelled_distance:
            max_travelled_distance = distance
    
    # Check the maximum distance
    if max_travelled_distance != max_consecutive_distance:
        return "FAIL"

    return "CORRECT"

# City coordinates index by their indices
cities_coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
    (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), 
    (70, 95), (29, 64), (32, 79)
]

# Proposed solution tour, total cost, and maximum distance between any two consecutive cities
submitted_tour = [0, 6, 8, 11, 2, 7, 3, 12, 4, 1, 14, 5, 9, 10, 13, 0]
submitted_total_cost = 281
submitted_max_distance = 48

# Verify the solution
result = check_requirements(submitted_tour, cities_coordinates, submitted_max_distance)
print(result)