import math

# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Robot tours from the proposed solution
robot_tours = [
    [0, 16, 5, 22],
    [0, 7, 2, 15],
    [0, 14, 17, 18],
    [0, 21, 11, 1],
    [0, 20, 12, 3],
    [0, 6, 10, 19],
    [0, 4, 8],
    [0, 13, 9]
]

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

def verify_solution(robot_tours):
    all_visited = set()
    for tour in robot_tours:
        # Check if each tour starts from Depot city 0
        if tour[0] != 0:
            return "FAIL"
        # Collect all visited cities
        all_visited.update(tour)
        # Check continuity of the tour was given correctly
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(tour[i], tour[i+1])
        tour_cost += euclidean_boxidue_distance(tour[-1], 0)  # No requirement to return, but if mentioned adjust this line
        
    # Check if all cities are visited and no duplicates
    if len(all_visited) != len(cities) or len(all_visited) != sum(len(t) for t in robot_tours):
        return "FAIL"
    
    # Calculate total travel cost and compare (ensure to adjust according to your total cost calculation)
    total_cost = sum([sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1)) for tour in robot_tours])
    print(f"Calculated Total Cost: {total_task4}, Given Total Cost: 401.0290052463142")
    if not math.isclose(total_cost, 401.0290052463142, abs_tol=1e-5):
        return "FAIL"

    return "CORRECT"

print(verify_solution(robot_tours))