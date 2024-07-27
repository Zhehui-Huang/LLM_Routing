import math

# Cities and their coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# City groups
city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Provided tour and cost
solution_tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
solution_cost = 371.1934423276749

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def verify_solution(tour, expected_cost):
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited = tour[1:-1]  # remove depot cities from check
    for group in city_groups:
        if sum(1 for city in group if city in visited) != 1:
            return "FAIL"
    
    # Check if the total travel path is as given (this implicitly checks the min distance condition)
    calculated_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    # Allowing a small margin for floating point arithmetic comparisons
    if not math.isclose(calculated_cost, expected_cost, abs_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Run the verification
result = verify_solution(solution_tour, solution_cost)
print(result)