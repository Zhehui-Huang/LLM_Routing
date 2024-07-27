import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def is_valid_tour(tour, total_cost, city_locations):
    # Check if the robot starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 10 cities (including the depot) are visited
    if len(tour) != 11:
        return "FAIL"
    
    if len(set(tour)) != 11:
        return "FAIL"

    # Calculate the total travel cost and compare with given total_cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(city_locations[tour[i]], city_locations[tour[i + 1]])
    
    # Due to floating point arithmetic, allow a small margin of error
    if not math.isclose(computed_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Provided data points
city_locations = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Provided tour and total travel cost
tour = [0, 1, 4, 12, 7, 10, 13, 5, 9, 14, 0]
total_travel_cost = 182.3471551326047

# Validate the solution
result = is_valid_tour(tour, total_travel_cost, city_locations)
print(result)