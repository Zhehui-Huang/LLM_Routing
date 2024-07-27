import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_tour_validity(tour, list_of_cities):
    # This function checks if the tour starts and ends at the depot and includes exactly 4 cities.
    if len(tour) != 5:
        return False
    if tour[0] != 0 or tour[-1] != 0:
        return False
    if len(set(tour)) != 4 + 1:  # Including the depot twice
        return False
    return all(city in range(len(list_of_cities)) for city in tour)

def calculate_tour_cost(tour, list_of_cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        x1, y1 = list_of_cities[city1]
        x2, y2 = list_of_cities[city2]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    return total_cost

# Environment cities with their coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
    4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}
city_list = [cities[index] for index in range(len(cities))]

# Given solution
solution_tour = [0, 1, 8, 4, 0]
solution_cost = 110.08796524611944

# Testing conditions
if check_tour_validity(solution_tour, city_list):
    calculated_cost = calculate_tour_cost(solution_tour, city_list)
    # Check if the calculated cost is close to the given solution cost with a tolerance of 1e-5
    if abs(calculated_cost - solution_cost) < 1e-5:
        print("CORRECT")
    else:
        print("FAIL")
else:
    print("FAIL")