import math

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Mockup of the solution output
solution = {
    'Robot 0 Tour': [0, 1, 2, 0],
    'Robot 0 Total Travel Cost': 50,
    'Robot 1 Tour': [0, 3, 4, 0],
    'Robot 1 Total Travel Cost': 60,
    'Overall Total Travel Cost': 110
}

# Function to validate the tours and costs
def validate_solution():
    # City coordinates including the depot
    cities = {
        0: (30, 40),
        1: (37, 52),
        2: (49, 43),
        3: (52, 64),
        4: (31, 62),
        5: (52, 33),
        6: (42, 41),
        7: (52, 41),
        8: (57, 58),
        9: (62, 42),
        10: (42, 57),
        11: (27, 68),
        12: (43, 67),
        13: (58, 27),
        14: (37, 69),
        15: (61, 33),
        16: (62, 63),
        17: (63, 69),
        18: (45, 35)
    }
    
    # Validate the number of cities
    if len(cities) != 19: return "FAIL"
    
    # Compute the actual travel cost and validate against provided values
    actual_costs = []
    for i in range(2):  # Since there are two robots
        tour_key = f'Robot {i} Tour'
        tour_cost_key = f'Robot {i} Total Travel Cost'
        
        tour = solution[tour_key]
        tour_cost = solution[tour_cost_key]
        calculated_cost = 0
        
        # Check if the tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0: return "FAIL"
        
        # Calculate the travel cost for the tour
        for j in range(1, len(tour)):
            calculated_cost += euclidean_distance(cities[tour[j-1]], cities[tour[j]])
        
        if not math.isclose(tour_cost, round(calculated_cost), rel_tol=1e-5): return "FAIL"
        actual_costs.append(calculated_cost)
    
    # Validate if all cities are visited exactly once except depot
    all_visited_cities = solution['Robot 0 Tour'][1:-1] + solution['Robot 1 Tour'][1:-1]
    unique_cities = set(all_visited_cities)
    if len(unique_cities) != 18 or len(all_visited_cities) != 18: return "FAIL"
    
    # Check the overall cost
    if not math.isclose(solution['Overall Total Travel Cost'], sum(actual_costs), rel_tol=1e-5): return "FAIL"

    return "CORRECT"

# Execute the validation function
validate_solution()