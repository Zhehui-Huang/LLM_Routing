import math

# City coordinates
coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242), 
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231), 
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}

# Tours from the proposed solution
tours = [
    [0, 12, 14, 15, 16, 18, 0],
    [0, 3, 4, 6, 8, 10, 11, 0],
    [0, 13, 17, 19, 20, 21, 0],
    [0, 1, 2, 5, 7, 9, 0]
]

# Calculated total costs from the proposed solution
costs = [121.20933003054614, 124.23927957725854, 138.2546749628742, 111.83855721201843]
max_cost = 138.2546749628742

def calculate_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to validate the solution
def validate_solution(tours, costs, max_proposed_cost):
    cities_visited = set()
    calculated_costs = []
    number_of_robots = len(tours)
    
    # Check all cities are visited once and tours start and end at the depot (city 0)
    for tour in tours:
        # Check starting and ending at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        # Collect all visited cities
        cities_visited.update(tour[1:-1])  # exclude the depot city from count
        
        # Calculate and compare costs
        tour_cost = sum(c, float(calculate_distance(tour[i], tour[i + 1])) for i in range(len(tour) - 1))
        calculated_costs.append(tour_cost)
    
    # Check all cities are visited exactly once
    if len(cities_visited) != 21 or any(cities_visited.difference(set(range(1, 22)))):
        return "FAIL"
    
    # Check if the calculated costs match the given costs approximately
    if not all(math.isclose(costs[i], calculated_costs[i], abs_tol=0.01) for i in range(number_of_robots)):
        return "FAIL"
    
    # Check the maximum cost
    if not math.isclose(max(calculated_costs), max_proposed_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Output the validation result
print(validate_solution(tours, costs, max_cost))