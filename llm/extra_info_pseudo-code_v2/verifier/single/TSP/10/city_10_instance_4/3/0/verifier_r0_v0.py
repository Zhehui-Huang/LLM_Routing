import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_tsp_solution():
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
    
    solution_tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
    reported_cost = 320.79
    
    # Requirement 1: Starts and ends at the depot city 0
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit all cities exactly once
    unique_cities = set(solution_tour[1:-1])
    if len(unique_cities) != len(cities) - 1:
        return "FAIL"
    
    # Requirement 5: Correct format of the tour (starts and ends at 0)
    if not (solution_tour[0] == 0 and solution_tour[-1] == 0):
        return "FAIL"

    # Calculate the total distance
    total_distance = 0
    for i in range(len(solution_tour) - 1):
        city1 = solution_tour[i]
        city2 = solution_tour[i + 1]
        total_distance += calculate_distance(cities[city1], cities[city2])
    
    # Requirement 4 & 6: Check the distance and reported cost
    if not math.isclose(total_distance, reported_cost, abs_tol=0.1):
        return "FAIL"

    return "CORRECT"

# Run the test
print(test_tsp_solution())