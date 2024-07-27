import math

# Define a function to compute Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Define cities coordinates according to the problem description
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Given solution
tour = [0, 5, 9, 4, 8, 3, 2, 1, 6, 7, 0]
total_cost_given = 271.4716218753353

# Function to validate the TSP solution
def validate_tsp_solution(tour, cities, total_cost_given):
    # Check if all cities are visited exactly once, except depot city
    if sorted(tour) != sorted(list(cities.keys()) + [0]):
        return "FAIL"

    # Calculate the total cost of the tour using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    # Check if the calculated cost matches the given cost
    if round(calculated_cost, 10) != round(total_cost_given, 10):
        return "FAIL"

    return "CORRECT"

# Testing the solution
result = validate_tsp_solution(tour, cities, total_cost_given)
print(result)