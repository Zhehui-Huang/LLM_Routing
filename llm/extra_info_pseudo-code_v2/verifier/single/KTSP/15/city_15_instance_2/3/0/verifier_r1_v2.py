import math

# Coordinates of all cities
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Provided tour and its cost
tour = [0, 13, 7, 9, 10, 3, 8, 6, 0]
reported_cost = 228.12

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour():
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if 8 unique cities are visited
    if len(set(tour) - {0}) != 7:  # 7 others except the depot town
        return "FAIL"
    
    # Calculate the total cost of the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        city_a = cities[tour[i]]
        city_b = cities[tour[i+1]]
        total_cost += euclidean_distance(city_a, city_b)

    # Validate the cost
    if not (abs(total_cost - reported_cost) <= 0.1):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Output the result of the verification
print(verify_tour())