import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, expected_cost):
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    
    # Check: The robot has to travel starting and ending at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check: The robot can visit exactly 5 cities in total, including the depot city
    if len(tour) != 6:
        return "FAIL"

    # Check: Travel cost calculation based on the Euclidean distance
    total_cost = 0
    for i in range(1, len(tour)):
        city1 = cities[tour[i-1]]
        city2 = cities[tour[i]]
        total_cost += calculate_euclidean_distance(city1[0], city1[1], city2[0], city2[1])

    # Check: The goal is to find the shortest possible tour path that meets the above requirements
    if abs(total_cost - expected_cost) > 1e-6:
        return "FAIL"

    return "CORRECT"

# Provided solution
tour = [0, 4, 8, 3, 5, 0]
total_travel_cost = 110.38072506104011

# Verify the solution
print(verify_solution(tour, total_travel_cost))