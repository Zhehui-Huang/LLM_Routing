import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    # Coordinates for each city, index represents the city number
    coordinates = [
        (35, 40),  # City 0: Depot
        (39, 41),  # City 1
        (81, 30),  # City 2
        (5, 50),   # City 3
        (72, 90),  # City 4
        (54, 46),  # City 5
        (8, 70),   # City 6
        (97, 62),  # City 7
        (14, 41),  # City 8
        (70, 44),  # City 9
        (27, 47),  # City 10
        (41, 74),  # City 11
        (53, 80),  # City 12
        (21, 21),  # City 13: Not visited
        (12, 39)   # City 14: Not visited
    ]

    # Solution provided
    tour = [0, 5, 9, 7, 4, 12, 11, 6, 3, 8, 10, 1, 0]
    reported_cost = 238.97

    # Check if tour starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if length of tour, excluding start and end, is 12
    if len(tour) - 1 != 12:
        return "FAIL"

    # Ensure all cities are unique in the tour except the depot
    unique_cities = set(tour[1:-1])
    if len(unique_cities) + 1 != len(tour) - 1:
        return "FAIL"

    # Check if all cities in the tour are among defined cities
    if any(city > len(coordinates) or city < 0 for city in tour):
        return "FAIL"

    # Check if computed travel cost matches the reported total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])

    # Use a tolerance for floating-point comparison
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Running the test
print(test_solution())