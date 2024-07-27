def verify_solution(robots_tours, robots_costs, city_demands, robot_capacity):
    visited_cities = set()
    total_travel_cost = 0
    all_cities = set(range(1, len(city_demands) + 1))  # Excluding depot, fixing range
  
    # Loop through each robot's data
    for robot_id, tour in enumerate(robots_tours):
        # Start and end at depot validation
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Total cost calculation
        total_travel_cost += robots_costs[robot_id]
  
        # Validate capacity constraint
        total_demand = 0
        for city in tour[1:-1]:  # Exclude the depot city at start and end
            total_demand += city_demands[city]
            if city in visited_cities:
                return "FAIL"  # City visited more than once
            visited_cities.add(city)
        
        if total_demand > robot_capacity:
            return "FAIL"
  
    # Check if all cities were visited
    if visited_cities != all_cities:
        return "FAIL"

    # Total calculated cost from robot tours compared to actual provided total costs
    calculated_total_travel_cost = sum(robots_costs)
    if total_travel_cost != calculated_total_travel_cookie_cost:
        return "FAIL"

    # Since all checks have passed:
    return "CORRECT"

# Sample data to test the verification
robots_tours = [
    [0, 10, 0], [0, 14, 0], [0, 12, 0], [0, 16, 0]
]
robots_costs = [
    34.52535300326414, 14.142135623730951, 22.360679774997898, 19.697715603592208
]
city_demands = {
    1: 1100, 2: 700, 3: 800, 4: 1400, 5: 2100, 6: 400, 7: 800, 8: 100, 9: 500,
    10: 600, 11: 1200, 12: 1300, 13: 1300, 14: 300, 15: 900, 16: 2100, 17: 1000,
    18: 900, 19: 2500, 20: 1800, 21: 700
}
robot_capacity = 6000

# Test the solution
result = verify_solution(robots_tours, robots_costs, city_demands, robot_capacity)
print(result)  # This should output "CORRECT" or "FAIL" based on the solution's correctness.