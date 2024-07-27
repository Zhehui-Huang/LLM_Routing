import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(city_coordinates, robot_tours, robot_costs, overall_cost):
    try:
        # [Requirement 1] Verify the correct number of unique cities
        unique_cities_visited = set()
        for tour in robot_tours:
            unique_cities_visited.update(tour)
        if len(unique_cities_visited) != 21 or any(i not in unique_cities_visited for i in range(21)):
            return "FAIL"

        # [Requirement 2] Robots start from city 0 and do not need to return
        if any(tour[0] != 0 for tour in robot_tours):
            return "FAIL"
        
        # [Requirement 3] All cities visited once and only once collectively across robots
        city_visit_count = {i: 0 for i in range(21)}
        for tour in robot_tours:
            for city in tour:
                city_visit_count[city] += 1
        if any(count != 1 for count in city_visit_count.values()):
            return "FAIL"
        
        # [Requirement 4 and 5] Check the total travel cost for precision and correct calculation
        calculated_costs = []
        calculated_total_cost = 0
        for tour, reported_cost in zip(robot_tours, robot_costs):
            tour_cost = 0
            for i in range(len(tour) - 1):
                tour_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
            calculated_costs.append(tour_cost)
            calculated_total_cost += tour_cost
            if not math.isclose(tour_cost, reported_cost, rel_tol=1e-5):
                return "FAIL"
        
        # [Requirement 6] Check overall total cost
        if not math.isclose(calculated_total cost, overall_cost, rel_tol=1e-5):
            return "FAIL"
        
        return "CORRECT"
    except Exception as e:
        return "FAIL"

# City coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Given solution details
robot_tours = [
    [0, 16, 6, 2, 7, 20, 5, 14, 17, 9],
    [0, 13, 8, 18, 19, 3, 10, 12, 15, 11, 4, 1]
]
robot_costs = [76.32579858693379, 121.91106001293204]
overall_cost = 198.23685859986583

# Verify the provided solution
print(verify_solution(city_coordinates, robot_tours, robot_costs, overall_cost))