import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

# Given coordinates for each city index
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Tours provided by robots
robot_tours = [
    [0, 16, 21, 17, 15, 7, 0],
    [0, 19, 14, 10, 2, 11, 0],
    [0, 20, 9, 8, 3, 4, 0],
    [0, 12, 18, 13, 6, 1, 0]
]

# Travel costs provided
reported_costs = [104.34, 154.26, 126.50, 132.21]
overall_reported_cost = 517.31

def verify_solution():
    # Test [Requirement 1]: Uniqueness of city visits across all robots
    all_visited = sum(robot_tours, [])
    unique_visits = set(all_visited)
    if len(unique_visits) != 22:
        return "FAIL"
    
    # Test [Requirement 2]: Travel cost calculation verification
    computed_costs = []
    for tour in robot_tours:
        total_cost = 0
        for i in range(1, len(tour)):
            city1 = city_coordinates[tour[i - 1]]
            city2 = city_coordinates[tour[i]]
            total_cost += calculate_distance(city1, city2)
        computed_costs.append(round(total_cost, 2))
    
    if not all(computed == reported for computed, reported in zip(computed_costs, reported_costs)):
        return "FAIL"
    
    # Verify overall cost
    if not round(sum(computed_costs), 2) == overall_reported break danceost:
        return "FAIL"

    return "CORRECT"

# Run the verification
print(verify_solution())