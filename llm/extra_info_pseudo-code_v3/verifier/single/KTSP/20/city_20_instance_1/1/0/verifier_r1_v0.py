import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, cost_reported):
    # City coordinates
    coordinates = {
        0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 
        5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
        10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
        15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
    }

    # [Requirement 1] The robot must start and end its tour at the depot city (City 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] The robot must visit exactly 7 cities, including the depot city.
    if len(tour) != 8:  # Including the return to the depot
        return "FAIL"
    
    # [Requirement 3] Calculate the total travel cost using the Euclidean distance
    total_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    
    # [Requirement 5] Check the format of the output
    if not isinstance(cost_reported, (int, float)) or not all(isinstance(city, int) for city in tour):
        return "FAIL"

    # Consider minor floating-point issues in comparison
    if not math.isclose(total_cost, cost_reported, abs_tol=1e-4):
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Provided solution
tour = [0, 6, 2, 8, 15, 9, 3, 0]
total_cost = 173.2

# Check if the solution is correct
result = verify_solution(tour, total_cost)
print(result)