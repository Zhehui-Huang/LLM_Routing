import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour_and_cost():
    # Define city coordinates
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20),
        4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
        8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
        12: (83, 96), 13: (60, 50), 14: (98, 1)
    }

    # Tour and calculated total distance (from submission)
    proposed_tour = [0, 6, 1, 7, 3, 9, 0]
    proposed_cost = 118.90

    # Check requirement: Depot is city 0
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"
    
    # Check requirement: Tour contains exactly 6 cities
    if len(proposed_tour) != 7:  # counting depot city at start and end
        return "FAIL"

    # Calculate the travel cost for the proposed tour
    actual_cost = 0
    for i in range(len(proposed_tour) - 1):
        actual_cost += calculate_distance(cities[proposed_tour[i]], cities[proposed_tour[i+1]])

    # Check requirement: Cost should be correct
    if not math.isclose(actual_cost, proposed_cost, rel_tol=1e-2):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Run the test
print(test_tour_and_cost())