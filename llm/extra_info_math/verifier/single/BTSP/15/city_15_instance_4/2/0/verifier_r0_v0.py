import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, cities, max_dist_between_cities):
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the tour contains all cities exactly once (excluding the final return to the depot)
    if sorted(tour[1:-1]) != sorted(list(range(1, len(cities)))):
        return "FAIL"

    # Check if the total travel cost and the maximum distance condition hold
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    # Comparing the calculated max distance to the given one with a small tolerance
    if max_distance > max_dist_between_cities + 1e-5:
        return "FAIL"

    return "CORRECT"

# Cities given in the problem:
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
          (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
          (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

# Given tour and metrics:
tour = [0, 3, 10, 1, 13, 14, 8, 6, 11, 4, 12, 5, 2, 9, 7, 0]
max_distance_between_cities = 65.79

# Output validation result:
print(validate_tour(tour, cities, max_distance_between_cities))