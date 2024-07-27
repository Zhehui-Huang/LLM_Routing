import math

def euclidean_distance(c1, c2):
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_travel_cost(tour, coordinates):
    """ Calculate the total travel cost for a given tour based on city coordinates. """
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return round(cost, 2)

def test_solution():
    coordinates = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
        (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
        (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
        (164, 193), (129, 189), (155, 185), (139, 182)
    ]

    # Provided tours and costs
    tours = [
        [0, 16, 14, 18, 15, 12, 0],
        [0, 10, 8, 6, 3, 4, 11, 0],
        [0, 17, 20, 21, 19, 13, 0],
        [0, 1, 2, 5, 7, 9, 0]
    ]
    provided_costs = [76.89, 99.61, 102.92, 111.84]
    provided_max_cost = 111.84

    # Check all cities are visited exactly once
    all_cities_visited = sum(tours, [])
    if len(set(all_cities_visited) - {0}) != 21 or all_cities_visited.count(0) != 8:
        return "FAIL"

    # Calculate and verify each tour's costs and maximum travel cost
    calculated_costs = [calculate_travel_cost(tour, coordinates) for tour in tours]
    if not all(abs(pc - cc) < 0.01 for pc, cc in zip(provided_costs, calculated_costs)):
        return "FAIL"
    
    calculated_max_cost = max(calculated_costs)
    if not abs(calculated_max_cost - provided_max_cost) < 0.01:
        return "FAIL"

    return "CORRECT"

# Execute the test
print(test_solution())