import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Generating the full distance matrix
distances = [[calculate_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def verify_solution(tours, distances):
    n_cities = len(cities)
    city_visited = [False] * n_cities
    flow_check = [0] * n_cities  # Track net flow into and out of each city

    # Check tours, visitation, and flow conservation
    for robot_id, tour in enumerate(tours):
        last_city = None
        for idx, city in enumerate(tour):
            if last_city is not None:
                # Check distance matrix bounds
                if city >= n_cities or last_city >= n_cities:
                    return "FAIL - Index out of range"
                # Distance calculation
                segment_distance = distances[last_city][city]
                if segment_distance != distances[city][last_city]:  # Symmetry check
                    return "FAIL - Distance symmetry mismatch"
            last_city = city
            city_visited[city] = True
            flow_check[city] += 1
    
    # Check that each city is visited exactly once except depot
    if not all(city_visited[1:]):
        return "FAIL - Not all cities visited"

    # Each city except depot must have net zero flow and 1 for depot for exit, 1 for entry
    if sum(flow_check[1:]) != n_cities - 1:
        return "FAIL - Flow conservation error"

    # Depot visitations
    if city_visited[0] is False or flow_check[0] != 2:
        return "FAIL - Improper depot usage"

    return "CORRECT"

robot_tours = [
    [0, 6, 0],
    [0, 1, 10, 4, 11, 14, 12, 3, 17, 16, 8, 9, 15, 13, 5, 7, 2, 18, 0]
]

output = verify_solution(robot_tours, distances)
print(output)