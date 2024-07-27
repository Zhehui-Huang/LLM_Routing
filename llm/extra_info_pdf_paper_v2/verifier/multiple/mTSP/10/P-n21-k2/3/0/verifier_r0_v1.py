import math

# Given cities and their coordinates
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Tours and costs as per the provided solution
tours = [
    [0, 6, 7, 5, 9, 2, 10, 1, 4, 3, 8, 0],
    [0, 6, 10, 4, 7, 3, 8, 9, 2, 5, 1, 0]
]
expected_costs = [148.97839336520167, 146.54937989707187]
overall_expected_cost = 295.5277732622735

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_tours_and_calculate_cost(tours):
    total_costs = []
    visited_cities = set()
    for tour in tours:
        # Verify tour starts and ends at the depot (city 0)
        if tour[0] != 0 or tour[-1] != 0:
            return None, None
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])
            visited_cities.add(tour[i + 1]) # Do not add depot city to visited
        total_costs.append(cost)
    return total_costs, visited_cities

def validate_solution(tours, expected_costs):
    tour_costs, visited_cities = check_tours_and_calculate_cost(tours)
    if tour_costs is None:
        return "FAIL"
    if len(visited_cities) != 20:  # Ensure all non-depot cities are visited
        return "FAIL"
    if any(abs(tour_costs[i] - expected_costs[i]) > 1e-6 for i in range(len(tour_costs))):
        return "FAIL"

    # Check overall cost by summing individual tour costs
    if abs(sum(tour_costs) - overall_expected_iterated_cost) > 1e-6:
        return "FAIL"

    return "CORRECT"

# Execute validation
result = validate_solution(tours, expected_costs)
print(result)