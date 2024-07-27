import math

# Define cities with their coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Solution tour and data
tour = [0, 13, 11, 12, 2, 5, 7, 6, 14, 8, 1, 3, 10, 9, 4, 0]
max_distance_in_tour = 50.21951811795888
total_cost_reported = 506.93756110908356

def calc_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, cities):
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once (excluding the depot which is visited twice)
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or any(tour.count(city) != 1 for city in cities if city != 0):
        return "FAIL"
    
    # Calculate actual longest distance and total cost
    actual_longest_distance = 0
    actual_total_cost = 0
    for i in range(len(tour) - 1):
        distance = calc_distance(cities[tour[i]], cities[tour[i+1]])
        actual_total_cost += distance
        if distance > actual_longest_distance:
            actual_longest_distance = distance

    # Check if the actual longest distance match reported and total cost
    if not math.isclose(actual_longest_distance, max_distance_in_tour, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(actual_total_cost, total_cost_reported, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Run the verification
print(verify_tour(tour, cities))