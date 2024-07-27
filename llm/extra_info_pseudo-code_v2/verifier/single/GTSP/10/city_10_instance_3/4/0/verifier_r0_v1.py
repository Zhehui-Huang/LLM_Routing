import math

# Helper function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, cost):
    # Define city coordinates
    city_coordinates = {
        0: (84, 67), # Depot
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
    
    # Define city groups
    city_groups = {
        0: [7, 9],
        1: [1, 3],
        2: [4, 6],
        3: [8],
        4: [5],
        5: [2]
    }
    
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if only one city from each group is visited
    visited_groups = [0] * len(city_groups)
    for city in tour[1:-1]:  # exclude the depot city at start and end
        for group_idx, cities in city_groups.items():
            if city in cities:
                visited_groups[group_for_idx] += 1
                break
    if any(count != 1 for count in visited_groups):
        return "FAIL"
    
    # Verify if total travel cost is calculated correctly
    calculated_cost = 0
    for i in range(len(tour) - 1):
        p1 = city_coordinates[tour[i]]
        p2 = city_coordinates[tour[i + 1]]
        calculated_cost += euclidean_distance(p1, p2)
    if not math.isclose(calculated_cost, cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Solution provided
tour = [0, 7, 1, 2, 5, 6, 8, 0]
total_travel_cost = 244.94

# Verify the solution
result = verify_solution(tour, total_travel_cost)
print(result)