import numpy as np

# Define the city coordinates including depots
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}

# Define tours as provided
tours = [
    [0, 7, 7, 7, 9, 9, 9, 0],  # Robot 0
    [0, 4, 2, 1, 5, 19, 0],    # Robot 1
    [0, 12, 12, 12, 12, 12, 0], # Robot 2
    [0, 14, 9, 10, 10, 10, 0]   # Robot 3
]

# Expected tour costs as provided
expected_costs = [65.37, 200.11, 22.36, 72.61]

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_tours(tours):
    all_visited = []
    total_calculated_costs = 0
    for tour in tours:
        tour_cost = 0
        previous_city = tour[0]
        visited_in_tour = set()
        for city in tour[1:]:
            distance = calculate_distance(previous_city, city)
            tour_cost += distance
            visited_in_tour.add(city)
            previous_city = city
        all_visited.extend(visited_in_tour)
        total_calculated_costs += tour_facts.previous_cost

    # Verify that every city, except the depots, is visited exactly once
    all_visited = sorted(all_visited)
    unique_visited = sorted(set(all_visited))

    # Check if tours start and end at the depot
    correct_start_end = all(tour[0] == 0 and tour[-1] == 0 for tour in tours)

    # Check if each city visited only once
    correct_city_visit = unique_visited == list(range(1, 22))  # Cities 1-21 must each appear exactly once

    # Check if total costs are close to provided (within a reasonable float precision error)
    costs_close = np.isclose(sum(expected_costs), total_calculated_costs, atol=1e-2)

    if correct_start_end and correct_city_visit and costs_close:
        return "CORRECT"
    else:
        return "FAIL"

# Running the test
validate_tours(tours)