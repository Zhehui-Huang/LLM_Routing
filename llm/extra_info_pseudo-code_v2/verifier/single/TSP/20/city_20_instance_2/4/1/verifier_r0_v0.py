import math

# Assume the coordinates of cities are provided by a constant dictionary
CITY_COORDINATES = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

def calculate_euclidean_distance(city1, city2):
    """
    Calculate the Euclidean distance between two cities
    based on their coordinates.
    """
    x1, y1 = CITY_COORDINATES[city1]
    x2, y2 = CITY_COORDINATES[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_tour(tour, total_travel_cost):
    """
    Check if the provided tour satisfies all the given requirements.
    """
    # Check if the tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if each city (1-19) is visited exactly once
    visited_cities = tour[1:-1]  # extract cities between the start and the finish
    unique_cities = set(visited_cities)
    if len(visited_cities) != 19 or len(unique_cities) != 19:
        return False

    # Check if the travel cost is correctly calculated
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_euclidean_distance(tour[i], tour[i+1])
    if not math.isclose(total_travel_cost, computed_cost, rel_tol=1e-5):
        return False

    return True

# Solution provided as an example
provided_tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
provided_total_travel_cost = 478.4306776278287

# Check if the provided solution is correct
if check_tour(provided_tour, provided_total_travel_cost):
    print("CORRECT")
else:
    print("FAIL")