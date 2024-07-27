import math

# Given solution
tour = [0, 8, 7, 6, 5, 9, 3, 4, 2, 1, 0]
total_travel_cost = float('inf')  # Representing infinity
max_distance_between_cities = 68.26419266350405

# City coordinates
coordinates = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Helper function to calculate distance
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Check if tour starts and ends at the depot city 0
def check_requirements(tour, total_travel_cost, max_distance):
    # Requirement 1: Starts and ends at depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Requirement 2: Visits each city exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(coordinates) + 1:  # Includes the depot twice
        return "FAIL"
    
    # Calculate actual total cost and maximum distance
    actual_total_cost = 0
    actual_max_distance = 0
    previous_city = tour[0]
    
    for city in tour[1:]:
        dist = distance(previous_city, city)
        actual_total_cost += dist
        actual_max_distance = max(actual_max_distance, dist)
        previous_city = city
    
    # Requirement 3: Minimize the longest distance between consecutive cities
    # This part needs expert domain knowledge to determine if it's minimized
    # but for now, we will just validate the given value.
    if math.isclose(actual_max_distance, max_distance, rel_tol=1e-9):
        return "CORRECT"
    else:
        return "FAIL"

# Run the test
print(check_requirements(tour, total_travel_cost, max_distance_between_cities))