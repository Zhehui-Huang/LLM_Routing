import math

# List of city coordinates
cities = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
          (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
          (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Proposed tour and calculated values
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 15, 4, 3, 19, 0]
total_travel_cost = 410.03585920085146
maximum_distance_between_cities = 89.00561780022652

def verify_tour(tour, total_cost, max_distance):
    # Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit each city exactly once (plus the starting city)
    if len(tour) != len(cities) + 1:
        return "FAIL"
    unique_cities = set(tour)
    if len(unique_cities) != len(cities):
        return "FAIL"

    # Calculate actual travel costs and distances
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)

    # Compare calculated costs and distances with given values
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Execute the verification function
result = verify_tour(tour, total_travel_cost, maximum_distance_between_cities)
print(result)