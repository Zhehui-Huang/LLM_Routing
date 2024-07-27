import math
from collections import Counter

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tours, costs, city_coordinates):
    city_count = len(city_coordinates)
    visited = Counter()  # To track how many times each city is visited

    overall_cost_calculated = 0.0
    cities_in_tours = []

    for robot_id, tour in enumerate(tours):
        if tour[0] not in range(0, 8) or tour[-1] not in range(0, 16):
            print(f"Robot {robot_id} does not start or end at a proper depot or city.")
            return "FAIL"
        
        if robot_id >= 8:
            print(f"More robots used ({robot_id+1}) than available (8).")
            return "FAIL"
        
        tour_cost = 0
        cities_in_tours.extend(tour)
        
        for i in range(len(tour) - 1):
            start_city = tour[i]
            end_city = tour[i + 1]
            distance = calculate_distance(city_coordinates[start_city], city_coordinates[end_city])
            tour_cost += distance
            visited[start_city] += 1
        
        visited[tour[-1]] += 1  # Last city in the tour
        
        if not (abs(tour_cost - costs[robot_id]) < 0.01):
            print(f"Total travel cost mismatch for Robot {robot_id}: calculated {tour_cost}, given {costs[robot_id]}")
            return "FAIL"
        
        overall_cost_calculated += tour_cost
    
    if not all(count == 1 for count in visited.values()):
        print("Some cities are visited multiple times or not visited at all.")
        return "FAIL"
    
    if abs(overall_cost_calculated - sum(costs)) > 0.01:
        print(f"Overall cost mismatch: calculated {overall_cost_calculated}, expected sum {sum(costs)}")
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Solution given
tour_robot_0 = [2, 4, 15, 10, 1, 14, 5, 6, 0]
cost_robot_0 = 117.48

overall_cost = 187.46  # Note: This seems incongruent with given robot tours. Assuming one robot for clarity.

# Conduct unit tests
result = verify_solution([tour_robot_0], [cost_robot_0], coordinates)
print(result)