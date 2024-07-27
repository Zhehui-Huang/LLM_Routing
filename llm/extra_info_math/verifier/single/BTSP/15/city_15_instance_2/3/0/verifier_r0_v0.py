import math

# Coordinates of the cities, indexed from 0 to 14 (15 cities including the depot)
city_coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), 
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# The reported tour and its properties
reported_tour = [0, 6, 2, 0]
reported_total_travel_cost = 37.80
reported_max_distance = 17.12

def calculate_distance(c1, c2):
    """Calculate the Euclidean distance between two cities."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def verify_solution(tour, total_cost, max_distance):
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once (excluding the depot which should be visited twice)
    visited_cities = tour[1:-1]
    unique_cities = set(visited_cities)
    if len(visited_cities) != len(unique_cities) or len(unique_cities) != 14:
        return "FAIL"
    
    # Calculate the actual total distance and maximum distance between consecutive cities
    actual_total_distance = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        actual_total_distance += distance
        actual_max_distance = max(actual_max_distance, distance)

    # Check the reported total and max distances
    if not math.isclose(actual_total_distance, total_cost, rel_tol=1e-5) or not math.isclose(actual_max_down, max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Run the verification
result = verify_solution(reported_tour, reported_total_travel_cost, reported_max_distance)
print(result)