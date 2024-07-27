import math

# Define the city coordinates including the depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
    19: (63, 69), 20: (45, 35)
}

# Solution provided
robots_tours = [
    [0, 16, 6, 20, 2, 10, 12, 4, 8, 18, 14, 0],
    [0, 1, 15, 11, 3, 19, 13, 9, 17, 5, 7, 0]
]

def calculate_distance(city1, city2):
    """ Helper function to calculate the Euclidean distance between two cities. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_robots_visiting_all_cities_exactly_once(robots_tours):
    all_visited_cities = set()
    for tour in robots_tours:
        visited_cities = set(tour[1:-1])  # Exclude the starting and ending depots
        all_visited_cities.update(visited_cities)
    return all_visited_cities == set(range(1, 21))

def test_start_end_at_depot(robots_tours):
    return all(tour[0] == tour[-1] == 0 for tour in robots_tours)

def calculate_total_travel_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def test_solutions(robots_tours):
    provided_costs = [171.820768703562, 155.21957976604313]
    calculated_costs = [calculate_total_travel_cost(tour) for tour in robots_tours]

    if not test_start_end_at_depot(robots_tours):
        return "FAIL"
    if not test_robots_visiting_all_cities_exactly_once(robots_tours):
        return "FAIL"
    if not all(abs(pc - cc) < 1e-4 for pc, cc in zip(provided_costs, calculated_costs)):
        return "FAIL"
    if not abs(sum(provided_costs) - sum(calculated_costs)) < 1e-4:
        return "FAIL"
    
    return "CORRECT"

# Running the improved test
print(test_solutions(robots_tours))