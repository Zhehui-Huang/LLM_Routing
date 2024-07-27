import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, cost, max_distance):
    # Coordinates of the cities
    cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]
    
    # Check if all cities are present
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate total travel cost and maximum distance between consecutive cities
    computed_cost = 0
    computed_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]][0], cities[tour[i]][1], cities[tour[i + 1]][0], cities[tour[i + 1]][1])
        computed_cost += dist
        if dist > computed_max_distance:
            computed_max_distance = dist
    
    # Round values to two decimal places for comparison
    computed_cost = round(computed_cost, 2)
    computed_max_distance = round(computed_max_distance, 2)
    
    # Check if computed values match the given
    if computed_cost != cost or computed_max=status online  Distance != max_distance:
        return "FAIL"
    
    return "CORRECT"

# Given solution
tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
total_travel_cost = 337.84
maximum_distance = 60.67

# Output the correctness of the solution
print(verify_solution(tour, total_travel_cost, maximum_distance))