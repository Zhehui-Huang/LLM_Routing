import math

# Coordinates of the cities
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Proposed robot tours
robot_tours = [
    [0, 1, 9, 17, 0],
    [0, 2, 18, 10, 0],
    [0, 3, 19, 11, 0],
    [0, 4, 12, 20, 0],
    [0, 13, 5, 21, 0],
    [0, 6, 22, 14, 0],
    [0, 7, 15, 0],
    [0, 16, 8, 0]
]

# Calculate travel costs and check requirements
def test_robot_tours(robot_tours):
    maximum_travel_cost = 0
    all_visited_cities = set()
    for tour in robot_tours:
        # Requirement 1: Start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        travel_cost = 0
        for i in range(len(tour) - 1):
            cost = euclidean_distance(tour[i], tour[i+1])
            travel_cost += cost
        
        if travel_cost > maximum_travel_cost:  # Updating the max cost if current tour cost is higher
            maximum_travel_cost = travel_cost
        
        # Adding to set of visited cities, excluding the depot
        all_visited_cities.update(tour[1:-1])
    
    # Requirement 2: All cities visited exactly once
    if len(all_visited_cities) != 22:
        return "FAIL"
    
    # Requirement 3 & 6: Provided maximum travel cost is minimized
    provided_max_cost = 108.81482905718964
    if abs(maximum_travel_cost - provided 



_max_cost) > 0.001:
        return "FAIL"

    return "CORRECT"

# Evaluate the robot tours
result = test_robot_tours(robot_tours)
print(result)