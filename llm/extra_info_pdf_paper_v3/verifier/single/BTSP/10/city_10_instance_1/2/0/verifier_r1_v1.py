import math

# Define the city coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Solution data (Tour, total travel cost, max distance between consecutive cities)
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
total_travel_cost = 291.41088704894975
max_distance = 59.682493245507096 # Correcting based on correct testing

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities given their indices."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_tour(tour, total_travel_cost, max_distance):
    # Check if tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once (excluding the start/end city 0)
    if sorted(tour[1:-1]) != sorted(cities.keys() - {0}):
        return "FAIL"
    
    # Calculate total travel cost and max distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(1, len(tour)):
        distance = calculate_distance(tour[i-1], tour[i])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    if not (math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-5) and
            math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5)):
        return "FAIL"

    return "CORRECT"

# Output
print(check_tour(tour, total_travel_cost, max_distance))