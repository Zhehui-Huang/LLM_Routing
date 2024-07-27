def verify_solution(tours, total_costs, overall_cost):
    # Verify each node is visited exactly once
    all_cities = set(range(4, 22))  # Customer cities are 4 to 21
    visited_cities = set()

    for tour in tours:
        for city in tour[1:-1]:  # exclude the depots
            visited_cities.add(city)

    if visited_cities != all_cities:
        return "FAIL"

    # Verify each salesman returns to their starting depot
    for tour in tours:
        if tour[0] != tour[-1]:
            return "FAIL"

    # Verify the total travel costs
    computed_overall_cost = sum(total_costs)
    if not (abs(computed_overall_cost - overall_cost) < 1e-5):
        return "FAIL"

    return "CORRECT"

# Given data from the MILP solution
tours = [
    [0, 12, 15, 18, 19, 21, 0],
    [1, 2, 5, 6, 7, 8, 9, 10, 14, 16, 17, 20, 1],
    [1, 2, 2],  # This is an issue, a repetition of node 2 in tour of Robot 2
    [3, 4, 11, 13, 3]
]
total_costs = [
    76.7737910064653,
    104.61941205966724,
    17.08800749063506,
    39.71562698134518
]
overall_cost = 238.1968375381128

# Call verification function
result = verify_solution(tours, total_costs, overall_cost)
print(result)