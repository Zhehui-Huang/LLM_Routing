import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(cities, tour, reported_cost):
    # Cities data: city_index: (x, y)
    cities_coordinates = {
        0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
        5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 
        10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
    }
    
    # Check tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check the tour visits each city exactly once except depot,
    # which should be visited twice (beginning and end).
    city_visit_count = {}
    for index in tour:
        if index in city_visit_count:
            city_visit_count[index] += 1
        else:
            city_visit_count[index] = 1
    if city_visit_count[0] != 2:
        return "FAIL"
    for city in cities:
        if city != 0 and city_visit_count.get(city, 0) != 1:
            return "FAIL"
    
    # Calculate the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += calculate_distance(*cities_coordinates[city1], *cities_coordinates[city2])
    
    # Compare the calculated cost to the reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 14, 1, 4, 12, 3, 7, 0]
total_travel_cost = 183.2573580011866

# Verify the solution
result = verify_tour(list(range(15)), tour, total_travel_cost)
print(result)