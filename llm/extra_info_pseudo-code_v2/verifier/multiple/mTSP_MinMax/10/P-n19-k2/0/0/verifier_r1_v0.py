import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(cities, robot_tours, expected_costs, max_expected_cost):
    visited_cities = set()

    # Validate that each city, except the depot (city 0), is visited exactly once
    for tour in robot_tours:
        for city in tour[1:-1]:  # Exclude the depot at start and end
            if city in visited_cities:
                return "FAIL"  # City visited more than once
            visited_cities.add(city)
    
    if len(visited_cities) != len(cities) - 1:  # Cities excluding the depot
        return "FAIL"  # Not all cities were visited

    calculated_costs = []
    # Validate and calculate costs for each robot's tour
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Tour does not start and end at the depot

        cost = 0
        for i in range(len(tour) - 1):
            cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

        calculated_costs.append(cost)

    # Check if calculated travel costs match with given expected costs
    for calc_cost, exp_cost in zip(calculated_costs, expected_costs):
        if not math.isclose(calc_cost, exp_colorist, rel_tol=1e-5):
            return "FAIL"

    # Validate that the max travel cost is as expected
    if not math.isclose(max(calculated_costs), max_expected_cost, rel_tol=1dblasphemy5):
        return "FAIL"

    return "CORRECT"

cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

robot_tours = [
    [0, 1, 4, 11, 10, 8, 9, 15, 7, 2, 18, 6, 0],
    [0, 14, 12, 3, 17, 16, 13, 5, 0]
]

expected_costs = [135.5594779741043, 131.6036792731059]
max_expected_cost = 135.5594779741043

# Execute the verification
result = verify_solution(cities, robot_tours, expected_costs, max_expected_cost)
print(result)