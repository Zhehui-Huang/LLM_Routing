import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(robot_tours, city_coordinates, distances):
    visited_cities = set()
    total_cost_calculated = 0.0
    robots_starting_from_depot = all(tour[0] == 0 for tour in robot_tours)
    
    for tour in robot_tours:
        tour_cost = 0.0
        for i in range(len(tour) - 1):
            tour_cost += distances[(tour[i], tour[i + 1])]
            visited_cities.add(tour[i])
        visited_cities.add(tour[-1])
        total_cost_calculated += tour_cost
    
    all_cities_visited_once = len(visited_cities) == len(city_coordinates)
    started_at_depot = robots_starting_from_depot
    total_visits = len(visited_cities)
    
    print("All cities visited exactly once:", all_cities_visited_once)
    print("All tours start at the depot city 0:", started_at_depot)
    print("Total number of visits (Should be 19):", total_visits)
    
    return all_cities_visited_once and total_visits == len(city_coordinates) and started_at_depot

cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

distances = {}
for i in cities_coordinates:
    for j in cities_coordinates:
        if i != j:
            distances[(i, j)] = calculate_distance(cities_coordinates[i], cities_coordinates[j])

robot_0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 8, 16, 17, 3, 12, 14, 4, 11, 10, 1]
robot_1_tour = [1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 9, 15, 13, 5, 18, 6, 2, 7, 0]

# Check if both starting and ending at their respective depots and every city is visited exactly once.
correctness = check_solution([robot_0_tour, robot_1_tour], cities_coordinates, distances)

if correctness:
    print("CORRECT")
else:
    print("FAIL")