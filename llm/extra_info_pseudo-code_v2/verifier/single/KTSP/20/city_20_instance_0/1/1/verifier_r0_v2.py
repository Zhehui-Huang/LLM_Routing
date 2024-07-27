from math import sqrt

# City coordinates from the problem statement
cities = {
    0: (8, 11),
    3: (80, 60),
    11: (40, 87),
    16: (13, 43)
}

def calculate_distance(c1_idx, c2_idx):
    """ Calculate the Euclidean distance between two cities given their indices. """
    c1, c2 = cities[c1_idx], cities[c2_idx]
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def verify_tour(tour, reported_cost):
    # Requirements 1, 4: Check tour starts/ends at city 0, well-formed tour elements
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Includes exactly four unique cities including the depot city
    if len(set(tour)) != 4:
        return "FAIL"

    # Ensure all indices are valid and the tour is composed properly of integers
    if not set(tour).issubset(cities.keys()):
        return "FAIL"
    
    # Requirement 5: Validate the total cost
    actual_cost = round(sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)), 2)
    if not abs(actual_cost - reported_cost) < 1e-2:  # Allowing a minor numerical precision tolerance
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Provided solution information
tour = [0, 3, 11, 16, 0]
total_cost_reported = 219.36

# Run verification
result = verify_tour(tour, total_cost_reported)
print(result)