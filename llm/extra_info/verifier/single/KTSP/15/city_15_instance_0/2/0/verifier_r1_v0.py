import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour_and_cost(tour, total_cost, coordinates):
    # Verify the tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify the tour visits exactly 4 cities including the depot city
    if len(tour) != 5:
        return "FAIL"
    
    # Calculate the expected travel cost using Euclidean distance and compare
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += calculate_euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    
    if not math.isclose(total_cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Coordinates of the cities
coordinates = [
    (9, 93),   # Depot city 0
    (8, 51),   # City 1
    (74, 99),  # City 2
    (78, 50),  # City 3
    (21, 23),  # City 4
    (88, 59),  # City 5
    (79, 77),  # City 6
    (63, 23),  # City 7
    (19, 76),  # City 8
    (21, 38),  # City 9
    (19, 65),  # City 10
    (11, 40),  # City 11
    (3, 21),   # City 12
    (60, 55),  # City 13
    (4, 39)    # City 14
]

# Provided tour solution and total cost
tour_provided = [0, 1, 10, 8, 0]
total_cost_provided = 90.53947981328088

# Verify the solution
result = verify_tour_and_cost(tour_provided, total_cost_provided, coordinates)
print(result)