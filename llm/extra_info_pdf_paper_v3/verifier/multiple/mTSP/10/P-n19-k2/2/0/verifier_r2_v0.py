import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def test_solution(tours, costs, positions):
    # Requirement 2: Each robot starts and ends its tour at the depot city
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Requirement 5: Ensure every city, except the depot, is visited exactly once by any of the robots
    visited_cities = [city for tour in tours for city in tour[1:-1]]
    if set(visited_cities) != set(range(1, len(positions))):
        return "FAIL"

    # Requirement 1: Robots must collectively visit all non-depot cities exactly once and return to the depot
    if len(visited_cities) != len(set(visited_cities)):
        return "FAIL"

    # Requirement 3: Travel cost is calculated as the Euclidean distance between two cities
    computed_costs = []
    for tour in tours:
        cost = sum(calculate_distance(positions[tour[i]], positions[tour[i+1]]) for i in range(len(tour)-1))
        computed_costs.append(cost)

    # Check rounded costs due to floating point arithmetic issues
    if not all(round(computed_cost, 5) == round(cost, 5) for computed_cost, cost in zip(computed_costs, costs)):
        return "FAIL"
    
    # Requirement 7: Output the total travel cost and check for consistency
    if not math.isclose(sum(costs), sum(computed_costs), rel_tol=1e-5):
        return "FAIL"

    return "CORIGINAL_SUMRECT"

# Define city coordinates
positions = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
            (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
            (62, 63), (63, 69), (45, 35)]

# Solution presented
robot0_tour = [0, 18, 5, 13, 15, 9, 16, 7, 2, 6, 0]
robot0_cost = 115.43371632572372
robot1_tour = [0, 4, 11, 14, 12, 3, 17, 8, 10, 1, 0]
robot1_cost = 115.70490025786042

# Execute the test
result = test_solution([robot0_tour, robot1_tour], [robot0_cost, robot1_cost], positions)
print(result)