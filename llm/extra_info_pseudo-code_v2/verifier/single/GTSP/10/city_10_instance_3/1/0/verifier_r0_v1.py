import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, cost):
    # Define the cities and their coordinates
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
    # Define the groups
    groups = [
        [7, 9],
        [1, 3],
        [4, 6],
        [8],
        [5],
        [2]
    ]
    
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    unique_cities = set(tour[1:-1])  # exclude the depot city from this set
    group_cities_covered = set()
    for group in groups:
        if not any(city in unique_cities for city in group):
            return "FAIL"
        for city in group:
            if city in unique_cities:
                group_cities_covered.add(city)
                break
    
    if len(group_cities_covered) != len(groups):
        return "FAIL"
    
    # Check the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Compare calculated cost with the provided cost (with a small tolerance for float comparison)
    if not math.isclose(calculated_cost, cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Provide the solution for validation
tour = [0, 8, 3, 5, 2, 4, 7, 0]
total_cost = 263.92

# Validate the solution
result = check_solution(tour, total_cost)
print(result)