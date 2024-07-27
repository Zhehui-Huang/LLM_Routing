import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour_and_cost(cities, tour, total_travel_cost):
    # Verify that the tour starts and ends at the depot city, which is city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify that exactly 4 cities are visited (including the depot)
    if len(tour) != 5:  # 4 cities + 1 additional time for depot at the end
        return "FAIL"

    # Calculate the travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Verify the total travel cost provided matches the calculated cost
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define the cities with their coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Provided tour and travel cost
tour_result = [0, 1, 4, 16, 0]
total_travel_cost_result = 111.71676092282922

# Check all the requirements
verification_result = verify_tour_and_cost(cities, tour_result, total_travel_cost_result)
print(verification_result)