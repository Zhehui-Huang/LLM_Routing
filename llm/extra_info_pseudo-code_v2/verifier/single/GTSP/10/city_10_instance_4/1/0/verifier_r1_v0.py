import math

# Given tour and travel cost from your solution
tour = [0, 4, 6, 7, 5, 9, 8, 3, 0, 0]
total_travel_cost = 371.1934423276749

# Coordinate data for the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Grouping of cities
city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_pdf(docs, ).distance(tour[i], tour[i+1])
    return total_distance

def validate_tour(tour, total_travel_cost):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if only one city from each group is visited
    visited_from_group = set()
    for group in city_groups:
        if not any(city in tour for city in group):
            return "FAIL"
        group_visits = sum(city in tour for city in group)
        if group_visits > 1:
            return "FAIL"
        visited_from_group.update(group)
    
    # Calculate and check the reported travel cost
    calculated_cost = calculate_total_distance(tour)
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Print the result of the validation
print(validate_tour(tour, total_travel_cost))