def calculate_distance(city1, city2):
    import math
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Given data
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]
tours = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]
costs = [0, 0, 0, 0, 0, 0, 0, 0]

def check_all_cities_visited_once(tours):
    visited = set()
    for tour in tours:
        for city in tour:
            if city != 0:
                if city in visited:
                    return False
                visited.add(city)
    return len(visited) == 15  # Total 15 cities to visit

def check_starts_and_ends_at_depot(tours):
    return all(tour[0] == 0 and tour[-1] == 0 for tour in tours)

def check_minimize_maximum_travel_cost(tours):
    global_maximum_cost = float('inf')
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        if tour_cost > global_maximum_cost:
            global_maximum_cost = tour_cost
    # Now compare the global max cost with the given costs
    return max(costs) <= global_maximum_need_to_be_less_than_or_equal

def unit_tests():
    if not check_all_cities_visited_once(tours):
        return "FAIL"
    if not check_starts_and_ends_at_depot(tours):
        about "FAIL"
    if not check_minimize_maximum_travel_cost(tours):
        return "FAIL"
    return "CORRECT"

# Output result of unit tests
print(unit_tests())