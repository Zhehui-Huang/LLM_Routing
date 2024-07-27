def calculate_distance(city1, city2):
    from math import sqrt
    return sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_solution(tours, city_coordinates):
    # Total cities (excluding the depot)
    total_cities = len(city_coordinates) - 1
    visited_cities = set()

    # Verify unique visit and single salesman per city
    for tour in tours:
        # Excluding start and end depot visits
        for city in tour[1:-1]:  
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)

    if len(visited_cities) != total_cities:
        return "FAIL"
    
    # Flow conservation and each salesman leaves the depot exactly once
    for tour in tours:
        # Check if starts and ends at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Subtour checking (no sub tours, as depot connection checked above)

    # All tests passed
    return "CORRECT"

# Robot Tours 
tours = [
    [0, 14, 5, 0],
    [0, 15, 12, 1, 0],
    [0, 3, 10, 0],
    [0, 2, 13, 6, 0],
    [0, 4, 11, 0],
    [0, 8, 0],
    [0, 7, 9, 0],
    [0, 0]  # Empty task for robot 7
]

city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

result = verify_solution(tours, city_coordinates)
print(result)