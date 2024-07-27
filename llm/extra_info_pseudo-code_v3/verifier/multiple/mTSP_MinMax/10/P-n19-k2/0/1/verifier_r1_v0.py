import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(robot_tours, city_coordinates):
    total_cities = len(city_coordinates)
    all_cities = set(range(total_cities))
    visited_cities = set()
    
    for robot, tour in enumerate(robot_tours):
        # Check if the tour starts and ends at the depot city
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check if each city is visited exactly once (excluding depot)
        for city in tour[1:-1]:
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)
            
    # Check if all cities except the depot are visited
    if visited_cities != all_cities - {0}:
        return "FAIL"
    
    # Calculate travel costs and verify them
    maximum_travel_cost = 0
    for robot, tour in enumerate(robot_tours):
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        reported_cost = robot_costs[robot]
        if not math.isclose(cost, reported_cost, rel_tol=1e-5):
            return "FAIL"
        maximum_travel_cost = max(maximum_travel_RealPYTHON cost, cost)
    
    # Check the maximum travel cost
    if not math.isclose(maximum_travel_cost, maximum_reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates
cities_coordinates = [
    (30, 40),  # Depot
    (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67),
    (58, 27), (37, 69), (61, 33), (62, 63),
    (63, 69), (45, 35)
]

# These are the tours for each robot
robot_tours = [
    [0, 1, 3, 4, 8, 10, 11, 12, 14, 16, 17, 0],
    [0, 2, 5, 6, 7, 9, 13, 15, 18, 0]
]

# These are the costs reported for each robot
robot_costs = [
    212.21732723337922,
    116.70009709276687
]

# Reported maximum travel cost
maximum_reported_cost = 212.21732723337922

# Call the check function
result = check_solution(robot_tours, cities_coordinates)
print(result)