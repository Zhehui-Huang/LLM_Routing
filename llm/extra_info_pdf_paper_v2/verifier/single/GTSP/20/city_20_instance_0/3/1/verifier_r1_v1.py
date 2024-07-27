import math

def check_solution(tour, total_travel_cost):
    # Test all requirements
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check unique city from each group
    groups = [
        [1, 3, 5, 11, 13, 14, 19],  # Group 0
        [2, 6, 7, 8, 12, 15],       # Group 1
        [4, 9, 10, 16, 17, 18]      # Group 2
    ]
    selected_cities = set(tour[1:-1])  # excluding starting and ending depot
    if any(len(selected_cities.intersection(group)) != 1 for group in groups):
        return "FAIL"
    
    # Verify Euclidean distances
    cities_coords = {
        0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
        6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 
        11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 
        16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
    }

    def compute_euclidean(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += compute_euclidean(cities_coords[tour[i]], cities_coords[tour[i + 1]])

    # Comparing computed cost closely due to floating-point precision issues.
    if not math.isclose(computed_cost, total_travel_cost, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 1, 8, 17, 0]
total_travel_cost = 123.30735638093229
result = check_solution(tour, total_travel_cost)
print(result)