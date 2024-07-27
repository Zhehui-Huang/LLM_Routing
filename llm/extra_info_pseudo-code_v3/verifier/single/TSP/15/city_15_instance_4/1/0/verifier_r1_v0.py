import math

# Define the cities and their locations
cities = {
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

# The tour and the actual total travel cost provided
tour = [0, 10, 11, 12, 4, 13, 14, 8, 9, 7, 3, 6, 2, 5, 1, 0]
total_travel_cost_provided = 520.7795498520583

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_tour_and_calculate_cost(tour, cities):
    # Checking if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False, 0
    
    # Checking if all cities are visited exactly once
    if set(tour) != set(cities.keys()):
        return False, 0
    
    # Calculate the total travel cost of the tour
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    return True, total_calculated_cost

# Run the test
is_valid_tour, calculated_cost = verify_tour_and_calculate_cost(tour, cities)
if is_valid_tour and abs(calculated_cost - total_travel_cost_provided) < 1e-5:
    print("CORRECT")
else:
    print("FAIL")