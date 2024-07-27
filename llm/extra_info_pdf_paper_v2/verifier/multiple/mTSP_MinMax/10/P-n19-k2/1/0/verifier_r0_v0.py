def calculate_distance(city1, city2):
    from math import sqrt
    return sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def test_solution():
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
        15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
    }
    
    robot_0_tour = [0, 1, 4, 10, 17, 16, 9, 13, 2, 18, 0]
    robot_1_tour = [0, 11, 14, 12, 3, 8, 7, 15, 5, 6, 0]
    
    provided_costs = (147.54432418571574, 125.96603912557025)
    calculated_costs = []

    # Check Requirement 1: Each robot must start and end its tour at the depot city (city 0).
    if not (robot_0_tour[0] == robot_0_tour[-1] == robot_1_tour[0] == robot_1_tour[-1] == 0):
        return "FAIL"

    # Requirement 2: Each city (1-18) is visited exactly once
    cities_visited = robot_0_tour[1:-1] + robot_1_tour[1:-1]
    cities_expected = list(range(1, 19))
    if sorted(cities_visited) != cities_expected:
        return "FAIL"

    # Calculate and compare costs for each robot
    for tour in [robot_0_tour, robot_1_tour]:
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_costs.append(total_cost)
    if not all(abs(provided - calculated) < 0.01 for provided, calculated in zip(provided_costs, calculated_costs)):
        return "FAIL"

    # Calculate Maximum Travel Cost
    if max(calculated_costs) != max(provided_costs):
        return "FAIL"

    return "CORRECT"

# Running the test
print(test_solution())