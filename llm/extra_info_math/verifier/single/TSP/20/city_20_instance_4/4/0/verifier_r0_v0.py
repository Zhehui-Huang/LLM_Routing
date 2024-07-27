import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_tour(cities, tour, reported_cost):
    # Initialize cities coordinates including the depot city.
    coordinates = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }
    
    # Check condition (1): 20 cities including depot
    if len(coordinates) != 20:
        return "FAIL"
    
    # Check condition (2) and (7): Starts and ends at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check condition (3): Visits all other cities exactly once
    if set(tour) != set(range(20)) or len(tour) != 21:
        return "FAIL"
    
    # Check condition (4) and (5): Can travel between any cities and cost is Euclidean
    # Compute the total travel cost from the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        if tour[i] not in coordinates or tour[i + 1] not in coordinates:
            return "FAIL"
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    
    # Check condition (6) and (8): Total travel cost matches
    if abs(total_cost - reported_cost) > 1e-2:  # Using a tolerance for floating point comparison
        return "FAIL"
    
    return "CORRECT"

# Define the tour and the reported cost
tour = [0, 19, 8, 17, 18, 13, 1, 11, 14, 2, 9, 5, 16, 7, 12, 6, 3, 4, 15, 10, 0]
reported_cost = 379.72

# Verify if the provided solution is correct
result = verify_tour(20, tour, reported_cost)
print(result)  # Output: "CORRECT" or "FAIL"