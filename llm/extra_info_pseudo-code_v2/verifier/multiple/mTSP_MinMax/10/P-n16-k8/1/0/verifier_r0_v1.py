import math

# Define the city coordinates again
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Provided robot tours
robot_tours = [
    [0, 12, 0],
    [0, 2, 14, 0],
    [0, 5, 11, 0],
    [0, 7, 13, 0],
    [0, 9, 15, 0],
    [0, 3, 4, 0],
    [0, 6, 10, 0],
    [0, 1, 8, 0]
]

# Calculating the Euclidean Distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Validating the solution
def validate_solution(robot_tours):
    visited_cities = set()
    max_cost = 0

    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:  # Check start and end at the depot
            return "FAIL"

        tour_cost = 0
        last_city = tour[0]
        for city in tour[1:]:
            tour_cost += calculate_distance(last_city, city)
            last_city = city

        # Check repeated cities excluding the depot
        tour_cities = set(tour[1:-1])
        if visited_cities & tour_cities:  # Intersection should be empty
            return "FAIL"
        visited_cities.update(tour_cities)

        if tour_cost > max_cost:
            max_cost = tour_cost

    # All cities except the depot should be visited once
    if len(visited_cities) != 15 or any(city not in visited_cities for city in range(1, 16)):
        return "FAIL"

    # Check number of robots used
    if len(robot_tours) != 8:
        return "FAIL"

    # For demonstration, printing the calculated max cost as well
    print(f"Calculated Maximum Travel Cost: {max_cost}")
    
    return "CORRECT"

# Execute validation
result = validate_solution(robot_tours)
print(result)