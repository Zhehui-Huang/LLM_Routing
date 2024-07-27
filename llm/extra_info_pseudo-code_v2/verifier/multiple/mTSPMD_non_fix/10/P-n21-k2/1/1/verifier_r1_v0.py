import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_cost):
    cities = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    num_cities = 21
    total_visited_cities = set()

    # Parsing tour
    tours = []
    current_tour = []
    for city in tour:
        if city >= 0:
            current_tour.append(city)
            total_visited_cities.add(city)
        else:
            if current_tour:
                tours.append(current_tour)
                current_tour = []
    
    if current_tour:
        tours.append(current_tour)

    # [Requirement 2] and [Requirement 6] Preparation
    robot_count = len(tours)
    start_city_each_robot = [t[0] for t in tours]

    # Initialize cost calculation
    calculated_cost = 0
    for tour in tours:
        for i in range(len(tour) - 1):
            calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # Check requirements:
    # [Requirement 1] Total number of cities equals num_cities
    if len(cities) != num_cities:
        return "FAIL: Incorrect number of cities"
        
    # [Requirement 2] Two robots used, starting their journey from city 0
    if robot_count != 2 or start_city_each_robot != [0, 0]:  # modify as required based on the problem's twist
        return "FAIL: Incorrect number of robots or starting city"
    
    # [Requirement 5] Every city visited exactly once
    if len(total_visited_cities) != num_cities or sum(1 for t in total_visited_cities if t > num_cities-1) > 0:
        return "FAIL: Not all cities were visited exactly once"
        
    # [Requirement 8] Check total cost minimization not trivially verifiable, comparing computed vs provided
    if abs(calculated_cost - total_cost) > 1.0:
        return "FAIL: Total travel cost mismatch with expected result."
        
    # [Requirement 9] Verify that each robot's tour either starts or ends at its depot city
    if not all(tour[0] == 0 or tour[-1] == 0 for tour in tours):  # modify as required based on the problem's twist
        return "FAIL: Each robot's tour does not start or end at a depot"

    # [Requirement 10]
    if calculated_cost != total_cost:
        return "FAIL: Calculated total cost does not match the given cost"
        
    return "CORRECT"

# The given solution
tour = [0, 10, 2, 17, 14, 20, 6, -1, 7, 8, 18, 3, 19, 12, 1, 11, 15, 4, 16, 13, 9, 5]
total_cost = 316.816035728699
print(test_solution(tour, total_cost))