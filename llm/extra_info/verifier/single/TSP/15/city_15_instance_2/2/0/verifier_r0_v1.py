import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_solution(tour, total_cost):
    # Define the city coordinates
    cities_coordinates = [
        (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), 
        (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
    ]

    # [Requirement 1] The robot must start and end the tour at the depot city (city 0).
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # [Requirement 2] The robot must visit each of the other 14 cities exactly once.
    if sorted(tour[1:-1]) != list(range(1, 15)):
        return "FAIL"
    
    # [Requirement 3] The calculated travel cost should be close to the given total cost.
    calculated_cost = sum(calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]]) for i in range(len(tour)-1))
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Define the provided solution
tour_solution = [0, 6, 11, 8, 1, 14, 12, 4, 3, 10, 5, 9, 13, 7, 2, 0]
total_travel_cost_solution = 322.5037276986899

# Verify the solution
result = check_solution(tour_solution, total_travel_cost_solution)
print(result)