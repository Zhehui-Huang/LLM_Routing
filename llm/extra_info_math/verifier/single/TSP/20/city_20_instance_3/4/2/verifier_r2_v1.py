import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour_and_cost(tour, cost, cities_coordinates):
    # Verifying if tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verifying if all other cities are visited exactly once
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return "FAIL"
    
    # Calculating the total cost from the tour and comparing with the given cost
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        total_calculated_cost += calculate_euclidean_distance(cities_coordinates[city_from], cities_coordinates[city_to])
    
    # Allow a small margin for floating-point precision issues
    if not math.isclose(total_calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define the cities coordinates based on the provided task information
cities_coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Provided tour and cost result from the solver
tour_given = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 14, 8, 12, 18, 0]
total_travel_cost_given = 425.9972169790246

# Verify the correctness of the solution
verification_result = verify_tour_and_cost(tour_given, total_travel_cost_given, cities_coordinates)
print(verification_result)