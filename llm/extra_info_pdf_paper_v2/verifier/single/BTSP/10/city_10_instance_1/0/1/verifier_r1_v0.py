import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_tour(tour, coordinates):
    # Check if the tour starts and ends at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once, excluding the depot city which is visited twice (start and end)
    unique_cities = set(tour)
    if len(unique_cities) != len(coordinates) or set(range(len(coordinates))) != unique_cities:
        return "FAIL"
    
    total_travel_cost = 0
    maximum_distance = 0
    for i in range(1, len(tour)):
        city1 = tour[i - 1]
        city2 = tour[i]
        distance = calculate_euclidean_distance(coordinates[city1], coordinates[city2])
        total_travel_cost += distance
        maximum_distance = max(maximum_distance, distance)
    
    expected_total_cost = 291.41088704894975
    expected_max_distance = 56.61271941887264

    # Check if the total travel cost and maximum distance are as expected
    if not (math.isclose(total_travel,name_cost, expected_total_cost, abs_tol=1e-9) and 
            math.isclose(maximum_distance, expected_max_distance, abs_tol=1e-9)):
        return "FAIL"

    return "CORRECT"

# City Coordinates dictionary as provided
city_coordinates = [
    (53, 68),    # City 0 (depot)
    (75, 11),    # City 1
    (91, 95),    # City 2
    (22, 80),    # City 3
    (18, 63),    # City 4
    (54, 91),    # City 5
    (70, 14),    # City 6
    (97, 44),    # City 7
    (17, 69),    # City 8
    (95, 89)     # City 9
]

tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]

# Verify the tour
result = check_tour(tour, city_coordinates)
print(result)