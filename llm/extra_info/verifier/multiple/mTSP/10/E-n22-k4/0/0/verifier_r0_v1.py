import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(city_coordinates, tours, expected_costs, expected_total_cost):
    city_visit_count = [0] * len(city_coordinates)
    
    # Verify each robot's tour
    for tour, expected_cost in zip(tours, expected_costs):
        travel_cost = 0
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i+1]
            travel_cost += calculate_distance(city_coordinates[city1], city_coordinates[city2])
            city_visit_count[city2] += 1

        # Check calculated cost against expected cost
        if not math.isclose(travel_cost, expected_cost, rel_tol=1e-9):
            return "FAIL"

    # Check that every city except the depot is visited exactly once
    if any(count != 1 for index, count in enumerate(city_visit_count) if index != 0):
        return "FAIL"

    # Verify overall total cost
    if not math.isclose(sum(expected_costs), expected_total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City Coordinates (Indexed by city number)
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Robot Tours and Expected Costs:
tours = [
    [0, 4, 3, 1, 2, 5, 0],
    [0, 10, 8, 6, 7, 9, 0],
    [0, 12, 15, 14, 13, 11, 0],
    [0, 16, 19, 17, 20, 18, 0]
]

expected_costs = [
    126.62572299222708,  # Robot 0
    84.05184209569894,   # Robot 1
    99.62431226939509,   # Robot 2
    101.52078554834101   # Robot 3
]

expected_total_cost = 411.8226629056621

# Execute tests
result = verify_solution(city_coordinates, tours, expected_costs, expected_total_cost)
print(result)