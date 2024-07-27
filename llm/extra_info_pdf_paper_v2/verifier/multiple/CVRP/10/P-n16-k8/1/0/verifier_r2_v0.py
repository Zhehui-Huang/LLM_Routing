import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Robot tour and travel information
robot_tours = [
    [0, 6, 0],
    [0, 2, 0],
    [0, 8, 11, 0],
    [0, 4, 15, 0],
    [0, 14, 3, 0],
    [0, 1, 7, 0],
    [0, 12, 5, 9, 0],
    [0, 10, 13, 0]
]
travel_costs_reported = [
    24.08318915758459, 42.04759208325728, 92.23299376151714,
    61.07512778319072, 100.9116689010483, 54.51623477273332,
    110.65372204851784, 68.2866513544927
]

# City coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# City demands and vehicle capacity
city_demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
robot_capacity = 35

# Check requirements
def check_solution(robot_tours, travel_costs_reported, city_coordinates, city_demands, robot_capacity):
    # Initialize total demands met and calculate the total travel cost
    demands_met = [0] * len(city_demands)
    total_travel_cost_calculated = 0
    
    # Check each robot's tour
    for robot_id, tour in enumerate(robot_tours):
        if tour[0] != 0 or tour[-1] != 0:
            print(f"Robot {robot_id} tour does not start or end at the depot.")
            return "FAIL"
        
        # Calculate total travel cost and check capacity
        tour_demand = 0
        last_city = tour[0]
        calculated_cost = 0
        
        for city in tour[1:]:
            tour_demand += city_demands[city]
            demands_met[city] += city_demands[city]
            # Calculate travel cost for this leg
            dist = euclidean_distance(*city_coordinates[last_city], *city_coordinates[city])
            calculated_cost += dist
            last_city = city
            
        if calculated_cost != travel_costs_reported[robot_id]:
            print(f"Travel cost discrepancy for Robot {robot_id}: {calculated_cost} instead of {travel_costs_reported[robot_id]}")
            return "FAIL"
        
        if tour_demand > robot_capacity:
            print(f"Capacity exceeded for Robot {robot_id}: {tour_demand} > {robot_capacity}")
            return "FAIL"
        
        total_travel_cost_calculated += calculated_cost
    
    if demands_met != city_demands:
        print(f"Demand mismatch: {demands_met} instead of {city_demands}")
        return "FAIL"
    
    # Optionally compare the total cost, if minimizing cost was in goal
    total_travel_costs_reported = sum(travel_costs_reported)
    if round(total_travel_costs_reported, 2) != round(total_travel_cost_calculated, 2):
        print(f"Total travel costs discrepancy: Calculated {total_travel_cost_calculated} vs Reported {total_travel_costs_reported}")
        return "FAIL"
    
    return "CORRECT"

# Run the test
output = check_solution(robot_tours, travel_costs_reported, city_coordinates, city_demands, robot_capacity)
print(output)