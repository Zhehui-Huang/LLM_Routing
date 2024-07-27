import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_tour(cities, tour, reported_cost):
    # Requirement 1: The tour must start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour does not start and end at depot city."

    # Requirement 2: Each city, except the depot, visited exactly once
    unique_cities = set(tour[1:-1])  # Excludes the initial and terminal depot cities
    if len(unique_cities) != len(cities) - 1 or not all(city in unique_cities for city in range(1, len(cities))):
        return False, "Not all cities are visited exactly once."

    # Requirement 3 & 5: Check the total travel cost using Euclidean distance
    total_cost_calculated = 0
    for i in range(len(tour) - 1):
        total_cost_calculated += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(total_cost_calculated, reported_cost, rel_tol=1e-3):
        return False, f"Reported cost is not equal to the calculated cost. Reported: {reported_cost}, Calculated: {total_cost_calculated}"

    # Requirements 4: Output list with starting and ending at depot city not explicitly needed in calculations
    
    # Output assumed correct structure if all above tests are passed
    return True, "CORRECT"

# Define the cities coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Provided tour and cost
tour = [0, 8, 10, 1, 11, 14, 9, 4, 12, 7, 3, 5, 6, 2, 13, 0]
total_cost = 373.97

# Verify the solution
is_correct, message = verify_tour(cities, tour, total_cost)
print(is_correct, message)