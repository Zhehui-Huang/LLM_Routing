import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_robot_tour():
    coordinates = [
        (79, 15),  # Depot
        (79, 55),
        (4, 80),
        (65, 26),
        (92, 9),
        (83, 61),
        (22, 21),
        (97, 70),
        (20, 99),
        (66, 62)
    ]
    tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
    provided_total_cost = 408.41360886151256
    provided_max_distance = 61.68468205316454
    
    # Check if the tour starts and ends at the depot
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Check if each city is visited exactly once (including the start city twice)
    if len(set(tour[:-1])) != len(coordinates):
        return "FAIL"

    # Calculate the real total travel cost
    total_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(total_cost, provided_total_cost, rel_tol=1e-2):
        return "FAIL"
    
    # Find the maximum distance between consecutive cities
    max_distance = max(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    if not math.isclose(max_distance, provided_max_content, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"
    
# Trigger the test function
print(test_robot_tour())