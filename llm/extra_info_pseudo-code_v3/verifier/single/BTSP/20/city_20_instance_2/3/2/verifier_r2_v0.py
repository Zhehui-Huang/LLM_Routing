import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities):
    # Check Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: Each city visited once
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Calculate travel cost and max distance
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        distance = euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Compare given total cost and max distance
    if abs(total_cost - 478.4306776278287) > 1e-4:
        return "FAIL"
    if abs(max_distance - 81.75477983645297) > 1e-4:
        return "FAIL"
    
    return "CORRECT"

# Cities data
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53),
    12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49), 17: (91, 94),
    18: (51, 58), 19: (30, 48)
}

# Tour provided
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]

# Verification check
result = verify_tour(tour, cities.values())
print(result)