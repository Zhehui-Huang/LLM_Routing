import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(robot_tours, city_coordinates, robot_costs):
    depot = city_coordinates[0]
    num_cities = len(city_coordinates)
    visited_cities = set()
    
    overall_cost_calculated = 0.0
    
    for robot_id, tour in enumerate(robot_tours):
        # Check if the tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            print(f"FAIL: Tour for Robot {robot_id} must start and end at the depot.")
            return
        
        # Calculate travel cost and collect visited cities
        tour_cost = 0.0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
            visited_cities.add(tour[i])
        
        # Include the last city visited
        visited_cities.add(tour[-1])

        # Check if the travel cost matches the provided cost
        if not math.isclose(tour_cost, robot_costs[robot_id], rel_tol=1e-2):
            print(f"FAIL: Travel cost mismatch for Robot {robot_id}. Expected: {robot_costs[robot_id]}, Calculated: {tour_cost}")
            return
        
        overall_cost_calculated += tour_cost
    
    # Check if all cities are visited once, excluding the depot
    if len(visited_cities) != num_cities:
        print("FAIL: Not all cities were visited or some were visited multiple times.")
        return
    
    # Check if all cities except depot were visited
    if visited_cities != set(range(num_cities)):
        print("FAIL: Each city must be visited exactly once.")
        return
    
    print("CORRECT")

# Robot tours and costs
robot_0_tour = [0, 1, 3, 4, 8, 10, 11, 12, 15, 18, 19, 0]
robot_1_tour = [0, 2, 5, 6, 7, 9, 13, 14, 16, 17, 20, 0]

robot_0_cost = 212.22
robot_1_cost = 184.31

# City coordinates as given in the problem
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Call verification function
verify_solution([robot_0_tour, robot_1_tour], cities_coordinates, [robot_0_cost, robot_1_cost])