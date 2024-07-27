import math

# Helper function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cities, total_travel_cost):
    # Requirement 1: Start and end at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Robot visits exactly 12 cities
    if len(set(tour)) != 12:
        return "FAIL"

    # Collect coordinates for the cities in the tour
    city_coords = [(cities[city][0], cities[city][1]) for city in tour]

    # Calculate the total travel cost from the tour
    calculated_cost = 0
    for i in range(1, len(city_coords)):
        calculated_cost += calc_clockwise_distance(city_coords[i - 1], city_coords[i])

    # Allow for slight errors due to precision
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=0.001):
        return "FAIL"

    # If all checks have passed
    return "CORRECT"

# Cities coordinates
cities = {0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
          5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 
          10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)}

# Provided tour and travel cost
tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 0]
total_travel_cost = 241.29121374601274

# Verify the solution
result = verify_solution(tour, cities, total_travel_cost)
print(result)