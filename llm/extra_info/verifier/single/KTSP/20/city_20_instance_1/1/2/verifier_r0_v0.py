import math

# Coordinates of cities including the depot city
city_locations = [
    (14, 77),  # Depot city 0
    (34, 20),  # City 1
    (19, 38),  # City 2
    (14, 91),  # City 3
    (68, 98),  # City 4
    (45, 84),  # City 5
    (4, 56),   # City 6
    (54, 82),  # City 7
    (37, 28),  # City 8
    (27, 45),  # City 9
    (90, 85),  # City 10
    (98, 76),  # City 11
    (6, 19),   # City 12
    (26, 29),  # City 13
    (21, 79),  # City 14
    (49, 23),  # City 15
    (78, 76),  # City 16
    (68, 45),  # City 17
    (50, 28),  # City 18
    (69, 9)    # City 19
]

# Given solution details
tour = [0, 3, 5, 7, 8, 9, 14, 0]
reported_cost = 173.14

def calculate_distance(city1, city2):
    """ Computes the Euclidean distance between two cities based on their coordinates. """
    x1, y1 = city_locations[city1]
    x2, y2 = city_locations[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, reported_cost):
    # [Requirement 1] Starts and ends at the depot city 0
    
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # [Requirement 2] Visits exactly 7 cities, including the depot city
    unique_cities = set(tour)
    if len(unique_cities) != 7:
        return "FAIL"

    # [Requirement 3] Shortest possible tour visiting these 7 cities by Euclidean distance
    total_distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    if not math.isclose(total_distance, reported_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Validate the provided solution and print the result
result = verify_tour(tour, reported_cost)
print(result)