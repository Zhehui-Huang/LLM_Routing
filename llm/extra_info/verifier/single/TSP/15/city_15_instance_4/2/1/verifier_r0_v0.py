import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution(tour, total_cost_claimed, coordinates):
    if len(coordinates) != 15:
        return "FAIL"
    
    if coordinates[0] != (35, 40):
        return "FAIL"
    
    if len(tour) != 16 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    visited = set(tour)
    if len(visited) != 15 or any([city not in visited for city in range(15)]):
        return "FAIL"
    
    total_cost_calculated = 0
    for i in range(len(tour)-1):
        total_cost_calculated += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])

    if round(total_cost_calculated, 2) != total_cost_claimed:
        return "FAIL"
    
    return "CORRECT"

coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), 
    (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]
tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
total_cost_claimed = 337.84

print(verify_solution(tour, total_cost_claimed, coordinates))