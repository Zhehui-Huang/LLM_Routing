import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, cities):
    # Verify if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify the number of cities visited (including depot, should be visited twice at start and end)
    if len(tour) != 17:
        return "FAIL"
    
    # Verify there are exactly 16 unique cities including the depot
    if len(set(tour)) != 16:
        return "FAIL"
    
    # Verify travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # Round calculated cost to avoid floating point arithmetic issues
    if round(calculated_cost) != int(total_cost):
        return "FAIL"
    
    return "CORRECT"

# City coordinates including the depot
city_coords = [
    (26, 60), (73, 84), (89, 36), (15, 0),
    (11, 10), (69, 22), (28, 11), (70, 2), 
    (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Tour and total cost from the assumed solution
solution_tour = [0, 13, 11, 8, 17, 6, 4, 3, 9, 1, 18, 10, 5, 7, 12, 15, 0]
solution_total_cost = 524

# Verification
result = verify_solution(solution_tour, solution_total_cost, city_coords)
print(result)