import math

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two city coordinates."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution():
    city_coordinates = {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
        5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
        10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
        15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
        20: (155, 185), 21: (139, 182)
    }
    
    tours = {
        0: [0, 12, 14, 15, 16, 18, 0],
        1: [0, 3, 4, 6, 8, 10, 11, 0],
        2: [0, 13, 17, 19, 20, 21, 0],
        3: [0, 1, 2, 5, 7, 9, 0]
    }

    visited_cities = set()
    for route in tours.values():
        if route[0] != 0 or route[-1] != 0:
            return "FAIL"
        visited_cities.update(route[1:-1])  # Exclude depot from visited cities

    if visited_cities != set(range(1, 22)):  # Check if all non-depot cities are visited
        return "FAIL"

    expected_costs = [121.21, 124.24, 138.25, 111.84]
    calculated_costs = []

    for route in tours.values():
        tour_cost = sum(calculate_distance(city_coordinates[route[i]], city_coordinates[route[i+1]]) for i in range(len(route) - 1))
        calculated_costs.append(round(tour_cost, 2))

    # Check each individual calculated tour cost
    if calculated_costs != expected_costs:
        return "FAIL"

    # Check overall cost
    total_cost = sum(calculated_costs)
    if round(total_cost, 2) != 495.54:
        return "FAIL"

    return "CORRECT"

# Run the verification
print(verify_solution())