import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35)
    }

    tours = [
        [0, 20, 17, 9, 19, 18, 8, 13, 7, 5, 14, 0],
        [0, 12, 4, 11, 15, 3, 2, 10, 1, 6, 16, 0]
    ]

    tour_costs = [147.79, 137.52]
    max_travel_cost = 147.79

    # Check Requirement 1
    if any(tour[0] != 0 or tour[-1] != 0 for tour in tours):
        return "FAIL"

    # Check Requirement 2
    all_cities_visited = set(city for tour in tours for city in tour[1:-1])  # Exclude depot
    if len(all_cities_visited) != 20 or any(city not in all_cities_visited for city in range(1, 21)):
        return "FAIL"

    # Check Requirement 4 and Requirement 5
    calculated_costs = []
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_costs.append(round(tour_cost, 2))

    if not all(abs(calculated_costs[i] - tour_costs[i]) < 0.01 for i in range(len(tour_costs))):
        return "FAIL"

    # Requirement 3 and check against max_travel_cost
    if max(calculated_costs) != max_travel_cost:
        return "FAIL"

    # Requirement 6 is inherently satisfied given the provided data structure
    return "CORRECT"

print(test_solution())