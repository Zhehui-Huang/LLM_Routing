import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tsp_solution(tour, total_cost, city_coordinates):
    # Check if the tour starts and ends at the depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once, except depot city
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(city_coordinates) - 1 or len(tour[1:-1]) != len(city_coordinates) - 1:
        return "FAIL"
    
    # Calculate the accumulated travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])

    # Check if the calculated tour cost is approximately equal to the provided total cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# City coordinates indexed by city number
city_coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Provided tour and total cost
tour = [0, 3, 1, 5, 7, 9, 8, 2, 6, 4, 0]
total_cost = 336.7740189101895

# Check the solution validity
result = verify_tsp_solution(tour, total_cost, city_coordinates)
print(result)