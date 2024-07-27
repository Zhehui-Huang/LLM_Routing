import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_tsp_solution():
    cities_coordinates = {
        0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
        5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
    }
    tour = [0, 4, 7, 5, 1, 9, 8, 2, 6, 3, 0]
    total_travel_cost = 320.7939094250147

    # Checking if the cities in the provided tour are valid
    if sorted(set(tour[:-1])) != sorted(cities_coordinates.keys()):
        return "FAIL"

    # Checking if the starting and ending city is the depot city 0
    if tour[0] != tour[-1] != 0:
        return "FAIL"

    # Verify all cities are visited exactly once
    for city in tour[1:-2]:
        if tour.count(city) != 1:
            return "FAIL"

    # Calculate travel cost from the provided tour and coordinates
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])

    # Check the total travel cost
    if not math.isclose(total_travel_cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Run the unit test
print(test_tsp_solution())