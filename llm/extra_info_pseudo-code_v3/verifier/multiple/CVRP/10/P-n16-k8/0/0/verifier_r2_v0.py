import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(tours, demands, capacities, city_coords):
    all_cities_covered = [0] * len(city_coords)
    total_demand_met = [0] * len(city_coords)
    total_travel_cost_computed = 0
    robot_capacity_usage = [0] * len(tours)
    
    for i, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Tours must start and end at the depot city 0
        
        for j in range(1, len(tour)):
            city_prev = tour[j-1]
            city_current = tour[j]
            demand_current = demands[city_current]
            distance = calculate_distance(city_coords[city_prev], city_coords[city_current])
            
            # Updating total demand met
            total_demand_met[city_current] += demand_current
            # Updating robot capacity usage
            robot_capacity_usage[i] += demand_current
            # Adding distance to total travel cost
            total_travel_cost_computed += distance
            
            if robot_capacity_usage[i] > capacities[i]:
                return "FAIL"  # Robot capacity exceeded
            
        # Include the return trip to depot cost
        return_to_depot_cost = calculate_distance(city_coords[tour[-1]], city_coords[0])
        total_travel _cost_computed += return_to_depot_cost
    
    # Check if all demands are exactly met
    for city_index in range(1, len(demands)):
        if total_demand_met[city_index] != demands[city_index]:
            return "FAIL"  # Demand not fully met
    
    # Check if all cities are covered
    for tour in tours:
        for city in tour:
            all_cities_covered[city] = 1
    if sum(all_cities_covered) < len(city_coords):
        return "FAIL"  # Not all cities are covered

    # Output the total calculated cost
    print("Calculated Total Travel Cost: {:.2f}".format(total_travel_cost_computed))
    return "CORRECT"

# Define city coordinates and their corresponding demands
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
capacities = [35] * 8 

# Tours and costs provided in the solution
tours = [
    [0, 1, 0], [0, 2, 0], [0, 3, 0], [0, 4, 5, 0], [0, 6, 0], [0, 7, 0],
    [0, 8, 0], [0, 9, 10, 11, 0]
]

# Execute the verification
result = verify_solution(tours, demands, capacities, city_coords)
print("Verification Result: " + result)