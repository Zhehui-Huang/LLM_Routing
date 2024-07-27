import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cities data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Solution to verify
robots_tours = [
    (0, [0, 1, 2, 0], 47.29),
    (1, [0, 3, 4, 0], 75.68),
    (2, [0, 5, 6, 0], 47.93),
    (3, [0, 7, 8, 0], 72.19),
    (4, [0, 9, 10, 0], 77.87),
    (5, [0, 11, 12, 0], 74.16),
    (6, [0, 13, 14, 0], 80.99),
    (7, [0, 15, 0], 59.67)
]

# Verify requirements
def verify_solution(robots_tours):
    total_cost = 0
    visited_cities = set()
    
    # Check requirements 2, 4, 5
    for robot, tour, reported_cost in robots_tours:
        # Calculate tour cost
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        
        # Rounding to 2 decimal places for consistency with reported costs
        tour_cost = round(tour_cost, 2)
        
        if tour_cost != reported_cost:
            return "FAIL"
        
        total_cost += tour_cost
        
        # Include visited cities, excluding the depot
        visited_cities.update(tour[1:-1])
        
        # Start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Check requirement 1
    if len(visited_cities) != 15:  # 16 cities total, excluding the depot city 0
        return "FAIL"
    
    # Accumulate total cost and verify against overall cost
    rounded_overall_cost = round(total_cost, 2)
    if rounded_overall_cost != 535.77:
        return "FAIL"
    
    return "CORRECT"

# Execute verification
result = verify_solution(robots_tours)
print(result)