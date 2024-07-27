import math

# Define unit tests to validate the given tour based on the requirements
def test_tour_requirements(tour, total_cost, cities):
    # [Requirement 1] Start and end at the depot city, which is city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Visit exactly 8 cities, including the depot city
    if len(set(tour)) != 8:
        return "FAIL"

    # [Requirement 4] Travel cost as Euclidean distance between any two cities
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        calculated_cost += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Check if the calculated total cost is close to the provided total cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    # [Requirement 5] Output should list the city indices starting and ending at the depot city
    # Automatically validated by [Requirement 1]

    # [Requirement 6] Include the total travel cost of the tour
    # This is calculated and compared in above code

    return "CORRECT"

# Given cities coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Given tour and total cost
tour = [0, 6, 1, 5, 7, 9, 3, 4, 0]
total_cost = 261.79

# Execute tests
result = test_tour_requirements(tour, total_cost, cities)
print(result)