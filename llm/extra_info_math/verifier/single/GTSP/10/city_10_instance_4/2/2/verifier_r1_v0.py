import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, all_groups):
    # Checking if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Creating a list to check the occurrence of groups and cities
    visited_groups = set()

    # Check if exactly one city from each group is visited
    for city in tour[1:-1]:  # excluding the first and last depot occurrences
        for group_index, group in enumerate(all_groups):
            if city in group:
                if group_index in visited_groups:
                    return False
                visited_groups.add(group_index)
                
    # Check if all groups are visited
    if visited_groups != set(range(len(all_groups))):
        return False
    
    return True

# Data setup
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

groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

solution_tour = [0, 3, 0, 3, 0, 3, 0, 3, 0]
calculated_total_cost = 142.43595051811886

# Check tour and cost correctness
if not verify_tour(solution_tour, groups):
    print("FAIL")
else:
    # Calculate the total travel cost
    total_cost = 0
    for i in range(len(solution_tour) - 1):
        city_a = solution_tour[i]
        city_b = solution_tour[i + 1]
        total_cost += calculate_euclidean_distance(*cities[city_a], *cities[city_b])
    
    if abs(total_cost - calculated_total_cost) < 1e-5:
        print("CORRECT")
    else:
        print("FAIL")