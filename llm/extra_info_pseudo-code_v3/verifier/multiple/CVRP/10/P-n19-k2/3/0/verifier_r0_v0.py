import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(robots_tours, demands, capacities, city_coordinates):
    total_demand_met = [0] * len(city_coordinates)
    total_capacity_used = [0] * len(capacities)
    
    # Calculate the actual total demands and count the capacities
    for robot_id, tour in enumerate(robots_tours):
        last_city = 0  # default start at depot city 0
        for city in tour[1:-1]:  # exclude the initial (0) and final (0) depot visits
            total_demand_met[city] += demands[city]
            total_capacity_used[robot_id] += demands[city]
            last_city = city
        if total_capacity_used[robot_id] > capacities[robot_id]:
            return "FAIL"
    
    # Verify start and end at depot city and demands met
    for robot_id, tour in enumerate(robots_tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    if total_demand_met[1:] != demands[1:]:  # City 0 demand doesn't count
        return "FAIL"

    return "CORRECT"

# Input Data:
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
capacities = [160, 160]
city_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]

robot_0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 16, 0]
robot_1_tour = [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 13, 0]
robots_tours = [robot_0_tour, robot_1_tour]

# Test the solution
print(verify_solution(robots_tours, demands, capacities, city_coordinates))