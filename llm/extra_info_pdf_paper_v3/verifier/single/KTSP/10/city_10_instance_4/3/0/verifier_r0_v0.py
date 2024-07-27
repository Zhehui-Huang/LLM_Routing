import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, cities, total_travel_cost):
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        print("The tour must start and end at the depot city (city 0).")
        return "FAIL"

    # Check if exactly 8 cities are visited, including the depot
    if len(tour) != 9:
        print("The tour must visit exactly 8 cities, including the depot.")
        return "FAIL"
    
    # Calculate total travel cost via Euclidean distances and compare it
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        print("The total travel cost does not match the calculated Euclidean distances.")
        return "FAIL"
    
    # If all conditions are satisfied
    return "CORRECT"

# City coordinates
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

# Provided tour and total travel cost
tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
total_travel_cost = 235.38

# Validate the solution
result = verify_tour(tour, cities, total_travel_cost)
print(result)