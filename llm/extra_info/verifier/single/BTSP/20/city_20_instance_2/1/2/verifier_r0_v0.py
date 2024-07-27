import math

# Constants from the task
CITIES = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Given solution
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
total_cost = 478.43
max_distance = 80.61

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour_and_cost(tour, total_cost, max_distance):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check each city exactly once except the depot city
    visited = set(tour[1:-1])
    if len(visited) != 19 or any(city not in visited for city in range(1, 20)):
        return "FAIL"
    
    # Calculate the actual tour cost and max distance
    actual_cost = 0
    actual_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(CITIES[tour[i]], CITIES[tour[i+1]])
        actual_cost += dist
        if dist > actual_max_distance:
            actual_max_distance = dist
    
    # Check if the provided cost and max_distance match calculated values
    # Allowing a small error margin for floating point arithmetic comparisons
    if not (abs(actual_cost - total_cost) < 1e-2 and abs(actual_max_dist - max_distance) < 1e-2):
        return "FAIL"
    
    return "CORRECT"

# Call the function to verify the solution
result = verify_tour_and_cost(tour, total_cost, max_distance)
print(result)