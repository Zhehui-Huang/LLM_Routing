import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tour_and_cost(cities, tour, total_cost):
    # Checking if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Checking if exactly 6 cities are visited, including the depot
    if len(tour) != 7: # 6 cities + 1 return to depot
        return "FAIL"
    
    # Calculate the total travel cost for the provided tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    # Check if the provided total cost is accurately calculated
    if not math.isclose(total_cost, calculated_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Provided solution tour and cost
solution_tour = [0, 6, 1, 7, 3, 9, 0]
solution_total_cost = 118.8954868377263

# Validate the provided solution
result = validate_tour_and_cost(cities, solution_tour, solution_total_cost)
print(result)