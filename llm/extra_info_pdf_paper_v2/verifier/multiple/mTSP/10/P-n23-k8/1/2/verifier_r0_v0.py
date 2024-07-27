import math
from collections import Counter

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_tours_and_costs(tours, city_coordinates, individual_costs, total_cost):
    all_visited_cities = []

    # Verify if all cities are visited exactly once and check individual tour costs
    for i, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # check if tour starts and ends at the depot

        visited_cities = tour[1:-1]  # exclude depot city at start/end
        all_visited_cities.extend(visited_cities)

        # Compute the travel cost and compare with the provided individual cost
        calculated_cost = sum(euclidean_distance(city_coordinates[tour[j]], city_coordinates[tour[j+1]]) 
                               for j in range(len(tour)-1))
        if not math.isclose(calculated_cost, individual_costs[i], rel_tol=1e-5):
            return "FAIL"

    # Check if all cities except depot are visited exactly once
    city_count = Counter(all_visited_cities)
    if any(count != 1 for count in city_count.values()) or city_count[0] > 0 or len(city_count) != len(city_coordinates) - 1:
        return "FAIL"

    # Verify the overall total travel cost
    if not math.isclose(sum(individual_costs), total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECTION"

# Test data from the output
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

tours = [
    [0, 8, 19, 1, 6, 0],
    [0, 3, 0],
    [0, 2, 0],
    [0, 16, 17, 9, 0],
    [0, 11, 13, 0],
    [0, 14, 0],
    [0, 5, 18, 15, 21, 0],
    [0, 12, 4, 7, 20, 10, 22, 0]
]

individual_costs = [
    100.16901525172257, 65.11528238439882, 42.04759208325728, 
    77.53751384914602, 94.17242872917295, 61.741396161732524,
    113.06937025626995, 154.67389659391802
]

overall_total_cost = 708.5264953096182

# Perform the verification
result = verify_tours_and_costs(tours, city_coordinates, individual_costs, overall_total_cost)
print(result)