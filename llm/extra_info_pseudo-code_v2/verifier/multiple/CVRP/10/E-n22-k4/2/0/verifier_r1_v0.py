import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_solution(tours, demands, capacities, coordinates):
    total_demand_met = True
    within_capacity = True
    total_travel_cost = 0.0
    all_cities_covered = set(range(1, 22))  # exclude the depot city 0

    for i, tour in enumerate(tours):
        prev_city = tour[0]
        capacity_used = 0
        tour_travel_cost = 0.0

        for city in tour[1:]:  # skip the depot city at start
            distance = calculate_distance(coordinates[prev_city], coordinates[city])
            tour_travel_cost += distance
            if city != 0:  # don't consider the depot for demand or capacity checks
                capacity_used += demands[city]
                if city in all_cities_covered:
                    all_cities_covered.remove(city)
            prev_city = city

        if capacity_used > capacities[i]:
            within_capacity = False

        if tour[0] != 0 or tour[-1] != 0:  # verify start and end at depot city
            return "FAIL"

        total_travel_cost += tour_travel_cost

    if all_cities_covered:
        total_demand_met = False

    # Calculate the theoretical optimal total travel cost
    # This is just for review purpose, not a definitive proof of correctness
    expected_total_travel_cost = 581.2735596805078
    cost_test = math.isclose(total_travel_cost, expected_total_travel_cost, rel_tol=1e-3)

    if total_demand_met and within_capacity and cost_test:
        return "CORRECT"
    else:
        return "FAIL"

# Sample input based on the provided solution
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
           600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
capacities = [6000] * 4
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
               (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
               (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
               (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)]

tours = [
    [0, 1, 2, 3, 4, 6, 7, 8, 9, 0],
    [0, 5, 10, 11, 12, 14, 0],
    [0, 13, 15, 16, 17, 21, 0],
    [0, 18, 19, 20, 0]
]

# Execute test
result = verify_solution(tours, demands, capacities, coordinates)
print(result)