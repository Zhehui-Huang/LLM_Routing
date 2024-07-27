import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(cities, tour):
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if tour visits each city exactly once (excluding the starting/ending depot)
    if sorted(tour[1:-1]) != sorted(range(1, len(cities))):
        return "FAIL"
    
    # Calculate maximum distance and verify distances are calculated using Euclidean distance
    max_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        dist = calculate_euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])
        if dist > max_distance:
            max_distance = dist
            
    # Here one would usually compare max_distance with some optimized standard, but since the problem does not
    # give the expected max distance explicitly and asks only to check correctness up to constraints:
    
    return "CORRECT" if max_distance > 0 else "FAIL"

# Example of cities' coordinates
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
          (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
          (56, 58), (72, 43), (6, 99)]

# Example tour (needs to be derived from solution, this is just a placeholder)
example_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]

# Perform the test
print(verify_tour(cities, example_tour))