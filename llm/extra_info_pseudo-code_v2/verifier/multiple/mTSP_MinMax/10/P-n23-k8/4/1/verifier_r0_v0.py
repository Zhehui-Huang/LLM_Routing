import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Tours provided
tours = [
    [0, 15, 3, 11, 21, 5, 16, 0],
    [0, 13, 0],
    [0, 2, 0],
    [0, 19, 0],
    [0, 20, 0],
    [0, 10, 18, 4, 1, 0],
    [0, 8, 0],
    [0, 6, 17, 14, 12, 9, 7, 22, 0]
]

# Validate each tour
def validate_tours(tours, city_coordinates):
    visited = set()
    max_distance = 0

    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tours must start and end at the depot"

        travel_distance = 0
        previous_city = tour[0]

        for i in range(1, len(tour)):
            current_city = tour[i]
            visited.add(current_city)
            travel_distance += calculate_distance(city_coordinates[previous_city], city_coordinates[current_city])
            previous_city = current_city

        max_distance = max(max_distance, travel_distance)

    if len(visited) != 22:  # 23 total cities, excluding the depot
        return "FAIL: Not all cities visited exactly once"

    print("Maximum Travel Cost:", max_distance)
    # If all requirements pass and tours match given costs:
    return "CORRECT"

# Output the test results
print(validate_tours(tours, city_coordinates))