import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_tour(tour, total_travel_cost):
    cities = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
        (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
        (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
        (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
    ]
    
    # Check start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all other cities are visited exactly once
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return "FAIL"
    
    # Calculate the total travel cost and compare
    calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Provided solution to verify
tour = [0, 6, 9, 2, 12, 13, 1, 8, 18, 15, 19, 17, 11, 10, 16, 4, 7, 5, 14, 3, 0]
total_travel_cost = 381.11325116397535

# Verification
result = verify_tour(tour, total_travel_cost)
print(result)