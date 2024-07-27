import numpy as np

# City coordinates including depots
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}

# Given tours from the provided solution
tours = [
    [0, 7, 7, 9, 9, 9, 0],  # Robot 0
    [0, 4, 2, 1, 5, 19, 0],  # Robot 1
    [0, 12, 12, 12, 12, 12, 0], # Robot 2
    [0, 14, 9, 10, 10, 10, 0]  # Robot 3
]

# Provided expected costs
expected_costs = [65.37, 200.11, 22.36, 72.61]

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def validate_tours(tours):
    total_calculated_costs = []
    all_visited_cities = set()
    
    for tour in tours:
        tour_cost = 0
        previous_city = tour[0]
        for city in tour[1:]:
            if city != 0:
                all_visited_cities.add(city)
            distance = calculate_distance(previous_city, city)
            tour_cost += distance
            previous_city = city
        total_calculated_costs.append(tour_cost)

    # Check if every city except depots is visited exactly once
    correct_city_visits = sorted(all_visited_cities) == list(range(1, 22))

    # Check if the costs are close to expected costs
    costs_correct = all(np.isclose(real_cost, calc_cost, atol=0.01) 
                        for real_cost, calc_cost in zip(expected_costs, total_calculated_costs))

    # Calculate total cost and compare
    total_cost_correct = np.isclose(sum(expected_costs), sum(total_calculated_costs), atol=0.01)

    # Validation checks
    if correct_city_visits and costs_correct and total_cost_correct:
        return "CORRECT"
    else:
        return "FAIL"

# Run validation
print(validate_tours(tours))