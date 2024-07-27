import numpy as np

# Define the cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Provided solution tours and costs
solution_data = {
    0: {'tour': [0, 15, 18, 20, 17, 16, 0], 'cost': 82.77043867416609},
    1: {'tour': [1, 13, 19, 21, 14, 12, 1], 'cost': 179.47721402585648},
    2: {'tour': [2, 10, 9, 7, 5, 2], 'cost': 72.81023944083397},
    3: {'tour': [3, 6, 8, 11, 4, 3], 'cost': 65.90374418964015}
}

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(solution):
    all_cities = set(range(22))
    visited_cities = set()
    total_calculated_cost = 0.0

    for robot, data in solution.items():
        tour = data['tour']
        reported_cost = data['cost']
        tour_cost = 0.0
        
        # Check if tour starts and ends at the same depot
        if tour[0] != tour[-1] or tour[0] != robot:
            return "FAIL"
        
        # Calculate the cost and check visited cities
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            if city_to in visited_cities and city_to not in {0, 1, 2, 3}:
                return "FAIL"
            visited_cities.add(city_to)
            tour_cost += euclidean_distance(cities[city_from], cities[city_to])
        
        # Check that the computed cost matches the reported cost
        if not np.isclose(tour_cost, reported_cost, atol=0.001):
            return "FAIL"
        
        total_calculated_cost += tour_cost

    # Check if all cities are visited exactly once
    if visited_cities != all_cities:
        return "FAIL"
    
    # Check minimization of the total travel cost
    reported_total_cost = sum(data['cost'] for data in solution.values())
    if not np.isclose(total_calculated_cost, reported_total_cost, atol=0.001):
        return "FAIL"

    return "CORRECT"

# Run the verification function
print(verify_solution(solution_data))