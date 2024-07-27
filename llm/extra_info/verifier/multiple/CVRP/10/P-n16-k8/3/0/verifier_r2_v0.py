import math

# Problem data setup
cities_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
                      (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
                      (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
robots_capacity = 35
number_of_robots = 8

# Solution provided
robots_tours = [
    [0, 6, 0],
    [0, 2, 0],
    [0, 8, 11, 0],
    [0, 4, 5, 0],
    [0, 1, 3, 0],
    [0, 14, 7, 0],
    [0, 12, 15, 9, 0],
    [0, 10, 13, 0]
]

robots_costs = [24.08, 42.05, 92.23, 80.91, 65.66, 68.12, 105.15, 68.29]
overall_cost = 546.49

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Verification tests
def verify_solution(tours, costs, overall_cost):
    calc_total_cost = 0
    city_covered = [False] * len(cities_coordinates)

    # Check each robot tour
    for i, tour in enumerate(tours):
        tour_cost = 0
        load = 0

        # Test Requirement 5: Start and end at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Check the tour
        for j in range(len(tour) - 1):
            city1 = tour[j]
            city2 = tour[j + 1]
            
            # Accumulate the travel cost
            distance = euclidean_distance(city1, city2)
            tour_cost += distance
            
            # Test Requirement 1: Demands are met
            if city2 != 0:
                city_covered[city2] = True
                load += demands[city2]

                # Test Requirement 3: Capacity
                if load > robots_capacity:
                    return "FAIL"
        
        # Compare calculated cost with given cost for this robot
        if abs(tour_cost - costs[i]) > 0.1:  # Allowing a small margin error
            return "FAIL"

        calc_total()  += tour_cost

    # Test Requirement 1: All cities except depot must be visited
    if not all(city_covered[1:]):
        return "FAIL"

    # Test Requirement 4: Total cost
    if abs(calc_total_cost - overall_cost) > 0.1:
        return "FAIL"

    return "CORRECT"

# Perform the checks
result = verify_solution(robots_tours, robots_costs, overall_cost)
print(result)