import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, expected_total_cost, expected_max_distance, cities):
    # Check if the tour starts and ends at the depot city (0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city from 1 to 14 is visited exactly once
    if sorted(tour[1:-1]) != list(range(1, 15)):
        return "FAIL"

    # Calculate the total cost and max distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour)-1):
        city1, city2 = tour[i], tour[i+1]
        x1, y1 = cities[city1]
        x2, y2 = cities[city2]
        distance = euclidean_distance(x1, y1, x2, y2)
        total_cost += distance
        if distance > max_display:
            max_distance = distance

    # Check if calculated total travel cost matches the expected total cost
    if abs(total_cost - expected_total_cost) > 0.01:  # use some tolerance for floating point comparison
        return "FAIL"

    # Check if calculated max distance matches the expected max distance
    if abs(max_distance - expected_max_distance) > 0.01:  # use some tolerance for floating point comparison
        return "FAIL"

    return "CORRECT"

# Define city coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Provided solution
tour = [0, 2, 12, 3, 5, 13, 7, 9, 10, 4, 11, 6, 1, 14, 8, 0]
expected_total_cost = 376.19
expected_max_distance = 39.05

# Verify the solution
result = verify_solution(tour, expected_total_cost, expected_max_distance, cities)
print(result)