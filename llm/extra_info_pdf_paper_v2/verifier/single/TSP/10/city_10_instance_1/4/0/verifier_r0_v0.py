import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour_and_cost(cities, tour, reported_cost):
    # Check Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Visits each city exactly once, except the depot
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or len(tour) != len(cities) + 1:
        return "FAIL"
      
    # Check Requirement 3 & 4: Compute the travel cost as the Euclidean distance
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    # Check Requirement 5: Compare computed cost with the provided cost
    if abs(computed_cost - reported_cost) > 1e-5:
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Define the cities
cities = {0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80),
          4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44),
          8: (17, 69), 9: (95, 89)}

# Provided tour and travel cost
provided_tour = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
provided_cost = 278.9348447394249

# Call verification function
result = verify_tour_and_cost(cities, provided_tour, provided_cost)
print(result)