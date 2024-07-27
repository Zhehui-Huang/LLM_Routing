import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_tour(tour, coordinates):
    """Verify the TSP solution based on given conditions."""
    # Tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour does not start and end at the depot."
    
    # All cities (except the depot which is visited twice) must be visited exactly once
    visited = set(tour[1:-1])
    if len(visited) != len(coordinates) - 1 or any(city not in visited for city in range(1, len(coordinates))):
        return False, "Not all cities are visited exactly once, or some are visited more than once."

    # Calculate the total travel cost
    total_distance = sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
                         for i in range(len(tour) - 1))
    
    return True, total_distance

# Coordinates of each city, including depot
coordinates = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Solution to be verified
tour_solution = [0, 4, 7, 5, 1, 9, 8, 2, 6, 3, 0]
reported_total_cost = 320.7939094250147

# Perform verification
is_valid, calculated_cost = verify_tour(tour_solution, coordinates)

if is_valid and math.isclose(calculated_cost, reported_total_cost, abs_tol=0.01):
    print("CORRECT")
    print(f"Calculated Total Travel Cost: {calculated_cost}")
else:
    print("FAIL")
    print(f"Calculated Total Travel Cost: {calculated_cost if is_valid else 'Invalid tour configuration.'}")