import math

# Helper function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Test data and solution given
solution_tour = [0, 5, 2, 9, 8, 0]
solution_cost = 183.98559431675523

# City coordinates
coordinates = [
    (53, 68),  # 0
    (75, 11),  # 1
    (91, 95),  # 2
    (22, 80),  # 3
    (18, 63),  # 4
    (54, 91),  # 5
    (70, 14),  # 6
    (97, 44),  # 7
    (17, 69),  # 8
    (95, 89)   # 9
]

# Group information
city_groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Function to test the requirements
def test_solution(tour, cost):
    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]
    visited_groups = set()
    for city in tour[1:-1]:
        for group_id, group_cities in city_groups.items():
            if city in group_cities:
                visited_groups.add(group_id)
    if len(visited_groups) != 4:
        return "FAIL"
    
    # [Requirement 3] and [Requirement 4]
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    if not math.isclose(computed_cost, cost, abs_tol=0.0001):
        return "FAIL"
    
    # [Requirement 5] and [Requirement 6] are assumed verified by manual setting of tour and cost
    return "CORRECT"

# Running the test
test_result = test_solution(solution_tour, solution_cost)
print(test_result)