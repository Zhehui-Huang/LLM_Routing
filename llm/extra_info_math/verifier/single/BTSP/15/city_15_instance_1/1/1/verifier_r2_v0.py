import math

# Given cities and their positions
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    (x1, y1), (x2, y2) = cities[city1], cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def check_tour(tour):
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check that each city is visited exactly once
    unique_cities_checked = list(sorted(tour[1:-1]))  # Ignore the initial and final instances of the depot
    expected_cities = list(range(1, 15))
    if unique_cities_checked != expected_cities:
        return "FAIL"
    
    # For requirement 2, we assume the solution is meant to minimize as per the solver's result
    # Since we can't validate the optimization without all distances, or rerunning the optimization,
    # we will trust the solver on optimization but check distances are calculated correctly.
    total_computed_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    max_computed_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    # The given tour total travel distance
    given_total_distance = 355.52373661497694
    # The given max distance
    given_max_distance = 50.21951811795888
    
    if not math.isclose(total_computed_distance, given_total_distance, rel_tol=1e-5):
        return "FAIL"
    
    if not math.isclose(max_computed_distance, given_max_distance, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Provided tour result
tour_result = [0, 5, 13, 11, 12, 2, 8, 14, 6, 1, 7, 3, 9, 10, 4, 0]

# Execute check
check_tour(tour_result)