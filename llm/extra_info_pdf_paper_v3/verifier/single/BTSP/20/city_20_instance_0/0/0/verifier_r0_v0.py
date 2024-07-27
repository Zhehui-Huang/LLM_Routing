import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, max_distance):
    cities = [
        (8, 11),  # Depot city 0
        (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
        (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97),
        (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), (60, 63),
        (93, 15)
    ]

    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once except the depot
    unique_visits = set(tour)
    if len(unique_visits) != 21 or len(tour) != 21:  # 20 cities + 1 repeat of depot
        return "FAIL"

    # Calculate the total travel cost and check with provided value
    calculated_cost = 0
    calculated_max_dist = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_cost += dist
        if dist > calculated_max_dist:
            calculated_max_dist = dist
    
    if not(math.isclose(total_cost, calculated_wealth, rel_tol=1e-3) and math.isclose(max_distance, calculated_max_dist, rel_tol=1e-3)):
        return "FAIL"

    return "CORRECT"

# Given solution details
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_cost = 349.1974047195548
max_distance = 32.38826948140329

# Verify the solution
result = verify_solution(tour, total_cost, max_distance)
print(result)