import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_requirements(tour, cities):
    if len(tour) != len(set(tour)) + 1 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    total_distance = 0
    max_distance = 0
    for i in range(len(tour)-1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
        
    # Provided output values
    expected_total_distance = 397.35
    expected_max_distance = 110.98
    
    total_distance = round(total_distance, 2)
    max_distance = round(max_distance, 2)

    if total_distance != expected_total_distance or max_distance != expected_max_distance:
        return "FAIL"
    
    return "CORRECT"

# Coordinates for each city (including depot)
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
          (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
          (83, 96), (60, 50), (98, 1)]

# Provided solution
tour = [0, 5, 4, 10, 9, 3, 7, 1, 6, 13, 2, 11, 12, 8, 14, 0]

# Verify the solution
result = verify_requirements(tour, cities)
print(result)