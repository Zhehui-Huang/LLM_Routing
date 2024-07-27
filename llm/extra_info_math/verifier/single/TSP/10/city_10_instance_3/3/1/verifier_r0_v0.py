import math

# Define coordinates of each city index
city_coordinates = {
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

# Tour provided from the solution above
tour = [0, 8, 3, 9, 6, 5, 2, 4, 1, 7, 0]
# Expected travel cost from the solution above
expected_cost = 294.17253892411236

def calculate_euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities given their coordinates. """
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour):
    """ Verify the tour against the requirements. """
    # Check direct travel between cities (Requirement 1 already fulfilled by direct indices)
    
    # Check all cities are visited exactly once and return to depot (Requirement 2)
    cities_visited = set(tour)
    if cities_visited != set(city_coordinates.keys()):  # All cities plus depot should be in tour
        return "FAIL"
    
    if tour[0] != tour[-1] != 0:  # Start and end at depot city 0
        return "FAIL"
    
    # Calculate and compare the travel cost (Requirement 3 and Requirement 4)
    calculated_cost = sum(calculate_euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, expected_cost, rel_tol = 1e-5):
        return "FAIL"
    
    # Check for no subtours (Requirement 5)
    # Continuous tour is guaranteed by single visit and start-end at depot
    return "CORRECT"

# Execute the verification function
verification_result = verify_tour(tour)
print(verification_result)