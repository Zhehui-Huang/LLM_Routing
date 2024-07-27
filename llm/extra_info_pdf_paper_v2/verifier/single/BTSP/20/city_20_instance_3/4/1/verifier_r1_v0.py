import math

# Coordinates of cities including the depot city 0
city_coords = [
    (30, 56),  # city 0
    (53, 42),  # city 1
    (1, 95),   # city 2
    (25, 61),  # city 3
    (69, 57),  # city 4
    (6, 58),   # city 5
    (12, 84),  # city 6
    (72, 77),  # city 7
    (98, 95),  # city 8
    (11, 0),   # city 9
    (61, 25),  # city 10
    (52, 0),   # city 11
    (60, 95),  # city 12
    (10, 94),  # city 13
    (96, 73),  # city 14
    (14, 47),  # city 15
    (18, 16),  # city 16
    (4, 43),   # city 17
    (53, 76),  # city 18
    (19, 72)   # city 19
]

# Solution provided
solution_tour = [0, 3, 19, 6, 13, 2, 15, 17, 16, 9, 5, 1, 10, 11, 4, 7, 18, 12, 14, 8, 0]
solution_cost = 576.0
solution_max_distance = 78.39

# Helper function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

def test_solution():
    # Check if the tour starts and ends at the depot city 0
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once
    if sorted(solution_tour[:-1]) != list(range(20)):
        return "FAIL"
    
    # Calculate and validate the total cost and maximum distance between consecutive cities
    calculated_cost, calculated_max_distance = 0.0, 0.0
    for i in range(len(solution_tour) - 1):
        dist = distance(solution_tour[i], solution_tour[i + 1])
        calculated_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist

    if not (math.isclose(calculated_cost, solution_cost) and math.isclose(calculated_max_distance, solution_max_distance, rel_tol=1e-2)):
        return "FAIL"
    
    return "CORRECT"

# Execute the test
result = test_solution()
print(result)