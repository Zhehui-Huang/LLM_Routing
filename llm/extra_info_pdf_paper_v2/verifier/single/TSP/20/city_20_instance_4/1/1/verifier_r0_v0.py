import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost):
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
        (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
        (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    
    # Check if the tour starts and ends at city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Check if all cities, except for the depot, are visited exactly once
    visited = set(tour)
    if len(visited) != 20 or any(tour.count(city) != 1 for city in range(1, 20)):
        return "FAIL"
    
    # Calculate the total travel cost and compare with the given total_cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        calculated_cost += calculate_distance(x1, y1, x2, y2)

    if abs(calculated_cost - total_cost) > 1e-9:
        return "FAIL"
    
    return "CORRECT"

# Provided tour and total cost
tour = [0, 19, 8, 17, 18, 13, 1, 11, 14, 2, 9, 5, 16, 7, 12, 3, 4, 6, 10, 15, 0]
total_cost = 390.8040948836427

# Verification of the solution
result = verify_solution(tour, total_cost)
print(result)