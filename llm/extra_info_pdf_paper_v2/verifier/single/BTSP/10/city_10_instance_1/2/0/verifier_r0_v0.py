def test_tsp_solution(tour, total_travel_cost, max_distance_between_cities):
    # Requirement 1: The robot starts and ends the tour at depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city must be visited exactly once by the robot.
    if sorted(tour[1:-1]) != list(range(1, 10)):
        return "FAIL"
    
    # Given data to verify distances
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }

    # Calculate distance using Euclidean formula
    def calc_distance(p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

    # Check maximum distance between consecutive cities matches
    distances = [calc_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1)]
    calculated_total = sum(distances)
    calculated_max_distance = max(distances)

    if abs(calculated_total - total_travel_cost) > 1e-5:
        return "FAIL"
    if abs(calculated_max_distance - max_distance_between_cities) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Provided tour solution
tour = [0, 0]
total_travel_cost = 0.0
max_distance_between_cities = 0

# Test the solution
print(test_tsp_solution(tour, total_travel_cost, max_distance_between_cities))