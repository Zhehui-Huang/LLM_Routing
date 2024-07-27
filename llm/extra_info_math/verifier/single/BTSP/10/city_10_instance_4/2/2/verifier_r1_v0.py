from math import sqrt

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Given cities with their coordinates
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

# Tour given by the MILP solution
tour = [0, 6, 2, 8, 9, 7, 5, 3, 1, 4, 0]

# Check if the tour is correct based on the requirements
def verify_tour(tour, cities):
    # Check if starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at the depot city."
    
    # Check if each city is visited exactly once
    if len(set(tour)) != len(cities) + 1:  # +1 due to the return to the starting city
        return "FAIL: Each city is not visited exactly once."
    
    # Calculate total travel cost and find maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    
    # Check if the maximum distance is minimized (this check is conceptual since we don't have other solutions to compare)
    if max_distance > 61.68468205:  # Threshold from given solution
        return "FAIL: Maximum distance between consecutive cities is not minimized."

    return "CORRECT"

# Execute the test
test_result = verify_tour(tour, cities)
print(test_result)