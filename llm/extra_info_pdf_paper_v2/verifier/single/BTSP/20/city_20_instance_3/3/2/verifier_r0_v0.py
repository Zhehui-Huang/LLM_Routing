import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, cities, max_allowed_edge_length):
    # Verify if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify if each city is visited exactly once (excluding the depot city which should be visited exactly twice)
    unique_cities = set(tour)
    if len(tour) != len(cities) + 1 or any(tour.count(city) != 1 for city in unique_cities if city != 0):
        return "FAIL"
    
    # Calculate the total travel cost and maximum edge cost
    total_travel_cost = 0
    max_edge_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        distance = calculate_euclidean_distance(x1, y1, x2, y2)
        total_travel_cost += distance
        if distance > max_edge_cost:
            max_edge_cost = distance
    
    # Verify if the maximum edge cost is minimized, it should be <= provided max_allowed_edge_length
    if max_edge_cost > max_allowed_edge_length:
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Provided solution details
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
total_travel_cost = 458.36719998557066
max_distance_between_cities = 68.15423684555495

# Perform the verification
result = verify_solution(tour, cities, max_distance_between_cities)
print(result)