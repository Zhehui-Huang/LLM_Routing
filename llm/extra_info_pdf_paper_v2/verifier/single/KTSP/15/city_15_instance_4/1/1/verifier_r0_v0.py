import math

def calculate_euclidean_distance(city_a, city_b):
    """ Helper function to calculate Euclidean distance between two cities """
    x1, y1 = city_a
    x2, y2 = city_b
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, reported_cost):
    # Coordinates of all cities
    coordinates = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }
    
    # Checks if the depots at the start and end are correct
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check for exactly 12 distinct cities visited including the depot city
    if len(set(tour)) != 12:
        return "FAIL"
    
    # Calculate the total travel cost of the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    # Compare the calculated cost to the reported cost
    if abs(calculated_cost - reported_cost) > 0.01:  # Allowing small margin due to floating point arithmetic variations
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Test the provided example solution
example_tour = [0, 14, 8, 10, 13, 1, 5, 9, 4, 12, 11, 6, 0]
example_reported_cost = 280.23

# Verify the example solution
test_result = verify_solution(example_tour, example_reported_cost)
print(test_result)