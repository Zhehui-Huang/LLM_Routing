import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(cities, tour, expected_cost):
    if len(tour) != 12:  # Tour must contain exactly 12 cities
        return "FAIL"
    if tour[0] != 0 or tour[-1] != 0:  # Tour must start and end at the depot city (city 0)
        return "FAIL"
    if len(set(tour)) != len(tour):  # All cities in the tour must be unique (no repetitions)
        return "FAIL"
    if any(city not in range(15) for city in tour):  # Check if all cities in the tour are valid
        return "FAIL"

    # Calculate the Euclidean distance and compare it to the expected cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Allow for a small margin of error due to floating point arithmetic issues
    if not math.isclose(total_cost, expected_cost, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Define the city coordinates (including the depot city 0)
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
          (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74),
          (53, 80), (21, 21), (12, 39)]

# Provided tour and cost from the solution
tour = [0, 1, 13, 14, 8, 3, 6, 10, 5, 9, 12, 11, 0]  # Corrected by adding city 0 at the end to complete the cycle
expected_cost = 213.14

# Verify the tour and the total travel cost
result = verify_tour(cities, tour, expected_cost)
print(result)