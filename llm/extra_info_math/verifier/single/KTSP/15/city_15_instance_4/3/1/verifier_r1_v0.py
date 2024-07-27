import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(tour, reported_total_cost):
    cities = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }
    
    # Check the tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly 12 unique cities are visited, including the depot
    if len(set(tour)) != 12:
        return "FAIL"
    
    # Calculate the Euclidean distance for the proposed tour
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if the calculated distance matches the reported total travel cost
    if not math.isclose(total_distance, reported_total_cost, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Sample solution provided
tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 0]
reported_total_cost = 241.29121374601274

# Run the verification tests
result = verify_tour(tour, reported_total_cost)
print(result)