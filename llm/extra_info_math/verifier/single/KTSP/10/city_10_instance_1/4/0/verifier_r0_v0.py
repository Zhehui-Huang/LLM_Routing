import math

# Cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def calculate_total_distance(tour):
    """ Calculate total distance for the given tour """
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(tour[i], tour[i+1])
    return total_distance

# Provided tour and total cost
solution_tour = [0, 4, 8, 3, 5, 0]
solution_cost = 110.38072506104011

def test_solution():
    # Check if the tour starts and ends at the depot city and has exactly 5 unique cities
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    if len(set(solution_tour)) != 5 + 1:  # +1 because the depot city is counted twice
        return "FAIL"
    
    # Check if the calculated tour cost matches the given total travel cost
    computed_cost = calculate_total_distance(solution_tour)
    if not math.isclose(computed_cost, solution_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Output test result
print(test_solution())