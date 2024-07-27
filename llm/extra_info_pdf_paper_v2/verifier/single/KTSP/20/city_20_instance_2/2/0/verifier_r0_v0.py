import math

# City coordinates
cities = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
          (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
          (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)]

def euclidean_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, reported_cost):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 10 cities are visited
    if len(set(tour)) != 10:
        return "FAIL"
    
    # Compute the travel cost and compare with the reported cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_raw_cost(tour[i], tour[i + 1])
    
    if abs(calculated_cost - reported_cost) > 0.001: # Allowing a small margin for floating-point arithmetic
        return "FAIL"
    
    # The above checks, when passed, imply the solution meets all requirements.
    return "CORRECT"

# Given solution details
tour = [0, 18, 4, 10, 14, 11, 19, 9, 2, 12, 0]
reported_cost = 312.5973320302805

# Function to convert indices to coordinates
def euclidean_raw_cost(city_index1, city_index2):
    return euclidean_distance(cities[city_index1], cities[city_index2])

result = verify_solution(tour, reported_cost)
print(result)