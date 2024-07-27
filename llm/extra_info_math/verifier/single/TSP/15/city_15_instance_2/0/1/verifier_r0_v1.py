import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, cost):
    cities = {
        0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40),
        4: (54, 42), 5: (36, 30), 6: (52, 82), 7: (93, 44),
        8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
        12: (56, 58), 13: (72, 43), 14: (6, 99)
    }
    # Requirement 1: Tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city visited exactly once
    if len(set(tour)) != len(cities) + 1:  # +1 because 0 appears twice
        return "FAIL"
    
    # Requirement 3: Travel cost calculated by Euclidean distance
    calculated_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

    # Round the cost, in real case scenario this ensures numerical stability in floating point comparisons
    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"
    
    # Requirement 5: Since tour[0] == tour[-1], the continuous loop requirement is met inherently.

    return "CORRECT"

# Provided solution
tour = [0, 6, 11, 1, 14, 8, 12, 4, 3, 5, 10, 9, 13, 7, 2, 0]
total_travel_cost = 307

# Verify the solution
print(check_solution(tour, total_travel_cost))