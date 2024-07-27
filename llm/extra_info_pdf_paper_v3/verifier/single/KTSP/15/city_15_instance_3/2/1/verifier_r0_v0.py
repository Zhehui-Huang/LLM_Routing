import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, distances, required_distance):
    """ Check if the tour satisfies all the requirements. """
    # Check start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check exactly 10 cities are visited including the depot
    if len(set(tour)) != 10:
        return "FAIL"
    
    # Calculate the total distance travelled
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(distances[tour[i]], distances[tour[i+1]])
    
    # Compare calculated distance with required distance
    if not math.isclose(total_distance, required_distance, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of the cities
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# The proposed tour and total travel cost
proposed_tour = [0, 0, 6, 8, 13, 10, 9, 5, 14, 4, 1, 0]
proposed_cost = 169.91

# Validate the tour
result = verify_tour(proposed_tour, cities, proposed_cost)
print(result)