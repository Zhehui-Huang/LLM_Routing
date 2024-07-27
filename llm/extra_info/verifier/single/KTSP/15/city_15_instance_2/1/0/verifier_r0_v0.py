import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, total_cost):
    cities = [
        (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
        (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
        (56, 58), (72, 43), (6, 99)
    ]

    # Verify the number of cities is exactly 8 and includes the depot city
    if len(tour) != 9 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify that all cities in tour are unique except for the start and end
    cities_in_tour = set(tour)
    if len(cities_in_tour) != 8:
        return "FAIL"

    # Check the number of unique places visited, excluding the depot if it's listed more than once
    if len(tour) - list(tour).count(0) + 1 != len(cities_in_tour):
        return "FAIL"

    # Verify correct calculation of travel cost
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    # Tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    return "CORRECT"

# Tour solution to verify
tour = [0, 2, 13, 3, 4, 12, 11, 6, 0]
total_cost = 132.1185774560832

# Output the result of verification
print(verify_tour(tour, total_cost))