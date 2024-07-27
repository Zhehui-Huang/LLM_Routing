def verify_solution(tours, total_costs, overall_cost):
    # Define depot and cities
    depots = [0, 1, 2, 3]
    cities = list(range(4, 22))  # From city 4 to city 21

    # 1. Each robot starts and ends at its assigned depot.
    for robot, tour in enumerate(tours):
        if tour[0] != depots[robot] or tour[-1] != depots[robot]:
            return "FAIL"

    # 2. Each city must be visited exactly once by the robots combined.
    all_visited_cities = [city for tour in tours for city in tour[1:-1]]
    unique_cities = set(all_visited_cities)
    if len(all_visited_cities) != len(unique_cities) or set(cities) != unique_cities:
        return "FAIL"

    # 3. The total travel cost for all tours combined must be consistent with the reported total.
    calculated_overall_cost = sum(total_costs)
    if not (abs(calculated_overall_cost - overall_cost) < 1e-6):  # Use a small threshold for floating point comparison
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Sample data from the solution
tours = [
    [14, 0],
    [2, 1],
    [5, 2],
    [4, 3]
]

total_costs = [
    14.142135623730951,
    17.08800749063506,
    29.120439557122072,
    5.656854249492381
]

overall_total_cost = 66.00743692098047

# Verify the solution
result = verify_solution(tours, total_costs, overall_total_cost)
print(result)