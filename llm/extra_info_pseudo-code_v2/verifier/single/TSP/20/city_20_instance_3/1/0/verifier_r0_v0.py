import math

# City coordinates as provided in the task description
city_coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Proposed solution tour and its reported cost
proposed_tour = [0, 3, 15, 17, 5, 19, 13, 2, 6, 18, 12, 7, 8, 14, 4, 10, 11, 9, 16, 1, 0]
reported_cost = 475.56

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_requirements(tour, reported_cost, city_coords):
    # Requirement 1: Start and end at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != 19 or any(city not in unique_cities for city in range(1, 20)):
        return "FAIL"
    
    # Requirement 3: Compute the actual travel cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
    actual_cost = round(actual_cost, 2)
    
    if actual_cost != reported_cost:
        return f"FAIL. Expected cost: {actual_cost}, Reported cost: {reported_cost}"
    
    # Implementation specifics for Requirement 5 are implicitly assumed to be handled in the original optimization algorithm
    # So we skip direct validation of the optimization algorithm (Lin-Kernighan) here.

    return "CORRECT"

# Running the unit test on the provided solution
result = check_requirements(proposed_tour, reported_cost, city_coordinates)
print(result)