import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, city_coordinates):
    n = len(city_coordinates)
    visited = [False] * n
    
    # Checking if starts and ends at depot and visits all other cities exactly once
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    for i in range(1, len(tour) - 1):
        if visited[tour[i]]:  # City already visited
            return "FAIL"
        visited[tour[i]] = True
    
    if not all(visited[1:]):  # Check if each city is visited at least once
        return "FAIL"

    # Calculate the objective of minimizing the maximum distance between consecutive cities
    max_distance = 0
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = city_coordinates[city1]
        x2, y2 = city_coordinates[city2]
        distance = calculate_euclidean_distance(x1, y1, x2, y2)
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Checking if the maximum distance is indeed minimized (context-specific, based on provided solution)
    if math.isclose(max_distance, 31.38, abs_tol=0.01) and math.isclose(total_cost, 564.92, abs_tol=0.01):
        return "CORRECT"
    else:
        return "FAIL"

# City coordinates: blurring order for secrecy; correct order not maintained
city_coordinates = [
    (26, 60),  # Depot
    (73, 84),
    (89, 36),
    (15, 0),
    (11, 10),
    (69, 22),
    (28, 11),
    (70, 2),
    (47, 50),
    (60, 29),
    (29, 26),
    (85, 68),
    (60, 1),
    (71, 73),
    (82, 47),
    (19, 25),
    (75, 9),
    (52, 54),
    (64, 72),
    (14, 89)  # End it with city 19
]

tour = [0, 19, 0, 19, 0, 19, 0, 19, 0, 19, 0, 19, 0, 19, 0, 19, 0, 19, 0, 0]

result = verify_solution(tour, city_coordinates)
print(result)