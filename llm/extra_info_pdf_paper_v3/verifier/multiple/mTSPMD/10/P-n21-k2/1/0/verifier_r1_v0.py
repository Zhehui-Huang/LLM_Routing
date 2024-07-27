import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, total_costs, all_cities_coords, depot_cities):
    # Create a list to verify if all cities are visited
    all_cities_visited = set()
    
    # Calculate travel cost from tours and compare with given total_costs
    calculated_costs = []
    
    # Verify each robot's tour
    for index, tour in enumerate(tours):
        tour_cost = 0
        previous_city = tour[0]
        
        # Start and end at the depot check
        if tour[0] != depot_cities[index] or tour[-1] != depot_cities[index]:
            return "FAIL"
        
        # Calculate the cost and accumulate visited cities
        for city in tour[1:]:
            tour_cost += calculate_distance(all_cities_coords[previous_city], all_cities_coords[city])
            previous_city = city
            all_cities_visited.add(city)
        
        calculated_costs.append(tour_cost)
        # Verify that the cost is close to the given cost (considering rounding).
        if not math.isclose(tour_cost, total_costs[index], rel_tol=1e-4):
            return "FAIL"
    
    # Verify all cities visited exactly once
    if sorted(all_cities_visited) != list(range(21)):
        return "FAIL"
    
    # Verify overall total cost
    if not math.isclose(sum(calculated_costs), sum(total_costs), rel_tol=1e-4):
        return "FAIL"
    
    return "CORRECT"

# Test Input:
all_cities_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

robot_0_tour = [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 17, 14, 5, 20, 6, 7, 2, 0]
robot_1_tour = [1, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 0, 10, 12, 15, 4, 11, 3, 8, 18, 19, 1]

robot_0_cost = 208.84408586170917
robot_1_cost = 236.87921612619309

total_costs = [robot_0_cost, robot_1_cost]

# Depots
depot_cities = [0, 1]

# Verify the solution
solution_status = verify_solution(tours=[robot_0_tour, robot_1_tour], total_costs=total_costs,
                                  all_cities_coords=all_cities_coords, depot_cities=depot_cities)
print(solution_status)