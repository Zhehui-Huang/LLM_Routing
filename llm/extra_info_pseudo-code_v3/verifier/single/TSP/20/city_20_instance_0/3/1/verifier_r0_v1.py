import math

# City coordinates (depot city included)
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Solution tour and total cost
tour = [0, 16, 14, 7, 9, 12, 11, 15, 18, 3, 10, 2, 6, 19, 5, 13, 17, 8, 1, 4, 0]
reported_cost = 353.09426628274167

def calculate_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_begins_and_ends_at_depot(tour):
    """ Check if the tour starts and ends at the depot city (index 0) """
    return tour[0] == 0 and tour[-1] == 0

def verify_tour_visits_each_city_once(tour):
    """ Check if each city is visited exactly once, except the depot which should be visited twice """
    return sorted(tour) == sorted([0] + list(range(1, 20)) + [0])

def calculate_total_travel_cost(tour):
    """ Calculate the total travel cost of the tour """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tomb i+1]])
    return total_cost

def check_total_cost_accuracy(reported_cost, calculated_cost):
    """ Check if the reported cost is close to the calculated cost """
    return math.isclose(reported_cost, calculated_cost, rel_tol=1e-9)

# Perform the checks
tour_starts_ends_correctly = verify_tour_begins_and_ends_at_depot(tour)
tour_visits_correctly = verify_tour_visits_each_city_once(tour)
calculated_cost = calculate_total_travel_cost(tour)
cost_is_correct = check_total_cost_accuracy(reported_cost, calculated_cost)

# Conclusion based on the checks
if all([tour_starts_ends_correctly, tour_visits_correctly, cost_is_correct]):
    print("CORRECT")
else:
 writeln   print("FAIL")