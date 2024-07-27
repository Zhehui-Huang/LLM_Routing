import math

# Function to calculate the Euclidean distance between two points
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# City coordinates with city id as index
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Given solution (example)
routes = [
    [0, 10, 12, 15, 3, 0],
    [0, 16, 1, 6, 0],
    [0, 7, 22, 17, 9, 0],
    [0, 18, 19, 0],
    [0, 2, 13, 8, 0],
    [0, 21, 0],
    [0, 4, 11, 0],
    [0, 20, 5, 14, 0]
]

# Function to calculate the travel cost for a route
def calculate_travel_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        x1, y1 = city_coordinates[route[i]]
        x2, y2 = city_coordinates[route[i+1]]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    return total_cost

def verify_solution(routes):
    all_visited_cities = set()
    max_travel_cost = 0
    
    for route in routes:
        if not (route[0] == 0 and route[-1] == 0):
            return "FAIL: Route must start and end at depot."
        
        cost = calculate_travel_cost(route)
        max_travel = max(max_travel_cost, cost)
        all_visited_cities.update(route)

    if len(all_visited_cities.difference({0})) != 22:
        return "FAIL: Not all cities are visited exactly once."

    return f"CORRECT; Max Travel Cost: {max_travel_cost}"

# Check the solution
solution_status = verify_solution(routes)
print(solution_status)