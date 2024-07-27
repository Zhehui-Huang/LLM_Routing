import math

def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, city_demands, city_coordinates, robot_capacity):
    total_demand_met = [0] * len(city_demands)
    robot_loads = [0] * len(tours)
    total_travel_costs = []

    for robot_id, tour in enumerate(tours):
        prev_city = tour[0]
        
        if tour[0] != 0 or tour[-1] != 0:  # Start and end at the depot
            return "FAIL"
        
        travel_cost = 0
        for city in tour[1:]:
            if city != 0:  # Assuming no reloading at depot within tour
                robot_loads[robot_id] += city_demands[city]
                if robot_loads[robot_id] > robot_capacity:
                    return "FAIL"
            
            travel_cost += compute_distance(city_coordinates[prev_city], city_coordinates[city])
            total_demand_met[city] += city_demands[city]
            prev_city = city

        total_travel_costs.append(travel_cost)
        travel_cost += compute_distance(city_coordinates[prev_city], city_coordinates[0])  # return to depot
        total_travel_costs[-1] = round(travel_cost, 2)
    
    # Confirm all demands are met and correct total travel costs
    if any(demand != met for demand, met in zip(city_demands, total_demand_met)):
        return "FAIL"

    # Confirm the total travel costs are as specified
    expected_costs = [130.98, 154.49, 144.20, 124.18]
    if not all(math.isclose(tc, ec, abs_tol=0.01) for tc, ec in zip(total_travel_costs, expected_costs)):
        return "FAIL"
    
    expected_overall_cost = 553.85
    overall_cost = sum(total_travel_costs)
    if not math.isclose(overall_cost, expected_overall_cost, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Define cities, demands, and coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

city_demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 
                1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

robot_capacity = 6000

# Define robot tours
tours = [
    [0, 14, 17, 20, 21, 16, 8, 0],
    [0, 19, 18, 15, 12, 6, 0],
    [0, 13, 11, 3, 2, 7, 9, 10, 0],
    [0, 5, 1, 4, 0]
]

# Verify the solution
output = verify_solution(tours, city_demands, city_coordinates, robot_capacity)
print(output)