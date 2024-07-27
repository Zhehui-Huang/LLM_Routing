import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_solution(tour, cities, claimed_cost):
    # Verify start and end at the depot city (city 0)
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Verify each city is visited exactly once, except the depot city
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Verify the correct calculation of the total travel cost
    total_cost_calculated = 0
    for i in range(len(tour) - 1):
        total_cost_calculated += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if abs(total_cost_calculated - claimed_cost) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# City positions, with city indices matching those provided in the problem
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Given tour and claimed travel cost
tour = [0, 19, 8, 10, 15, 4, 3, 6, 12, 7, 16, 5, 9, 2, 14, 11, 13, 1, 18, 17, 0]
claimed_cost = 398.67

# Execute the verification
result = verify_solution(tour, cities, claimed_cost)
print(result)