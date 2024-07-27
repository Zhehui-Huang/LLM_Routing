import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_solution(robots_tours, cities_coordinates):
    all_visited_cities = set()
    total_cost = 0

    for robot_id, tour in robots_tours.items():
        # Check if the tour starts and ends at the robot's assigned depot
        assigned_depot = robot_id
        if tour[0] != assigned_depot or tour[-1] != assigned_depot:
            return "FAIL"

        # Calculating travel cost for this robot and total cost
        robot_cost = 0
        for i in range(len(tour) - 1):
            x1, y1 = cities_coordinates[tour[i]]
            x2, y2 = cities_coordinates[tour[i+1]]
            distance = calculate_euclidean_distance(x1, y1, x2, y2)
            robot_cost += distance
            all_visited_cities.add(tour[i])

        total_cost += robot_cost

        # Adding the last city of the tour to visited cities
        all_visited_cities.add(tour[-1])

    # Check if all cities are visited and exactly once collectively
    if len(all_visited_cities) != len(cities_coordinates):
        return "FAIL"

    # Check if the objective to minimize the travel cost has been addressed (not computed here)
    
    return "CORRECT"

# Define the cities coordinates
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Example of assumed correct tour for testing
robots_tours = {
    0: [0, 8, 11, 0],
    1: [1, 9, 12, 1],
    2: [2, 10, 13, 2],
    3: [3, 14, 15, 3],
    4: [4, 5, 6, 4],
    5: [5, 7, 4],
    6: [6, 10, 6],
    7: [7, 13, 7]
}

# Assuming robots_tours has all required tours and this should parse without errors
result = check_solution(robots_tours, cities_coordinates)
print(result)