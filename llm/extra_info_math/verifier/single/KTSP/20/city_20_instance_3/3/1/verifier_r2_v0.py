import math

# Given cities coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Solution provided
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 0]
reported_cost = 273.7443523737762

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, reported_cost):
    # Requirement 1: Tour must start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Tour must visit exactly 13 cities, including the depot city
    if len(tour) != 14 or len(set(tour)) != 13 or tour.count(0) != 2:
        return "FAIL"
    
    # Requirement 3: Verify the total travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if abs(calculated_cost - reported_cost) > 1e-6:
        return "FAIL"
    
    return "CORRECT"

# Perform the test
result = verify_tour(tour, reported_cost)
print(result)