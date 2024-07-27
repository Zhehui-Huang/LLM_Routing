import math

# Cities coordinates including the depot city
cities = [
    (145, 215),  # City 0: Depot
    (151, 264),  # City 1
    (159, 261),  # City 2
    (130, 254),  # City 3
    (128, 252),  # City 4
    (163, 247),  # City 5
    (146, 246),  # City 6
    (161, 242),  # City 7
    (142, 239),  # City 8
    (163, 236),  # City 9
    (148, 232),  # City 10
    (128, 231),  # City 11
    (156, 217),  # City 12
    (129, 214),  # City 13
    (146, 208),  # City 14
    (164, 208),  # City 15
    (141, 206),  # City 16
    (147, 193),  # City 17
    (164, 193),  # City 18
    (129, 189),  # City 19
    (155, 185),  # City 20
    (139, 182)   # City 21
]

# Tests to validate the solution
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tours, costs, overall_cost):
    city_visits = set()
    calculated_costs = []
    calculated_overall_cost = 0

    for tour in tours:
        # Check all tours start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Calculate the travel cost of each tour
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
            city_visits.add(tour[i + 1])
        calculated_costs.append(tour_cost)
    
    # Compare calculated costs with given costs
    for c1, c2 in zip(calculated_costs, costs):
        if not math.isclose(c1, c2, rel_tol=1e-9):
            return "FAIL"
    
    calculated_overall_cost = sum(calculated_costs)
    if not math.isclose(calculated_overall_cost, overall_cost, rel_tol=1e-9):
        return "FAIL"

    # Ensure each city except depot is visited exactly once
    if len(city_visits) != 21 or any(city not in city_visits for city in range(1, 22)):
        return "FAIL"

    return "CORRECT"

# Given solution
tours = [
    [0, 16, 20, 12, 8, 4, 0],
    [0, 9, 5, 1, 13, 21, 17, 0],
    [0, 6, 2, 10, 18, 14, 0],
    [0, 15, 7, 3, 11, 19, 0]
]
costs = [
    153.00366685556634,
    183.3115883251445,
    154.53797757466393,
    183.24946422163586
]
overall_cost = 674.1026969770106

# Validate the solution using the provided test framework
solution_status = verify_solution(tours, costs, overall_cost)
print(solution_status)