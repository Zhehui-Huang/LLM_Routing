import math

# Given data
depot = (30, 40)
cities_coordinates = [(37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
                      (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
cities = [i+1 for i in range(len(cities_coordinates))]  # 1 to 15
demands = [19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
robot_capacity = 35
tours = [
    [0, 1, 3, 0],
    [0, 2, 0],
    [0, 4, 5, 0],
    [0, 6, 0],
    [0, 7, 9, 10, 0],
    [0, 8, 11, 0],
    [0, 12, 13, 15, 0],
    [0, 14, 0]
]
tour_costs = [
    65.65945789394776,
    42.04759208325728,
    80.91453588671195,
    24.08318915758459,
    77.88124321335094,
    92.23299376151714,
    113.7054375915514,
    61.741396161732524
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tours, tour_costs):
    all_cities = set(range(1, 16))
    visited_cities = set()
    overall_cost = 0
    
    for robot_id, tour in enumerate(tours):
        # Check tour starting and ending at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check tour costs and compute again from coordinates
        calc_cost = 0
        load = 0
        previous_city = 0  # starting from depot
        
        for city in tour[1:]:
            if city != 0:  # exclude depot from demand and capacity checks
                visited_cities.add(city)
                load += demands[city - 1]
            
            # Calculate travel costs
            if previous_city == 0:
                distance = euclidean_distance(depot, cities_coordinates[city - 1])
            elif city == 0:
                distance = euclidean_distance(depot, cities_coordinates[previous_city - 1])
            else:
                distance = euclidean_distance(cities_coordinates[previous_city - 1], cities_coordinates[city - 1])
            
            calc_cost += distance
            previous_city = city
        
        # Verify calculated cost with given
        if not math.isclose(calc_cost, tour_costs[robot_id], rel_tol=1e-5):
            return "FAIL"
        
        # Check capacity
        if load > robot_capacity:
            return "FAIL"
        
        overall_cost += calc_cost
    
    # Check all cities were visited
    if all_cities != visited_cities:
        return "FAIL"
    
    # Compare overall cost
    if not math.isclose(overall_cost, sum(tour_costs), rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Test the given solution with the verification function
test_result = verify_solution(tours, tour_costs)
print(test_result)