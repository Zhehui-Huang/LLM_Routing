import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_requirements(tour, total_cost, city_coordinates, groups):
    # Check start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    # Check only one city from each group is visited
    if any(sum(city in tour for city in group) != 1 for group in groups):
        return "FAIL"
    # Calculate and check the total cost
    calculated_cost = sum(calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    return "CORRECT"

# Coordinates of each city including the depot.
city_coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Groups of cities. Each sublist represents a group.
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Solution details as provided
tour = [0, 12, 7, 4, 1, 2, 0]
total_cost = 44.36594224827562

# Run the test
result = check_requirements(tour, total))cost, city_coordinates, groups)
print(result)  # Should print "CORRECT" if everything matches the requirements, otherwise "FAIL"