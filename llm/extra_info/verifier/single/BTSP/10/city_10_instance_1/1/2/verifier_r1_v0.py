import math

def compute_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_tour(tour, cities):
    total_cost = 0
    max_distance = 0
    visited = set()

    for i in range(len(tour) - 1):
        city_index1 = tour[i]
        city_index2 = tour[i + 1]
        visited.add(city_index1)
        distance = compute_distance(cities[city_index1], cities[city_index2])
        total_cost += distance
        max_distance = max(max_distance, distance)

    # Check all city requirements
    start_end_requirement = tour[0] == 0 and tour[-1] == 0
    visit_once_requirement = len(visited) == len(cities) and all(i in visited for i in range(len(cities)))
    
    # Output results
    if start_end_requirement and visit_once_requirement and round(total_cost, 2) == 291.41 and round(max_distance, 2) == 56.61:
        return "CORRECT"  # Means all requirements are correct.
    else:
        return "FAIL"

# City coordinates
cities = [
    (53, 68),  # City 0 (Depot)
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Tour to test
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]

# Perform the test
result = test_tour(tour, cities)
print(result)