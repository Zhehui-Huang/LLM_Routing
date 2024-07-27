import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(team_tours, city_coordinates):
    total_travel_cost = 0
    all_cities_visited = set()

    for robot_id, tour in enumerate(team_tours):
        correct_start_and_end = tour[0] == 0 and tour[-1] == 0
        if not correct_start_and_end:
            return "FAIL"
        
        robot_tour_cost = 0
        previous_city = tour[0]
        all_cities_visited.add(previous_city)

        for city in tour[1:]:
            if city in all_cities_visited and city != 0:
                return "FAIL"
            all_cities_visited.add(city)
            robot_tour_cost += calculate_euclidean_distance(city_coordinates[previous_city], city_coordinates[city])
            previous_city = city
        
        total_travel_cost += robot_tour_cost
        if not math.isclose(robot_tour_cost, team_tours[robot_id][1], rel_tol=1e-5):
            return "FAIL"

    if len(all_cities_visited) != len(city_coordinates):
        return "FAIL"

    if not math.isclose(total_travel_cost, team_tours[0][1] + team_tours[1][1], rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# City coordinates indexed by city ID
city_coordinates = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
                    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
                    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
                    18: (62, 63), 19: (63, 69), 20: (45, 35)}

# Provided solution (assume from an outer source or by solving an algorithm)
team_tours = [
    ([0, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 0], 143.98241284438606),
    ([0, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 0], 109.8362166450987)
]

# Test the solution
print(verify_solution(team_tours, city_coordinates))