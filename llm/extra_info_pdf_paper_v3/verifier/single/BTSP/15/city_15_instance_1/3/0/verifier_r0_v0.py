import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def validate_solution(tour, cost, longest_distance):
    cities = [
        (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
        (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
        (83, 96), (60, 50), (98, 1)
    ]
    
    if len(cities) != 15:
        return "FAIL"
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if len(set(tour)) != len(tour):
        return "FAIL"
    
    calculated_cost = 0
    max_segment_distance = 0
    
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        max_segment_distance = max(max_segment_distance, dist)
        calculated_cost += dist
    
    if round(calculated_cost, 2) != cost:
        return "FAIL"
    
    if round(max_segment_distance, 2) != longest_distance:
        return "FAIL"
    
    return "CORRECT"

# Example output provided to validate
tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
cost = 442.57
longest_distance = 85.21

# Test the provided solution
result = validate_solution(tour, cost, longest_distance)
print(result)