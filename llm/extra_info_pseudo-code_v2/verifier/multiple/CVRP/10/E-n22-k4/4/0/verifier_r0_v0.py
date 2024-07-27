import math

# City data - coordinates and demands
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
]
city_demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 
    1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700
]

# Robot tour and cost data from the solution
robot_tours = {
    0: [0, 1, 2, 3, 4, 2, 1, 8, 0],  # This should be analyzed for feasibility
    1: [0, 0],
    2: [0, 0],
    3: [0, 0]
}
robot_costs = [
    182.15274112373024, 0.0, 0.0, 0.0
]

def calculate_distance(c1, c2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def check_solution():
    total_supply_delivered = [0] * 22
    robot_capacities = [6000] * 4  # Each robot has a carrying capacity of 6000 units
    
    # Check all robots
    robot_number = 0
    for tour, cost in zip(robot_tours.values(), robot_costs):
        route_demand = 0
        actual_cost = 0
        last_city = 0
        
        # Ensure tours start and end at the depot and calculate cost
        if tour[0] != 0 or tour[-1] != 0:
            print(f"Robot {robot_number} FAIL: Tour does not start and end at depot")
            return "FAIL"
        
        # Check demand fulfillment and route costs
        for i in range(1, len(tour)):
            city = tour[i]
            if city != 0:
                route_demand += city_demands[city]
                total_supply_delivered[city] += city_demands[city]
            # Calculate travel cost
            actual_cost += calculate_distance(cities[last_city], cities[city])
            last_city = city
        
        if route_demand > robot_capacities[robot_number]:
            print(f"Robot {robot_number} FAIL: Capacity exceeded")
            return "FAIL"
        
        if not math.isclose(actual_cost, cost, abs_tol=0.01):
            print(f"Robot {robot_number} FAIL: Reported cost {cost} does not match calculate cost {actual_number}")
            return "FAIL"
        
        robot_number += 1
        
    # Check if all demands are met
    for i in range(1, len(total_supply_delivered)):
        if total_supply_delivered[i] != city_demands[i]:
            print(f"City {i} FAIL: Demand not met")
            return "FAIL"
        
    print("All conditions met")
    return "CORRECT"

# Verify the solution
result = check_solution()
print(result)