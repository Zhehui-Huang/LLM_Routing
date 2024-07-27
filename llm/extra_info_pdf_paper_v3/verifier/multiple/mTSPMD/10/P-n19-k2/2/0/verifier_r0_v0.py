import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def verify_solution(robot_tours, city_coordinates):
    # Requirement 1: Check if all cities are visited once and depots exactly twice
    visit_frequency = {i: 0 for i in range(len(city_coordinates))}
    for tour in robot_tours.values():
        for city in tour:
            visit_frequency[city] += 1
    
    for city, frequency in visit_frequency.items():
        if city in [0, 1]:  # Depot cities
            if frequency != 2:
                return "FAIL"
        else:
            if frequency != 1:
                return "FAIL"
    
    # Requirement 2: Check if each robot starts and ends at the assigned depot
    if robot_tours[0][0] != 0 or robot_tours[0][-1] != 0:
        return "FAIL"
    if robot_tours[1][0] != 1 or robot_tours[1][-1] != 1:
        return "FAIL"
    
    # Requirement 3: Verify total costs
    computed_costs = []
    for robot_id, tour in robot_tours.items():
        computed_cost = calculate_total_cost(tour, city_coordinates)
        computed_costs.append(computed_cost)

    # The known correct total cost as per the solution given
    correct_total_cost = 312.103929127161
    if not math.isclose(sum(computed_costs), correct_total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Given solution
city_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
robot_tours = {
    0: [0, 6, 13, 15, 9, 2, 3, 8, 16, 0],
    1: [1, 18, 7, 5, 14, 10, 4, 11, 12, 17, 1]
}
result = verify_solution(robot_tours, city_coordinates)
print(result)