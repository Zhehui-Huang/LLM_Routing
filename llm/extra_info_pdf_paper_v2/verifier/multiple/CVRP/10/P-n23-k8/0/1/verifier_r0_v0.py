import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_tours_and_costs(tours, cities_coordinates, robots_capacity, demands):
    total_demand_met = [0] * len(cities_coordinates)
    all_tours_cost = 0

    # Verify tour's requirements
    for robot_id, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Robots must start and end at the depot city
        
        current_capacity = robots_capacity
        prev_city = 0
        tour_cost = 0
        
        for city_idx in tour[1:]:
            distance = euclidean distance(cities_coordinates[prev_city], cities_coordinates[city_idx])
            tour_cost += distance
            total_demand_met[city_idx] += demands[city_idx]
            current_capacity -= demands[city_idx]
            if current_capacity < 0:
                return "FAIL"  # Capacity exceeded
            prev_city = city_idx
        
        # Returns to depot
        tour_cost += euclidean_distance(cities_coordinates[prev_city], cities_coordinates[0])
        all_tours_cost += tour_cost
    
    # Check if all tours cost combined equals the reported overall cost
    if not math.isclose(all_tours_cost, reported_total_cost, rel_tol=1e-9):
        return "FAIL"

    # Verify if all demands are completely met
    if any(total != demand for total, demand in zip(total_demand_met, demands)):
        return "FAIL"
    
    return "CORRECT"

# Given city coordinates (index matches city id)
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 12, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40

# Provided solution data
solution_tours = [
    [0, 18, 19, 9, 13, 0],
    [0, 19, 18, 13, 9, 0],
    [0, 3, 19, 9, 22, 0],
    [0, 19, 3, 22, 9, 0],
    [0, 8, 19, 0],
    [0, 19, 8, 0],
    [0, 3, 18, 0],
    [0, 18, 3, 0]
]

reported_total_cost = 784.3319810241186

# Run verification
result = verify_tours_and_costs(solution_tours, cities, robot_capacity, demands)
print(result)