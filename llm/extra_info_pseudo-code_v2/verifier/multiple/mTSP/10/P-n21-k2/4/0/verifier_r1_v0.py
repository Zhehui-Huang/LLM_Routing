import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, tours, calculated_costs):
    visited = set()
    num_cities = len(cities)
    num_robots = len(tours)
    total_cost_computed = 0.0

    # Check if all tours start and end at the depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Check if each city is visited exactly once and calculate costs
    for idx, tour in enumerate(tours):
        for i in range(1, len(tour)):
            if tour[i] in visited:
                return "FAIL"
            visited.add(tour[i])
        
        # calculate travel cost
        tour_cost = 0.0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        
        # Compare calculated cost with provided cost
        if not math.isclose(tour_cost, calculated_costs[idx], abs_tol=0.01):
            return "FAIL"
        
        total_cost_computed += tour_cost

    # Check if every city except depot is visited
    if len(visited) != num_cities - 1:
        return "FAIL"

    # Check number of robots
    if num_robots != 2:
        return "FAIL"

    # Check overall cost
    overall_cost = sum(calculated_costs)
    if not math.isclose(total_cost_computed, overall_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Given data and solution
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

robot0_tour = [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 0]
robot1_tour = [0, 6, 20, 5, 7, 2, 13, 9, 17, 14, 19, 0]
robot0_cost = 135.57
robot1_cost = 160.83
overall_cost = 296.4

# Running the test
result = verify_solution(cities_coordinates, [robot0_tour, robot1_tour], [robot0_cost, robot1_cost])
print(result)