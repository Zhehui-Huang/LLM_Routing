import math

# Given solution
tour = [0, 5, 1, 2, 9, 7, 6, 4, 3, 8, 0]
total_travel_cost = 418.32344417340323
max_distance_between_cities = 69.42621983083913

# Given city coordinates
city_coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def calculate_distance(city1, city2):
    """Euclidean distance between two cities."""
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0])**2 + 
                     (city_coordinates[city1][1] - city_coordinates[city2][1])**2)

def verify_tour(tour, total_travel_cost, max_distance_between_cities):
    """Verifies the provided tour against given requirements."""
    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once, except for returning to the depot
    unique_cities = set(tour[1:-1])  # Exclude the repeated depot city at the end
    if len(unique_cities) != len(city_coordinates) - 1:
        return "FAIL"

    # Calculate the total distance and the maximum distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(tour[i], tour[i+1])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Check if the calculated max distance and total cost are as stated
    if not math.isclose(calculated_max_distance, max_distance_between_cities, rel_tol=1e-5):
        return "FAIL"
    if not math.isholds(calculated_total_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Run the verification
result = verify_tour(tour, total_travel_cost, max_distance_between_cities)
print(result)