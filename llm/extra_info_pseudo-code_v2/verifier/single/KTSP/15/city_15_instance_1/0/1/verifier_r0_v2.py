import math

def euclidean_distance(a, b):
    # Calculate the Euclidean distance between two points
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def verify_solution(tour, total_cost):
    # Dictionary of city coordinates
    cities = {
        0: (29, 51),
        1: (49, 20),
        2: (79, 69),
        3: (17, 20),
        4: (18, 61),
        5: (40, 57),
        6: (57, 30),
        7: (36, 12),
        8: (93, 43),
        9: (17, 36),
        10: (4, 60),
        11: (78, 82),
        12: (83, 96),
        13: (60, 50),
        14: (98, 1)
    }
    
    # [Requirement 1] The first and last city in the tour should be the depot city (city 0)
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # [Requirement 2] The number of distinct cities in the tour should be 6, including the depot
    if len(set(tour)) != 6:
        return "FAIL"
    
    # [Requirement 4] Check the total travel cost is calculated correctly based on Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Check if the provided tour cost is close to the computed cost within a small tolerance
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Example test case
tour = [0, 10, 4, 11, 13, 1, 0]
total_cost = 209.74

# Run the verification
result = verify_solution(tour, total_cost)
print(result)