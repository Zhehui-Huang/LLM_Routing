import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    """ Calculate Euclidean distance between two points (x1, y1) and (x2, y2). """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(cities, tour, reported_cost):
    # Requirement 4 & 1: Check if the tour starts and ends with the depot city and includes all cities
    if tour[0] != 0 or tour[-1] != 0 or sorted(tour) != sorted([i for i in range(len(cities))]):
        return "FAIL"

    # Requirement 1 & 3: Check that each city (except the depot) is visited exactly once
    if len(set(tour[1:-1])) != len(cities) - 1:
        return "FAIL"

    # Calculate the total travel cost traversing the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i+1]]
        total_cost += calculate_euclidean_distance(city1[0], city1[1], city2[0], city2[1])
    
    # Requirement 2 & 5: Check that the reported distance matches the calculated distance
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# City coordinates: city index : (x, y)
city_coordinates = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
    6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}
# Proposed solution details
tour = [0, 2, 7, 13, 4, 5, 10, 9, 3, 12, 11, 14, 1, 8, 6, 0]
total_cost = 339.033906708712

# Given the city coordinates and the proposed tour with its total cost,
# we verify if the solution is correct by checking all requirements.
result = verify_tour([city_coordinates[i] for i in range(len(city_coordinates))], tour, total_cost)
print(result)