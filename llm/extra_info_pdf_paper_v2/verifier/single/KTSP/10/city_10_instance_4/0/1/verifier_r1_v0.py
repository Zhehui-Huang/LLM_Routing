import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
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

    # [The robot starts and ends its journey at depot city 0.]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [The robot must visit exactly 8 cities, including the depot city.]
    if len(set(tour)) != 9:  # Including start and end the same
        return "FAIL"

    # [Output the tour as a list of city indices starting and ending at city 0.]
    if not all(city in tour for city in tour):
        return "FAIL"

    # [Travel cost is the Euclidean distance between two cities.]
    # Calculate all successive distances, sum them and compare with reported total cost
    calculated_total_cost = 0
    for i in range(1, len(tour)):
        calculated_total_cost += calculate_euclidean_distance(cities[tour[i-1]], cities[tour[i]])

    # Rounded to two decimals for floating-point comparison issues
    if not math.isclose(calculated_total_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    # If all tests passed
    return "CORRECT"

# Provided Solution
tour = [0, 3, 5, 7, 1, 9, 6, 4, 0]
total_cost = 257.48

# Validate the solution
result = verify_solution(tour, total_cost)
print(result)