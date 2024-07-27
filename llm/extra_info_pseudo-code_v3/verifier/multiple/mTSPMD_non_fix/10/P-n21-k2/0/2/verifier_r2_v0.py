import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_all_cities_visited_once(tours, num_cities):
    visited = set()
    for tour in tours:
        visited.update(tour)
    return len(visited) == num_cities and all(i in visited for i in range(num_cities))

def calculate_tour_cost(tour, city_coordinates):
    cost = 0
    for i in range(1, len(tour)):
        cost += calculate_distance(city_coordinates[tour[i-1]], city_coordinates[tour[i]])
    return cost

def validate_solution(tours, city_coordinates, number_of_robots):
    total_cost = 0
    if not len(tours) == number_of_robots:
        return "FAIL"
    for tour in tours:
        if tour[0] != 0:  # Since each robot starts at depot 0 in this test case
            return "FAIL"
        total_cost += calculate_tour_cost(tour, city_coordinates)
    if not check_all_cities_visited_once(tours, len(city_coordinates)):
        return "FAIL"
    return "CORRECT", total_cost

# Example tour setup for the purpose of this testing
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Hypothetical robot tours (This should be the output of a TS algorithm designed for the task)
# These tours are thus considered placeholders for the purpose of this testing.
tours = [
    [0, 2, 6, 7, 9, 17, 14, 5, 20, 0],
    [0, 3, 12, 10, 4, 11, 15, 16, 1, 18, 19, 8, 13, 0]
]

result, total_cost = validate_solution(tours, city_coordinates, 2)
print(result)  # Should be "CORRECT" if the example tours are properly structured
if result == "CORRECT":
    print(f"Overall Total Travel Cost: {total_cost}")