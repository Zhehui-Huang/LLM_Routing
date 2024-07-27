import numpy as np

# Provided cities coordinates and given solution
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82),
    4: (97, 28), 5: (0, 31), 6: (8, 62), 7: (74, 56),
    8: (85, 71), 9: (6, 76)
}

tour = [0, 7, 1, 4, 2, 5, 6, 9, 3, 8, 0]
given_total_cost = 294.17

# Function to calculate the Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Function to calculate the total cost of the tour
def calculate_total_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        total_cost += euclidean_distance(cities[city_from], cities[city_to])
    return total_cost

# Unit tests to verify the solution
def test_tour(tour, cities, given_total_cost):
    # Test 1: The robot must start and end the tour at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Test 2: Each city must be visited exactly once by the robot, except for the depot city.
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or not all(city in unique_cities for city in cities):
        return "FAIL"

    # Test 3: Check the total travel cost with a leniency in floating point comparison
    calculated_cost = calculate_total_cost(tour, cities)
    if not np.isclose(calculated_cost, given_total_tour_cost, atol=0.1):
        return "FAIL"

    return "CORRECT"

# Run the test
result = test_tour(tour, cities, given_total_cost)
print(result)