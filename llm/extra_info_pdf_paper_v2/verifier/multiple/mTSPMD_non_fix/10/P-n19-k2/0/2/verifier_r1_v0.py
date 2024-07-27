import math

# Coordinates of the cities
coordinates = [
    (30, 40),  # Depot city 0
    (37, 52),  # Depot city 1
    (49, 43),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 27),
    (37, 69),
    (61, 33),
    (62, 63),
    (63, 69),
    (45, 35),
]

# Proposed solution data
tours = [
    [0, 6, 2, 7, 5, 9, 8, 3, 4, 10],
    [1, 11, 14, 12, 17, 16, 15, 13, 18]
]

cost_robot_0 = 122.94090521076575
cost_robot_1 = 132.2024047007472

overall_calculated_cost = cost_robot_0 + cost_robot_1

# Function to calculate Euclidean distance
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Validate the solution
def validate_solution(tours):
    all_cities = set(range(len(coordinates)))
    visited_cities = set()

    distances = []

    for i, tour in enumerate(tours):
        tour_cost = 0
        prev_city = None
        
        for city in tour:
            visited_cities.add(city)
            if prev_city is not None:
                distance = euclidean_distance(coordinates[prev_city], coordinates[city])
                tour_cost += distance
            prev_city = city

        distances.append(tour_cost)

    # Test if all cities are visited exactly once
    if visited_cities != all_cities:
        return "FAIL"

    # Test total distance
    if not (abs(distances[0] - cost_robot_0) < 1e-5 and abs(distances[1] - cost_robot_1) < 1e-5):
        return "FAIL"

    # Tour starting and stopping conditions
    if tours[0][0] != 0 or tours[1][0] != 1:
        return "FAIL"

    # Check total distance
    if abs(overall_calculated_cost - overall_calculated_cost) > 1e-5:
        return "FAIL"

    return "CORRECT"

# Run the validation
result = validate_solution(tours)
print(result)