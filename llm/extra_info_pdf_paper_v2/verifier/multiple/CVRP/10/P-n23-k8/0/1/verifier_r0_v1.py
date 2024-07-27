import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_tours_and_costs(tours, cities_coordinates, demands, robot_capacity, reported_total_cost):
    total_demand_met = [0] * len(cities_coordinates)
    all_tours_cost = 0

    for tour in tours:
        # Verify tour start and end at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        current_capacity = robot_capacity
        prev_city = tour[0]
        route_cost = 0

        for city in tour[1:]:
            if city != 0:  # Calculate cost if it's not returning to depot
                distance = euclidean_distance(cities_coordinates[prev_city], cities_coordinates[city])
                route_cost += distance
                total_demand_met[city] += demands[city]
                current_capacity -= demands[city]
                
                if current_capacity < 0:
                    return "FAIL"  # Exceeds capacity
                    
                prev_city = city
        
        # Closing the route back to the depot
        route_cost += euclidean_distance(cities_coordinates[prev_city], cities_coordinates[0])
        all_tours_cost += route_cost

    # Check demands are fully met
    if not all(original == met for original, met in zip(demands, total_demand_met)):
        return "FAIL"

    # Check if summed cost of all routes matches reported total cost
    if not math.isclose(all_tours_cost, reported_total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Setup data for verification
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40

tours = [
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
validation_result = verify_tours_and_costs(tours, cities_coordinates, demands, robot_capacity, reported_total_cost)
print(validation_result)