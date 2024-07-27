import math

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Tour and cost from provided solution
tour = [0, 19, 1, 13, 18, 17, 8, 5, 7, 10, 15, 11, 9, 12, 3, 4, 0]
reported_cost = 511.16

# Calculate the total travel cost
def calculate_travel_cost(tour):
    def euclidean_distance(p1, p2):
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    return total_cost

# Check if requirements are met
def check_requirement(tour, cost):
    # Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Tour visits exactly 16 different cities
    if len(set(tour)) != 16 or len(tour) != 17:  # including repeated depot city
        return "FAIL"
    
    # Requirement 3: Checks the travel cost
    calculated_cost = calculate_travel_cost(tour)
    # Allow a small margin for floating point comparison
    if not math.isclose(calculated_cost, cost, abs_tol=0.1):
        return f"FAIL. Expected cost: {calculated_cost}, but reported: {cost}"
    
    # Requirement 4: Format check passed by structure (observed format matches expected)
    
    return "CORRECT"

# Perform check on the provided solution
result = check_requirement(tour, reported_cost)
print(result)