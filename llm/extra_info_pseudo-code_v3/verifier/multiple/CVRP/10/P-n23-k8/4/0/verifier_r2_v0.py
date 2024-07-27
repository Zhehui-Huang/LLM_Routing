# Let's perform unit tests on the provided solution
def test_solution(tours, demands, capacities, travel_costs, total_cost):
    demands_covered = [0] * len(demands)
    total_travel_cost_computed = 0

    # Check if each tour starts and ends at the depot (city 0)
    for idx, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL: Tour does not start and end at the depot.")
            return "FAIL"

        current_capacity_used = 0
        last_city = tour[0]
        
        # Check demand coverage and calculate total travel cost
        for city in tour[1:]:
            current_capacity_used += demands[city]
            demands_covered[city] += demands[city]
        
        # Verify travel costs by recalculating
        for i in range(1, len(tour)):
            total_travel_cost_computed += travel_costs[tour[i-1]][tour[i]]
        
        # Verify if capacities are exceeded
        if current_capacity_used > capacities[idx]:
            print(f"FAIL: Capacity exceeded for robot {idx}.")
            return "FAIL"

    # Verify if every demand is met exactly once
    if not all(x == y for x, y in zip(demands_covered, demands)):
        print("FAIL: Not all demands are properly covered.")
        return "FAIL"
    
    # Comparing computed travel costs with given travel costs
    computed_cost = sum(travel_costs[route[i-1]][route[i]] for route in tours for i in range(1, len(route)))
    if abs(computed_cost - total_cost) > 1e-6:
        print("FAIL: Total travel cost does not match.")
        return "FAIL"
    
    return "CORRECT"

# Given Solution details
tours = [
    [0, 21, 16, 1, 10, 13, 0],
    [0, 21, 16, 1, 10, 13, 0],
    [0, 21, 16, 1, 10, 13, 0],
    [0, 21, 16, 1, 10, 13, 0],
    [0, 21, 16, 1, 10, 13, 0],
    [0, 21, 16, 1, 10, 13, 0],
    [0, 21, 16, 1, 10, 13, 0],
    [0, 21, 16, 1, 10, 13, 0]
]
robot_capacity = 40
capacities = [robot_capacity] * 8  # There are 8 robots
total_cost = 576.70

# City demands (including the depot with 0 demand)
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Assume travel costs using Euclidean distance, need to be provided for full verification
# Here, let's mock up a plausible distance matrix based on city indices as incremental costs
travel_costs = [[0 if i == j else abs(i - j) * 2 for j in range(len(demands))] for i in range(len(demands))]

# Validation Test
print(test_solution(tours, demands, capacities, travel_costs, total_cost))