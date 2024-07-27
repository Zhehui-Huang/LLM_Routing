import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_solution(tour, total_cost, city_coordinates, city_groups):
    # Check if tour starts and ends at the depot (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour visits one city from each group
    visited_groups = set()
    for city_index in tour[1:-1]:  # Exclude the depot city at start and end
        for group_index, group in enumerate(city_groups):
            if city_index in group:
                visited_groups.add(group_index)
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Calculate the travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    # Check if calculated cost matches the provided total cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Define city coordinates based on the main problem
city_coordinates = [
    (8, 11),  # Depot
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

city_groups = [
    [1, 3, 5, 11, 13, 14, 19], # Group 0
    [2, 6, 7, 8, 12, 15],      # Group 1
    [4, 9, 10, 16, 17, 18]     # Group 2
]

# Test the provided solution
result = validate_solution(
    tour=[1, 1, 15, 17, 1],
    total_cost=98.37,
    city_coordinates=city_coordinates,
    city_groups=city_groups
)

print(result)