import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(cities, tour, total_cost):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once, except the depot city
    city_visit_counts = {i: 0 for i in range(len(cities))}
    for city in tour:
        city_visit_counts[city] += 1

    if any(city_visit_counts[city] != 1 for city in range(1, len(cities))) or city_visit_counts[0] != 2:
        return "FAIL"
    
    # Calculate the tour's travel distance
    computed_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    
    # As this is a floating point comparison, we should allow for a small error margin
    # However, minimizing the total travel cost should provide the least possible tour value
    if not math.isclose(computed_cost, total_cost, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given cities with their coordinates
cities = [
    (35, 40), # City 0 (depot)
    (39, 41),
    (81, 30),
    (5, 50),
    (72, 90),
    (54, 46),
    (8, 70),
    (97, 62),
    (14, 41),
    (70, 44),
    (27, 47),
    (41, 74),
    (53, 80),
    (21, 21),
    (12, 39)
]

# Given solution tour and cost
tour = [0, 1, 5, 9, 2, 7, 4, 12, 11, 6, 3, 8, 14, 13, 10, 0]
total_cost = 288.5242816725832

# Perform verification
result = verify_solution(cities, tour, total_cost)
print(result)