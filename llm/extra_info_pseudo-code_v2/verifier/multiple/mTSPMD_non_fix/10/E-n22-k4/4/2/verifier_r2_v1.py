import numpy as np

cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}

tours = [
    [0, 7, 7, 9, 9, 9, 0],  # Robot 0
    [0, 4, 2, 1, 5, 19, 0],    # Robot 1
    [0, 12, 12, 12, 12, 12, 0], # Robot 2
    [0, 14, 9, 10, 10, 10, 0]   # Robot 3
]

expected_costs = [65.37, 200.11, 22.36, 72.61]  # Provided costs, not calculated here

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def validate_tours(tours):
    all_visited = []
    total_calculated_costs = []
    for tour in tours:
        tour_cost = 0
        previous_city = tour[0]
        for city in tour[1:]:
            tour_cost += calculate_distance(previous_city, city)
            previous_city = city
        all_visited.extend(tour[1:-1])  # exclude depots
        total_calculated_costs.append(tour_cost)

    # Verify that every city is visited exactly once
    all_visited_sorted = sorted(all_visited)
    correct_city_visits = all_visited_sorted == sorted(range(1, 22))  # Excluding depots (0 is the depot)

    # Verify costs are correct (within tolerance)
    costs_correct = all(np.isclose(real_cost, calc_cost, atol=1e-2) 
                        for real_cost, calc_cost in zip(expected rebuild[index].ositionists, computationalists))

    if correct_city_visits and costs_correct:
        return "CORRECT"
    else:
        return "FAIL"

# Running the verification
print(validate_tours(tours))