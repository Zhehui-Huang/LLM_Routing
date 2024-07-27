import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_tour(coordinates, tour, reported_cost):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if 16 unique cities are visited (including the depot city)
    if len(set(tour)) != 17 or len(tour) != 17:
        return "FAIL"
    
    # Calculate the actual travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    # Compare the calculated travel cost with the reported cost
    if not math.isclose(total_cost, reported_cost, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Define coordinates
coordinates = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Provided solution
tour = [0, 15, 4, 3, 10, 12, 7, 16, 5, 9, 2, 14, 1, 13, 17, 19, 0]
total_travel_cost = 379.2371147937699

# Validate the solution
result = validate_tour(coordinates, tour, total_travel_cost)
print(result)