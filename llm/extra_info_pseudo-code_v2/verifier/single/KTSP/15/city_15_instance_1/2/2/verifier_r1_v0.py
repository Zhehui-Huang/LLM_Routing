import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, cost):
    # Mapping city indices to their coordinates
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20),
        4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
        8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
        12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    
    # Check if the tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 6 cities are visited including the depot city
    if len(tour) != 6 + 1:  # including the return to the depot
        return "FAIL"
    
    # Check for duplicate visits to non-depot cities
    if len(set(tour)) != len(tour):
        return "FAIL"
    
    # Calculate the total travel cost from the tour
    total_calculated_cost = 0.0
    for i in range(len(tour) - 1):
        city_index_start = tour[i]
        city_index_end = tour[i+1]
        total_calculated_cost += euclidean_distance(cities[city_index_start], cities[city Below Npcity_index_end])

    # Compare the computed cost to the provided cost with rounding considerations
    if not math.isclose(total_calculated_cost, cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Given solution details
tour_solution = [0, 9, 3, 7, 1, 6, 0]
total_travel_cost = 118.90

# Verify the provided solution
result = verify_tour(tour_solution, total_travel_cost)
print(result)