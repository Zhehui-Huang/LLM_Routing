import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour_and_cost(tour, cities, reported_cost):
    # Requirement 1: Check if the tour includes exactly 13 cities
    if len(tour) != 13 + 1:  # +1 because it should return to the starting city
        return "FAIL"

    # Requirement 1: Check starting and ending at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Calculate the total travel cost using Euclidean distance
    total_distance = 0
    for i in range(len(tour) - 1):
        city_index1 = tour[i]
        city_index2 = tour[i + 1]
        total_distance += calculate_distance(cities[city_index1], cities[city_index2])
    
    # Requirement 4: Check if the calculated distance matches the reported cost
    if not math.isclose(total_distance, reported_cost, abs_tol=0.001):
        return "FAIL"

    # If all checks passed
    return "CORRECT"

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0),
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43),
    18: (53, 76), 19: (19, 72)
}

# Solution details
tour = [0, 10, 11, 16, 17, 5, 4, 14, 8, 7, 12, 18, 3, 0]
reported_cost = 753.8901621432298

# Verify the solution
result = verify_tour_and_cost(tour, cities, reported_cost)
print(result)