import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, cities, reported_cost):
    # Requirement 1: The tour must start and end at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot is required to visit exactly 7 cities, including the depot.
    if len(set(tour)) != 8:  # Including depot twice (start and end), set to remove duplicates
        return "FAIL"
    
    # Requirement 5: Output the tour as a list of city indices, starting and ending at depot city 0.
    if not all(isinstance(x, int) for x in tour):  # All items must be integer city indices
        return "FAIL"
    
    # Calculate total cost
    total_cost = 0
    for i in range(len(tour) - 1):
        city1_index = tour[i]
        city2_index = tour[i + 1]
        total_cost += calculate_euclidean_distance(cities[city1_index], cities[city2_index])
    
    # Requirement 4: The travel cost is calculated using the Euclidean distance between cities.
    # Requirement 6: Output the total travel cost of the tour.
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given data
cities_info = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Provided solution details
tour = [0, 6, 2, 13, 8, 9, 14, 0]
reported_cost = 130.67

# Check if the provided solution meets all the requirements
result = validate_tour(tour, cities_info, reported_cost)
print(result)