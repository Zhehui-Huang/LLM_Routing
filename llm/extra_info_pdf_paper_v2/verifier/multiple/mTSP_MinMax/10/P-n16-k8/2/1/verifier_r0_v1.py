import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, distances):
    cities = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
    ]
    visited_cities = set()
    max_distance = 0
    for tour, reported_distance in zip(tours, distances):
        tour_distances = []
        for i in range(len(tour) - 1):
            distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
            tour_distances.append(distance)
        total_distance = sum(tour_distances)
        max_distance = max(max_distance, total_distance)
        if round(total_distance, 8) != round(reported_distance, 8):
            return "FAIL"
        visited_cities.update(tour)

    # Check if all cities are visited exactly once excluding the depot
    if len(visited_cities) != 16 or visited_cities != set(range(16)):
        return "FAIL"
    
    # Check if max reported distance is the maximum
    reported_max_distance = max(distances)
    if round(reported_max_diff, 8) != round(max_distance, 8):
        return "FAIL"
    
    return "CORRECT"

# Given tours and distances
tours = [
    [0, 1, 0],
    [0, 2, 0],
    [0, 3, 0],
    [0, 4, 0],
    [0, 5, 0],
    [0, 6, 0],
    [0, 7, 0],
    [0, 8, 9, 10, 11, 12, 13, 14, 15, 0]
]
distances = [
    27.784887978899608,
    42.04759208325728,
    65.11528238439882,
    44.04543109109048,
    46.17358552246078,
    24.08318915758459,
    44.04543109109048,
    230.84304305470437
]

# Verify the solution
print(verify_solution(tours, distances))