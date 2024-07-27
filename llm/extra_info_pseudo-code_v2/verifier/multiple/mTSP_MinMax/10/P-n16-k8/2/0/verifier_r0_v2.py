import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two points. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tours, costs):
    """ Test the provided solution for correctness. """
    # Define City Coordinates
    coords = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
        6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
    }

    # Check all cities are visited exactly once excluding depot
    visited_cities = set()
    for tour in tours:
        for city in tour[1:-1]:  # Skip the depot cities at start and end
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)

    # Ensure all cities, except the depot, are visited
    if visited_cities != set(range(1, 16)):
        return "FAIL"

    # Ensure total distances match with provided costs
    for tour, reported_cost in zip(tours, costs):
        calculated_cost = 0
        for i in range(len(tour) - 1):
            calculated_cost += calculate_distance(coords[tour[i]], coords[tour[i + 1]])
        if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-2):
            return "FAIL"

    # Ensure that tours start and end at the depot 0
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Ensure exactly 8 robots' tours are provided
    if len(tours) != 8:
        return "FAIL"

    return "CORRECT"

# Test the implementation
tours = [
    [0, 0],
    [0, 13, 9, 10, 11, 0],
    [0, 5, 15, 0],
    [0, 0],
    [0, 6, 3, 12, 2, 0],
    [0, 0],
    [0, 7, 0],
    [0, 14, 8, 1, 4, 0]
]
costs = [0.0, 108.09, 91.92, 0.0, 86.61, 0.0, 44.05, 116.45]

# Execute the test and print results
solution_status = test_solution(tours, costs)
print(solution_status)