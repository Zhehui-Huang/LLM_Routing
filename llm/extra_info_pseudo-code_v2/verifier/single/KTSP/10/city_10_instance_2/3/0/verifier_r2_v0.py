import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    cities = {
        0: (90, 3),
        1: (11, 17),
        2: (7, 27),
        3: (95, 81),
        4: (41, 54),
        5: (31, 35),
        6: (23, 95),
        7: (20, 56),
        8: (49, 29),
        9: (13, 17)
    }
    
    solution_tour = [0, 8, 2, 5, 3, 0]
    reported_cost = 272.8710918399864
    
    # [Requirement 1] The robot must visit exactly 6 cities, including the depot (city 0)
    if len(set(solution_tour)) != 6:
        return "FAIL - Tour does not visit exactly 6 unique cities"

    # [Requirement 2] The robot tour must start and end at the depot city (city 0)
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL - Tour does not start and end at the depot city"
    
    # [Requirement 3] Calculate the total travel cost of the tour
    calculated_cost = 0
    for i in range(len(solution_tour) - 1):
        calculated_cost += euclidean_distance(cities[solution_tour[i]], cities[solution_tour[i + 1]])
    
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL - Reported total cost does not match the calculated cost"

    # [Requirement 5] Output verification: Correct tour format and cost accuracy
    # This is partially checked by other tests, so it's mainly for ensuring format.
    if not isinstance(solution_tour, list) or not all(isinstance(city, int) for city in solution_tour):
        return "FAIL - Output format not followed correctly for the tour list"
    
    return "CORRECT"

# Run the test function
result = test_solution()
print(result)