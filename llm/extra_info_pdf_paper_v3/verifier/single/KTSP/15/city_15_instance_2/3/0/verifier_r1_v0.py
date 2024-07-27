import math

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, reported_cost):
    cities = {
        0: (54, 87),
        1: (21, 84),
        2: (69, 84),
        3: (53, 40),
        4: (54, 42),
        5: (36, 30),
        6: (52, 82),
        7: (93, 44),
        8: (21, 78),
        9: (68, 14),
        10: (51, 28),
        11: (44, 79),
        12: (56, 58),
        13: (72, 43),
        14: (6, 99),
    }
    
    # Check if the robot starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the robot visits exactly 8 cities including the depot city
    if len(set(tour)) != 8:
        return "FAIL"
    
    # Check if the total travel cost matches the reported cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Allow a small margin for floating point arithmetic errors
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Assume a provided solution
solution_tour = [0, 2, 13, 10, 3, 4, 11, 6, 0]
solution_cost = 148.87

# Run unit test
result = verify_solution(solution_tour, solution_cost)
print(result)