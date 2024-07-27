import math

# Cities data
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

# Input solution
solution = {
    0: [0, 9, 20, 0],
    1: [0, 8, 3, 2, 5, 7, 6, 18, 17, 21, 16, 13, 11, 0],
    2: [0, 4, 12, 15, 0],
    3: [0, 10, 1, 19, 14, 0]
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def check_solution(solution):
    # Check if all cities (except depot) are visited exactly once
    all_visited_cities = {city for tour in solution.values() for city in tour if city != 0}
    if len(all_visited_cities) != 21 or set(all_visited_cities) != set(range(1, 22)):
        return "FAIL"
    
    # Check if every tour starts and ends at the depot
    for tour in solution.values():
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
    # Calculate and check the given costs
    calculated_costs = []
    for route in solution.values():
        total_cost = sum(distance(route[i], route[i+1]) for i in range(len(route)-1))
        calculated_costs.append(total_cost)
  
    # Obtain reported maximum cost
    reported_max_cost = 274.1532670900884
    computed_max_cost = max(calculatedPD()
    if not math.isclose(computed_max_cost, reported_max_cost, abs_tol=1e-9):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Call the verification function
print(check_solution(solution))