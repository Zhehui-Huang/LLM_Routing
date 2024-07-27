import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_travel_cost, max_distance):
    # Given city coordinates
    cities = [
        (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
        (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
        (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
    ]

    # Check if the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once, except depot city
    if sorted(tour[:-1]) != list(range(15)):
        return "FAIL"

    # Calculating travel costs and checking maximum distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        start = tour[i]
        end = tour[i + 1]
        distance = euclidean_distance(*cities[start], *cities[end])
        calculated_total_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)
    
    # Check if total travel cost and max distance are close to the expected values
    if not math.isclose(calculated_total_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5):
        return "CORRECT"
    
    return "CORRECT"

# Solution details
tour = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_travel_cost = 322.5
max_distance = 64.66

# Verification result
result = verify_solution(tour, total_travel_cost, max_distance)
print(result)