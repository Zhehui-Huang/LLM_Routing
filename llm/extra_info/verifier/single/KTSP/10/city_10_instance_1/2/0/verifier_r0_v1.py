import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_tour_and_cost(tour, cities, reported_cost):
    # Verify start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify exactly 5 cities are visited (including the depot)
    if len(tour) != 6:  # includes return to depot, hence 6 entries
        return "FAIL"
    
    # Calculate the total travel cost using Euclidean distance
    total_cost = 0
    for i in range(len(tour) - 1):
        city_index_from = tour[i]
        city_index_to = tour[i + 1]
        x1, y1 = cities[city_index_from]
        x2, y2 = cities[city_index_to]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Check if computed total cost matches the reported total cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Checks passed
    return "CORRECT"

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

# Provided solution
tour = [0, 4, 8, 3, 5, 0]
reported_cost = 110.38072506104011

# Invoke verification
result = verify_tour_and_cost(tour, cities, reported_cost)
print(result)