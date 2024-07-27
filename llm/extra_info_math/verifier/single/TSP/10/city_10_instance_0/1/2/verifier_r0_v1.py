import math

# Given city coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Solution tour and reported travel cost
solution_tour = [0, 7, 6, 1, 2, 3, 8, 4, 9, 5, 0]
reported_cost = 271.47162187533536

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def validate_solution(tour, cost):
    # Check that tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check that all other cities are visited exactly once
    visited_cities = tour[1:-1]
    if len(visited_cities) != len(set(visited_cities)) or len(visited_cities) != len(cities) - 1:
        return "FAIL"
    
    # Calculate the actual travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(tour[i], tour[i + 1])
    
    # Check if the calculated cost matches the reported cost
    if not math.isclose(calculated_cost, cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run the validation
validation_result = validate_solution(solution_tour, reported_cost)
print(validation_result)  # Correct printing of the variable validation_result