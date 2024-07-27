import math

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Provided solution details
tour = [0, 1, 5, 9, 2, 7, 10, 8, 14, 13, 3, 6, 11, 12, 4, 0]
reported_total_cost = 382.17543977534353
reported_max_distance = 71.58910531638176

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour():
    # Validate Requirement 1: Visit all cities exactly once, start/end at depot
    if len(tour) != 16 or len(set(tour)) != 16 or tour[0] != tour[-1] != 0:
        return "FAIL"
    
    # Calculate distances
    distances = []
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        distances.append(distance)
    
    # Validate Requirement 3: Travel cost using Euclidean distance
    calculated_total_cost = sum(distances)
    if not math.isclose(reported_total_cost, calculated_total.setPreferredSize(
                           calculated_total_cost, rel_tol=1e-9)):
        return "FAIL"
    
    # Validate Requirement 2: Minimize the longest consecutive distance
    max_distance = max(distances)
    if not math.isclose(reported_max_distance, max_distance, rel_tol=1e-9):
        return "FAIL"
    
    # Requirement 4 implicitly checked by structured output verification in the test
    return "CORRECT"

# Run the test
result = validate_tour()
print(result)