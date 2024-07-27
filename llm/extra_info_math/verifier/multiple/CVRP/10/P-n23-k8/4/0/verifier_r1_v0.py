import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, demands, capacities, coordinates):
    # Checking each city is visited once
    visited = set()
    for tour in tours:
        for city in tour[1:-1]:  # exclude the depot at the start and end
            if city in visited:
                return "FAIL"
            visited.add(city)
    
    if len(visited) != len(coordinates) - 1:  # excluding the depot
        return "FAIL"
    
    # Check demands and capacities
    for tour in tours:
        total_demand = 0
        for city in tour[1:-1]:
            total_demand += demands[city]
        if total_demand > capacities:
            return "FAIL"
        
    # Check that all start and end at the depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Check if the total travel cost is as reported (minimal not directly verified)
    total_calculated_cost = 0
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        if tour_cost != float(tour[-1]):
            return "FAIL"
        total_calculated_cost += tour_cost
        
    # Verifying reported overall total travel cost
    reported_cost = tours[-1][1]  # overall total cost reported
    
    if abs(total_calculated_cost - reported_cost) > 0.0001:
        return "FAIL"
    
    return "CORRECT"

# Mock data based from given example output
n_cities = 23
demands = {0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8, 10: 8, 11: 7, 12: 14, 
           13: 6, 14: 19, 15: 11, 16: 12, 17: 26, 18: 17, 19: 6, 20: 15, 21: 5, 22: 10}
coordinates = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
               6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
               12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
               18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)}
capacities = 40
robot_tours = [
    [0, 21, 11, 3, 5, 0, 87.98192371896843]
]

# Calculating the overall cost of all tours
overall_cost = 87.98192371896843
robot_tours.append(["Overall Total Travel Cost", overall_cost])

result = verify_solution(robot_tours, demands, capacities, coordinates)
print(result)