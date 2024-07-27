import math

# City coordinates provided (indexed by city number)
city_coordinates = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98)
}

# Solution provided
tour = [0, 1, 2, 3, 4, 0]
total_travel_cost = 249.46446619443228
max_distance_between_cities = 60.40695324215582

def calculate_euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities based on their coordinates."""
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution():
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once (excluding the starting/ending city)
    if sorted(tour[:-1]) != sorted(range(len(city_coordinates))):
        return "FAIL"
        
    # Calculate total travel cost and maximum distance in the tour
    computed_tour_length = 0
    computed_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(tour[i], tour[i+1])
        computed_tour_length += distance
        if distance > computed_max_distance:
            computed_max_distance = distance

    # Check if calculated total travel cost and maximum distance match the provided values
    if not math.isclose(total_travel_cost, computed_tour_length, rel_tol=1e-9):
        return "FAIL"
    if not math.isclose(max_distance_between_cities, computed_max_distance, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Output the result of the test
print(test_solution())