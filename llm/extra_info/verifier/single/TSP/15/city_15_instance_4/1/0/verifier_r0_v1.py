import math

# Define city coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Solution provided
tour = [0, 13, 10, 8, 14, 3, 6, 11, 12, 4, 7, 2, 5, 9, 1, 0]
reported_cost = 324.91232585922467

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calculate_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

def verify_tour(tour, reported_cost):
    # Check if tour starts and ends at the depot city (Requirement 1)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all other cities are visited exactly once (Requirement 2)
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != 14 or not all(city in visited_cities for city in range(1, 15)):
        return "FAIL"

    # Calculating the actual travel cost
    actual_cost = calculate_total_travel_cost(tour)
    
    # Check if the travel cost is calculated correctly (Requirement 5)
    if not math.isclose(actual_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"

    # If all tests pass
    return "CORRECT"

# Check for correctness
result = verify_tour(tour, reported_cost)
print(result)