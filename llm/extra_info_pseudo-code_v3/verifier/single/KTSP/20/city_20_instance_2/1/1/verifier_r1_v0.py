import math

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def test_solution():
    # City coordinates as given in the problem
    cities = [
        (3, 26),   # Depot City 0
        (85, 72),
        (67, 0),
        (50, 99),
        (61, 89),
        (91, 56),
        (2, 65),
        (38, 68),
        (3, 92),
        (59, 8),
        (30, 88),
        (30, 53),
        (11, 14),
        (52, 49),
        (18, 49),
        (64, 41),
        (28, 49),
        (91, 94),
        (51, 58),
        (30, 48)
    ]
    
    # Claimed solution tour and cost
    tour = [0, 12, 14, 7, 4, 18, 2, 15, 11, 16, 0]
    claimed_cost = 317.1936577205922

    # Check number of cities
    if len(cities) != 20:
        return "FAIL"

    # Check depot city
    if cities[0] != (3, 26):
        return "FAIL"

    # Check if starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 10 cities are visited
    if len(set(tour)) != 10:
        return "FAIL"

    # Verify that correct cities are visited and no city outside range is visited
    if any(city_index < 0 or city_index >= len(cities) for city_index in tour):
        return "FAIL"

    # Verify the total travel cost
    calculated_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, claimed_cost, rel_tol=1e-9):
        return "FAIL"

    # If all checks passed
    return "CORRECT"

# Call the function to test the solution
print(test_solution())