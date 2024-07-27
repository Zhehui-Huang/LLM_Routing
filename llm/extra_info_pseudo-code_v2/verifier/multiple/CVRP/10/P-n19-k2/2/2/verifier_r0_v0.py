import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tours, capacities, demands, coordinates, total_costs):
    # Check if all tours start and end at the depot (city 0)
    if any(t[0] != 0 or t[-1] != 0 for t in tours):
        return "FAIL"

    # Check if the demands are met and capacities are not exceeded
    total_demand_covered = [0] * len(demands)
    for i, tour in enumerate(tours):
        current_capacity = 0
        for j in range(1, len(tour) - 1):  # excluding the depot start and end
            city = tour[j]
            total_demand_covered[city] += demands[city]
            current_capacity += demands[city]
        if current_capacity > capacities[i]:
            return "FAIL"

    # Check if every city's demand is fully met
    if any(demand != covered for demand, covered in zip(demands, total_demand_covered[1:])):
        return "FAIL"
    
    # Check the total travel costs for each robot and overall
    calculated_costs = []
    overall_calculated_cost = 0.0
    for tour in tours:
        tour_cost = 0.0
        for k in range(len(tour) - 1):
            tour_cost += euclidean_distance(coordinates[tour[k]], coordinates[tour[k + 1]])
        calculated_costs.append(tour_cost)
        overall_calculated_cost += tour_cost

    # Check if the costs match
    if not all(math.isclose(tc, cc, rel_tol=1e-9) for tc, cc in zip(total_costs, calculated_costs)):
        return "FAIL"
    
    if not math.isclose(sum(total_costs), overall_calculated_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Example test cases:

# Test environment setup
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
capacities = [160, 160] 
tours = [
    [0, 1, 0],
    [0, 2, 0]
]
total_costs = [27.784887978899608, 38.47076812334269]
overall_cost = 66.2556561022423

# Run verification
print(verify_solution(tours, capacities, demands, coordinates, total_costs))