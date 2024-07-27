import math

# Given city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Solution provided
tour = [0, 8, 0]
total_travel_cost = 97.09788875150684
max_distance_between_cities = 48.54894437575342

def calculate_euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two city coordinates."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def verify_solution(tour, total_cost, max_distance):
    """ Verify the solution with the requirements."""
    # Check if all cities are visited exactly once and start/end at depot
    if set(tour) != set(range(len(cities))) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the calculated distances match reported cost and maximum
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(tour[i], tour[i + 1])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Run verification
result = verify_solution(tour, total_travel_cost, max_distance_between_cities)
print(result)