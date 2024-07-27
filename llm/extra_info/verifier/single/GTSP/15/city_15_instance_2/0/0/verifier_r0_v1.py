import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_requirements(tour, total_cost, city_coordinates, groups):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Start and end city check
    # Check if exactly one city from each group is visited
    for group in groups:
        if sum(city in tour[1:-1] for city in group) != 1:
            return "FAIL"
    # Calculate the total travel cost from the tour
    calculated_cost = sum(calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"  # Total cost calculation check
    return "CORRECT"

# Provided city coordinates and groups
city_coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Provided solution details
tour = [0, 12, 7, 4, 1, 2, 0]  # from problem solution
total_cost = 44.36594224827562  # from problem solution

# Check if the provided solution meets all requirements
result = check_requirements(tour, total_cost, city_intervals, groups)
if result == "CORRECT":
    print("CORRECT")
else:
    print("FAIL")