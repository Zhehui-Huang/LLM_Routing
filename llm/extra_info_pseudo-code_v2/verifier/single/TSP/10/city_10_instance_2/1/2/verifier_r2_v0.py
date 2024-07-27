import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(depots, solution_tour, solution_cost):
    # [There are 10 cities, each with specified coordinates, including a depot city labeled 0.]
    expected_number_of_cities = 10
    if len(depots) != expected_number_of_cities:
        return "FAIL"
    
    # [The robot starts at the depot city 0.]
    # [The robot must visit all cities exactly once and then return to the depot city.]
    # [The output must include the shortest tour as a list of city indices beginning and ending at city 0.]
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    if len(set(solution_tour)) != expected_number_of_cities:
        return "FAIL"
    if sorted(solution_tour[:-1]) != list(range(expected_number_of_cities)):
        return "FAIL"
    
    # [Travel cost is calculated as the Euclidean distance between cities.]
    # [The output must include the total travel cost of the tumult.]
    calculated_cost = 0
    for i in range(len(solution_tour) - 1):
        distance = calculate_distance(depots[solution_tour[i]], depots[solution_tour[i+1]])
        calculated_cost += distance
    
    if not math.isclose(calculated_cost, solution_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
depots = [
    (90, 3),  # City 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Provided solution
solution_tour = [0, 3, 6, 4, 7, 2, 1, 9, 5, 8, 0]
solution_cost = 354.91010610434057

# Validate solution
result = validate_tour(depots, solution_tour, solution_cost)
print(result)