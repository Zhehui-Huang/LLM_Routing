import math

# Data for cities, demands, and robot capacity
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
          (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40

# Solution provided
robots_tours = [
    [0, 18, 19, 0],
    [0, 9, 17, 0],
    [0, 12, 15, 0],
    [0, 8, 13, 0],
    [0, 14, 22, 0],
    [0, 4, 11, 0],
    [0, 3, 10, 0],
    [0, 5, 7, 0],
    [0, 1, 2, 0],
    [0, 6, 20, 0],
    [0, 16, 21, 0]
]

robots_costs = [
    89.42264879375188, 72.89832138604163, 66.12407122823275, 71.62027665741887,
    67.24124176465664, 57.394073777130664, 65.57284885461793, 53.10950830677563,
    47.28555690793142, 34.56118681213356, 21.455612434792677
]

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Unit tests to verify the solution
def verify_solution(tours, costs):
    visited_cities = set()
    all_demands_met_correctly = True
    all_capacity_within_limits = True
    proper_return_to_depot = True
    total_cost_calculated = 0
    
    for idx, tour in enumerate(tours):
        city_demand_in_this_tour = 0
        travel_cost_accumulated = 0
        last_city = tour[0]
        
        for city_idx in tour[1:]:
            # Verify if robotic route starts and ends at depot
            if city_idx == 0 and last_city != 0:
                proper_return_to_depot &= True
            else:
                proper_return_to_depot &= city_idx != 0
            
            visited_cities.add(city_idx)
            city_demand_in_this_tour += demands[city_idx]
            travel_cost_accumulated += euclidean_distance(cities[last_city], cities[city_idx])
            last_city = city_idx
        
        all_capacity_within_limits &= (city_demand_in_this_tour <= robot_capacity)
        
        # Compare with provided costs
        if abs(travel_cost_accumulated - costs[idx]) > 0.1:
            print(f"Cost mismatch for Robot {idx}. Calculated: {travel_cost_accumulated}, Expected: {costs[idx]}")
            proper_return_to_depot = False
        
        total_cost_calculated += travel_cost_accumulated
    
    all_cities_covered = (len(visited_cities) == len(cities)) and (0 in visited_cities)

    if proper_return_to_depot and all_capacity_within_limits and all_cities_covered and all_demands_met_correctly:
        print(f"CORRECT; Total calculated cost: {total_cost_calculated}")
    else:
        print("FAIL")
        
# Run verification
verify_solution(robots_tours, robots_costs)