import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tour():
    # City coordinates indexed by city number
    coordinates = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0),
        4: (11, 10), 5: (69, 22), 6: (28, 11), 7: (70, 2),
        8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
        12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25),
        16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }
    
    # Groups of cities
    city_groups = [
        [5, 6, 16], [8, 18, 19], [11, 12, 13],
        [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
    ]
    
    # Provided Solution
    tour = [0, 8, 1, 11, 2, 5, 7, 10, 0]
    reported_cost = 244.39
    
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate the actual travel cost of the tour
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    # Compare calculated cost to reported cost
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-02):
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_from_group = [set() for _ in range(len(city_need_visit))]
    for city in tour[1:-1]:  # exclude the depot city from the ends
        for group_index, group in enumerate(city_groups):
            if city in group:
                visited_from_group[group_index].add(city)
    
    if not all(len(group) == 1 for group in visited_from_group):
        return "FAIL"
    
    return "CORRECT"

# Running the test
print(test_tour())  # Expected Output: "CORRECT"