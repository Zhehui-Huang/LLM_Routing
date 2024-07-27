import math

# Coordinates of cities including depots
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

# Sample tours provided in the problem description
tours_details = [
    {"tour": [0, 1, 10, 17, 16, 8, 3, 12, 14, 11, 4, 18, 6, 2, 7, 9, 15, 13, 5, 0], "cost": 204.57994811313367},
    {"tour": [0, 6, 18, 1, 10, 12, 14, 11, 4, 8, 3, 17, 16, 9, 15, 13, 5, 7, 2, 0], "cost": 206.61632650246156}
]

def calculate_tour_cost(tour):
    """Calculate the total travel cost for a given tour based on Euclidean distance."""
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        total_cost += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return total_cost

def verify_tours():
    all_cities_visited = set(range(19))  # Set of all city indices
    tours_cities_visited = set()
    
    for details in tours_details:
        tour = details["tour"]
        reported_cost = details["cost"]
        calculated_cost = calculate_tour_cost(tour)
        
        # Start and end at the depot:
        if not (tour[0] == tour[-1] and tour[0] in [0, 1]):
            return "FAIL: Tour must start and end at the same depot"
        
        # Ensure all cities are visited exactly once:
        tours_cities_visited.update(tour[1:-1])
        
        # Checking cost with a tolerance due to potential float precision issues:
        if not math.isclose(reported_cost, calculated_cost, abs_tol=1e-6):
            return "FAIL: Incorrect travel cost calculation"
    
    if tours_cities_visited != all_cities_visited:
        return "FAIL: Not all cities are visited or some cities are visited more than once"
    
    return "CORRECT"

# Running the verification function
result = verify_tours()
print(result)