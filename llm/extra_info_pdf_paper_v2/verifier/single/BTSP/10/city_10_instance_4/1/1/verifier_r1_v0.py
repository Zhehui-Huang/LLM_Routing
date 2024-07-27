import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_solution(tour, distances, cities_coordinates):
    # Check if the tour starts and ends at the depot (city 0), and exactly once for each city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour) != sorted([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]):
        return "FAIL"
    
    # Calculate total travel cost from the tour using the distances matrix
    total_cost_calculated = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    
    # Find the maximum distance between any two consecutive cities in the tour
    max_distance_calculated = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    
    # Check if total travel cost and maximum distance matches the provided ones
    if not math.isclose(total_travel_cost, total_cost_calculated, rel_tol=1e-9):
        return "FAIL"
    if not math.isclose(max_distance, max_distance_calculated, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates
cities_coordinates = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9), 5: (83, 61), 
    6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Compute distances between every pair of cities
distances = {
    i: {j: euclidean_distance(cities_coordinates[i], cities_coordinates[j]) for j in cities_coordinates}
    for i in cities_coordinates
}

# Solution details
tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
total_travel_cost = 408.41360886151256
max_distance = 61.68468205316454

# Validate the solution
result = check_solution(tour, distances, cities_coordinates)
print(result)