import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, total_travel_cost):
    # City coordinates
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
        (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
        (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]

    # Check the number of unique cities (Requirement 1)
    if len(set(tour)) != 16:
        return "FAIL"
    
    # Check if the tour starts and ends with the depot city (Requirement 2)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if computed travel cost matches the provided total travel cost (Requirement 3 and 4)
    computed_cost = 0
    for i in range(len(tour) - 1):
        city1_index = tour[i]
        city2_index = tour[i + 1]
        computed_cost += euclidean_distance(*cities[city1_index], *cities[city2_index])
    
    # Compare computed cost with a tolerance for floating-point operations
    if abs(computed_cost - total_travel_cost) > 1e-5:
        return "FAIL"

    # If all checks passed
    return "CORRECT"

# Given solution details
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 16, 7, 12, 6, 10, 15, 0]
total_travel_cost = 275.48440554083993

# Verify the solution
print(verify_tour(tour, total_travel_cost))