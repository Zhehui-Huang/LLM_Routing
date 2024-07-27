import math

def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def verify_tour_and_cost(cities, tour, total_cost):
    # Verify that tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify that all cities are visited exactly once except depot city
    visited = set(tour)
    if len(visited) != len(cities) or set(range(len(cities))) != visited:
        return "FAIL"
    
    # Calculate the total travel cost and compare with the given total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Round the calculated cost to match the given precision
    calculated_cost = round(calculated_cost, 2)
    if calculated_cost != total_cost:
        return "FAIL"
    
    return "CORRECT"

cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

tour = [0, 7, 1, 4, 2, 5, 6, 9, 3, 8, 0]
total_travel_cost = 294.17

# Call the verification function
result = verify_tour_and_cost(cities, tour, total_travel_cost)
print(result)