import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, total_cost):
    cities_coordinates = [
        (54, 87), (21, 84), (69, 84), (53, 40),
        (54, 42), (36, 30), (52, 82), (93, 44),
        (21, 78), (68, 14), (51, 28), (44, 79),
        (56, 58), (72, 43), (6, 99)
    ]
    
    # Check if starts and ends at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 8 cities are visited, including the depot city
    if len(tour) != 9:  # Includes the returning to the starting point
        return "FAIL"
    
    # Check if all cities in the tour are unique (except the returning to the starting point)
    if len(set(tour[:-1])) != 8:
        return "FAIL"
    
    # Calculate the computed total travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        computed_cost += euclidean_distance(cities_coordinates[city1], cities_coordinates[city2])
    
    # Check for nearly equal computed cost and given total cost using a tolerance
    if not math.isclose(computed_cost, total_cost, abs_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Provided solution
tour = [0, 2, 11, 12, 4, 3, 8, 14, 0]
total_cost = 208.30272552977152

result = verify_tour(tour, total cost)
print(result)