import math

# Coordinates of the cities
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

# Provided tour and cost
tour = [0, 3, 6, 9, 1, 5, 7, 4, 0]
cost = 235.37735391753955

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def test_solution(tour, cost):
    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if 8 cities are visited (including depot city, and excluding the final return to depot in count)
    if len(set(tour[:-1])) != 8:
        return "FAIL"
    
    # Calculate the actual tour cost and compare it to the provided cost
    actual_cost = 0
    for i in range(len(tour) - 1):
        actual_cost += calculate_euclidean_distance(tour[i], tour[i + 1])

    # Using a tolerance due to potential floating point arithmetic issues
    if not math.isclose(actual_cost, cost, abs_tol=1e-5):
        print("Calculated Cost:", actual_cost)
        return "FAIL"
    
    return "CORRECT"

# Run the tests and print the result
result = test_solution(tour, cost)
print(result)