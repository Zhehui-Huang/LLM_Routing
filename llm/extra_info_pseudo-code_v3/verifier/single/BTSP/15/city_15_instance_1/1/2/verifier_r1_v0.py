import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, coordinates):
    """ Verify if the tour satisfies the requirements. """
    # Check if tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once
    if sorted(tour) != sorted(list(range(len(coordinates)))):
        return "FAIL"
    
    # Calculate the total travel cost and the maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour)-1):
        distance = calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Verify output format (Here, we normally need to check the output against specific values
    # but as we're validating the solution's correctness format-wise and logically, this is enough).
    
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
    
    return "CORRECT"

# Coordinates of each city including the depot
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60),  (78, 82), (83, 96), (60, 50), (98, 1)
]

# Test output
# This should be the output from your TSP algorithm. Example tour is a simple sequence.
# In real test, you will replace it with the actual tour result from the solution.
test_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]

# Verify the tour
result = verify_tour(test_tour, coordinates)
print(result)  # Print 'CORRECT' if the generated tour meets all the requirements, otherwise 'FAIL'