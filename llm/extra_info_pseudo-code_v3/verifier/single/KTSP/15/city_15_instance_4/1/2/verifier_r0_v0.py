import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def validate_tour_and_cost(tour, total_travel_cost, cities_coordinates):
    expected_num_cities = 12

    # Check if the tour starts and ends at depot city (city 0), and is valid format
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if tour includes exactly 12 cities (counting the depot city as only one city)
    if len(set(tour)) != expected_num_cities:
        return "FAIL"
    
    # Calculate the travel cost based on Euclidean distances and compare with provided cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        x1, y1 = cities_coordinates[city1]
        x2, y2 = cities_coordinates[city2]
        calculated_cost += euclidean(distance(x1, y1, x2, y2))
    
    # Considering floating point precision issues, we use a small epsilon
    if not math.isclose(total_travel_cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates with depot city as city 0
cities_coordinates = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Solution data provided
tour_provided = [0, 10, 8, 14, 0]
total_travel_cost_provided = 50.798122867199865

# Run the validation
result = validate_tour_and_cost(tour_provided, total_travel_cost_provided, cities_coordinates)
print(result)