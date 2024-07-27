import math

# Provided tour and the calculated total travel cost
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 9, 5, 16, 7, 12, 6, 10, 0]
calculated_cost = 280.69500045619816

# Coordinates of the cities
city_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def test_solution(tour, calculated_cost, city_coordinates):
    # Test if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test if exactly 16 cities are included
    if len(set(tour)) - 1 != 16:  # -1 is to exclude the depot city 0 from counting twice
        return "FAIL"
    
    # Calculate the actual travel cost and compare it with the given cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_euclidean_distance(
            city_coordinates[tour[i]], city_coordinates[tour[i + 1]]
        )
    
    # Due to floating-point arithmetic, we allow a small difference
    if not math.isclose(actual_cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Run the test
result = test_solution(tour, calculated_cost, city_coordinates)
print(result)