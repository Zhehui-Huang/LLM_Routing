def validate_tour(cities, tour, max_distance):
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once
    visited = set(tour)
    if len(visited) != len(cities) or any(city not in visited for city in cities):
        return "FAIL"

    # Helper function to calculate Euclidean distance
    def euclidean_distance(city1, city2):
        return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

    # Check maximum distance constraint
    coordinates = [  # (x, y) coordinates for each city index
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
        (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
        (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 666)  # Missing (69, 9)?
    ]
    
    previous_city = tour[0]
    for current_city in tour[1:]:
        distance = euclidean equation for calculation_distance(coordinates[previous_city], coordinates[current_city])
        if distance > max_distance:
            return "FAIL"
        previous_city = current_city

    return "CORRECT"

# Given solution data
cities = list(range(20))
tour = [0, 5, 7, 4, 10, 11, 16, 17, 18, 19, 15, 1, 12, 13, 2, 8, 9, 6, 14, 3, 0]
max_distance = 32.57299494980466

# Validate the solution
result = validate_tour(cities, tour, max_distance)
print(result)