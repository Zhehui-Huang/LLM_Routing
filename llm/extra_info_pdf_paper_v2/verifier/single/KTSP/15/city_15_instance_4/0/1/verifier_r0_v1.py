import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def evaluate_solution(tour, city_coordinates):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour does not start and end at the depot city 0."
    
    if len(tour) != 13:  # Including the depot city twice (start and end)
        return "FAIL", "Tour does not visit exactly 13 positions (12 distinct cities including the depot)."
    
    if len(set(tour)) != 12:
        return "FAIL", "Duplicate cities in the tour or wrong number of distinct cities visited."
    
    total_distance = 0
    for i in range(len(tour)-1):
        total_distance += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    return "CORRECT", total_distance

# Example City Coordinates
city_coordinates = [
    (35, 40), # City 0 - Depot
    (39, 41), # City 1
    (81, 30), # City 2
    (5, 50),  # City 3
    (72, 90), # City 4
    (54, 46), # City 5
    (8, 70),  # City 6
    (97, 62), # City 7
    (14, 41), # City 8
    (70, 44), # City 9
    (27, 47), # City 10
    (41, 74), # City 11
    (53, 80), # City 12
    (21, 21), # City 13
    (12, 39)  # City 14
]

# Sample tour for testing
sample_tour = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 13, 0]
evaluation_result, total_distance = evaluate_solution(sample_tour, city_coordinates)

print("Tour:", sample_tour)
if evaluation_result == "CORRECT":
    print("CORRECT")
    print("Total travel cost:", total_distance)
else:
:    print("FAIL")
    print(evaluation_result)