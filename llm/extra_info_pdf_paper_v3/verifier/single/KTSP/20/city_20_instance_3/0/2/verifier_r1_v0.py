import math

# City coordinates map as provided
city_coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 
    18: (53, 76), 19: (19, 72)
}

# Tour and cost as provided in solution
provided_tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 0]
provided_total_cost = 273.7443523737762

def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_tour(tour, expected_cost):
    # Check number of cities in tour (should be exactly 13 unique cities + return to depot)
    if len(tour) != 14:
        return "FAIL"
    
    # Check the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check only valid city indices are used (within the range and account for 20 cities)
    if any(city not in city_coordinates for city in tour):
        return "FAIL"
    
    # Check if there are exactly 13 unique cities visited (considering the visited city and depot city)
    if len(set(tour)) != 13:
        return "FAIL"
    
    # Check the total cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(city_coordinates[city_from], city_coordinates[city_to])
    
    # Compare calculated cost with the provided cost (allowing for slight floating-point discrepancies)
    if not math.isclose(calculated_cost, expected_cost, abs_tol=1e-6):
        return "FAIL"

    return "CORRECT"

# Running the verification
result = verify_tour(provided_tour, provided_total_cost)
print(result)