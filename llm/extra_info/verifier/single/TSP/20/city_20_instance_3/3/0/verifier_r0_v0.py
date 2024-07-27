import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities):
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once except the depot
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or any(tour.count(city) != 1 for city in cities if city != 0):
        return "FAIL"

    # Calculate the total travel cost from the tour and compare with provided cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if abs(calculated_cost - total_cost) > 0.1:  # allow some floating point error
        return "FAIL"

    return "CORRECT"

# Cities coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# Solution provided
tour_solution = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
total_travel_cost_solution = 458.36719998557066

# Verify the solution
result = verify_solution(tour_solution, total_travel_can't, cities)
print(result)