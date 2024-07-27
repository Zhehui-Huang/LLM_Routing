import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    if len(set(tour)) != len(cities):
        return "FAIL"
    
    if len(tour) != len(cities) + 1:
        return "FAIL"
    
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        distance = calculate_euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])
        total_cost += distance
        max_distance = max(max_distance, distance)
        
    return "CORRECT"

# Define the city coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), (97, 62), (14, 41),
    (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Test with an example tour (this should be the output of the BTSP solution)
test_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]

# Validate the solution
result = verify_tour(test_tour, cities)
print(result)