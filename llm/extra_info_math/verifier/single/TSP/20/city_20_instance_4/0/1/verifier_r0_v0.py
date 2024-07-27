import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def test_solution(tour, cities, expected_cost):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once, except for the depot
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Calculate the total travel cost
    total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    
    # Check if the reported total cost matches the calculated cost
    if not math.isclose(total_cost, expected_cost, abs_tol=1e-3):
        return "FAIL"
    
    # All tests passed
    return "CORRECT"

# City coordinates including the depot city
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Given tour and cost
tour = [0, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
reported_cost = 0  # Seems incorrect but for testing purpose, we calculate real cost

result = test_solution(tour, cities, reported_cost)
print(result)