import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(route, best_cost, city_coordinates, depots):
    # Check if the route starts and ends at the robot's designated depots
    if route[0] != depots[0] or route[-1] != depots[1]:
        return "FAIL: Route does not start/end at assigned depots"

    # Check if every city is visited exactly once
    unique_cities = set(route)
    if len(unique_cities) != len(route):
        return "FAIL: Some cities are visited more than once or some cities are missing"

    # Calculate the actual travel cost based on Euclidean distance
    calculated_cost = 0
    for i in range(len(route) - 1):
        calculated_cost += calculate_distance(city_coordinates[route[i]], city_coordinates[route[i + 1]])
    
    # Compare computed cost with the best claimed cost
    if not math.isclose(calculated_cost, best_cost, rel_tol=1e-9):
        return f"FAIL: Computed cost ({calculated_cost}) does not match the best cost ({best_cost})"

    # The solution meets all tests
    return "CORRECT"

# Example test
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69),
    18: (45, 35)
}
route = [0, 4, 11, 14, 12, 10, 3, 17, 16, 8, 2, 7, 9, 15, 13, 5, 18, 6, 1]
best_cost = 174.07721372737845

# Depots for the robots; assuming first element and last element represent the starting and ending depots respectively
depots = [route[0], route[-1]]

result = verify_solution(route, best_cost, city_coordinates, depots)
print(result)