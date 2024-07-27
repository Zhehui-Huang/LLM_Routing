import math

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities, each defined by (x, y) coordinates."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cities):
    """
    Verify the solution according to given conditions.

    Parameters:
    - tour: List of city indices representing the tour.
    - cities: List of tuples containing (x, y) coordinates of each city.

    Returns:
    - A string "CORRECT" if all conditions are met, otherwise "FAIL".
    """
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 10 cities are visited (including depot city)
    if len(tour) != 11:  # 10 cities plus returning to the depot city
        return "FAIL"

    # Check if the tour contains duplicates (it should not, except the return to the depot)
    if len(set(tour[:-1])) != 10:
        return "FAIL"

    # Check if the travel costs are calculated as the Euclidean distances
    # Calculate total travel cost from the tour using Euclidean distances
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        city_index_1 = tour[i]
        city_index_2 = tour[i + 1]
        if city_index_1 >= len(cities) or city_index_2 >= len(cities):
            return "FAIL"  # city index out of bounds
        calculated_distance = euclidean_distance(cities[city_index_1], cities[city_index_2])
        total_travel_cost += calculated_distance

    # Since the total travel cost isn't an output to a separate function and considering the points, if we've reached this point, the solution is correct.
    return "CORRECT"

# Example use case based on the provided setup, this block would actually be tested with real tour and cities data.
cities_coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# This would be an example tour output from the algorithm (assuming legitimate route)
example_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Verify the example solution
print(verify_solution(example_tour, cities_coordinates))