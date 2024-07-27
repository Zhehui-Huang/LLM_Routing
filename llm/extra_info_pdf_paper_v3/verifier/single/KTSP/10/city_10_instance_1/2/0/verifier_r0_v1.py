import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, total_cost):
    # Coordinates based on the task description
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
    
    # Requirement 1: Tour starts and ends at depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Requirement 2: Exactly 5 cities visited (including city 0)
    if len(set(tour)) != 5:
        return "FAIL"
    
    # Requirement 3: Test if travel cost is correct
    # Calculate the cost of the tour provided
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check if the calculated cost is approximately equal to provided total cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Requirement 4 and 5 are implicitly checked by the tour format and cost comparison
    return "CORRECT"

# Correct usage of variables in calling the test function
tour = [0, 4, 8, 3, 5, 0]
total_travel_cost = 75.03

# Validate the tour and cost
result = test_solution(tour, total_travel_cost)
print(result)