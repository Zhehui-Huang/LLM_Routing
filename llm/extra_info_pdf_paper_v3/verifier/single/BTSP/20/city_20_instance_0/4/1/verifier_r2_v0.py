from math import sqrt

# Define the cities' positions
cities = [
    (8, 11),  # City 0
    (40, 6),  # City 1
    (95, 33), # City 2
    (80, 60), # City 3
    (25, 18), # City 4
    (67, 23), # City 5
    (97, 32), # City 6
    (25, 71), # City 7
    (61, 16), # City 8
    (27, 91), # City 9
    (91, 46), # City 10
    (40, 87), # City 11
    (20, 97), # City 12
    (61, 25), # City 13
    (5, 59),  # City 14
    (62, 88), # City 15
    (13, 43), # City 16
    (61, 28), # City 17
    (60, 63), # City 18
    (93, 15)  # City 19
]

# Given tour and expected results
provided_tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
provided_cost = 349.20
provided_max_dist = 32.39

# Helper function to calculate the Euclidean distance
def euclidean_distance(city_a, city_b):
    return sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

# Check if the tour starts and ends at the depot city
def check_start_and_end(tour):
    return tour[0] == 0 and tour[-1] == 0

# Check if each city is visited exactly once
def check_visit_once(tour):
    return len(set(tour)) == len(cities) and len(tour) == len(cities) + 1

# Calculate the total travel cost and the maximum distance between consecutive cities
def travel_cost_and_max_dist(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        max_distance = max(max_distance, distance)
    return total_cost, max_distance

# Unit Test Execution
if check_start_and_end(provided_tour) and check_visit_once(provided_tour):
    total_cost, max_distance = travel_cost_and_max_dist(provided_tour)
    if abs(total_cost - provided_cost) < 0.01 and abs(max_distance - provided_max_dist) < 0.01:
        print("CORRECT")
    else:
        print("FAIL: Total cost or max distance is incorrect.")
else:
    print("FAIL: Tour start/end or city visits are incorrect.")