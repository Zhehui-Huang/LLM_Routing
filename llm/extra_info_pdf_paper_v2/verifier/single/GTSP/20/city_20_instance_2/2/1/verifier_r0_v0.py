import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_tour(tour, coordinates, city_groups):
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = []
    for city in tour[1:-1]:  # exclude the depot city at the start and end
        for i, group in enumerate(city_groups):
            if city in group:
                visited_groups.append(i)
                break
    if sorted(visited_groups) != list(range(len(city_tools))):
        return "FAIL"
    
    # Calculate the travel cost and compare
    # Add coordinates for each city in the tour
    tour_coords = [coordinates[city] for city in tour]
    
    # Calculate total distance
    total_distance = sum(calculate_euclidean_distance(tour_coords[i], tour_coords[i+1]) for i in range(len(tour_coords) - 1))
    
    # Given total cost in the solution
    given_total_cost = 162.3829840233368

    # Allow for small floating-point discrepancies
    if not math.isclose(total_distance, given_total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If passes all checks
    return "CORRECT"

# Define city coordinates and groups
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Example tour to verify
example_tour = [0, 11, 16, 18, 19, 6, 0]

# Run the test on the provided tour
test_result = test_tour(example_tour, coordinates, city_groups)
print(test_result)