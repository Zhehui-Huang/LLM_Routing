import numpy as np
from itertools import chain

# Constants
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232),
    11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185),
    21: (139, 182)
}

# Solutions
solutions = [
    [0, 14, 10, 8, 9, 7, 0],
    [1, 5, 6, 12, 18, 15, 1],
    [2, 19, 17, 21, 20, 13, 2],
    [3, 4, 11, 16, 3]
]

def calculate_distance(city1, city2):
    return np.linalg.norm(np.array(cities[city1]) - np.array(cities[city2]))

def total_route_cost(route):
    return sum(calculate_distance(route[i], route[i + 1]) for i in range(len(route) - 1))

def check_requirements():
    # Requirement 1: All cities visited exactly once excluding depots
    all_cities_visited = sorted(list(chain.from_iterable(sol[:-1] for sol in solutions)))
    if len(set(all_cities_visited)) != 22 or sorted(all_cities_visited) != list(range(22)):
        return "FAIL"
    
    # Requirement 2: Each robot starts and ends at their respective depots
    for idx, tour in enumerate(solutions):
        if tour[0] != idx or tour[-1] != idx:
            return "FAIL"
    
    # Requirement 3 (Example Calculation): Check if total costs are minimized (we could not exactly validate the minimisation without comparing to optimal, but here we calculate the expected)
    expected_costs = [total_route_cost(solution) for solution in solutions]
    print("Individual Robot Costs:")
    print('\n'.join(f"Robot {i} Total Travel Cost: {cost}" for i, cost in enumerate(expected_costs)))
    
    overall_cost = sum(expected_costs)
    print(f"Overall Total Travel Cost: {overall_detail}")
    
    print("Calculation finished. Unable to validate actual minimization without optimal solutions.")

    # Other requirements are related to the algorithm approach and cannot be directly evaluated by the solution.
    return "CORRECT"

# Perform the test
result = check_requirements()
print("Validity of the solution based on given requirements:", result)